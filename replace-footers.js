/**
 * replace-footers.js
 * Scans all HTML files and replaces hard-coded footers
 * with a placeholder div + include script.
 * Usage: node replace-footers.js
 */

const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const PLACEHOLDER = '<div id="footer-placeholder"></div>\n<script src="/assets/include-footer.js" defer></script>';

// Recursively find HTML files, excluding node_modules/.git/assets
function findHtml(dir) {
  const results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (['node_modules', '.git', 'assets'].includes(e.name)) continue;
      results.push(...findHtml(p));
    } else if (e.isFile() && e.name.endsWith('.html')) {
      results.push(p);
    }
  }
  return results;
}

// Match from <footer class="site-footer" ... > through </footer>
// Uses a non-greedy approach to match the first closing </footer>
function replaceFooter(html) {
  // Find the start of the footer
  const startIdx = html.indexOf('<footer class="site-footer"');
  if (startIdx === -1) return html;

  // Find the matching </footer> — the one that closes the opening tag
  // We need to handle nested footer? No, footers don't nest.
  // Find first </footer> after startIdx
  const endIdx = html.indexOf('</footer>', startIdx);
  if (endIdx === -1) return html;

  const before = html.slice(0, startIdx);
  const after = html.slice(endIdx + '</footer>'.length);

  // Check if there's whitespace/newlines before the opening footer tag
  // that we should preserve
  return before + PLACEHOLDER + '\n' + after;
}

function main() {
  const files = findHtml(ROOT);
  let replaced = 0;
  let skipped = 0;

  for (const fp of files) {
    const content = fs.readFileSync(fp, 'utf-8');
    const result = replaceFooter(content);
    if (result !== content) {
      fs.writeFileSync(fp, result, 'utf-8');
      replaced++;
      console.log('  ✓ ' + path.relative(ROOT, fp));
    } else {
      skipped++;
    }
  }

  console.log('\nDone. Replaced: ' + replaced + ', Skipped: ' + skipped);
}

main();
