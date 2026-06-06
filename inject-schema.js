/**
 * inject-schema.js
 * Adds missing JSON-LD (Organization, WebSite) + OG image to all HTML pages.
 * Usage: node inject-schema.js
 */

const fs = require("fs");
const path = require("path");

const ROOT = __dirname;
const SITE = "https://freelancetaxcalc.online";

// ── Schema templates ──

function organizationSchema(pageUrl) {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "FreelanceTaxCalc",
    "url": SITE,
    "logo": SITE + "/favicon.svg",
    "description": "Free tax calculators and financial tools for freelancers, gig workers, and self-employed professionals.",
    "sameAs": [
      "https://www.facebook.com/freelancetaxcalc",
      "https://twitter.com/freelancetaxcalc",
      "https://www.linkedin.com/company/freelancetaxcalc"
    ]
  }, null, 2);
}

function websiteSchema(pageUrl) {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "FreelanceTaxCalc",
    "url": SITE,
    "description": "Free tax calculators and financial tools for freelancers and self-employed professionals.",
    "potentialAction": {
      "@type": "SearchAction",
      "target": {
        "@type": "EntryPoint",
        "urlTemplate": SITE + "/search?q={search_term_string}"
      },
      "query-input": "required name=search_term_string"
    }
  }, null, 2);
}

// ── Page categorization ──

function categorizePage(relPath) {
  if (relPath === "index.html") return "homepage";
  if (relPath === "404.html") return "404";
  if (relPath.startsWith("blog/")) return "blog";
  if (relPath.startsWith("guides/")) return "guide";
  if (relPath.startsWith("deductions/")) return "deduction";
  if (relPath.startsWith("digital-nomad-tax/")) return "nomad";
  if (relPath.startsWith("contact/")) return "contact";
  if (relPath.startsWith("legal/")) return "legal";
  if (relPath.startsWith("tools/quarterly-tax-calculator/")) return "state";
  if (relPath.startsWith("tools/")) return "tool";
  return "other";
}

// ── Check if a schema type already exists in the page ──

function hasSchemaType(html, type) {
  const escaped = type.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const re = new RegExp('"@type"\\s*:\\s*"' + escaped + '"');
  return re.test(html);
}

function hasOgImage(html) {
  return html.includes('property="og:image"') || html.includes("property='og:image'");
}

function hasTwitterImage(html) {
  return html.includes('name="twitter:image"') || html.includes("name='twitter:image'");
}

// ── Inject before </head> ──

function injectBeforeHeadEnd(html, snippet) {
  const idx = html.lastIndexOf("</head>");
  if (idx === -1) return html;
  return html.slice(0, idx) + "\n" + snippet.trim() + "\n" + html.slice(idx);
}

// ── Find all HTML files ──

function findHtml(dir) {
  const results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (["node_modules", ".git", "assets"].includes(e.name)) continue;
      results.push(...findHtml(p));
    } else if (e.isFile() && e.name.endsWith(".html") && !e.name.startsWith("_")) {
      results.push(p);
    }
  }
  return results;
}

// ── Main ──

const files = findHtml(ROOT);
let orgAdded = 0;
let wsAdded = 0;
let ogAdded = 0;
let twAdded = 0;
let skipped = 0;
let orgExists = 0;

for (const fp of files) {
  let html = fs.readFileSync(fp, "utf-8");
  const relPath = path.relative(ROOT, fp).replace(/\\/g, "/");

  // Skip redirect-only pages
  if (html.includes('http-equiv="refresh"')) {
    skipped++;
    continue;
  }

  const category = categorizePage(relPath);
  const pageUrl = SITE + "/" + (relPath === "index.html" ? "" : relPath);

  let additions = "";

  // ── Organization schema ──
  if (!hasSchemaType(html, "Organization")) {
    additions += '\n<script type="application/ld+json">\n' +
                 organizationSchema(pageUrl) +
                 '\n</script>';
    orgAdded++;
  } else {
    orgExists++;
  }

  // ── WebSite schema (only if missing) ──
  if (!hasSchemaType(html, "WebSite")) {
    additions += '\n<script type="application/ld+json">\n' +
                 websiteSchema(pageUrl) +
                 '\n</script>';
    wsAdded++;
  }

  // ── OG image ──
  if (!hasOgImage(html)) {
    additions += '\n<meta property="og:image" content="' + SITE + '/favicon.svg" />';
    additions += '\n<meta property="og:image:width" content="512" />';
    additions += '\n<meta property="og:image:height" content="512" />';
    additions += '\n<meta property="og:image:type" content="image/svg+xml" />';
    ogAdded++;
  }

  // ── Twitter image ──
  if (!hasTwitterImage(html)) {
    additions += '\n<meta name="twitter:image" content="' + SITE + '/favicon.svg" />';
    twAdded++;
  }

  if (additions) {
    html = injectBeforeHeadEnd(html, additions);
    fs.writeFileSync(fp, html, "utf-8");
  }
}

console.log("Files scanned: " + files.length);
console.log("Redirect pages skipped: " + skipped);
console.log("");
console.log("Organization schema:");
console.log("  Already had: " + orgExists);
console.log("  Added:       " + orgAdded);
console.log("");
console.log("WebSite schema:");
console.log("  Added:       " + wsAdded);
console.log("");
console.log("OG image tag:");
console.log("  Added:       " + ogAdded);
console.log("");
console.log("Twitter image tag:");
console.log("  Added:       " + twAdded);
