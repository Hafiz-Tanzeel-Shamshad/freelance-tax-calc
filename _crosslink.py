import os, re, json

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

# Tool relationships: which tools are related to which
RELATED = {
    "quarterly-tax-calculator.html": {
        "title": "Quarterly Tax Estimator",
        "links": [
            ("/tools/gig-deduction-finder.html", "Gig Worker Deduction Finder", "Find deductions to lower your quarterly tax bill"),
            ("/tools/side-hustle-tax-estimator.html", "Side Hustle Tax Estimator", "See if you owe taxes on side income"),
            ("/tools/1099-vs-w2-calculator.html", "1099 vs W-2 Calculator", "Compare contractor vs employee taxes"),
            ("/tools/retirement-calculator.html", "Retirement Calculator", "Save for retirement while reducing taxable income"),
        ]
    },
    "gig-deduction-finder.html": {
        "title": "Gig Worker Deduction Finder",
        "links": [
            ("/tools/quarterly-tax-calculator.html", "Quarterly Tax Estimator", "Calculate what you owe after deductions"),
            ("/tools/side-hustle-tax-estimator.html", "Side Hustle Tax Estimator", "Estimate total tax on gig income"),
            ("/tools/budget-invoice-calculators.html", "Freelance Invoice Tax Calculator", "Add VAT/GST to invoices"),
            ("/tools/first-paycheck-calculator.html", "First Paycheck Calculator", "See take-home pay after deductions"),
        ]
    },
    "first-paycheck-calculator.html": {
        "title": "First Paycheck Calculator",
        "links": [
            ("/tools/side-hustle-tax-estimator.html", "Side Hustle Tax Estimator", "Add side income to your paycheck calculation"),
            ("/tools/quarterly-tax-calculator.html", "Quarterly Tax Estimator", "Plan quarterly payments if self-employed"),
            ("/tools/freelance-hourly-rate-calculator.html", "Freelance Hourly Rate Calculator", "Convert salary to freelance rate"),
            ("/tools/budget-invoice-calculators.html", "Student Budget Calculator", "Budget your take-home pay with 50/30/20"),
        ]
    },
    "side-hustle-tax-estimator.html": {
        "title": "Side Hustle Tax Estimator",
        "links": [
            ("/tools/gig-deduction-finder.html", "Gig Worker Deduction Finder", "Reduce your side hustle tax bill"),
            ("/tools/quarterly-tax-calculator.html", "Quarterly Tax Estimator", "Calculate quarterly payments on side income"),
            ("/tools/1099-vs-w2-calculator.html", "1099 vs W-2 Calculator", "Should you take contractor or employee work?"),
            ("/tools/first-paycheck-calculator.html", "First Paycheck Calculator", "See how side income affects take-home pay"),
        ]
    },
    "finance-app-recommender.html": {
        "title": "Best Finance App Recommender",
        "links": [
            ("/tools/budget-invoice-calculators.html", "Student Budget Calculator", "Apply 50/30/20 rule after choosing an app"),
            ("/tools/retirement-calculator.html", "Retirement Calculator", "Pick the right retirement plan for your app"),
            ("/tools/rate-calculator-debt-planner.html", "Debt Payoff Planner", "Pay off debt with your budgeting app"),
            ("/tools/first-paycheck-calculator.html", "First Paycheck Calculator", "See your take-home pay"),
        ]
    },
    "digital-nomad-tax-calculator.html": {
        "title": "Digital Nomad Tax Calculator",
        "links": [
            ("/tools/quarterly-tax-calculator.html", "Quarterly Tax Estimator", "Plan US tax payments while abroad"),
            ("/tools/1099-vs-w2-calculator.html", "1099 vs W-2 Calculator", "Compare remote work options"),
            ("/tools/freelance-hourly-rate-calculator.html", "Freelance Hourly Rate Calculator", "Set rates for remote clients"),
            ("/tools/side-hustle-tax-estimator.html", "Side Hustle Tax Estimator", "Tax on international side income"),
        ]
    },
    "1099-vs-w2-calculator.html": {
        "title": "1099 vs W-2 Tax Calculator",
        "links": [
            ("/tools/quarterly-tax-calculator.html", "Quarterly Tax Estimator", "Calculate quarterly taxes if you go 1099"),
            ("/tools/gig-deduction-finder.html", "Gig Worker Deduction Finder", "Find deductions as a 1099 worker"),
            ("/tools/freelance-hourly-rate-calculator.html", "Freelance Hourly Rate Calculator", "Set your 1099 hourly rate"),
            ("/tools/retirement-calculator.html", "Retirement Calculator", "Choose retirement plan for contractors"),
        ]
    },
    "rate-calculator-debt-planner.html": {
        "title": "Debt Payoff Planner",
        "links": [
            ("/tools/freelance-hourly-rate-calculator.html", "Freelance Hourly Rate Calculator", "Calculate rate to pay debt faster"),
            ("/tools/budget-invoice-calculators.html", "Student Budget Calculator", "Budget for debt payments"),
            ("/tools/first-paycheck-calculator.html", "First Paycheck Calculator", "See how debt affects take-home pay"),
            ("/tools/retirement-calculator.html", "Retirement Calculator", "Balance debt payoff with retirement savings"),
        ]
    },
    "freelance-hourly-rate-calculator.html": {
        "title": "Freelance Hourly Rate Calculator",
        "links": [
            ("/tools/quarterly-tax-calculator.html", "Quarterly Tax Estimator", "Calculate taxes on your freelance earnings"),
            ("/tools/gig-deduction-finder.html", "Gig Worker Deduction Finder", "Reduce taxable income with deductions"),
            ("/tools/1099-vs-w2-calculator.html", "1099 vs W-2 Calculator", "Compare freelance vs employee income"),
            ("/tools/rate-calculator-debt-planner.html", "Debt Payoff Planner", "Plan debt payoff with freelance income"),
        ]
    },
    "retirement-calculator.html": {
        "title": "Self-Employed Retirement Calculator",
        "links": [
            ("/tools/quarterly-tax-calculator.html", "Quarterly Tax Estimator", "See how retirement contributions reduce taxes"),
            ("/tools/gig-deduction-finder.html", "Gig Worker Deduction Finder", "Maximize retirement + expense deductions"),
            ("/tools/freelance-hourly-rate-calculator.html", "Freelance Hourly Rate Calculator", "Set rate to hit retirement goals"),
            ("/tools/finance-app-recommender.html", "Best Finance App Recommender", "Find an app to track retirement savings"),
        ]
    },
    "budget-invoice-calculators.html": {
        "title": "Student Budget & Invoice Tax Calculator",
        "links": [
            ("/tools/first-paycheck-calculator.html", "First Paycheck Calculator", "Budget your actual take-home pay"),
            ("/tools/finance-app-recommender.html", "Best Finance App Recommender", "Find an app to track your budget"),
            ("/tools/rate-calculator-debt-planner.html", "Debt Payoff Planner", "Pay off debt with your budget surplus"),
            ("/tools/freelance-hourly-rate-calculator.html", "Freelance Hourly Rate Calculator", "Set rates for invoicing clients"),
        ]
    },
}

RELATED_HTML = '''<!-- Related Tools -->
<section class="related-tools" aria-label="Related Tools">
  <div class="container">
    <h2>Related Tools You Might Need</h2>
    <div class="related-grid">
      {links}
    </div>
  </div>
</section>

<style>
.related-tools{{background:#fff;padding:48px 0;border-top:1px solid #E8ECF0;margin-top:0}}
.related-tools h2{{font-family:"DM Serif Display",serif;font-size:22px;color:#1A1A2E;text-align:center;margin-bottom:24px}}
.related-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;max-width:900px;margin:0 auto}}
.related-grid a{{display:block;background:#F4F6F9;border-radius:10px;padding:16px;font-size:14px;color:#1A1A2E;font-weight:500;transition:all 0.3s ease;text-decoration:none;border:1px solid transparent}}
.related-grid a:hover{{background:#F0FDF9;border-color:#00C896;color:#00C896;transform:translateY(-2px)}}
.related-grid a small{{display:block;font-weight:400;color:#6B7280;font-size:13px;margin-top:4px}}
</style>'''

def add_related_tools(filepath, data):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links_html = "\n      ".join(
        f'<a href="{url}">{title}<small>{desc}</small></a>'
        for url, title, desc in data["links"]
    )
    
    section = RELATED_HTML.replace("{links}", links_html)
    
    if 'Related Tools' in content:
        print(f"  SKIP (already has related tools): {os.path.basename(filepath)}")
        return False
    
    # Insert before </body>
    if '</body>' in content:
        content = content.replace('</body>', section + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ADDED: {os.path.basename(filepath)}")
        return True
    else:
        print(f"  ERROR: no </body> in {filepath}")
        return False

# Process tools
tools_dir = os.path.join(ROOT, 'tools')
for fname, data in RELATED.items():
    fpath = os.path.join(tools_dir, fname)
    if os.path.exists(fpath):
        add_related_tools(fpath, data)
    else:
        print(f"  NOT FOUND: {fpath}")

print("\nDone!")
