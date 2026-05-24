#!/usr/bin/env python3
"""Generate country-specific digital nomad tax pages."""
import os

OUT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools\digital-nomad-tax"
os.makedirs(OUT, exist_ok=True)

SITE = "https://freelancetaxcalc.online"

PAGES = [
    {
        "slug": "portugal",
        "name": "Portugal",
        "flag": "\U0001F1F5\U0001F1F9",
        "title": "Portugal Digital Nomad Visa Tax 2026 — D8 Visa & NHR 2.0 Complete Guide",
        "desc": "Complete guide to Portugal digital nomad visa tax 2026. D8 visa requirements, NHR 2.0 flat 20% tax rate, residency rules & double taxation treaty for US citizens.",
        "h1": "Portugal Digital Nomad Visa Tax Guide 2026",
        "vol": "1,600",
        "content": """
    <h2>Portugal D8 Digital Nomad Visa: Overview</h2>
    <p>Portugal's D8 Digital Nomad Visa (also called the Remote Work Visa) allows remote workers and freelancers to live in Portugal for 1 year, renewable up to 5 years, with a path to permanent residency and citizenship. It is one of Europe's most popular digital nomad visa options, offering excellent infrastructure, safety, and quality of life at a moderate cost (~€1,500-2,500/month).</p>
    <p><strong>Key Requirements:</strong> Minimum income of ~€3,280/month (€39,360/year), proof of remote work or freelance contracts, health insurance, clean criminal record, and a Portuguese tax identification number (NIF). The visa application is processed through Portuguese consulates in your home country.</p>
    <p><strong>Tax Benefits:</strong> Under the NHR 2.0 (Non-Habitual Resident) regime, qualified digital nomads pay a flat 20% income tax rate on Portuguese-source income for 10 consecutive years. Foreign-source income is generally not taxed in Portugal if you can demonstrate it was taxed in the source country or qualifies for exemption under Portugal's territorial system.</p>

    <h2>Portugal NHR 2.0 Tax Regime Explained</h2>
    <p>The NHR 2.0 regime (updated from the original NHR in 2024) offers significant tax advantages for digital nomads and remote workers who become tax residents of Portugal:</p>
    <ul>
      <li><strong>Flat 20% rate</strong> on Portuguese-source income from high-value activities (including tech, consulting, and freelance work) — compared to the standard progressive rate of up to 48%.</li>
      <li><strong>Foreign income exemption</strong> — income earned outside Portugal may be exempt if certain conditions are met (taxed in source country, or qualifies under Portugal's territorial rules).</li>
      <li><strong>10-year duration</strong> — the NHR 2.0 benefit applies for the first 10 consecutive years of tax residency in Portugal.</li>
      <li><strong>Pension income</strong> — flat 10% rate on foreign pension income (if certain conditions met).</li>
    </ul>
    <p>To qualify for NHR 2.0, you must become a tax resident of Portugal (spend 183+ days in any 18-month period or have your habitual residence/center of vital interests in Portugal) and not have been a Portuguese tax resident in the previous 5 years.</p>

    <h2>US-Portugal Tax Treaty for Digital Nomads</h2>
    <p>The US-Portugal tax treaty (entered into force in 1994) provides important protections for American digital nomads in Portugal:</p>
    <ul>
      <li><strong>Residency tie-breaker</strong> — if you qualify as a resident of both countries, the treaty uses factors like permanent home, center of vital interests, and habitual abode to determine your single country of residence.</li>
      <li><strong>Permanent establishment</strong> — working remotely for a US company from Portugal generally does not create a permanent establishment in Portugal for your US employer.</li>
      <li><strong>Foreign Tax Credit</strong> — US citizens can claim FTC on Form 1116 for taxes paid to Portugal, offsetting US tax liability dollar-for-dollar.</li>
      <li><strong>FEIE compatibility</strong> — the Foreign Earned Income Exclusion works alongside Portugal's NHR regime for maximum tax efficiency.</li>
    </ul>
    <p>Use our <a href="/tools/digital-nomad-tax-calculator">digital nomad tax calculator</a> to estimate your combined US-Portugal tax obligations.</p>

    <h2>Portugal Tax Residency Rules</h2>
    <p>You become a Portuguese tax resident if you:</p>
    <ol>
      <li>Spend 183 days or more in Portugal in any 18-month period, OR</li>
      <li>Have a habitual residence in Portugal on December 31 (indicating intention to stay), OR</li>
      <li>Maintain your "center of vital interests" (business, family, personal relationships) in Portugal</li>
    </ol>
    <p>Once tax resident, you must file Portuguese tax returns and report worldwide income. However, NHR 2.0 significantly reduces the tax burden on foreign income.</p>

    <h2>Portugal Digital Nomad Visa FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">How long does the Portugal D8 visa take to process? <span class="arrow">&#9660;</span></button><div class="faq-answer">Processing times vary but typically take 60-90 days after submitting a complete application through a Portuguese consulate. The visa is initially valid for 4 months (entry visa), then you apply for a 1-year residence permit in Portugal after arrival.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I bring my family on the D8 visa? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. Spouses and dependent children can apply for family reunification. They need separate applications and additional income proof. The minimum income requirement increases with dependents (approximately 50% more for spouse, 30% per child).</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do I pay Portuguese taxes on my US freelance income? <span class="arrow">&#9660;</span></button><div class="faq-answer">Under NHR 2.0, Portuguese-source income is taxed at 20% flat. Foreign-source income may be exempt if taxed in the US or if it qualifies as foreign income under Portugal's rules. You should consult a Portuguese tax advisor for your specific situation.</div></div>
""",
    },
    {
        "slug": "spain",
        "name": "Spain",
        "flag": "\U0001F1EA\U0001F1F8",
        "title": "Spain Digital Nomad Visa Tax Guide 2026 — 24% Flat Rate for Remote Workers",
        "desc": "Complete guide to Spain's digital nomad visa tax rules 2026. Learn about the 24% flat tax rate, requirements, US citizen obligations & double taxation treaty benefits.",
        "h1": "Spain Digital Nomad Visa Tax Guide 2026",
        "vol": "1,200",
        "content": """
    <h2>Spain Digital Nomad Visa: Key Benefits</h2>
    <p>Spain's digital nomad visa (launched January 2023) offers remote workers the ability to live in one of Europe's most vibrant countries with a dramatically reduced tax rate. The visa allows stays of up to 3 years and is one of the most generous in terms of duration and tax benefits.</p>
    <p><strong>Key Tax Benefit:</strong> A reduced 24% flat tax rate on income under €600,000 for digital nomad visa holders. This compares to the standard Spanish progressive rate that can reach 47% — a significant savings. The 24% rate applies for the first 4-5 years of residency under the Beckham Law / Special Regime for Impatriates, which was extended to cover digital nomads.</p>
    <p><strong>Requirements:</strong> Remote work for non-Spanish companies (at least 80% of income must come from abroad), university degree or 3+ years professional experience, proof of ~€2,700/month income, health insurance, and clean criminal record.</p>

    <h2>Spain Digital Nomad Tax: What US Citizens Need to Know</h2>
    <p>For US citizens considering Spain's digital nomad visa, the tax situation involves both Spanish and US obligations:</p>
    <ul>
      <li><strong>Spanish tax:</strong> 24% flat rate on income under €600K for up to 5 years under the Special Regime. This covers both Spanish-source and foreign-source income earned while resident.</li>
      <li><strong>US tax:</strong> US citizens must file US taxes regardless of where they live. The Foreign Earned Income Exclusion (FEIE) can exclude up to ~$130,000 of foreign-earned income in 2026.</li>
      <li><strong>US-Spain Tax Treaty:</strong> The treaty provides residency tie-breaker rules, prevents double taxation through foreign tax credits, and clarifies that remote work for a US company from Spain does not create a permanent establishment.</li>
      <li><strong>Foreign Tax Credit:</strong> If you pay Spanish tax, you can claim a credit on your US return (Form 1116) to reduce US tax on the same income.</li>
    </ul>
    <p>Use our <a href="/tools/digital-nomad-tax-calculator">digital nomad tax calculator</a> to estimate your combined US-Spain tax obligations with FEIE and FTC.</p>

    <h2>Spain Tax Residency & 183-Day Rule</h2>
    <p>You become a Spanish tax resident if you spend 183 days or more in Spain during a calendar year. Spain counts partial days as full days, and short trips count toward the total. If you also have your "center of economic interests" (primary business activities or main assets) in Spain, you may be considered resident even with fewer than 183 days. The digital nomad visa specifically targets non-residents for tax purposes, but careful day-counting is essential.</p>

    <h2>Spain Digital Nomad Visa FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">How long does Spain's digital nomad visa last? <span class="arrow">&#9660;</span></button><div class="faq-answer">Initially valid for 1 year, renewable for up to 3 years total. After 5 years of legal residency, you can apply for permanent residency. After 10 years, you can apply for Spanish citizenship.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I work for Spanish companies on the digital nomad visa? <span class="arrow">&#9660;</span></button><div class="faq-answer">Up to 20% of your income can come from Spanish sources. The visa is designed for remote workers whose income primarily comes from outside Spain. If you work full-time for a Spanish company, you need a standard work visa instead.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Is the 24% tax rate guaranteed? <span class="arrow">&#9660;</span></button><div class="faq-answer">The 24% rate applies to income under €600,000 under the Special Regime for Impatriates (Beckham Law). Income above €600,000 is taxed at 47%. The regime typically lasts 5 tax years from the year you become resident. You must apply for this special tax regime when registering as a tax resident.</div></div>
""",
    },
    {
        "slug": "thailand",
        "name": "Thailand",
        "flag": "\U0001F1F9\U0001F1ED",
        "title": "Thailand Digital Nomad Visa 2026 — DTV Visa Tax Rules & Guide",
        "desc": "Complete guide to Thailand's DTV Digital Nomad Visa 2026. Tax rules, 5-year stay, territorial taxation, and remittance-based tax system explained.",
        "h1": "Thailand Digital Nomad Visa Tax Guide 2026",
        "vol": "900",
        "content": """
    <h2>Thailand DTV (Destination Thailand Visa) Overview</h2>
    <p>Thailand's Destination Thailand Visa (DTV) is designed for digital nomads, remote workers, and freelancers. Launched in mid-2024, it offers a 5-year multiple-entry visa with stays of up to 180 days per entry, extendable at immigration. It is one of Asia's most attractive digital nomad visa options due to its long validity and low cost of living (~$800-1,500/month).</p>
    <p><strong>Requirements:</strong> ~$17,000 in bank funds OR proof of income of at least $17,000/year, health insurance covering Thailand, and proof of remote work/freelance status. No minimum monthly income requirement like many European visas.</p>
    <p><strong>Tax System:</strong> Thailand operates a territorial tax system. Under new rules effective 2024, foreign-source income is only taxable in Thailand if it is <strong>remitted into Thailand in the same tax year</strong> it was earned. This means income kept in foreign bank accounts or brought in a later year may escape Thai taxation entirely.</p>

    <h2>Thailand Tax Rules for Digital Nomads</h2>
    <p>Thailand's tax system has important nuances for digital nomads:</p>
    <ul>
      <li><strong>Territorial taxation:</strong> Thailand only taxes income derived from Thailand or remitted into Thailand. Foreign income earned abroad and kept abroad is not taxed.</li>
      <li><strong>Year of remittance rule (2024 update):</strong> Foreign income is now taxable only if remitted to Thailand in the same calendar year it was earned. This creates planning opportunities for timing your transfers.</li>
      <li><strong>Tax residency:</strong> You become a Thai tax resident if you spend 183 days or more in Thailand in any calendar year. However, even as a tax resident, only remitted foreign income is taxable.</li>
      <li><strong>Progressive rates:</strong> If taxable, Thai income tax rates range from 0-35% progressive, with a personal allowance of 60,000 THB (~$1,700) and standard deduction of 50% of assessable income (capped at 100,000 THB/~$2,800).</li>
    </ul>

    <h2>Thailand-US Tax Treaty</h2>
    <p>The US-Thailand tax treaty (1965) provides basic protections but is older than many modern treaties. Key provisions include: foreign tax credit availability for US citizens paying Thai tax, residency tie-breaker rules, and permanent establishment protections. However, US citizens should consult a tax professional as the treaty's age means some provisions may not fully cover modern digital work arrangements. The FEIE can still be claimed by US citizens living in Thailand who pass the physical presence test.</p>

    <h2>Thailand DTV Visa FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I work for Thai companies on the DTV? <span class="arrow">&#9660;</span></button><div class="faq-answer">The DTV is designed for remote work. Working for a Thai company requires a separate work permit and non-B visa. DTV holders should have their primary income from outside Thailand.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">How long can I stay in Thailand on the DTV? <span class="arrow">&#9660;</span></button><div class="faq-answer">The DTV is valid for 5 years with 180-day entries. After 180 days, you can extend at immigration for 180 more days, or leave and re-enter. You cannot stay continuously for 5 years without leaving.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do I need to pay Thai tax if I keep my income abroad? <span class="arrow">&#9660;</span></button><div class="faq-answer">Under the 2024 rules, if you earn foreign income and do not remit it to Thailand in the same tax year, it is generally not taxable in Thailand. This makes Thailand very attractive for digital nomads who can manage their finances across multiple countries.</div></div>
""",
    },
    {
        "slug": "estonia",
        "name": "Estonia",
        "flag": "\U0001F1EA\U0001F1EA",
        "title": "Estonia Digital Nomad Visa & e-Residency Tax Guide 2026",
        "desc": "Complete guide to Estonia's digital nomad visa and e-Residency tax rules. Territorial taxation, 0% on foreign income, and EU business presence explained.",
        "h1": "Estonia Digital Nomad Visa Tax Guide 2026",
        "vol": "700",
        "content": """
    <h2>Estonia Digital Nomad Visa & e-Residency Overview</h2>
    <p>Estonia is unique in offering both a digital nomad visa and the world-famous e-Residency program, making it a top choice for location-independent entrepreneurs. Estonia's digital infrastructure is among the best globally, with 99% of government services available online.</p>
    <p><strong>Digital Nomad Visa:</strong> Valid for 1 year, requires minimum income of ~€5,040/month (significantly higher than most other nomad visas), and allows you to live in Estonia while working remotely. You can apply at Estonian embassies or through the digital nomad visa online portal.</p>
    <p><strong>e-Residency:</strong> Not a visa or residency permit — it's a digital identity card that allows non-residents to register and manage an EU company online. e-Residency alone does not grant tax residency or the right to live in Estonia.</p>

    <h2>Estonia Tax System for Digital Nomads</h2>
    <p>Estonia has one of the most favorable tax systems for digital nomads and freelancers:</p>
    <ul>
      <li><strong>Territorial taxation:</strong> Estonia taxes only income generated within Estonia. Foreign-sourced income is not taxed in Estonia for non-residents.</li>
      <li><strong>0% corporate tax on retained profits:</strong> Estonian companies pay 0% corporate income tax on reinvested profits. Tax is only due when profits are distributed as dividends (20/80 rate on net dividend, or 14/86 on regular dividends).</li>
      <li><strong>e-Residency company benefit:</strong> Through e-Residency, you can register an Estonian company (EU legal entity), invoice clients from the EU, and pay 0% tax on retained business income. You only pay tax when you withdraw dividends.</li>
      <li><strong>Tax residency:</strong> You become an Estonian tax resident if you spend 183 days or more in Estonia in a calendar year. Non-residents are only taxed on Estonian-source income.</li>
    </ul>

    <h2>Estonia for US Citizens</h2>
    <p>The US-Estonia tax treaty (effective 2000) provides modern protections for digital nomads and remote workers. Key features include: foreign tax credit availability, permanent establishment rules (working remotely for a US company from Estonia does not create a PE), and residency tie-breaker provisions. US citizens should note that e-Residency alone does not change US tax obligations — you still file US taxes on worldwide income and can claim FEIE if qualified.</p>

    <h2>Estonia Digital Nomad Visa FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">What is the difference between e-Residency and the digital nomad visa? <span class="arrow">&#9660;</span></button><div class="faq-answer">e-Residency is a digital identity for managing an EU company online — it does not grant the right to live or work in Estonia. The digital nomad visa allows you to physically live in Estonia for 1 year while working remotely. You can have both e-Residency and a digital nomad visa simultaneously.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">What is the minimum income for the Estonia digital nomad visa? <span class="arrow">&#9660;</span></button><div class="faq-answer">~€5,040/month (based on 4.5x Estonia's average salary). This is one of the highest minimum income requirements among digital nomad visas globally, making it best suited for high-earning remote workers and freelancers.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I extend the Estonia digital nomad visa? <span class="arrow">&#9660;</span></button><div class="faq-answer">The digital nomad visa is valid for 1 year (Type C or D visa) and is not renewable. After 1 year, you must leave Estonia or apply for a different residency permit if you qualify (e.g., business visa, start-up visa).</div></div>
""",
    },
    {
        "slug": "mexico",
        "name": "Mexico",
        "flag": "\U0001F1F2\U0001F1FD",
        "title": "Mexico Digital Nomad Tax & Temporary Resident Visa Guide 2026",
        "desc": "Complete guide to Mexico's temporary resident visa for digital nomads. Territorial tax system, no tax on foreign income, and US proximity benefits explained.",
        "h1": "Mexico Digital Nomad Tax Guide 2026",
        "vol": "800",
        "content": """
    <h2>Mexico Temporary Resident Visa for Digital Nomads</h2>
    <p>Mexico has long been one of the most popular destinations for digital nomads, offering US proximity, excellent infrastructure, rich culture, and a relatively affordable cost of living (~$1,000-1,800/month). While Mexico doesn't have a specific "digital nomad visa," the Temporary Resident Visa serves this purpose perfectly for remote workers.</p>
    <p><strong>Requirements:</strong> Proof of monthly income of ~$2,700/month for the past 6 months (or ~$43,000 in savings/investments), valid passport, and application at a Mexican consulate. The visa is initially valid for 1 year, renewable for up to 4 years. After 4 years of temporary residency, you can apply for permanent residency.</p>
    <p><strong>Tax System:</strong> Mexico operates a territorial tax system — only Mexican-source income is taxable. Foreign income earned by Mexican tax residents is generally NOT taxed in Mexico, making it highly attractive for digital nomads whose income comes from abroad.</p>

    <h2>Mexico Tax Rules for Digital Nomads</h2>
    <p>Mexico's territorial tax system offers significant advantages:</p>
    <ul>
      <li><strong>Territorial taxation:</strong> Only income from Mexican sources is taxed. Foreign income earned by residents is generally exempt from Mexican income tax.</li>
      <li><strong>Tax residency:</strong> You become a Mexican tax resident if you spend 183 days or more in Mexico in a calendar year OR if your center of vital interests is in Mexico. However, you must file a tax return if you have a permanent home in Mexico even with fewer days.</li>
      <li><strong>Progressive rates:</strong> For Mexican-source income, rates are progressive up to 35% (2026). For most digital nomads earning abroad, this doesn't apply since foreign income is not taxed.</li>
      <li><strong>No wealth tax:</strong> Mexico does not have a wealth or net worth tax, unlike some other countries.</li>
    </ul>
    <p>Note: As a Mexican tax resident, you must report your worldwide income to Mexican tax authorities, but foreign income is generally exempt from taxation. A Mexican tax advisor can help ensure proper reporting.</p>

    <h2>Mexico for US Citizens: Tax Treaty & FEIE</h2>
    <p>The US-Mexico tax treaty provides strong protections for American digital nomads. Mexico's territorial system means US citizens living in Mexico generally don't pay Mexican tax on US-sourced income. US citizens still file US taxes and can claim the FEIE if they pass the physical presence test (330+ days outside the US). The short flight distance to the US (Mexico City to many US cities is 3-4 hours) makes it easy to maintain US connections while maximizing time outside the US for FEIE qualification. However, frequent travel back to the US can jeopardize FEIE qualification — careful day counting is essential.</p>

    <h2>Mexico Digital Nomad FAQ</h2>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Can I work remotely for a US company while living in Mexico? <span class="arrow">&#9660;</span></button><div class="faq-answer">Yes. The Temporary Resident Visa allows you to work remotely for foreign companies. You cannot work for Mexican companies without a work permit. Your income should come from outside Mexico.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">Do I need to pay Mexican taxes on my US freelance income? <span class="arrow">&#9660;</span></button><div class="faq-answer">Generally no. Mexico's territorial system exempts foreign-source income from taxation. However, if you invest that income in Mexico and it generates Mexican-source returns, those returns may be taxable. Consult a Mexican tax specialist for your specific situation.</div></div>
    <div class="faq-item"><button class="faq-question" aria-expanded="false">How long does Mexico's temporary resident visa last? <span class="arrow">&#9660;</span></button><div class="faq-answer">Initially valid for 1 year, renewable annually up to 4 years total. After 4 years of temporary residency, you can apply for permanent residency. The visa is processed through Mexican consulates abroad, not within Mexico.</div></div>
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
<link rel="canonical" href="{SITE}/digital-nomad-tax/{p['slug']}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FreelanceTaxCalc">
<meta property="og:url" content="{SITE}/digital-nomad-tax/{p['slug']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p['title']}">
<meta name="twitter:description" content="{p['desc']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<script type="application/ld+json">
[{{
  "@context":"https://schema.org","@type":"WebApplication",
  "name":"{p['name']} Digital Nomad Tax Guide 2026",
  "url":"{SITE}/digital-nomad-tax/{p['slug']}",
  "description":"{p['desc']}",
  "applicationCategory":"FinanceApplication","operatingSystem":"All"
}},{{
  "@context":"https://schema.org","@type":"BreadcrumbList",
  "itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}/"}},
    {{"@type":"ListItem","position":2,"name":"Digital Nomad Tax Guides","item":"{SITE}/tools/digital-nomad-tax-calculator"}},
    {{"@type":"ListItem","position":3,"name":"{p['name']} Tax Guide"}}
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
.content-section ul,.content-section ol{{padding-left:24px;margin-bottom:20px}}
.content-section li{{font-size:16px;color:#4B5563;line-height:1.8;margin-bottom:6px}}
.content-section li strong{{color:#1A1A2E}}
.content-section ol li{{list-style-type:decimal}}
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
.nomad-links{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:24px 0}}
.nomad-links a{{padding:8px 16px;background:#F9FAFB;border:1px solid #E8ECF0;border-radius:6px;font-size:14px;font-weight:500;color:#1A1A2E;text-decoration:none;transition:all 0.2s ease}}
.nomad-links a:hover{{background:#00C896;color:#fff;border-color:#00C896}}
.nomad-links a.active{{background:#00C896;color:#fff;border-color:#00C896}}
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
    <a href="/tools/digital-nomad-tax-calculator" class="header-back">&larr; Nomad Tax Calculator</a>
  </div>
</header>
<div class="page-title">
  <div class="container">
    <h1>{p['h1']}</h1>
    <p>Everything you need to know about {p['name']}'s visa, tax rules, residency requirements &amp; double taxation treaties for digital nomads in 2026.</p>
    <span class="vol">{p['flag']} {p['vol']} searches/month &bull; 2026 Guide</span>
  </div>
</div>
<div class="nomad-links">
  <a href="/digital-nomad-tax/portugal">Portugal</a>
  <a href="/digital-nomad-tax/spain">Spain</a>
  <a href="/digital-nomad-tax/thailand">Thailand</a>
  <a href="/digital-nomad-tax/estonia">Estonia</a>
  <a href="/digital-nomad-tax/mexico">Mexico</a>
</div>
<section class="content-section">
  <div class="container">
    {p['content']}

    <div class="cta-card">
      <h3>Calculate Your Tax Situation as a Digital Nomad</h3>
      <p>Answer a few questions to get a personalized tax analysis — FEIE eligibility, double taxation risk, and top country recommendations.</p>
      <a href="/tools/digital-nomad-tax-calculator" class="btn-cta">Try the Digital Nomad Tax Calculator &rarr;</a>
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

for p in PAGES:
    fname = os.path.join(OUT, f"{p['slug']}.html")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(build_page(p))
    print(f"  Created: {p['slug']}.html")

print(f"\nDone! {len(PAGES)} country pages generated.")
