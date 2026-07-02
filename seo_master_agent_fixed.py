import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET

class MasterSEOAgentFixed:
    def __init__(self, target_url):
        self.url = target_url.rstrip('/')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://google.com)'
        }
        self.generated_pages = []

        self.niches = [
            {
                "id": "uberdriver",
                "title_keyword": "Uber & Rideshare Driver",
                "niche_keyword": "rideshare",
                "description": "Calculate your rideshare net income, track self-employment tax obligations, and discover hidden mileage deductions.",
                "deductions_text": "Rideshare drivers can deduct vehicle mileage at the standard rate, platform fees and commissions, phone and data plan (business portion), phone mount, dashcam, car washes, tolls, parking, water and refreshments for passengers, and a portion of auto insurance and maintenance.",
                "deadlines_text": "Quarterly estimated tax payments are due April 15, June 16, September 15, 2026, and January 15, 2027. Pay online via IRS Direct Pay or the IRS2Go app."
            },
            {
                "id": "fiverrfreelancer",
                "title_keyword": "Fiverr Graphic Designer & Writer",
                "niche_keyword": "freelance",
                "description": "Estimate your freelance take-home pay after platform fees, income taxes, and creative software expenses.",
                "deductions_text": "Fiverr freelancers can deduct platform service fees (20% commission), software subscriptions (Adobe, Figma, Canva), home office expenses, internet and phone costs, computer equipment, education and courses, and a portion of utilities.",
                "deadlines_text": "Quarterly estimated tax payments are due April 15, June 16, September 15, 2026, and January 15, 2027. Use IRS Direct Pay or EFTPS for online payments."
            },
            {
                "id": "doordashcourier",
                "title_keyword": "DoorDash & Food Delivery Courier",
                "niche_keyword": "delivery",
                "description": "Track your 1099 food delivery earnings, calculate quarterly tax estimates, and maximize vehicle write-offs.",
                "deductions_text": "DoorDash couriers can deduct vehicle mileage at $0.70/mile (2026 rate), insulated delivery bags, hot/cold packs, phone plan (business portion), parking fees, tolls, car washes, a portion of auto insurance, and Dasher Direct card fees.",
                "deadlines_text": "Quarterly estimated tax payments are due April 15, June 16, September 15, 2026, and January 15, 2027. DoorDash provides a yearly tax summary in your account."
            }
        ]

        self.countries = [
            {"code": "us", "name": "United States", "currency": "USD", "symbol": "$", "authority": "IRS", "term": "1099 Self-Employment Tax", "year": "2026", "rate": "0.153", "income_placeholder": "50000", "expenses_placeholder": "8000"},
            {"code": "uk", "name": "United Kingdom", "currency": "GBP", "symbol": "\u00a3", "authority": "HMRC", "term": "Self Assessment & National Insurance", "year": "2026-27", "rate": "0.09", "income_placeholder": "30000", "expenses_placeholder": "5000"},
            {"code": "ca", "name": "Canada", "currency": "CAD", "symbol": "C$", "authority": "CRA", "term": "Self-Employed Income Tax & CPP", "year": "2026", "rate": "0.105", "income_placeholder": "60000", "expenses_placeholder": "7000"}
        ]

        self.html_blueprint = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<title>{niche_title} Tax Calculator {year} ({country_name}) — Free Tool</title>
<meta name="description" content="Free {year} tax estimator for {niche_title}s in the {country_name}. {niche_desc} No signup required.">
<link rel="canonical" href="{domain}/tools/{country_code}/{page_slug}.html">
<meta name="dateModified" content="2026-06-07">
<link rel="alternate" type="application/rss+xml" title="Freelance Tax Calculator - Tips & Updates" href="/feed.xml" />
<meta property="og:title" content="Free {year} {niche_title} Tax Calculator ({country_name})">
<meta property="og:description" content="Free {year} tax estimator for {niche_title}s in the {country_name}. {niche_desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FreelanceTaxCalc">
<meta property="og:url" content="{domain}/tools/{country_code}/{page_slug}.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Free {year} {niche_title} Tax Calculator ({country_name})">
<meta name="twitter:description" content="Free {year} tax estimator for {niche_title}s in the {country_name}. {niche_desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<script type="application/ld+json">
[
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "{niche_title} Tax Calculator ({country_name})",
    "url": "{domain}/tools/{country_code}/{page_slug}.html",
    "description": "Free {year} tax estimator for {niche_title}s in the {country_name}.",
    "applicationCategory": "FinanceApplication",
    "operatingSystem": "All",
    "browserRequirements": "Requires JavaScript",
    "image": "https://freelancetaxcalc.online/favicon.svg",
    "publisher": {{
      "@type": "Organization",
      "name": "FreelanceTaxCalc",
      "url": "https://freelancetaxcalc.online",
      "sameAs": [
        "https://www.facebook.com/freelancetaxcalc",
        "https://twitter.com/freelancetaxcalc",
        "https://www.linkedin.com/company/freelancetaxcalc"
      ]
    }},
    "about": [
      {{ "@type": "Thing", "name": "freelance" }},
      {{ "@type": "Thing", "name": "tax" }},
      {{ "@type": "Thing", "name": "calculator" }},
      {{ "@type": "Thing", "name": "{niche_keyword}" }}
    ]
  }},
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://freelancetaxcalc.online/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Tools",
        "item": "https://freelancetaxcalc.online/tools/"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{niche_title} Tax Calculator {country_name}"
      }}
    ]
  }}
]
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "author": {{
    "@type": "Person",
    "name": "Tanzeel",
    "url": "https://freelancetaxcalc.online/legal/about.html"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "FreelanceTaxCalc",
    "url": "https://freelancetaxcalc.online",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://freelancetaxcalc.online/favicon.svg"
    }}
  }},
  "dateModified": "2026-06-07"
}}
</script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:"DM Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,sans-serif;font-size:16px;line-height:1.7;color:#1A1A2E;background:#F4F6F9;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
a{{text-decoration:none;color:inherit}}
ul{{list-style:none}}
.container{{max-width:1100px;margin:0 auto;padding:0 24px}}
.site-header{{background:#0A1628;border-bottom:1px solid rgba(255,255,255,0.05);position:sticky;top:0;z-index:100}}
.site-header .container{{display:flex;align-items:center;justify-content:space-between;height:64px}}
.header-logo{{display:flex;align-items:center;gap:10px;font-family:"DM Serif Display",serif;font-size:20px;font-weight:700;color:#fff}}
.logo-icon{{width:32px;height:32px;background:#00C896;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px;font-weight:700;flex-shrink:0}}
.header-back{{color:#B0B8C4;font-size:14px;transition:color 0.3s ease}}
.header-back:hover{{color:#00C896}}
.breadcrumb{{background:#fff;padding:12px 0;border-bottom:1px solid #E8ECF0;font-size:14px;color:#6B7280}}
.breadcrumb a{{color:#00C896;transition:color 0.3s ease}}
.breadcrumb a:hover{{color:#00B085}}
.breadcrumb span{{color:#6B7280}}
.page-title{{background:#fff;padding:28px 0 0}}
.page-title h1{{font-family:"DM Serif Display",serif;font-size:32px;color:#1A1A2E;margin-bottom:6px}}
.page-title p{{color:#6B7280;font-size:15px;max-width:680px}}
.tool-section{{padding:28px 0 60px;background:linear-gradient(180deg,#F4F6F9 0%,#FFFFFF 100%)}}
.tool-card{{background:#fff;border-radius:16px;padding:36px;box-shadow:0 8px 28px rgba(10,22,40,0.08);border:1px solid #E8ECF0}}
.tool-card h2{{font-family:"DM Serif Display",serif;font-size:22px;color:#1A1A2E;margin-bottom:4px}}
.tool-card .subtitle{{font-size:15px;color:#6B7280;margin-bottom:24px}}
.tool-layout{{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}}
@media(max-width:768px){{.tool-layout{{grid-template-columns:1fr}}}}
.form-group{{margin-bottom:20px}}
.form-group label{{display:block;font-weight:600;font-size:14px;color:#1A1A2E;margin-bottom:6px}}
.input-wrapper{{position:relative;display:flex;align-items:center}}
.input-prefix{{position:absolute;left:14px;font-weight:600;color:#6B7280;font-size:16px;pointer-events:none;z-index:1}}
.form-group input{{width:100%;padding:12px 14px 12px 32px;border:2px solid #DDE1E7;border-radius:8px;font-size:16px;font-family:"DM Sans",sans-serif;color:#1A1A2E;background:#fff;transition:border-color 0.3s ease;outline:none}}
.form-group input:focus{{border-color:#00C896;box-shadow:0 0 0 3px rgba(0,200,150,0.1)}}
.calc-btn{{width:100%;padding:14px 24px;background:#00C896;color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:600;cursor:pointer;transition:all 0.3s ease;font-family:inherit}}
.calc-btn:hover{{background:#00B085;transform:translateY(-1px)}}
.calc-btn:active{{transform:translateY(0)}}
.result-section{{margin-top:24px}}
.result-card{{background:#F0FDF8;border:1px solid #A7F3D0;border-radius:12px;padding:20px;display:none}}
.result-card p{{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(0,200,150,0.15);font-size:15px}}
.result-card p:last-child{{border-bottom:none;font-weight:700}}
.result-card .label{{color:#4B5563}}
.result-card .value{{color:#1A1A2E;font-weight:600}}
.content-section{{padding:0 0 60px}}
.content-section h2{{font-family:"DM Serif Display",serif;font-size:24px;color:#1A1A2E;margin-bottom:16px}}
.content-section h3{{font-family:"DM Serif Display",serif;font-size:18px;color:#1A1A2E;margin:20px 0 10px}}
.content-section p{{color:#4B5563;font-size:15px;line-height:1.8;margin-bottom:14px}}
.disclaimer-bar{{background:#FFF8E1;border-top:1px solid #FFE082;padding:16px 24px;font-size:13px;color:#6B7280;text-align:center}}
.disclaimer-bar .icon{{margin-right:6px}}
.disclaimer-bar a{{color:#00C896;text-decoration:underline}}
</style>
</head>
<body>

<noscript>
<div style="background:#FFF8E1;border:1px solid #FFD700;border-radius:10px;padding:20px;margin-bottom:24px">
<p><strong>JavaScript is required for the calculator.</strong> Enable JavaScript or visit our <a href="/guides/quarterly-taxes-guide.html">guide</a> for manual steps.</p>
</div>
</noscript>

<!-- HEADER -->
<header class="site-header" role="banner">
<div class="container">
<a href="/" class="header-logo" aria-label="FreelanceTaxCalc Home">
<span class="logo-icon" aria-hidden="true">$</span>
<span>Freelance<span class="logo-dot">.</span>TaxCalc</span>
</a>
<a href="/tools/" class="header-back">&larr; All Tools</a>
</div>
</header>

<!-- BREADCRUMB -->
<nav class="breadcrumb" aria-label="Breadcrumb">
<div class="container">
<a href="/">Home</a> / <a href="/tools/">Tools</a> / <span>{niche_title} Tax Calculator ({country_code_upper})</span>
</div>
</nav>

<!-- PAGE TITLE -->
<section class="page-title">
<div class="container">
<h1>{niche_title} Tax Calculator {year} — {country_name}</h1>
<p>{niche_desc}</p>
</div>
</section>

<!-- TOOL SECTION -->
<section class="tool-section">
<div class="container">
<div class="tool-layout">

<!-- INPUT COLUMN -->
<div class="tool-card">
<h2>Enter Your Income</h2>
<p class="subtitle">Calculate your estimated {tax_term}</p>

<div class="form-group">
<label for="gross-income">Annual Gross Income ({currency})</label>
<div class="input-wrapper">
<span class="input-prefix">{currency_symbol}</span>
<input type="number" id="gross-income" placeholder="e.g. {placeholder_income}" min="0" step="100">
</div>
</div>

<div class="form-group">
<label for="expenses">Business Expenses ({currency})</label>
<div class="input-wrapper">
<span class="input-prefix">{currency_symbol}</span>
<input type="number" id="expenses" placeholder="e.g. {placeholder_expenses}" min="0" step="100">
</div>
</div>

<button class="calc-btn" onclick="calculateTax()">Calculate {tax_term}</button>

<div class="result-section">
<div id="result-card" class="result-card">
<p><span class="label">Net Self-Employment Income</span> <span class="value" id="net-income">{currency_symbol}0</span></p>
<p><span class="label">{tax_term} Due to {tax_authority}</span> <span class="value" id="tax-due">{currency_symbol}0</span></p>
<p><span class="label">Effective Tax Rate</span> <span class="value" id="tax-rate">0%</span></p>
<p><span class="label">Est. Quarterly Payment</span> <span class="value" id="quarterly-payment">{currency_symbol}0</span></p>
</div>
</div>
</div>

<!-- INFO COLUMN -->
<div class="tool-card">
<h2>About This Tool</h2>
<p class="subtitle">For gig workers in the {country_name}</p>
<p style="font-size:15px;color:#4B5563;line-height:1.8;margin-bottom:14px">This calculator estimates your {tax_term} based on {year} {tax_authority} rates. Enter your gross income and deductible business expenses to get an instant estimate of what you owe.</p>
<p style="font-size:15px;color:#4B5563;line-height:1.8;margin-bottom:14px">Results are estimates only. Actual tax liability may vary based on filing status, credits, deductions, and other factors.</p>
<h3 style="font-family:'DM Serif Display',serif;font-size:18px;color:#1A1A2E;margin:20px 0 10px">Key Features</h3>
<ul style="font-size:15px;color:#4B5563;line-height:2">
<li>&bull; {year} {tax_authority} tax rates</li>
<li>&bull; Accounts for standard deduction</li>
<li>&bull; Quarterly payment estimates</li>
<li>&bull; Self-employment tax included</li>
</ul>
</div>
</div>
</div>
</section>

<!-- CONTENT SECTION -->
<section class="content-section">
<div class="container">
<h2>About {niche_title} Taxes in the {country_name}</h2>
<p>Working as a {niche_title} in the {country_name} means you are classified as an independent contractor. Unlike traditional employees, no taxes are withheld from your pay, making it essential to track your income and expenses throughout the year.</p>
<h3>Understanding {tax_term}</h3>
<p>As a self-employed worker, you are responsible for both the employee and employer portions of {tax_term_lower}. This is calculated on your net earnings — your gross income minus allowable business deductions. The {tax_authority} requires quarterly estimated payments if you expect to owe over a certain threshold.</p>
<h3>Common Deductions for {niche_title}</h3>
<p>{deductions_text}</p>
<h3>Quarterly Tax Deadlines</h3>
<p>{deadlines_text}</p>
</div>
</section>

<!-- RELATED TOOLS -->
<section class="related-tools" style="background:#fff;border-top:1px solid #E8ECF0;padding:40px 0">
<div class="container">
<h3 style="font-family:'DM Serif Display',serif;font-size:22px;color:#1A1A2E;margin-bottom:16px">Related Calculators</h3>
<div style="display:flex;flex-wrap:wrap;gap:12px">
<a href="/tools/quarterly-tax-calculator.html" style="background:#F4F6F9;border:1px solid #E8ECF0;border-radius:8px;padding:10px 18px;font-size:14px;color:#1A1A2E;text-decoration:none">Quarterly Tax Calculator</a>
<a href="/tools/gig-deduction-finder.html" style="background:#F4F6F9;border:1px solid #E8ECF0;border-radius:8px;padding:10px 18px;font-size:14px;color:#1A1A2E;text-decoration:none">Gig Deduction Finder</a>
<a href="/tools/1099-vs-w2-calculator.html" style="background:#F4F6F9;border:1px solid #E8ECF0;border-radius:8px;padding:10px 18px;font-size:14px;color:#1A1A2E;text-decoration:none">1099 vs W-2 Calculator</a>
<a href="/tools/tax-bracket-calculator.html" style="background:#F4F6F9;border:1px solid #E8ECF0;border-radius:8px;padding:10px 18px;font-size:14px;color:#1A1A2E;text-decoration:none">Tax Bracket Calculator</a>
</div>
</div>
</section>

<!-- DISCLAIMER -->
<div class="disclaimer-bar" role="note">
<span class="icon">&#9888;&#65039;</span>
<strong>Disclaimer:</strong> This calculator provides estimates for informational purposes only. Consult a qualified tax professional for advice specific to your situation.
</div>

<!-- FOOTER -->
<div id="footer-placeholder"></div>
<script src="/assets/include-footer.js" defer></script>

<!-- Cookie Consent -->
<div id="cookie-consent" role="dialog" aria-label="Cookie Consent" aria-modal="true" style="display:none;position:fixed;bottom:0;left:0;right:0;background:#0A1628;color:#fff;padding:16px 24px;z-index:99999;box-shadow:0 -4px 20px rgba(0,0,0,0.3);font-family:'DM Sans',sans-serif;font-size:14px;line-height:1.5">
<div style="max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:16px;justify-content:space-between">
<p style="margin:0;flex:1;min-width:200px;color:#B0B8C4;font-size:13px">This site uses cookies for analytics and personalized ads. See our <a href="/legal/privacy-policy.html" style="color:#00C896;text-decoration:underline">Privacy Policy</a> for details.</p>
<div style="display:flex;gap:10px;flex-shrink:0">
<button id="cookie-decline" style="background:transparent;border:1px solid #667080;color:#B0B8C4;padding:8px 18px;border-radius:6px;cursor:pointer;font-size:13px;font-family:inherit">Decline</button>
<button id="cookie-accept" style="background:#00C896;border:none;color:#0A1628;padding:8px 24px;border-radius:6px;cursor:pointer;font-weight:600;font-size:13px;font-family:inherit">Accept All</button>
</div>
</div>
</div>
<script>
(function(){{
var banner = document.getElementById('cookie-consent');
var accept = document.getElementById('cookie-accept');
var decline = document.getElementById('cookie-decline');
if(!banner || !accept) return;
var consent = localStorage.getItem('cookie_consent');
if(consent !== 'accepted' && consent !== 'declined'){{ banner.style.display = 'block'; }}
accept.addEventListener('click', function(){{
localStorage.setItem('cookie_consent', 'accepted');
banner.style.display = 'none';
if(typeof gtag !== 'undefined'){{ gtag('consent', 'update', {{'analytics_storage':'granted','ad_storage':'granted'}}); }}
}});
decline.addEventListener('click', function(){{
localStorage.setItem('cookie_consent', 'declined');
banner.style.display = 'none';
if(typeof gtag !== 'undefined'){{ gtag('consent', 'update', {{'analytics_storage':'denied','ad_storage':'denied'}}); }}
}});
}})();
</script>

<script>
function calculateTax() {{
var gross = parseFloat(document.getElementById('gross-income').value) || 0;
var expenses = parseFloat(document.getElementById('expenses').value) || 0;
var net = Math.max(0, gross - expenses);
var seTax = net * {se_rate};
var totalTax = seTax;
var quarterly = totalTax / 4;
var rate = net > 0 ? (totalTax / gross * 100) : 0;
document.getElementById('net-income').textContent = '{currency_symbol}' + net.toFixed(2);
document.getElementById('tax-due').textContent = '{currency_symbol}' + totalTax.toFixed(2);
document.getElementById('tax-rate').textContent = rate.toFixed(1) + '%';
document.getElementById('quarterly-payment').textContent = '{currency_symbol}' + quarterly.toFixed(2);
document.getElementById('result-card').style.display = 'block';
}}
</script>

</body>
</html>"""

    def generate_programmatic_pages(self):
        print("STEP 1: Launching Programmatic SEO Page Engine into /tools/ structure...")

        if not os.path.exists("tools"):
            os.makedirs("tools")

        for country in self.countries:
            dir_path = os.path.join("tools", country["code"])
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            for niche in self.niches:
                slug = f"{niche['id']}-tax-calculator"
                page_content = self.html_blueprint.format(
                    domain=self.url,
                    lang_code="en-GB" if country["code"] == "uk" else "en-US",
                    year=country["year"],
                    niche_title=niche["title_keyword"],
                    niche_keyword=niche["niche_keyword"],
                    niche_desc=niche["description"],
                    country_name=country["name"],
                    country_code=country["code"],
                    country_code_upper=country["code"].upper(),
                    page_slug=slug,
                    currency=country["currency"],
                    currency_symbol=country["symbol"],
                    placeholder_income=country["income_placeholder"],
                    placeholder_expenses=country["expenses_placeholder"],
                    tax_term=country["term"],
                    tax_term_lower=country["term"].lower(),
                    tax_authority=country["authority"],
                    se_rate=country["rate"],
                    deductions_text=niche["deductions_text"],
                    deadlines_text=niche["deadlines_text"]
                )
                file_path = os.path.join(dir_path, f"{slug}.html")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(page_content)

                relative_path = f"tools/{country['code']}/{slug}.html"
                self.generated_pages.append(relative_path)
                print(f"  [OK] Generated: /{relative_path}")

    def update_and_merge_sitemap(self):
        print("\nSTEP 2: Merging new paths with original sitemap.xml...")
        existing_urls = set()
        today = datetime.today().strftime('%Y-%m-%d')
        NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
        sitemap_filename = "sitemap.xml"

        if os.path.exists(sitemap_filename):
            try:
                tree = ET.parse(sitemap_filename)
                root = tree.getroot()
                for url in root.findall(f'{{{NS}}}url'):
                    loc = url.find(f'{{{NS}}}loc')
                    if loc is not None and loc.text:
                        existing_urls.add(loc.text.strip())
                print(f"  -> Found {len(existing_urls)} original URLs in local sitemap.xml")
            except Exception as e:
                print(f"  Local parse issue: {e}")

        if len(existing_urls) <= 15:
            try:
                live_url = f"{self.url}/sitemap.xml"
                print(f"  -> Trying live recovery: {live_url}")
                res = requests.get(live_url, headers=self.headers, timeout=10)
                if res.status_code == 200:
                    root = ET.fromstring(res.text)
                    for url in root.findall(f'{{{NS}}}url'):
                        loc = url.find(f'{{{NS}}}loc')
                        if loc is not None and loc.text:
                            existing_urls.add(loc.text.strip())
                    print(f"  -> Recovered {len(existing_urls)} URLs from live")
            except Exception as e:
                print(f"  Live recovery skipped: {e}")

        xml_entries = []
        for url in sorted(existing_urls):
            skip = False
            for c in ["us", "uk", "ca"]:
                if f"/{c}/" in url and "/tools/" not in url:
                    skip = True
            if skip:
                continue
            xml_entries.append(f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n  </url>')

        for page in self.generated_pages:
            full_url = f"{self.url}/{page}"
            if full_url not in existing_urls:
                xml_entries.append(f'  <url>\n    <loc>{full_url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>')

        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(xml_entries) + "\n</urlset>"
        with open(sitemap_filename, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print(f"  [OK] Sitemap saved. Total URLs: {len(xml_entries)}")

    def run_all(self):
        self.generate_programmatic_pages()
        self.update_and_merge_sitemap()
        print("\nClean Update Finished.")

if __name__ == "__main__":
    agent = MasterSEOAgentFixed("https://freelancetaxcalc.online")
    agent.run_all()
