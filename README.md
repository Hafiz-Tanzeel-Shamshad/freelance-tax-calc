# FreelanceTaxCalc

> Free online tax calculators, deduction guides, and financial tools for freelancers, gig workers, and the self-employed.

**Website:** [https://freelancetaxcalc.online](https://freelancetaxcalc.online)

---

## About

FreelanceTaxCalc is a static HTML website that provides free tax calculation tools for freelancers and self-employed individuals. All calculators run entirely client-side in the browser — no data is ever sent to a server. No login required.

---

## Features

### Calculators (11 tools)
| Tool | Description |
|------|-------------|
| Quarterly Tax Estimator | Estimate quarterly tax payments for US, Canada, UK |
| Gig Worker Deduction Finder | 3-step tool to find tax deductions by gig type |
| 1099 vs W-2 Calculator | Compare take-home pay as contractor vs employee |
| Side Hustle Tax Estimator | Estimate taxes on side gig income |
| First Paycheck Calculator | See take-home pay before starting a job |
| Digital Nomad Tax Calculator | 26-country tax obligation guide for nomads |
| Freelance Hourly Rate Calculator | Salary to hourly, day rate, value-based pricing |
| Self-Employed Retirement Calculator | Compare Solo 401k vs SEP-IRA with 2026 limits |
| Freelance Budget & Invoice Calculator | 50/30/20 budget and invoice tax calculator |
| Finance App Recommender | Quiz-based app matching from 12 options |
| Rate Calculator & Debt Planner | Hourly rate + avalanche/snowball debt payoff |

### State Pages (50 states + DC)
Each state has a dedicated page under `/tools/quarterly-tax-calculator/` with 9 FAQ items and FAQPage schema for localized quarterly tax information.

### Deduction Guides (6 platforms)
Airbnb, DoorDash, Etsy, Fiverr, Instacart, Uber — each with platform-specific deduction guides.

### Digital Nomad Guides (5 countries)
Estonia, Mexico, Portugal, Spain, Thailand — tax guides for remote workers.

### Guides (4 articles)
- Quarterly Taxes Guide
- Gig Worker Deductions Guide
- 1099 vs W-2 Comparison Guide
- Guides Index

### Legal Pages
Privacy Policy, Terms of Service, Disclaimer, About, Contact (via Web3Forms)

---

## Tech Stack

- **Language:** HTML5, CSS3, Vanilla JavaScript
- **Schema:** JSON-LD (WebSite, WebApplication, FAQPage, BreadcrumbList, Article, AboutPage, ContactPage)
- **Analytics:** Google Analytics (GA4) ready
- **Ads:** Google AdSense (placeholder, pending approval)
- **Forms:** Web3Forms API
- **Fonts:** DM Serif Display + DM Sans (Google Fonts)
- **Hosting:** Static site (no backend, no database)

---

## SEO & Compliance

- **86 HTML pages** with unique title tags (50-60 chars) and meta descriptions (<160 chars)
- **Breadcrumb nav** (visible HTML + JSON-LD) on every page
- **All internal links** use `.html` extensions — no clean URL dependency
- **robots.txt** — blocks assets/ and pre-launch-checklist
- **Sitemap:** `sitemap.xml` with 84 indexable URLs
- **404.html** — custom error page
- **Cookie consent** — banner with Google Consent Mode v2
- **.htaccess** — HTTPS redirect, www→non-www, clean URL fallbacks, security headers, caching (Apache only; Vercel ignores)

---

## AdSense Compliance Checklist

- [x] Privacy Policy — includes Google-required language (third-party vendors, Ads Settings opt-out, aboutads.info)
- [x] Disclaimer — prominent "not financial, tax, or legal advice" clause at top
- [x] About page, Contact page, Terms of Service
- [x] Cookie consent with GDPR/CCPA options
- [x] No placeholder ad code in live pages
- [x] No sensitive content (no gambling, drugs, weapons, etc.)
- [x] All pages have sufficient content (not empty/thin)
- [x] Contact form via Web3Forms forwarding to site owner

**Status:** Pre-approval. Site needs 3-6 months age and blog content before applying.

---

## Project Structure

```
/ (root)
├── index.html                     # Homepage
├── 404.html                       # Custom 404
├── robots.txt                     # Crawl rules
├── sitemap.xml                    # XML sitemap
├── assets/
│   ├── _ad-units.html             # Ad code templates (internal)
│   ├── _cookie-consent.js         # Cookie consent script
│   └── _head-snippet.html         # Head template (internal)
├── tools/                         # Main calculator tools
│   ├── quarterly-tax-calculator/
│   │   ├── alabama.html ...       # 51 state pages
│   │   └── wyoming.html
│   ├── quarterly-tax-calculator.html
│   ├── gig-deduction-finder.html
│   ├── ... (11 total tools)
├── deductions/                    # Platform deduction guides
│   ├── airbnb.html ... uber.html  # 6 platforms
├── digital-nomad-tax/             # Nomad country guides
│   ├── estonia.html ... thailand.html  # 5 countries
├── guides/                        # Informational articles
│   ├── index.html
│   ├── quarterly-taxes-guide.html
│   ├── gig-worker-deductions.html
│   └── 1099-vs-w2-comparison.html
├── legal/                         # Legal pages
│   ├── about.html
│   ├── contact.html
│   ├── disclaimer.html
│   ├── privacy-policy.html
│   └── terms.html
├── contact/                       # Contact form
│   └── index.html
└── README.md
```

---

## Development Notes

- **Hosting:** Upload all files as-is to any static host (Vercel, Netlify, Cloudflare Pages, Apache, Nginx)
- **Vercel:** No config file needed; `.html` extensions in URLs work out of the box; `404.html` auto-detected
- **Apache:** `.htaccess` provides HTTPS redirect, clean URL rewriting, and security headers
- **Nginx:** Convert `.htaccess` rewrite rules to `server` block directives

---

## Tags

`freelance-tax-calculator` `gig-economy` `self-employment-tax` `quarterly-taxes` `1099` `digital-nomad` `tax-deductions` `static-site` `adsense-ready` `seo-optimized`

---

## License

Private project. All rights reserved.
