import os, re, json

BASE = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"
TOOL_DIR = os.path.join(BASE, "tools", "quarterly-tax-calculator")
os.makedirs(TOOL_DIR, exist_ok=True)

# Load the main page as template
with open(os.path.join(BASE, "tools", "quarterly-tax-calculator.html"), encoding="utf-8") as f:
    template = f.read()

states = [
    ("Alabama", 0.05, "Moderate 5% income tax"),
    ("Alaska", 0, "No state income tax"),
    ("Arizona", 0.025, "Low 2.5% flat tax"),
    ("Arkansas", 0.049, "4.9% income tax"),
    ("California", 0.075, "High 7.5–13.3% progressive tax"),
    ("Colorado", 0.044, "Flat 4.4% income tax"),
    ("Connecticut", 0.05, "5% income tax"),
    ("Delaware", 0.055, "5.5% income tax"),
    ("Florida", 0, "No state income tax"),
    ("Georgia", 0.0549, "5.49% income tax"),
    ("Hawaii", 0.072, "High 7.2% income tax"),
    ("Idaho", 0.058, "5.8% income tax"),
    ("Illinois", 0.0495, "Flat 4.95% income tax"),
    ("Indiana", 0.0315, "Flat 3.15% income tax"),
    ("Iowa", 0.057, "5.7% income tax"),
    ("Kansas", 0.0525, "5.25% income tax"),
    ("Kentucky", 0.045, "Flat 4.5% income tax"),
    ("Louisiana", 0.0425, "4.25% income tax"),
    ("Maine", 0.0645, "6.45% income tax"),
    ("Maryland", 0.05, "5% income tax"),
    ("Massachusetts", 0.05, "Flat 5% income tax"),
    ("Michigan", 0.0405, "Flat 4.05% income tax"),
    ("Minnesota", 0.0785, "High 7.85% income tax"),
    ("Mississippi", 0.047, "4.7% income tax"),
    ("Missouri", 0.0495, "4.95% income tax"),
    ("Montana", 0.0575, "5.75% income tax"),
    ("Nebraska", 0.0584, "5.84% income tax"),
    ("Nevada", 0, "No state income tax"),
    ("New Hampshire", 0, "No state income tax"),
    ("New Jersey", 0.0637, "6.37% income tax"),
    ("New Mexico", 0.04875, "4.88% income tax"),
    ("New York", 0.065, "High 6.5–10.9% progressive tax"),
    ("North Carolina", 0.045, "Flat 4.5% income tax"),
    ("North Dakota", 0.029, "Low 2.9% income tax"),
    ("Ohio", 0.035, "3.5% income tax"),
    ("Oklahoma", 0.0475, "4.75% income tax"),
    ("Oregon", 0.0875, "High 8.75% income tax"),
    ("Pennsylvania", 0.0307, "Flat 3.07% income tax"),
    ("Rhode Island", 0.054, "5.4% income tax"),
    ("South Carolina", 0.064, "6.4% income tax"),
    ("South Dakota", 0, "No state income tax"),
    ("Tennessee", 0, "No state income tax"),
    ("Texas", 0, "No state income tax"),
    ("Utah", 0.0485, "Flat 4.85% income tax"),
    ("Vermont", 0.0675, "6.75% income tax"),
    ("Virginia", 0.0575, "5.75% income tax"),
    ("Washington", 0, "No state income tax"),
    ("West Virginia", 0.0535, "5.35% income tax"),
    ("Wisconsin", 0.053, "5.3% income tax"),
    ("Wyoming", 0, "No state income tax"),
    ("District of Columbia", 0.0675, "6.75% income tax"),
]

for state_name, rate, note in states:
    slug = state_name.lower().replace(" ", "-").replace("district-of-columbia", "dc")
    no_tax = rate == 0
    no_tax_tag = " — No State Income Tax" if no_tax else ""
    state_abbr = state_name if state_name != "District of Columbia" else "DC"

    # Title
    title = f"Freelancer Tax Calculator {state_name} 2026 — Self-Employed Quarterly Tax Estimator{no_tax_tag} | FreelanceTaxCalc"

    # Meta description
    if no_tax:
        meta = f"Free freelancer tax calculator for {state_name}. Self-employed quarterly tax estimator for {state_name} freelancers and gig workers. {note}. See how much to save for taxes in {state_name} 2026."
    else:
        meta = f"Free freelancer tax calculator for {state_name}. Self-employed quarterly tax estimator with {note.lower()}. See how much {state_name} freelancers should save for quarterly taxes."

    meta = meta[:170]  # cap

    # H1
    h1 = f"Freelancer Tax Calculator {state_name} 2026"

    # Description paragraph
    if no_tax:
        desc_p = f"Estimate your quarterly and annual self-employment taxes as a freelancer, gig worker, Uber driver, or Etsy seller in {state_name}. {note}, which means you only pay federal self-employment tax and federal income tax. Updated for 2026."
    else:
        desc_p = f"Estimate your quarterly and annual self-employment taxes as a freelancer, gig worker, Uber driver, or Etsy seller in {state_name}. Includes {note.lower()} on top of federal self-employment and income taxes. Updated for 2026."

    # OG
    og_title = f"Freelancer Tax Calculator {state_name} 2026 — Self-Employed Quarterly Estimator"
    og_desc = f"Free freelancer tax calculator for {state_name}. Quarterly tax estimator with {note.lower() if not no_tax else 'no state income tax'}."

    # Canonical
    canonical = f"https://freelancetaxcalc.online/tools/quarterly-tax-calculator/{slug}"

    # Make the page
    page = template[:]

    # Title
    page = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', page)

    # Meta description
    page = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{meta}">', page)

    # Canonical
    page = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{canonical}">', page)

    # OG title
    og_title_esc = og_title.replace("&", "&amp;")
    page = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{og_title_esc}">', page)

    # OG description
    og_desc_esc = og_desc.replace("&", "&amp;")
    page = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{og_desc_esc}">', page)

    # OG url
    page = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{canonical}">', page)

    # Twitter title
    page = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{og_title_esc}">', page)

    # Twitter description
    page = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{og_desc_esc}">', page)

    # JSON-LD name + description
    page = re.sub(
        r'"name": "Self-Employed & Freelancer Quarterly Tax Calculator"',
        f'"name": "Freelancer Tax Calculator {state_name}"',
        page
    )
    jsonld_desc = f"Free self-employment tax calculator for freelancers, gig workers, and small businesses in {state_name}."
    page = re.sub(
        r'"description": "Free self-employment tax calculator for freelancers, gig workers, Uber drivers, DoorDashers, and Etsy sellers\. Quarterly tax estimator with state taxes\."',
        f'"description": "{jsonld_desc}"',
        page
    )

    # Breadcrumb
    page = re.sub(
        r'"name": "Quarterly Tax Calculator"',
        f'"name": "Quarterly Tax Calculator {state_name}"',
        page
    )

    # H1
    page = re.sub(
        r'<h1>Self-Employed &amp; Freelancer Quarterly Tax Calculator 2026</h1>',
        f'<h1>{h1}</h1>',
        page
    )

    # Description paragraph
    page = re.sub(
        r'<p>Estimate your quarterly and annual self-employment taxes as a freelancer, gig worker, Uber driver, DoorDasher, or Etsy seller\. Works for USA, Canada, and UK\. Updated for 2026\.</p>',
        f'<p>{desc_p}</p>',
        page
    )

    # Breadcrumb text
    page = re.sub(
        r'<span>Quarterly Tax Calculator</span>',
        f'<span>Quarterly Tax Calculator {state_name}</span>',
        page
    )

    # Auto-select state via JS injection (since options are generated by JS)
    state_js = f'''
  // Auto-select {state_name}
  setTimeout(function(){{
    var sel = document.getElementById('stateProvince');
    if(sel){{ sel.value = '{state_name}'; }}
  }}, 50);
'''
    page = page.replace(
        "  // ─── ENTER KEY TRIGGER CALCULATE ───",
        state_js + "\n  // ─── ENTER KEY TRIGGER CALCULATE ───"
    )

    # Add SEO content section for this state (before the generic content about US/Canada/UK)
    if no_tax:
        state_rate_desc = "no state income tax"
        savings_pct = "25% of their income for taxes"
        state_tax_note = f"This means you only need to worry about federal self-employment tax (15.3%) and federal income tax when calculating your quarterly payments. Since {state_name} has no state income tax, you only need to pay the IRS — not a state tax agency."
    else:
        # Extract the tax rate from note
        note_parts = note.split(" income tax")[0] if " income tax" in note else note
        state_rate_desc = f"a {note_parts} rate"
        savings_pct = "28-32% of their income for taxes"
        state_tax_note = f"This means your total tax rate in {state_name} includes both federal taxes and state income tax. In addition to IRS payments, {state_name} requires state estimated tax payments on a similar schedule."

    state_seo = f'''
    <h2>Why {state_name} Freelancers Need This Tax Calculator</h2>
    <p>{state_name} has {state_rate_desc}. {state_tax_note} Whether you drive for Uber, deliver for DoorDash, sell on Etsy, or freelance as a designer or developer, this {state_name} quarterly tax calculator gives you accurate payment amounts based on your specific location.</p>
    <p>Freelancers in {state_name} should save {savings_pct} to cover federal self-employment tax, federal income tax, and state income tax. The exact percentage depends on your annual earnings and filing status — use this calculator to get precise numbers.</p>
    <h2>Quarterly Tax Due Dates for {state_name} Freelancers 2026</h2>
    <p>As a self-employed freelancer in {state_name}, you must make estimated quarterly tax payments to the IRS on April 15, June 15, September 15, 2026 and January 15, 2027. {f"Since {state_name} has no state income tax, you only need to pay the IRS — not a state tax agency." if no_tax else f"In addition to IRS payments, {state_name} requires state estimated tax payments on a similar schedule."} Missing these deadlines results in underpayment penalties and interest charges.</p>
    '''

    # Insert state SEO after the How to Use section but before the generic What Are Quarterly Taxes section
    # Find the "What Are Quarterly Estimated Taxes?" H2 and insert before it
    page = page.replace(
        '<h2>What Are Quarterly Estimated Taxes?</h2>',
        state_seo.strip() + '\n\n    <h2>What Are Quarterly Estimated Taxes?</h2>'
    )

    # Write file
    fname = f"{slug}.html"
    fpath = os.path.join(TOOL_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(page)

    print(f"  Created: {fname}")

print(f"\nDone! {len(states)} state pages generated.")
