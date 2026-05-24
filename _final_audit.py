import os, re
from collections import defaultdict

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

all_html = []
for root, dirs, files in os.walk(ROOT):
    if 'assets' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html') and not f.startswith('_'):
            rel = os.path.relpath(os.path.join(root, f), ROOT).replace(os.sep, '/')
            all_html.append(rel)
all_html.sort()
print(f"Total HTML files: {len(all_html)}\n")

issues = defaultdict(list)

for rel in all_html:
    fpath = os.path.join(ROOT, rel)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()

    # H1
    h1s = re.findall(r'<h1[^>]*>', c)
    if not h1s and rel != 'pre-launch-checklist.html' and rel != 'legal/contact.html':
        issues['MISSING H1'].append(rel)

    # Title length
    t = re.search(r'<title>(.*?)</title>', c, re.DOTALL)
    if t:
        tl = len(t.group(1).strip())
        if tl > 60: issues['TITLE >60c'].append(f"{rel} ({tl}c)")
        if tl < 10: issues['TITLE <10c'].append(f"{rel} ({tl}c)")

    # Meta desc length
    md = re.search(r'<meta\s+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', c)
    if md:
        mlen = len(md.group(1))
        if mlen > 160: issues['META >160c'].append(f"{rel} ({mlen}c)")
        if mlen < 40:  issues['META <40c'].append(f"{rel} ({mlen}c)")

    # Schema
    if 'application/ld+json' not in c:
        issues['NO JSON-LD'].append(rel)
    elif 'BreadcrumbList' not in c and rel != 'legal/contact.html':
        issues['NO BreadcrumbList'].append(rel)

    # Breadcrumb nav
    if 'class="breadcrumb"' not in c and rel != 'pre-launch-checklist.html' and rel != 'legal/contact.html':
        issues['NO BREADCRUMB NAV'].append(rel)

    # Cookie consent
    if 'cookie-consent' not in c:
        issues['NO COOKIE CONSENT'].append(rel)

    # Old .com domain
    if 'freelancetaxcalc.com' in c or 'FreelanceTaxCalc.com' in c:
        issues['OLD .com DOMAIN'].append(rel)

    # AdSense placeholder
    if 'ca-pub-XXXXXXXXXXXXXXXX' in c or 'ca-pub-XXXXX' in c:
        issues['ADSENSE PLACEHOLDER'].append(rel)

print("=" * 60)
print("FINAL AUDIT REPORT")
print("=" * 60)
for issue, files in sorted(issues.items()):
    print(f"\n  {issue}: {len(files)}")
    for f in files[:15]:
        print(f"    - {f}")
    if len(files) > 15:
        print(f"    ... and {len(files)-15} more")

total = sum(len(v) for v in issues.values())
print(f"\n{'='*60}")
print(f"TOTAL REMAINING ISSUES: {total}")
