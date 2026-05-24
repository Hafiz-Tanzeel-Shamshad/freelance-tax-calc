import os, re

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

# Build set of all .html files (relative paths without extension)
html_files = set()
for root, dirs, files in os.walk(ROOT):
    if 'assets' in root: continue
    for f in files:
        if f.endswith('.html') and not f.startswith('_'):
            rel = os.path.relpath(os.path.join(root, f), ROOT).replace(os.sep, '/')
            # Add both with and without .html
            html_files.add(rel)
            if rel.endswith('.html'):
                html_files.add(rel[:-5])  # without .html
            if f == 'index.html':
                dir_path = os.path.dirname(rel)
                if dir_path:
                    html_files.add(dir_path)

print(f"Total known paths: {len(html_files)}")

# Now scan all HTML files for broken hrefs
fix_count = 0
file_fixes = {}

for root, dirs, files in os.walk(ROOT):
    if 'assets' in root: continue
    for f in files:
        if not f.endswith('.html') or f.startswith('_'): continue
        fpath = os.path.join(root, f)
        with open(fpath, 'r', encoding='utf-8') as fh:
            content = fh.read()

        original = content
        # Find all href="/..." patterns
        for m in list(re.finditer(r'href=["\'](/[^"\']*)["\']', content)):
            url = m.group(1)
            # Skip if already has .html, ends with /, has #, has ?, is external (http)
            if url.endswith('.html') or url.endswith('/') or '#' in url or '?' in url or url.startswith('http'):
                continue
            
            # Remove trailing slash if any
            clean_url = url.rstrip('/')
            
            # Check if this path exists as .html
            path_no_ext = clean_url[1:]  # remove leading /
            if path_no_ext in html_files:
                new_url = clean_url + '.html'
                old_attr = f'href="{url}"'
                new_attr = f'href="{new_url}"'
                if old_attr in content:
                    content = content.replace(old_attr, new_attr, 1)
                    file_fixes.setdefault(os.path.relpath(fpath, ROOT).replace(os.sep, '/'), []).append(f"{url} -> {new_url}")
                    fix_count += 1
            elif path_no_ext + '.html' in html_files:
                new_url = clean_url + '.html'
                old_attr = f'href="{url}"'
                new_attr = f'href="{new_url}"'
                if old_attr in content:
                    content = content.replace(old_attr, new_attr, 1)
                    file_fixes.setdefault(os.path.relpath(fpath, ROOT).replace(os.sep, '/'), []).append(f"{url} -> {new_url}")
                    fix_count += 1

        if content != original:
            with open(fpath, 'w', encoding='utf-8') as fh:
                fh.write(content)

print(f"\nTotal links fixed: {fix_count}")
print(f"Files modified: {len(file_fixes)}")

# Show files with most fixes
for rel, links in sorted(file_fixes.items()):
    print(f"\n  {rel} ({len(links)} fixes):")
    for l in links[:5]:
        print(f"    {l}")
    if len(links) > 5:
        print(f"    ... and {len(links)-5} more")
