import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class MasterSEOAgent:
    def __init__(self, target_url):
        self.url = target_url.rstrip('/')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://google.com)'
        }
        self.audit_issues = []
        self.audit_passed = []
        self.generated_pages = []

        self.niches = [
            {
                "id": "uberdriver",
                "title_keyword": "Uber & Rideshare Driver",
                "description": "Calculate your rideshare net income, track self-employment tax obligations, and discover hidden mileage deductions.",
                "faq_q1": "What deductions can rideshare drivers claim?",
                "faq_a1": "You can write off standard mileage, passenger refreshments, phone mounts, dashcams, and a percentage of your phone bill."
            },
            {
                "id": "fiverrfreelancer",
                "title_keyword": "Fiverr Graphic Designer & Writer",
                "description": "Estimate your freelance take-home pay after platform fees, income taxes, and creative software expenses.",
                "faq_q1": "How do I calculate taxes on platform earnings?",
                "faq_a1": "Track your gross payouts before fees. Platform commissions and software subscriptions count as direct business expenses."
            },
            {
                "id": "doordashcourier",
                "title_keyword": "DoorDash & Food Delivery Courier",
                "description": "Track your 1099 food delivery earnings, calculate quarterly tax estimates, and maximize vehicle write-offs.",
                "faq_q1": "Do delivery drivers pay quarterly estimated taxes?",
                "faq_a1": "Yes, if you expect to owe over a certain threshold at year-end, you must make quarterly payments to avoid underpayment penalties."
            }
        ]

        self.countries = [
            {"code": "us", "name": "United States", "currency": "USD", "authority": "IRS", "term": "1099 Self-Employment Tax", "year": "2026"},
            {"code": "uk", "name": "United Kingdom", "currency": "GBP", "authority": "HMRC", "term": "Self Assessment & National Insurance", "year": "2026-27"},
            {"code": "ca", "name": "Canada", "currency": "CAD", "authority": "CRA", "term": "Self-Employed Income Tax & CPP", "year": "2026"}
        ]

        self.html_blueprint = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free {year} {niche_title} Tax Calculator ({country_name}) — FreelanceTaxCalc</title>
    <meta name="description" content="Free {year} tax estimator built specifically for {niche_title}s in the {country_name}. {niche_desc} No signup required.">
    <link rel="canonical" href="{domain}/{country_code}/{page_slug}.html">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
        header {{ border-bottom: 2px solid #eaeaea; padding-bottom: 20px; margin-bottom: 30px; }}
        .nav-logo {{ font-weight: bold; font-size: 24px; text-decoration: none; color: #111; }}
        .calculator-container {{ background: #f9f9f9; border: 1px solid #ddd; padding: 30px; border-radius: 8px; margin-bottom: 30px; }}
        .form-group {{ margin-bottom: 15px; }}
        label {{ display: block; margin-bottom: 5px; font-weight: 600; }}
        input {{ width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }}
        button {{ background: #0070f3; color: white; border: none; padding: 12px 20px; font-size: 16px; border-radius: 4px; cursor: pointer; font-weight: bold; }}
        .result-box {{ margin-top: 20px; padding: 15px; background: #eef7ff; border-left: 5px solid #0070f3; display: none; }}
        .disclaimer {{ font-size: 12px; color: #666; background: #fff8e6; padding: 15px; border: 1px solid #ffeeba; border-radius: 4px; margin-top: 40px; }}
        footer {{ margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; text-align: center; font-size: 14px; }}
        footer a {{ color: #0070f3; text-decoration: none; margin: 0 10px; }}
    </style>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "{year} {niche_title} Tax Calculator ({country_name})",
      "url": "{domain}/{country_code}/{page_slug}.html",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "All",
      "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "{currency}" }}
    }}
    </script>
</head>
<body>
    <header><a href="{domain}/" class="nav-logo">$ Freelance.TaxCalc</a></header>
    <main>
        <h1>Free {year} {niche_title} Tax Calculator for {country_name}</h1>
        <p>Built specifically for gig workers, self-employed contractors, and solo creators operating within the {country_name}.</p>
        <div class="calculator-container">
            <h3>Calculate Your Dynamic Net {currency} Earnings</h3>
            <div class="form-group">
                <label>Annual Gross Business Revenue ({currency}):</label>
                <input type="number" id="gross_income" placeholder="e.g. 50000">
            </div>
            <div class="form-group">
                <label>Total Tracked Expenses / Write-offs ({currency}):</label>
                <input type="number" id="business_expenses" placeholder="e.g. 8000">
            </div>
            <button onclick="runCalculations()">Calculate Net {tax_term}</button>
            <div id="results" class="result-box">
                <p><strong>Net Taxable Business Base:</strong> {currency}<span id="res_net_base">0</span></p>
                <p><strong>Estimated {tax_term} Due to {tax_authority}:</strong> {currency}<span id="res_tax_due">0</span></p>
            </div>
        </div>
        <section>
            <h2>How This {niche_title} Tax Tool Protects Your Revenue</h2>
            <p>Managing financials as an independent professional requires understanding net operating metrics. When processing revenues inside the {country_name}, calculating gross transaction numbers alone is not sufficient.</p>
            <h3>Understanding {tax_term} Requirements</h3>
            <p>Unlike standard payroll employees, independent contractors working as a {niche_title} must file assessments manually to the <strong>{tax_authority}</strong>.</p>
            <h3>Frequently Asked Questions</h3>
            <p><strong>{faq_q1}</strong><br>{faq_a1}</p>
        </section>
        <div class="disclaimer">
            <strong>Important Disclaimer:</strong> All tools on this website provide estimates for informational purposes only. Results do not constitute professional tax, financial, or legal advice. Always consult a certified CPA or tax authority professional.
        </div>
    </main>
    <footer>
        <p>&copy; 2026 FreelanceTaxCalc. All rights reserved.</p>
        <a href="{domain}/">Home Directory</a> |
        <a href="{domain}/privacy-policy.html">Privacy Policy</a> |
        <a href="{domain}/terms.html">Terms of Service</a> |
        <a href="{domain}/about.html">About Us</a> |
        <a href="{domain}/contact.html">Contact Us</a>
    </footer>
    <script>
    function runCalculations() {{
        const gross = parseFloat(document.getElementById('gross_income').value) || 0;
        const expenses = parseFloat(document.getElementById('business_expenses').value) || 0;
        const netBase = Math.max(0, gross - expenses);
        document.getElementById('res_net_base').innerText = netBase.toFixed(2);
        document.getElementById('res_tax_due').innerText = (netBase * 0.20).toFixed(2);
        document.getElementById('results').style.display = 'block';
    }}
    </script>
</body>
</html>"""

    def run_live_seo_audit(self):
        print(f"STEP 1: Running Live SEO & AdSense Audit on {self.url}...")
        try:
            res = requests.get(self.url, headers=self.headers, timeout=10)
            if res.status_code != 200:
                self.audit_issues.append(f"CRITICAL: Homepage down or returned {res.status_code}")
                return
            soup = BeautifulSoup(res.text, 'html.parser')
            html_lower = res.text.lower()

            if soup.find('title'):
                self.audit_passed.append("Meta Title tag verified.")
            else:
                self.audit_issues.append("MISSING: HTML <title> element.")
            if soup.find('meta', attrs={'name': 'description'}):
                self.audit_passed.append("Meta Description verified.")
            else:
                self.audit_issues.append("MISSING: Meta Description tag.")

            for term in ['privacy policy', 'terms of service', 'about us', 'contact']:
                if term in html_lower:
                    self.audit_passed.append(f"AdSense Safety: Found mention of '{term}'")
                else:
                    self.audit_issues.append(f"COMPLIANCE RISK: Missing visible link/text for '{term}'")

            print("\n--- AUDIT RESULTS ---")
            for p in self.audit_passed:
                print(f"  [PASS] {p}")
            for i in self.audit_issues:
                print(f"  [FAIL] {i}")
        except Exception as e:
            print(f"  [FAIL] Audit skipped due to connection failure: {e}")

    def generate_programmatic_pages(self):
        print("\nSTEP 2: Launching Programmatic SEO Page Engine...")
        for country in self.countries:
            dir_name = country["code"]
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            for niche in self.niches:
                slug = f"{niche['id']}-tax-calculator"
                page_content = self.html_blueprint.format(
                    domain=self.url,
                    lang_code="en-GB" if country["code"] == "uk" else "en-US",
                    year=country["year"],
                    niche_title=niche["title_keyword"],
                    niche_desc=niche["description"],
                    country_name=country["name"],
                    country_code=country["code"],
                    page_slug=slug,
                    currency=country["currency"],
                    tax_term=country["term"],
                    tax_authority=country["authority"],
                    faq_q1=niche["faq_q1"],
                    faq_a1=niche["faq_a1"]
                )
                file_path = os.path.join(dir_name, f"{slug}.html")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(page_content)
                relative_path = f"{country['code']}/{slug}.html"
                self.generated_pages.append(relative_path)
                print(f"  [OK] Generated: /{relative_path}")

    def build_sitemap(self):
        print("\nSTEP 3: Rebuilding sitemap.xml with new paths...")
        today = datetime.today().strftime('%Y-%m-%d')
        xml_entries = []

        core_paths = ["", "privacy-policy.html", "terms.html", "about.html", "contact.html"]
        for path in core_paths:
            full_url = f"{self.url}/{path}".rstrip('/')
            xml_entries.append(f'  <url>\n    <loc>{full_url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>')

        for page in self.generated_pages:
            xml_entries.append(f'  <url>\n    <loc>{self.url}/{page}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>')

        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(xml_entries) + "\n</urlset>"
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print("  [OK] sitemap.xml generated and saved to current directory.")

    def run_all(self):
        self.run_live_seo_audit()
        self.generate_programmatic_pages()
        self.build_sitemap()
        print("\nMission Complete. Upload the generated subfolders and sitemap.xml to your hosting space.")

if __name__ == "__main__":
    agent = MasterSEOAgent("freelancetaxcalc.online")
    agent.run_all()
