import os, re

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

STATES = {
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

count = 0
state_dir = os.path.join(ROOT, 'tools', 'quarterly-tax-calculator')
for st, st_name in STATES.items():
    fpath = os.path.join(state_dir, f'{st}.html')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    t = re.search(r'<title>(.*?)</title>', c, re.DOTALL)
    if t:
        old_title = t.group(1).strip()
        if len(old_title) > 60:
            # Build new title: [State] Tax Calculator 2026 \u2014 Free Tool
            new_title = f'{st_name} Tax Calculator 2026 \u2014 Free Tool'
            c = c.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>', 1)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c)
            count += 1
            if count <= 3:
                print(f'  FIXED: {st}.html ({len(old_title)}c -> {len(new_title)}c)')

print(f'\nFixed {count} state page titles')
