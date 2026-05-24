import os, re

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

# Fix index.html description (188c -> <160c)
INDEX_DESC = 'Free online tax calculators for freelancers, gig workers, and the self-employed. Calculate quarterly taxes, find deductions, estimate take-home pay.'

# Fix state page descriptions (170c -> <160c)
STATE_DESC = 'Free freelancer tax calculator for [STATE]. Self-employed quarterly tax estimator with [STATE] state rates, due dates, and payment amounts for 2026.'

STATE_SHORT = {
    'alabama': 'Alabama', 'alaska': 'Alaska', 'arizona': 'Arizona', 'arkansas': 'Arkansas',
    'california': 'California', 'colorado': 'Colorado', 'connecticut': 'Connecticut',
    'dc': 'Washington DC', 'delaware': 'Delaware', 'florida': 'Florida', 'georgia': 'Georgia',
    'hawaii': 'Hawaii', 'idaho': 'Idaho', 'illinois': 'Illinois', 'indiana': 'Indiana',
    'iowa': 'Iowa', 'kansas': 'Kansas', 'kentucky': 'Kentucky', 'louisiana': 'Louisiana',
    'maine': 'Maine', 'maryland': 'Maryland', 'massachusetts': 'Massachusetts',
    'michigan': 'Michigan', 'minnesota': 'Minnesota', 'mississippi': 'Mississippi',
    'missouri': 'Missouri', 'montana': 'Montana', 'nebraska': 'Nebraska', 'nevada': 'Nevada',
    'new-hampshire': 'New Hampshire', 'new-jersey': 'New Jersey', 'new-mexico': 'New Mexico',
    'new-york': 'New York', 'north-carolina': 'North Carolina', 'north-dakota': 'North Dakota',
    'ohio': 'Ohio', 'oklahoma': 'Oklahoma', 'oregon': 'Oregon', 'pennsylvania': 'Pennsylvania',
    'rhode-island': 'Rhode Island', 'south-carolina': 'South Carolina', 'south-dakota': 'South Dakota',
    'tennessee': 'Tennessee', 'texas': 'Texas', 'utah': 'Utah', 'vermont': 'Vermont',
    'virginia': 'Virginia', 'washington': 'Washington', 'west-virginia': 'West Virginia',
    'wisconsin': 'Wisconsin', 'wyoming': 'Wyoming',
}

# Fix OG descriptions for pages that have short ones
OG_FIXES = {
    '404.html': 'Page not found. The page you are looking for does not exist. Find free tax calculators for freelancers on our homepage.',
    'digital-nomad-tax/estonia.html': "Complete guide to Estonia's digital nomad visa and e-Residency tax rules for remote workers.",
    'digital-nomad-tax/mexico.html': 'Complete guide to Mexico digital nomad visa tax rules including residency and FEIE for US remote workers.',
    'digital-nomad-tax/spain.html': 'Complete guide to Spain digital nomad visa tax rules including Beckham Law and tax treaties for remote workers.',
    'digital-nomad-tax/thailand.html': 'Complete guide to Thailand digital nomad visa tax rules including SMART visa and remittance-based taxation.',
}

count = 0

# Fix index.html
idx_path = os.path.join(ROOT, 'index.html')
with open(idx_path, 'r', encoding='utf-8') as f:
    c = f.read()
m = re.search(r'<meta\s+name="description"[^>]*content="([^"]*)"', c)
if m and len(m.group(1)) > 160:
    old = m.group(1)
    c = c.replace(f'content="{old}"', f'content="{INDEX_DESC}"', 1)
    # Also fix OG
    ogm = re.search(r'<meta\s+property="og:description"[^>]*content="([^"]*)"', c)
    if ogm:
        c = c.replace(f'content="{ogm.group(1)}"', f'content="{INDEX_DESC}"', 1)
    twm = re.search(r'<meta\s+name="twitter:description"[^>]*content="([^"]*)"', c)
    if twm:
        c = c.replace(f'content="{twm.group(1)}"', f'content="{INDEX_DESC}"', 1)
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(c)
    count += 1
    print(f'  FIXED: index.html ({len(old)}c -> {len(INDEX_DESC)}c)')

# Fix state pages
state_dir = os.path.join(ROOT, 'tools', 'quarterly-tax-calculator')
for st, st_name in STATE_SHORT.items():
    fpath = os.path.join(state_dir, f'{st}.html')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<meta\s+name="description"[^>]*content="([^"]*)"', c)
    if m and len(m.group(1)) > 160:
        new_desc = STATE_DESC.replace('[STATE]', st_name)
        old = m.group(1)
        c = c.replace(f'content="{old}"', f'content="{new_desc}"', 1)
        # Fix OG + twitter
        for attr in ['property="og:description"', 'name="twitter:description"']:
            om = re.search(f'<meta\\s+{attr}[^>]*content="([^"]*)"', c)
            if om and len(om.group(1)) > 160:
                c = c.replace(f'content="{om.group(1)}"', f'content="{new_desc}"', 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1
        if count <= 5:
            print(f'  FIXED: tools/quarterly-tax-calculator/{st}.html ({len(old)}c -> {len(new_desc)}c)')

# Fix OG descriptions on 404 and nomad pages
for rel, new_og in OG_FIXES.items():
    fpath = os.path.join(ROOT, rel)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    # Fix og:description
    ogm = re.search(r'<meta\s+property="og:description"[^>]*content="([^"]*)"', c)
    if ogm and ogm.group(1) != new_og:
        c = c.replace(f'content="{ogm.group(1)}"', f'content="{new_og}"', 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'  OG FIXED: {rel}')

print(f'\nTotal descriptions fixed: {count}')
