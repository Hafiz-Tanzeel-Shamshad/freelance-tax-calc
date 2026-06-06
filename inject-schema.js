/**
 * inject-schema.js
 * Adds page-specific JSON-LD to every HTML page:
 *   - Organization (brand)
 *   - WebSite (with SearchAction)
 *   - WebPage (with page-specific title, description, url, image, publisher)
 *   - OG image + Twitter image
 *
 * Usage: node inject-schema.js
 */

const fs = require("fs");
const path = require("path");

const ROOT = __dirname;
const SITE = "https://freelancetaxcalc.online";

// ── Extract page details from HTML ──

function extractTitle(html) {
  const m = html.match(/<title>([^<]*)<\/title>/i);
  return m ? m[1].trim() : "";
}

function extractDescription(html) {
  const m = html.match(/<meta\s+name="description"\s+content="([^"]*)"/i);
  return m ? m[1].trim() : "";
}

function extractDate(html) {
  // JSON-LD datePublished
  const jm = html.match(/"datePublished"\s*:\s*"([^"]+)"/);
  if (jm) return jm[1].substring(0, 10);
  // meta article:published_time
  const mm = html.match(/<meta\s+(?:property|itemprop)\s*=\s*"(?:article:published_time|datePublished)"\s+content\s*=\s*"([^"]+)"/i);
  if (mm) return mm[1].substring(0, 10);
  return "";
}

function extractKeywords(html) {
  const topics = [];
  // Extract h1 text
  const h1 = html.match(/<h1[^>]*>([^<]+)<\/h1>/i);
  if (h1) topics.push(h1[1].trim());
  // Extract words commonly found in titles/keywords
  const known = ["freelance", "tax", "calculator", "quarterly", "deductions", "self-employed", "1099", "retirement", "guide", "budget", "invoice", "crypto", "capital gains", "UK", "Canada", "Australia"];
  const body = html.toLowerCase();
  const found = known.filter(k => body.includes(k.toLowerCase()));
  return found.slice(0, 5);
}

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

function webpageSchema(title, description, pageUrl, dateStr, keywords) {
  const obj = {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": title,
    "description": description,
    "url": pageUrl,
    "image": SITE + "/favicon.svg",
    "publisher": {
      "@type": "Organization",
      "name": "FreelanceTaxCalc",
      "url": SITE
    }
  };
  if (dateStr) obj.dateModified = dateStr;
  if (keywords.length > 0) {
    obj.about = keywords.map(k => ({ "@type": "Thing", "name": k }));
  }
  return JSON.stringify(obj, null, 2);
}

// ── Helpers ──

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

function injectBeforeHeadEnd(html, snippet) {
  const idx = html.lastIndexOf("</head>");
  if (idx === -1) return html;
  return html.slice(0, idx) + "\n" + snippet.trim() + "\n" + html.slice(idx);
}

// Primary schema types that already describe the page in detail
const PRIMARY_TYPES = ["WebApplication", "BlogPosting", "Article", "FAQPage", "ContactPage", "AboutPage", "404Error", "CollectionPage", "Blog"];

function hasPrimarySchema(html) {
  for (const t of PRIMARY_TYPES) {
    if (hasSchemaType(html, t)) return true;
  }
  return false;
}

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
let orgAdded = 0, orgExists = 0;
let wsAdded = 0;
let ogAdded = 0, twAdded = 0;
let wpAdded = 0, wpSkipped = 0;
let skipped = 0;

for (const fp of files) {
  let html = fs.readFileSync(fp, "utf-8");
  const relPath = path.relative(ROOT, fp).replace(/\\/g, "/");

  if (html.includes('http-equiv="refresh"')) {
    skipped++;
    continue;
  }

  const pageUrl = SITE + "/" + (relPath === "index.html" ? "" : relPath);
  const title = extractTitle(html);
  const desc = extractDescription(html);
  const dateStr = extractDate(html);
  const keywords = extractKeywords(html);

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

  // ── WebSite schema ──
  if (!hasSchemaType(html, "WebSite")) {
    additions += '\n<script type="application/ld+json">\n' +
                 websiteSchema(pageUrl) +
                 '\n</script>';
    wsAdded++;
  }

  // ── Page-specific WebPage schema (only if no primary type AND no WebPage exists) ──
  if (!hasPrimarySchema(html) && !hasSchemaType(html, "WebPage") && title) {
    additions += '\n<script type="application/ld+json">\n' +
                 webpageSchema(title, desc, pageUrl, dateStr, keywords) +
                 '\n</script>';
    wpAdded++;
  } else {
    wpSkipped++;
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
console.log("Organization:  " + orgAdded + " added, " + orgExists + " existing");
console.log("WebSite:       " + wsAdded + " added");
console.log("WebPage:       " + wpAdded + " added (pages without primary schema)");
console.log("  (skipped:    " + wpSkipped + " pages already have primary schema)");
console.log("OG image:      " + ogAdded + " added");
console.log("Twitter image: " + twAdded + " added");

// Log which pages got WebPage added
if (wpAdded > 0) {
  console.log("\nPages that received WebPage schema:");
  for (const fp of files) {
    const html = fs.readFileSync(fp, "utf-8");
    const relPath = path.relative(ROOT, fp).replace(/\\/g, "/");
    if (html.includes('http-equiv="refresh"')) continue;
    const hasPrimary = PRIMARY_TYPES.some(t => {
      const re = new RegExp('"@type"\\s*:\\s*"' + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + '"');
      return re.test(html);
    });
    const wpCount = (html.match(/"@type"\s*:\s*"WebPage"/g) || []).length;
    if (!hasPrimary && wpCount > 0) {
      const m = html.match(/<title>([^<]*)<\/title>/i);
      const title = m ? m[1].trim() : "";
      console.log("  " + relPath + "  → " + title);
    }
  }
}
