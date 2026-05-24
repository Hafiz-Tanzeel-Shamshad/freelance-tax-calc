import os, re

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

all_html = []
for root, dirs, files in os.walk(ROOT):
    if 'assets' in root: continue
    for f in files:
        if f.endswith('.html') and not f.startswith('_'):
            all_html.append(os.path.relpath(os.path.join(root, f), ROOT).replace('\\', '/'))

TITLE_FIXES = {
    'tools/quarterly-tax-calculator.html': 'Quarterly Tax Calculator \u2014 Free Estimator for Freelancers',
    'tools/gig-deduction-finder.html': 'Gig Worker Tax Deduction Finder \u2014 Free Tool',
    'tools/first-paycheck-calculator.html': 'First Paycheck Calculator \u2014 Take-Home Pay Estimator',
    'tools/side-hustle-tax-estimator.html': 'Side Hustle Tax Calculator \u2014 How Much You Owe',
    'tools/finance-app-recommender.html': 'Best Budgeting App for Freelancers \u2014 Free Quiz',
    'tools/digital-nomad-tax-calculator.html': 'Digital Nomad Tax Calculator \u2014 26 Countries',
    'tools/1099-vs-w2-calculator.html': '1099 vs W-2 Calculator \u2014 Compare Take-Home Pay',
    'tools/rate-calculator-debt-planner.html': 'Freelancer Rate Calculator & Debt Payoff Planner',
    'tools/retirement-calculator.html': 'Self-Employed Retirement Calculator \u2014 Solo 401k & SEP',
    'tools/budget-invoice-calculators.html': 'Freelance Budget & Invoice Tax Calculator',
    'tools/freelance-hourly-rate-calculator.html': 'Freelance Hourly Rate Calculator \u2014 Free Tool',
    'deductions/airbnb.html': 'Airbnb Host Tax Deductions 2026 \u2014 Complete Guide',
    'deductions/doordash.html': 'DoorDash Tax Deductions 2026 \u2014 Write-Off Guide',
    'deductions/etsy.html': 'Etsy Seller Tax Deductions 2026 \u2014 Write-Off Guide',
    'deductions/fiverr.html': 'Fiverr Freelancer Tax Deductions 2026 \u2014 Guide',
    'deductions/instacart.html': 'Instacart Shopper Tax Deductions 2026 \u2014 Guide',
    'deductions/uber.html': 'Uber & Lyft Driver Tax Deductions 2026 \u2014 Guide',
    'digital-nomad-tax/estonia.html': 'Estonia Digital Nomad Visa Tax Guide 2026',
    'digital-nomad-tax/mexico.html': 'Mexico Digital Nomad Visa Tax Guide 2026',
    'digital-nomad-tax/portugal.html': 'Portugal Digital Nomad Visa Tax Guide 2026',
    'digital-nomad-tax/spain.html': 'Spain Digital Nomad Visa Tax Guide 2026',
    'digital-nomad-tax/thailand.html': 'Thailand Digital Nomad Visa Tax Guide 2026',
    'guides/index.html': 'Free Tax & Finance Guides for Freelancers 2026',
    'guides/quarterly-taxes-guide.html': 'Quarterly Taxes Guide for Freelancers 2026',
    'guides/gig-worker-deductions.html': 'Gig Worker Deductions Guide \u2014 What You Can Write Off',
    'guides/1099-vs-w2-comparison.html': '1099 vs W-2 \u2014 Which is Better for You?',
    'legal/about.html': 'About Us \u2014 Free Freelancer Tax Calculators',
    'legal/privacy-policy.html': 'Privacy Policy \u2014 FreelanceTaxCalc',
    'legal/terms.html': 'Terms of Service \u2014 FreelanceTaxCalc',
    'legal/disclaimer.html': 'Disclaimer \u2014 FreelanceTaxCalc',
    'legal/contact.html': 'Contact Redirect \u2014 FreelanceTaxCalc',
    'index.html': 'Free Freelancer Tax Calculators & Finance Tools 2026',
    '404.html': '404 \u2014 Page Not Found | FreelanceTaxCalc',
    'contact/index.html': 'Contact Us \u2014 FreelanceTaxCalc',
    'pre-launch-checklist.html': 'Pre-Launch Checklist \u2014 FreelanceTaxCalc',
}

DESC_FIXES = {
    'tools/quarterly-tax-calculator.html': 'Calculate your quarterly estimated taxes as a freelancer. Free tool with state rates. See payment amounts and due dates instantly.',
    'tools/gig-deduction-finder.html': 'Find every tax deduction you qualify for as a gig worker. Free tool for DoorDash, Uber, Etsy, and freelance workers.',
    'tools/first-paycheck-calculator.html': 'See your first paycheck broken down before you start working. Free salary-to-take-home calculator with 2026 tax brackets.',
    'tools/side-hustle-tax-estimator.html': 'Estimate taxes on your side hustle income. Free calculator for freelancers with a regular job. Shows self-employment tax.',
    'tools/finance-app-recommender.html': 'Find the perfect budgeting app for your freelance finances. Free quiz matches you with the best app from 12 top options.',
    'tools/digital-nomad-tax-calculator.html': 'Calculate tax obligations as a digital nomad. Free tool covering FEIE, 183-day rule, and tax treaties across 26 countries.',
    'tools/1099-vs-w2-calculator.html': 'Compare 1099 contractor vs W-2 employee income after taxes. Free calculator with QBI deduction, SE tax, and breakeven analysis.',
    'tools/rate-calculator-debt-planner.html': 'Find your ideal freelance hourly rate and compare debt payoff methods. Two free tools in one page for freelancers.',
    'tools/retirement-calculator.html': 'Maximize retirement savings as a self-employed person. Free calculator compares Solo 401k, SEP-IRA, and other plans.',
    'tools/budget-invoice-calculators.html': 'Free 50/30/20 budget calculator and freelance invoice tax calculator for US, CA, UK, EU, and AU with VAT and sales tax.',
    'tools/freelance-hourly-rate-calculator.html': 'Calculate your ideal freelance hourly rate based on desired salary, expenses, and billable hours. Free interactive tool.',
    'deductions/airbnb.html': 'Complete list of Airbnb host tax deductions for 2026. Learn what cleaning, supplies, utilities, and maintenance costs you can write off.',
    'deductions/doordash.html': 'Complete list of DoorDash driver tax deductions for 2026. Learn what mileage, phone, and platform fees you can write off.',
    'deductions/etsy.html': 'Complete list of Etsy seller tax deductions for 2026. Learn what materials, fees, shipping, and tools you can write off.',
    'deductions/fiverr.html': 'Complete list of Fiverr freelancer tax deductions for 2026. Learn what subscriptions, tools, and home office costs you can write off.',
    'deductions/instacart.html': 'Complete list of Instacart shopper tax deductions for 2026. Learn what mileage, phone, and shopping supplies you can write off.',
    'deductions/uber.html': 'Complete list of Uber and Lyft driver tax deductions for 2026. Learn what mileage, tolls, and platform fees you can write off.',
    'digital-nomad-tax/estonia.html': 'Complete guide to Estonia digital nomad visa tax rules including e-Residency and double tax treaties for remote workers.',
    'digital-nomad-tax/mexico.html': 'Complete guide to Mexico digital nomad visa tax rules including residency, FEIE, and tax obligations for US remote workers.',
    'digital-nomad-tax/portugal.html': 'Complete guide to Portugal digital nomad visa and D7 tax rules including NHR regime and double tax treaties for remote workers.',
    'digital-nomad-tax/spain.html': 'Complete guide to Spain digital nomad visa tax rules including Beckham Law, residency, and tax treaties for remote workers.',
    'digital-nomad-tax/thailand.html': 'Complete guide to Thailand digital nomad visa tax rules including SMART visa and remittance-based taxation for remote workers.',
    'guides/index.html': 'Free guides on freelancer taxes, quarterly payments, deductions, and digital nomad finances. Expert-written for self-employed workers.',
    'guides/quarterly-taxes-guide.html': 'Everything freelancers need to know about quarterly estimated taxes. Covers deadlines, Form 1040-ES, and avoiding penalties.',
    'guides/gig-worker-deductions.html': 'Complete guide to gig worker tax deductions for 2026. What DoorDash, Uber, Etsy, and freelance workers can write off.',
    'guides/1099-vs-w2-comparison.html': 'Compare 1099 contractor and W-2 employee income, taxes, and benefits. See which status leaves you with more take-home pay.',
    'legal/about.html': 'FreelanceTaxCalc provides free tax calculators for freelancers and self-employed people. No login required. All tools run in your browser.',
    'legal/privacy-policy.html': 'Privacy policy for FreelanceTaxCalc. Learn about data collection, cookies, Google AdSense, and your GDPR and CCPA rights.',
    'legal/terms.html': 'Terms of service for FreelanceTaxCalc. By using our free tax calculators, you agree to the terms governing use, disclaimers, and liability.',
    'legal/disclaimer.html': 'Disclaimer for FreelanceTaxCalc. The tax calculators provide estimates only. Consult a CPA for professional tax advice.',
    'legal/contact.html': 'Contact redirect for FreelanceTaxCalc.',
    '404.html': 'Page not found. The page you are looking for does not exist or has been moved. Find free tax calculators for freelancers on our homepage.',
    'pre-launch-checklist.html': 'Pre-launch checklist for FreelanceTaxCalc site. Verify all pages, links, and tools before going live.',
}

count = 0
for rel in all_html:
    fpath = os.path.join(ROOT, rel)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Fix title
    if rel in TITLE_FIXES:
        new_title = TITLE_FIXES[rel]
        t = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        if t:
            old_title = t.group(1)
            if old_title.strip() != new_title:
                content = content.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>', 1)
                changed = True

    # Fix meta description
    if rel in DESC_FIXES:
        new_desc = DESC_FIXES[rel]
        md = re.search(r'<meta\s+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content)
        if md and md.group(1) != new_desc:
            old_desc = md.group(1)
            content = content.replace(f'content="{old_desc}"', f'content="{new_desc}"', 1)
            changed = True

    # Fix og:description
    if rel in DESC_FIXES:
        new_desc = DESC_FIXES[rel]
        ogd = re.search(r'<meta\s+property=["\']og:description["\'][^>]*content=["\']([^"\']*)["\']', content)
        if ogd and ogd.group(1) != new_desc:
            old_og = ogd.group(1)
            content = content.replace(f'content="{old_og}"', f'content="{new_desc}"', 1)
            changed = True

    # Fix twitter:description
    if rel in DESC_FIXES:
        new_desc = DESC_FIXES[rel]
        twd = re.search(r'<meta\s+name=["\']twitter:description["\'][^>]*content=["\']([^"\']*)["\']', content)
        if twd and twd.group(1) != new_desc:
            old_tw = twd.group(1)
            content = content.replace(f'content="{old_tw}"', f'content="{new_desc}"', 1)
            changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Fixed {count} pages (titles + descriptions)")
