/**
 * generate-feeds.js
 *
 * Scans the project directory for HTML pages and generates:
 *   /feed.xml  — RSS 2.0 feed of blog posts and guides
 *   /sitemap.xml — XML sitemap of all pages
 *
 * Usage: node generate-feeds.js
 *
 * Zero dependencies — uses only built-in Node.js modules.
 */

const fs = require('fs');
const path = require('path');

const SITE_URL = 'https://freelancetaxcalc.online';
const ROOT_DIR = __dirname;

// ── Helpers ────────────────────────────────────────────────────────

function readFile(p) {
  try { return fs.readFileSync(p, 'utf-8'); } catch { return ''; }
}

function escapeXml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

/** Extract <title> from HTML */
function extractTitle(html) {
  const m = html.match(/<title>([^<]*)<\/title>/i);
  return m ? m[1].trim() : '';
}

/** Extract <meta name="description"> from HTML */
function extractDescription(html) {
  const m = html.match(/<meta\s+name="description"\s+content="([^"]*)"/i);
  return m ? m[1].trim() : '';
}

/**
 * Extract date from HTML.
 * Checks: JSON-LD datePublished, <meta property="article:published_time">,
 * <meta itemprop="datePublished">, <time datetime="...">, then file mtime.
 */
function extractDate(html, filePath) {
  // JSON-LD datePublished
  const jm = html.match(/"datePublished"\s*:\s*"([^"]+)"/);
  if (jm) return jm[1].substring(0, 10);

  // <meta property="article:published_time">
  const mm = html.match(/<meta\s+(?:property|itemprop)\s*=\s*"(?:article:published_time|datePublished)"\s+content\s*=\s*"([^"]+)"/i);
  if (mm) return mm[1].substring(0, 10);

  // <time datetime="">
  const tm = html.match(/<time\s+[^>]*datetime="([^"]+)"/i);
  if (tm) return tm[1].substring(0, 10);

  // Fallback to file modification date
  try {
    const stat = fs.statSync(filePath);
    return stat.mtime.toISOString().substring(0, 10);
  } catch { return '2026-06-06'; }
}

/** Convert YYYY-MM-DD to RFC 822 */
function toRfc822(dateStr) {
  const d = new Date(dateStr + 'T10:00:00Z');
  return d.toUTCString().replace('GMT', '+0000');
}

/** Recursively find all .html files, excluding assets/ and node_modules/ */
function findHtmlFiles(dir) {
  const results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (e.name === 'node_modules' || e.name === '.git' || e.name === 'assets') continue;
      results.push(...findHtmlFiles(p));
    } else if (e.isFile() && e.name.endsWith('.html') && !e.name.startsWith('_')) {
      results.push(p);
    }
  }
  return results;
}

/** Relative path to full URL */
function toUrl(relPath) {
  let p = relPath
    .replace(/\\/g, '/')
    .replace(/^\.\//, '')
    .replace(/^\.\.\//, '');
  // Remove ROOT_DIR prefix
  const root = ROOT_DIR.replace(/\\/g, '/');
  if (p.startsWith(root)) p = p.slice(root.length);
  p = p.replace(/^\//, '');
  return SITE_URL + '/' + p;
}

// ── Page classification ────────────────────────────────────────────

function classifyPage(urlPath) {
  const p = urlPath.replace(SITE_URL, '');

  // Exclude these
  if (p === '/pre-launch-checklist.html' || p === '/404.html') return 'exclude';
  if (p.startsWith('/assets/')) return 'exclude';

  if (p === '/' || p === '/index.html') return 'homepage';
  if (p === '/tools/' || p === '/tools/index.html') return 'tools-index';
  if (p.startsWith('/tools/quarterly-tax-calculator/')) return 'state-page';
  if (p.startsWith('/tools/')) return 'tool-page';
  if (p.startsWith('/blog/')) return 'blog-page';
  if (p.startsWith('/guides/')) return 'guide-page';
  if (p.startsWith('/deductions/')) return 'deduction-page';
  if (p.startsWith('/digital-nomad-tax/')) return 'nomad-page';
  if (p === '/contact/' || p === '/contact/index.html') return 'contact-page';
  if (p.startsWith('/legal/')) return 'legal-page';
  return 'other';
}

function getPriority(type) {
  switch (type) {
    case 'homepage': return 1.0;
    case 'tool-page': return 0.9;
    case 'tools-index': return 0.8;
    case 'blog-page': return 0.6;
    case 'guide-page': return 0.6;
    case 'deduction-page': return 0.5;
    case 'nomad-page': return 0.5;
    case 'state-page': return 0.4;
    case 'contact-page': return 0.3;
    case 'legal-page': return 0.3;
    default: return 0.5;
  }
}

function getChangefreq(type) {
  switch (type) {
    case 'homepage': return 'weekly';
    case 'tools-index': return 'weekly';
    case 'tool-page': return 'monthly';
    case 'blog-page': return 'monthly';
    case 'guide-page': return 'monthly';
    case 'state-page': return 'yearly';
    default: return 'monthly';
  }
}

// ── Main ───────────────────────────────────────────────────────────

function main() {
  const htmlFiles = findHtmlFiles(ROOT_DIR);

  const pages = [];
  const contentItems = []; // for RSS feed (blog + guide pages)

  for (const filePath of htmlFiles) {
    const html = readFile(filePath);
    if (!html) continue;

    const url = toUrl(filePath);
    const type = classifyPage(url);
    if (type === 'exclude') continue;

    const title = extractTitle(html);
    const description = extractDescription(html);
    const date = extractDate(html, filePath);

    pages.push({ url, type, title, description, date });

    if (type === 'blog-page' || type === 'guide-page') {
      contentItems.push({
        url,
        title,
        description: description || title,
        date,
      });
    }
  }

  // ── Sort content items newest first for RSS ──
  contentItems.sort((a, b) => b.date.localeCompare(a.date));

  // ── Generate feed.xml ──
  const mostRecent = contentItems.length > 0 ? contentItems[0].date : '2026-06-06';

  let feedXml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  feedXml += '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n';
  feedXml += '  <channel>\n';
  feedXml += '    <title>Freelance Tax Calculator - Tips &amp; Updates</title>\n';
  feedXml += '    <link>' + SITE_URL + '</link>\n';
  feedXml += '    <description>Expert tax guides, tips, and resources for freelancers and self-employed professionals</description>\n';
  feedXml += '    <language>en</language>\n';
  feedXml += '    <lastBuildDate>' + toRfc822(mostRecent) + '</lastBuildDate>\n';
  feedXml += '    <atom:link href="' + SITE_URL + '/feed.xml" rel="self" type="application/rss+xml" />\n';
  feedXml += '\n';

  for (const item of contentItems) {
    feedXml += '    <item>\n';
    feedXml += '      <title>' + escapeXml(item.title) + '</title>\n';
    feedXml += '      <link>' + item.url + '</link>\n';
    feedXml += '      <description>' + escapeXml(item.description) + '</description>\n';
    feedXml += '      <pubDate>' + toRfc822(item.date) + '</pubDate>\n';
    feedXml += '      <guid isPermaLink="true">' + item.url + '</guid>\n';
    feedXml += '    </item>\n';
    feedXml += '\n';
  }

  feedXml += '  </channel>\n';
  feedXml += '</rss>\n';

  fs.writeFileSync(path.join(ROOT_DIR, 'feed.xml'), feedXml, 'utf-8');
  console.log('✓ feed.xml written (' + contentItems.length + ' items)');

  // ── Generate sitemap.xml ──
  let sitemapXml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  sitemapXml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';

  for (const page of pages) {
    sitemapXml += '\n';
    sitemapXml += '  <url>\n';
    sitemapXml += '    <loc>' + page.url + '</loc>\n';
    sitemapXml += '    <lastmod>' + page.date + '</lastmod>\n';
    sitemapXml += '    <changefreq>' + getChangefreq(page.type) + '</changefreq>\n';
    sitemapXml += '    <priority>' + getPriority(page.type).toFixed(1) + '</priority>\n';
    sitemapXml += '  </url>\n';
  }

  sitemapXml += '\n</urlset>\n';

  fs.writeFileSync(path.join(ROOT_DIR, 'sitemap.xml'), sitemapXml, 'utf-8');
  console.log('✓ sitemap.xml written (' + pages.length + ' URLs)');
}

main();
