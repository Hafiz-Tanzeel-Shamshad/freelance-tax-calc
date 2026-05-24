#!/usr/bin/env python3
"""Generate platform-specific deduction sub-pages."""
import os, re

OUT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools\deductions"
os.makedirs(OUT, exist_ok=True)

SITE = "https://freelancetaxcalc.online"

PLATFORMS = [
    {
        "slug": "doordash",
        "name": "DoorDash",
        "title": "DoorDash Tax Deductions 2026 — Complete Write-Off List for Dashers",
        "desc": "Complete DoorDash tax deductions 2026 guide. See what Dashers can deduct — mileage ($0.70/mi), insulated bags, phone, platform fees & more. Free DoorDash deduction finder.",
        "h1": "DoorDash Tax Deductions 2026",
        "vol": "5,400",
        "seo_content": """
    <h2>Top DoorDash Tax Deductions for 2026</h2>
    <p>DoorDash classifies all Dashers as independent contractors (1099-NEC), meaning no taxes are withheld from your deliveries. Every dollar you deduct saves you 20-30% in taxes. Here are the most valuable DoorDash tax deductions:</p>
    <ul>
      <li><strong>Standard Mileage Deduction</strong> — $0.70 per mile driven from pickup to drop-off. A Dasher driving 15,000 delivery miles saves $10,500 in taxable income.</li>
      <li><strong>DoorDash Service Fees</strong> — DoorDash's commission (typically 20-25% per order) is 100% deductible.</li>
      <li><strong>Delivery Equipment</strong> — Insulated bags, hot/cold packs, catering bags, drink carriers.</li>
      <li><strong>Cell Phone &amp; Data</strong> — Business portion of your phone plan (60-80% is typical).</li>
      <li><strong>Parking &amp; Tolls</strong> — All parking fees and tolls incurred during deliveries.</li>
      <li><strong>Car Maintenance</strong> — If using actual expenses instead of mileage: gas, oil changes, tires, repairs.</li>
      <li><strong>Dasher Direct Card Fees</strong> — Any fees from using the Dasher Direct debit card.</li>
    </ul>
    <p>DoorDash provides a yearly Tax Summary in your account showing gross earnings and fees paid. Use this to calculate your net income. Most Dashers should save 25-30% of net earnings for taxes. Try our <a href="/tools/gig-deduction-finder">free gig worker deduction finder</a> for a personalized list.</p>

    <h2>DoorDash Mileage Deduction Calculator</h2>
    <p>The mileage deduction is the single largest write-off for DoorDash drivers. In 2026, the IRS standard mileage rate is $0.70 per business mile. If you drove 15,000 delivery miles as a Dasher, your mileage deduction is $10,500 — potentially saving you $2,100-$3,150 in taxes. Unlike Uber drivers, DoorDash mileage only counts from the restaurant to the customer, not while waiting for orders. Use our <a href="/tools/gig-deduction-finder">mileage deduction calculator</a> to estimate your vehicle write-off.</p>

    <h2>DoorDash Tax Deductions FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can DoorDash drivers deduct the standard mileage rate? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. DoorDash drivers can deduct $0.70 per mile driven while delivering. This covers gas, maintenance, repairs, insurance, and depreciation. You cannot deduct both mileage AND actual car expenses — choose whichever gives you a larger deduction.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do I need to track every DoorDash mile? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes, the IRS requires a contemporaneous mileage log. Apps like Stride, Gridwise, or Everlance can automatically track your miles. DoorDash does not provide mileage tracking in their app — you must track it yourself. Record date, starting odometer, ending odometer, and purpose of each trip.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct my car insurance for DoorDash? <span class="arrow">&#9660;</span></button><div class="faq-answer">If using the actual expense method, you can deduct a portion of your car insurance. If using the standard mileage rate, insurance is included in the $0.70/mile rate and cannot be separately deducted. Most Dashers use the standard mileage rate because it's simpler and usually provides a larger deduction.</div></div>
""",
    },
    {
        "slug": "uber",
        "name": "Uber",
        "title": "Uber Driver Tax Deductions List 2026 — Every Write-Off for Rideshare Drivers",
        "desc": "Complete Uber driver tax deductions list 2026. See every write-off for rideshare drivers — mileage, platform fees, phone, car accessories & more. Free Uber deduction finder.",
        "h1": "Uber Driver Tax Deductions 2026",
        "vol": "4,400",
        "seo_content": """
    <h2>Top Uber Driver Tax Deductions for 2026</h2>
    <p>Uber drivers are independent contractors and can deduct almost every cost of operating their vehicle and running their driving business. Here are the most valuable Uber tax deductions:</p>
    <ul>
      <li><strong>Standard Mileage Deduction</strong> — $0.70 per mile driven while the Uber app is on. This includes all miles — waiting for rides, driving to pickup, and driving to dropoff.</li>
      <li><strong>Uber Service Fee</strong> — Uber's 25% commission on every ride is 100% deductible on Schedule C.</li>
      <li><strong>Cell Phone &amp; Data</strong> — 60-80% of your phone bill used for Uber driving.</li>
      <li><strong>Car Accessories</strong> — Phone mount, charger cables, dash cam, auxiliary cord.</li>
      <li><strong>Car Washes &amp; Detailing</strong> — Keeping your car clean for rider ratings and comfort.</li>
      <li><strong>Water &amp; Snacks</strong> — Complimentary items for riders (Uber doesn't supply these).</li>
      <li><strong>Parking &amp; Tolls</strong> — Tolls paid during trips, airport parking fees while waiting.</li>
    </ul>
    <p>Uber provides a yearly Tax Summary in your Driver Dashboard with gross fares, Uber's service fee, and your net earnings. Use this to calculate your taxable income. Most Uber drivers should save 25-30% of net earnings for taxes. Use our <a href="/tools/gig-deduction-finder">free Uber driver deduction finder</a> for a personalized write-off list.</p>

    <h2>Uber vs Lyft: Same Deductions?</h2>
    <p>Uber and Lyft drivers qualify for the same deductions since both are rideshare platforms. The key difference is each platform's fee structure — Uber charges approximately 25% commission while Lyft charges about 20-25%. Both provide tax summaries, but Uber's is more detailed with mileage breakdowns. If you drive for both platforms, you can combine all miles driven while either app is on. Our <a href="/tools/gig-deduction-finder">rideshare deduction finder</a> works for both Uber and Lyft drivers.</p>

    <h2>Uber Deductions FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct my car payment for Uber? <span class="arrow">&#9660;</span></button><div class="faq-answer">You cannot directly deduct car loan payments. However, if you use the actual expense method (instead of mileage), you can deduct a percentage of your lease payments or the interest portion of your car loan. The standard mileage rate is usually more beneficial for Uber drivers.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct my phone bill as an Uber driver? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. Most Uber drivers use their phone 60-80% for work and can deduct that percentage of their monthly bill. If you have a dedicated phone for Uber, you can deduct 100%. Phone accessories like mounts and chargers are also deductible as supplies.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do Uber drivers need a mileage tracker? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. The IRS requires a mileage log for any business vehicle use. Uber's app does NOT automatically track deductible miles — you need a third-party app like Stride, Gridwise, or QuickBooks Self-Employed. Uber provides an annual mileage estimate in your Tax Summary, but this may not include all deductible miles.</div></div>
""",
    },
    {
        "slug": "etsy",
        "name": "Etsy",
        "title": "Etsy Seller Tax Deductions Checklist 2026 — Complete Guide & Calculator",
        "desc": "Complete Etsy seller tax deductions checklist 2026. See every write-off — listing fees, materials, shipping, home office & more. Free Etsy deduction finder.",
        "h1": "Etsy Seller Tax Deductions Checklist 2026",
        "vol": "2,400",
        "seo_content": """
    <h2>Top Etsy Seller Tax Deductions for 2026</h2>
    <p>Etsy sellers are self-employed and can deduct virtually every cost of running their shop. Your taxable income is gross sales minus ALL business expenses — not your total revenue. Here are the most valuable Etsy deductions:</p>
    <ul>
      <li><strong>Etsy Fees</strong> — Listing fees ($0.20/listing), transaction fees (6.5%), payment processing (3%+$0.25), offsite ads (12-15%).</li>
      <li><strong>Materials &amp; Supplies</strong> — Cost of goods sold, raw materials, packaging, labels, poly mailers.</li>
      <li><strong>Shipping Costs</strong> — Postage, shipping labels, boxes, tape, bubble wrap, insurance.</li>
      <li><strong>Product Photography</strong> — Camera, lighting, backdrop, photo editing software (Canva, Photoshop).</li>
      <li><strong>Home Office Deduction</strong> — $5/sq ft for your workspace where you create and pack items.</li>
      <li><strong>Tools &amp; Equipment</strong> — Cutting machines (Cricut), sewing machines, 3D printers, kilns.</li>
      <li><strong>Etsy Plus Subscription</strong> — Monthly subscription fee for Etsy Plus.</li>
    </ul>
    <p>Etsy sends a 1099-K if you exceed $600 in gross sales. Your taxable income is calculated as: Gross Sales — Etsy Fees — Materials — Shipping — All Other Expenses = Net Profit. Many Etsy sellers overpay by not tracking all their deductions. Use our <a href="/tools/gig-deduction-finder">free Etsy seller deduction finder</a> to see your personalized write-off list.</p>

    <h2>Etsy Home Office Deduction Guide</h2>
    <p>Etsy sellers who use a dedicated space in their home for creating, packing, and shipping can claim the home office deduction. The simplified method gives $5 per square foot up to 300 sq ft ($1,500 max). You need a space used regularly and exclusively for your Etsy business — a spare bedroom, garage workshop, or dedicated craft room. This deduction covers a portion of your rent/mortgage, utilities, and internet. Use our <a href="/tools/gig-deduction-finder">Etsy home office calculator</a> in the deduction finder.</p>

    <h2>Etsy Deductions FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do Etsy sellers pay taxes on gross or net income? <span class="arrow">&#9660;</span></button><div class="faq-answer">You pay taxes on your net income — gross sales minus all deductible expenses. This includes Etsy fees, materials, shipping, home office, and equipment. Many new Etsy sellers mistakenly think they owe taxes on their total revenue.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct Etsy fees even without a 1099-K? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. Etsy fees are deductible regardless of whether you receive a 1099-K. Download your monthly Etsy fee statements from your Shop Manager and keep them with your tax records. Every listing fee, transaction fee, and offsite ad fee is deductible.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct supplies I bought but haven't used yet? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes, if you use accrual accounting or if the supplies are consumed within the year. Most Etsy sellers use the cash method and deduct supplies when purchased, not when used. Keep receipts for all material purchases.</div></div>
""",
    },
    {
        "slug": "airbnb",
        "name": "Airbnb",
        "title": "Airbnb Host Tax Deductions 2026 — Complete Write-Off Guide for Hosts",
        "desc": "Complete Airbnb host tax deductions 2026 guide. See every write-off for short-term rental hosts — cleaning, amenities, maintenance, utilities & more.",
        "h1": "Airbnb Host Tax Deductions 2026",
        "vol": "1,800",
        "seo_content": """
    <h2>Top Airbnb Host Tax Deductions for 2026</h2>
    <p>Airbnb hosts can deduct expenses related to their rental property, whether it's a spare room or an entire home. Here are the most valuable Airbnb tax deductions:</p>
    <ul>
      <li><strong>Cleaning &amp; Supplies</strong> — Cleaning products, laundry supplies, professional cleaning services.</li>
      <li><strong>Amenities</strong> — Coffee, tea, snacks, toiletries (shampoo, soap, toilet paper), welcome baskets.</li>
      <li><strong>Linens &amp; Bedding</strong> — Sheets, towels, pillows, blankets, mattress protectors.</li>
      <li><strong>Furniture &amp; Decor</strong> — Beds, sofas, tables, chairs, artwork, curtains, rugs.</li>
      <li><strong>Utilities</strong> — Electricity, water, gas, internet, cable TV — proportional to rental use.</li>
      <li><strong>Airbnb Service Fee</strong> — The 3% host service fee charged by Airbnb per booking.</li>
      <li><strong>Property Maintenance</strong> — Repairs, landscaping, pest control, painting, snow removal.</li>
      <li><strong>Mortgage Interest &amp; Property Taxes</strong> — Proportional to the rented space and time.</li>
    </ul>
    <p>If you rent out a room in your primary residence, expenses are allocated based on the percentage of square footage rented. The Augusta Rule allows up to 14 days of tax-free rental income if you rent your entire home. Use our <a href="/tools/gig-deduction-finder">free deduction finder</a> to discover all your write-offs.</p>

    <h2>Airbnb Short-Term Rental vs. Long-Term Rental Tax Rules</h2>
    <p>Airbnb hosts renting short-term (average less than 7 days) are treated as business owners and can deduct all ordinary and necessary expenses. Hosts renting long-term follow standard rental property tax rules with depreciation schedules. Short-term rentals generally offer more deductions since they're treated as active businesses rather than passive investments.</p>

    <h2>Airbnb Deductions FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct home improvements for my Airbnb? <span class="arrow">&#9660;</span></button><div class="faq-answer">Major improvements that add value or extend the life of the property (new roof, renovation, addition) must be depreciated over 27.5 years. Minor repairs and maintenance (fixing a leak, painting a room) are fully deductible in the current year.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do I pay taxes on all my Airbnb income? <span class="arrow">&#9660;</span></button><div class="faq-answer">You pay taxes on your net income after deducting all expenses. If you rent fewer than 15 days per year, the income is tax-free under the Augusta Rule. Otherwise, Airbnb reports income to the IRS if you earn over $600 annually.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct my personal use of the Airbnb property? <span class="arrow">&#9660;</span></button><div class="faq-answer">You cannot deduct expenses during your personal use. Expenses must be allocated between rental days and personal days. If you use the property for 30 days and rent it for 120 days, only 80% of expenses are deductible (120/150).</div></div>
""",
    },
    {
        "slug": "fiverr",
        "name": "Fiverr",
        "title": "Fiverr Freelancer Tax Deductions 2026 — Complete Guide & Calculator",
        "desc": "Complete Fiverr freelancer tax deductions 2026 guide. See every write-off for Fiverr sellers — platform fees, software, home office, training & more. Free deduction finder.",
        "h1": "Fiverr Freelancer Tax Deductions 2026",
        "vol": "1,300",
        "seo_content": """
    <h2>Top Fiverr Freelancer Tax Deductions for 2026</h2>
    <p>Fiverr sellers (freelancers) are independent contractors and can deduct all ordinary and necessary business expenses. Here are the most valuable Fiverr tax deductions:</p>
    <ul>
      <li><strong>Fiverr Service Fee</strong> — Fiverr's 20% commission on each order is 100% deductible.</li>
      <li><strong>Fiverr Seller Plus</strong> — Monthly subscription fee for Seller Plus ($19.99-$39.99/mo).</li>
      <li><strong>Software &amp; Tools</strong> — Adobe Creative Cloud, Canva Pro, Figma, CapCut, Grammarly, and any software used for your gigs.</li>
      <li><strong>Portfolio Website</strong> — Domain name, hosting, SSL certificate, WordPress themes.</li>
      <li><strong>Home Office</strong> — $5/sq ft for your dedicated workspace (up to $1,500).</li>
      <li><strong>Internet &amp; Phone</strong> — Business portion of your home internet and phone bills.</li>
      <li><strong>Equipment</strong> — Computer, monitor, keyboard, mouse, drawing tablet, microphone.</li>
      <li><strong>Professional Development</strong> — Online courses, certifications, books, workshops.</li>
    </ul>
    <p>Fiverr sellers providing digital services (design, writing, programming, marketing) have high profit margins since material costs are low. Your biggest deductions are typically Fiverr fees and software subscriptions. Use our <a href="/tools/gig-deduction-finder">free Fiverr deduction finder</a> for a personalized write-off list.</p>

    <h2>Fiverr vs Upwork: Tax Deduction Differences</h2>
    <p>Fiverr (20% fee) and Upwork (5-20% sliding fee) have different fee structures but the same deduction categories. Fiverr sellers typically pay higher platform fees but get more visibility on the platform. Both platforms provide earnings summaries at year-end. The deduction categories for both platforms are identical — software, equipment, home office, training, internet, and phone.</p>

    <h2>Fiverr Deductions FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can Fiverr freelancers deduct a home office? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. If you use a dedicated space in your home regularly and exclusively for your Fiverr work, you can claim the home office deduction. The simplified method gives $5/sq ft up to 300 sq ft ($1,500 max).</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I deduct my laptop as a Fiverr freelancer? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. Under Section 179, you can deduct the full cost of equipment (computers, monitors, tablets) in the year of purchase up to certain limits. This is one of the largest deductions for digital freelancers.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do Fiverr freelancers need to pay quarterly taxes? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. Fiverr freelancers who expect to owe at least $1,000 must make estimated quarterly tax payments. Use our free <a href="/tools/quarterly-tax-calculator">quarterly tax calculator</a> to determine your payment amounts.</div></div>
""",
    },
    {
        "slug": "instacart",
        "name": "Instacart",
        "title": "Instacart Shopper Tax Deductions & Write-Offs 2026 — Complete List",
        "desc": "Complete Instacart shopper tax write-offs 2026 list. See what Instacart shoppers can deduct — mileage, insulated bags, phone, service fees & more. Free deduction finder.",
        "h1": "Instacart Shopper Tax Deductions 2026",
        "vol": "800",
        "seo_content": """
    <h2>Top Instacart Shopper Tax Deductions for 2026</h2>
    <p>Instacart shoppers (full-service and in-store) are independent contractors and can deduct their business expenses. Here are the most valuable Instacart tax deductions:</p>
    <ul>
      <li><strong>Standard Mileage</strong> — $0.70/mile driven from store to customer delivery locations. Full-service shoppers who drive to stores and deliver can claim this.</li>
      <li><strong>Insulated Bags &amp; Coolers</strong> — Thermal bags, cold packs, insulated backpacks for grocery delivery.</li>
      <li><strong>Cell Phone &amp; Data</strong> — You need data to shop and deliver. Deduct 60-80% of your phone plan.</li>
      <li><strong>Instacart Service Fees</strong> — Instacart's fee on each batch is 100% deductible.</li>
      <li><strong>Parking Fees</strong> — Parking costs while picking up orders at stores.</li>
      <li><strong>Phone Mount &amp; Charger</strong> — Car accessories for navigation and deliveries.</li>
      <li><strong>Car Maintenance</strong> — If using actual expenses method: gas, oil changes, tires, repairs.</li>
    </ul>
    <p>Instacart provides an earnings summary for tax purposes. Full-service shoppers have more deductions than in-store shoppers since they drive their own vehicles. In-store shoppers can still deduct work-related costs like non-slip shoes and uniforms. Use our <a href="/tools/gig-deduction-finder">free Instacart deduction finder</a> for a personalized list.</p>

    <h2>Instacart Full-Service vs In-Store Shopper Deductions</h2>
    <p>Full-service shoppers (shop and deliver) can claim mileage from store to customer, vehicle expenses, and delivery-related costs. In-store shoppers (work in a single store) cannot claim vehicle mileage but can deduct work clothing, non-slip shoes, and any required equipment. Full-service shoppers generally have larger deduction totals due to vehicle expenses.</p>

    <h2>Instacart Deductions FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can Instacart shoppers deduct mileage from home to store? <span class="arrow">&#9660;</span></button><div class="faq-answer">No. Commuting from home to your first store is considered personal mileage and is not deductible. Only miles driven from the store to customer delivery locations and between stores count as business miles.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do Instacart shoppers get a 1099? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. Instacart sends a 1099-NEC to shoppers who earn $600 or more in a calendar year. You are responsible for reporting all income, including tips, on your tax return.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can Instacart shoppers deduct car maintenance? <span class="arrow">&#9660;</span></button><div class="faq-answer">If you use the standard mileage rate ($0.70/mile), car maintenance is already included and cannot be separately deducted. If you use the actual expense method, you can deduct a percentage of gas, oil changes, repairs, tires, and insurance based on business-use percentage.</div></div>
""",
    },
]

def build_page(p):
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['title']} | FreelanceTaxCalc</title>
<meta name="description" content="{p['desc']}">
<link rel="canonical" href="{SITE}/deductions/{p['slug']}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FreelanceTaxCalc">
<meta property="og:url" content="{SITE}/deductions/{p['slug']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p['title']}">
<meta name="twitter:description" content="{p['desc']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<script type="application/ld+json">
[{{
  "@context":"https://schema.org","@type":"WebApplication",
  "name":"{p['name']} Tax Deduction Guide",
  "url":"{SITE}/deductions/{p['slug']}",
  "description":"Complete guide to {p['name']} tax deductions 2026.",
  "applicationCategory":"FinanceApplication","operatingSystem":"All"
}},{{
  "@context":"https://schema.org","@type":"BreadcrumbList",
  "itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}/"}},
    {{"@type":"ListItem","position":2,"name":"Deduction Guides","item":"{SITE}/tools/gig-deduction-finder"}},
    {{"@type":"ListItem","position":3,"name":"{p['name']} Tax Deductions"}}
  ]
}}]
</script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:"DM Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,sans-serif;font-size:16px;line-height:1.7;color:#1A1A2E;background:#F4F6F9}}
a{{color:#00C896;text-decoration:none}}
a:hover{{color:#00B085}}
.container{{max-width:800px;margin:0 auto;padding:0 24px}}
.site-header{{background:#0A1628;border-bottom:1px solid rgba(255,255,255,0.05);position:sticky;top:0;z-index:100}}
.site-header .container{{display:flex;align-items:center;justify-content:space-between;height:64px;max-width:1100px}}
.header-logo{{display:flex;align-items:center;gap:10px;font-family:"DM Serif Display",serif;font-size:20px;font-weight:700;color:#fff}}
.logo-icon{{width:32px;height:32px;background:#00C896;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px;font-weight:700;flex-shrink:0}}
.logo-dot{{color:#00C896}}
.header-back{{color:#B0B8C4;font-size:14px}}
.header-back:hover{{color:#00C896}}
.page-title{{background:#fff;padding:28px 0;text-align:center}}
.page-title h1{{font-family:"DM Serif Display",serif;font-size:34px;color:#1A1A2E;margin-bottom:8px}}
.page-title p{{color:#6B7280;font-size:15px}}
.page-title .vol{{display:inline-block;background:#E8F8F5;color:#00C896;padding:4px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-top:8px}}
.content-section{{padding:40px 0 60px}}
.content-section h2{{font-family:"DM Serif Display",serif;font-size:26px;color:#1A1A2E;margin:40px 0 16px}}
.content-section h2:first-child{{margin-top:0}}
.content-section p{{font-size:16px;color:#4B5563;line-height:1.8;margin-bottom:16px}}
.content-section ul{{padding-left:24px;margin-bottom:20px}}
.content-section li{{font-size:16px;color:#4B5563;line-height:1.8;margin-bottom:6px}}
.content-section li strong{{color:#1A1A2E}}
.cta-card{{background:linear-gradient(135deg,#0A1628,#1A2A4A);border-radius:12px;padding:32px;text-align:center;color:#fff;margin:32px 0}}
.cta-card h3{{font-family:"DM Serif Display",serif;font-size:24px;margin-bottom:12px}}
.cta-card p{{color:rgba(255,255,255,0.85)!important;margin-bottom:20px!important}}
.btn-cta{{display:inline-block;background:#00C896;color:#fff;padding:14px 32px;border-radius:8px;font-weight:700;font-size:16px;transition:all 0.3s ease}}
.btn-cta:hover{{background:#00B085;transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,200,150,0.3);color:#fff}}
.faq-item{{border:1px solid #E8ECF0;border-radius:8px;margin-bottom:8px;overflow:hidden}}
.faq-question{{width:100%;padding:16px 20px;background:#fff;border:none;text-align:left;font-size:16px;font-weight:600;color:#1A1A2E;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:inherit}}
.faq-question:hover{{background:#F9FAFB}}
.faq-question .arrow{{transition:transform 0.3s ease;font-size:12px;color:#6B7280}}
.faq-item.open .faq-question .arrow{{transform:rotate(180deg)}}
.faq-answer{{padding:0 20px;max-height:0;overflow:hidden;transition:all 0.3s ease;font-size:15px;color:#4B5563;line-height:1.7}}
.faq-item.open .faq-answer{{padding:0 20px 16px;max-height:500px}}
.platform-links{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:24px 0}}
.platform-links a{{padding:8px 16px;background:#F9FAFB;border:1px solid #E8ECF0;border-radius:6px;font-size:14px;font-weight:500;color:#1A1A2E;text-decoration:none;transition:all 0.2s ease}}
.platform-links a:hover{{background:#00C896;color:#fff;border-color:#00C896}}
.platform-links a.active{{background:#00C896;color:#fff;border-color:#00C896}}
.site-footer{{background:#0A1628;color:#B0B8C4;padding:40px 0 24px}}
.site-footer .container{{max-width:1100px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}}
.site-footer a{{color:#8892A0}}
.site-footer a:hover{{color:#00C896}}
.site-footer .copyright{{font-size:13px;color:#667080}}
@media(max-width:600px){{
  .page-title h1{{font-size:26px}}
  .content-section h2{{font-size:22px}}
  .cta-card{{padding:24px 16px}}
}}
</style>
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="/" class="header-logo"><span class="logo-icon">$</span>Freelance<span class="logo-dot">.</span>TaxCalc</a>
    <a href="/tools/gig-deduction-finder" class="header-back">&larr; Deduction Finder</a>
  </div>
</header>
<div class="page-title">
  <div class="container">
    <h1>{p['h1']}</h1>
    <p>Complete guide to every tax deduction {p['name']} workers can claim this year &mdash; with estimated savings and IRS form references.</p>
    <span class="vol">&#128200; {p['vol']} searches/month &bull; 2026 Guide</span>
  </div>
</div>
<section class="content-section">
  <div class="container">
    {p['seo_content']}

    <div class="cta-card">
      <h3>Get Your Personalized Deduction List</h3>
      <p>Answer 3 quick questions to see every tax deduction you qualify for as a {p['name']} worker. Free &mdash; no signup needed.</p>
      <a href="/tools/gig-deduction-finder" class="btn-cta">Try the Free Deduction Finder &rarr;</a>
    </div>
  </div>
</section>
<footer class="site-footer">
  <div class="container">
    <span class="copyright">&copy; 2026 FreelanceTaxCalc &mdash; Free tools for independent workers.</span>
    <a href="/">Back to Home</a>
  </div>
</footer>
<script>
document.querySelectorAll('.faq-question').forEach(function(q){{
  q.addEventListener('click',function(){{
    var item=this.parentElement,isOpen=item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(function(el){{
      el.classList.remove('open');
      el.querySelector('.faq-question').setAttribute('aria-expanded','false');
    }});
    if(!isOpen){{item.classList.add('open');this.setAttribute('aria-expanded','true');}}
  }});
}});
</script>
</body>
</html>"""

for p in PLATFORMS:
    fname = os.path.join(OUT, f"{p['slug']}.html")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(build_page(p))
    print(f"  Created: {p['slug']}.html")

print(f"\nDone! {len(PLATFORMS)} platform deduction pages generated.")
