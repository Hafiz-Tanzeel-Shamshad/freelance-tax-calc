import os, re

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

FOOTER_CSS = '''
/* FOOTER */
.site-footer{background:#0A1628;color:#B0B8C4;padding:40px 0 24px;margin-top:40px}
.site-footer .container{max-width:1100px;margin:0 auto;padding:0 24px}
.footer-inner{display:flex;flex-wrap:wrap;gap:32px;margin-bottom:28px}
.footer-brand{flex:1;min-width:200px}
.footer-logo{display:flex;align-items:center;gap:8px;font-family:"DM Serif Display",serif;font-size:18px;font-weight:700;color:#fff;text-decoration:none}
.footer-logo-icon{width:28px;height:28px;background:#00C896;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;font-weight:700;flex-shrink:0}
.logo-dot{color:#00C896}
.footer-tagline{font-size:13px;color:#8892A0;margin-top:8px}
.footer-links{display:flex;flex-wrap:wrap;gap:32px}
.footer-col h4{font-family:"DM Serif Display",serif;font-size:14px;color:#fff;margin-bottom:10px}
.footer-col ul{list-style:none;padding:0;margin:0}
.footer-col ul li{margin-bottom:6px}
.footer-col ul li a{font-size:13px;color:#8892A0;text-decoration:none;transition:color 0.3s ease}
.footer-col ul li a:hover{color:#00C896}
.footer-bottom{border-top:1px solid rgba(255,255,255,0.08);padding-top:16px;font-size:12px;color:#667080;text-align:center;line-height:1.6}
.footer-bottom a{color:#00C896;text-decoration:none}
.footer-bottom a:hover{text-decoration:underline}
@media(max-width:768px){.footer-inner{flex-direction:column;gap:24px}}
'''

FOOTER_HTML = '''<!-- FOOTER -->
<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-brand">
        <a href="/" class="footer-logo" aria-label="FreelanceTaxCalc Home">
          <span class="footer-logo-icon" aria-hidden="true">$</span>
          Freelance<span class="logo-dot">.</span>TaxCalc
        </a>
        <p class="footer-tagline">Free financial tools for independent workers.</p>
      </div>
      <div class="footer-links">
        <div class="footer-col">
          <h4>Tools</h4>
          <ul>
            <li><a href="/tools/quarterly-tax-calculator.html">Quarterly Tax Estimator</a></li>
            <li><a href="/tools/gig-deduction-finder.html">Gig Worker Deduction Finder</a></li>
            <li><a href="/tools/freelance-hourly-rate-calculator.html">Hourly Rate Calculator</a></li>
            <li><a href="/tools/digital-nomad-tax-calculator.html">Digital Nomad Tax Calculator</a></li>
            <li><a href="/tools/1099-vs-w2-calculator.html">1099 vs W-2 Calculator</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <ul>
            <li><a href="/guides/index.html">Guides</a></li>
            <li><a href="/legal/about.html">About Us</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/legal/privacy-policy.html">Privacy Policy</a></li>
            <li><a href="/legal/terms.html">Terms of Service</a></li>
            <li><a href="/legal/disclaimer.html">Disclaimer</a></li>
            <li><a href="#cookie-preferences">Cookie Settings</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      This website provides estimates for informational purposes only. Not financial or tax advice. | We use cookies and display ads. See <a href="/legal/privacy-policy.html">Privacy Policy</a> for details.
    </div>
  </div>
</footer>'''

def replace_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file already has the NEW footer (Privacy Policy link in footer)
    if '<a href="/legal/privacy-policy.html">Privacy Policy</a>' in content and 'footer-inner' in content:
        print(f"  OK (already has full footer): {os.path.basename(filepath)}")
        return False
    
    # Pattern 1: Old minimal footer HTML (with or without ===)
    old_footer_patterns = [
        # Pattern: the exact minimal footer structure
        r'<!--\s*===\s*FOOTER\s*===\s*-->\s*<footer class="site-footer" role="contentinfo">\s*<div class="container">\s*<span class="copyright">&copy; 2026 FreelanceTaxCalc[^<]*</span>\s*<a href="/">Back to Home</a>\s*</div>\s*</footer>',
        r'<!--\s*===\s*FOOTER\s*===\s*-->\s*<footer class="site-footer" role="contentinfo">\s*<div class="container">\s*<span class="copyright">&copy; 2026 FreelanceTaxCalc[^<]*</span>\s*</div>\s*</footer>',
        r'<!-- FOOTER -->\s*<footer class="site-footer" role="contentinfo">\s*<div class="container">\s*<span class="copyright">&copy; 2026 FreelanceTaxCalc[^<]*</span>\s*<a href="/">Back to Home</a>\s*</div>\s*</footer>',
        r'<!-- FOOTER -->\s*<footer class="site-footer" role="contentinfo">\s*<div class="container">\s*<span class="copyright">&copy; 2026 FreelanceTaxCalc[^<]*</span>\s*</div>\s*</footer>',
    ]
    
    replaced = False
    for pattern in old_footer_patterns:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, FOOTER_HTML, content, flags=re.DOTALL)
            replaced = True
            break
    
    if not replaced:
        # Try a more general pattern
        old_pattern = r'<!-- FOOTER -->\s*<footer class="site-footer"[^>]*>.*?</footer>'
        if re.search(old_pattern, content, re.DOTALL):
            content = re.sub(old_pattern, FOOTER_HTML, content, flags=re.DOTALL)
            replaced = True
    
    if not replaced:
        print(f"  SKIP (pattern not found): {os.path.basename(filepath)}")
        return False
    
    # Replace old footer CSS with new
    old_css_patterns = [
        r'/\* === FOOTER === \*/\s*\.site-footer\{background[^}]*\}\s*\.site-footer \.container\{display[^}]*\}\s*\.site-footer a\{color[^}]*\}\s*\.site-footer a:hover\{color[^}]*\}\s*\.site-footer \.copyright\{font-size[^}]*\}',
        r'/\* FOOTER \*/\s*\.site-footer\{background[^}]*\}\s*\.site-footer \.container\{display[^}]*\}\s*\.site-footer a\{color[^}]*\}\s*\.site-footer a:hover\{color[^}]*\}\s*\.site-footer \.copyright\{font-size[^}]*\}',
    ]
    css_replaced = False
    for p in old_css_patterns:
        if re.search(p, content, re.DOTALL):
            content = re.sub(p, FOOTER_CSS, content, flags=re.DOTALL)
            css_replaced = True
            break
    
    if not css_replaced:
        # Try simpler CSS pattern
        simpler = r'/\*.*?FOOTER.*?\*/.*?(?=/\*|\n@media|\n\n)'
        if re.search(simpler, content, re.DOTALL):
            content = re.sub(simpler, FOOTER_CSS, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  UPDATED: {os.path.basename(filepath)}")
    return True

def process_directory(dirpath, label):
    if not os.path.isdir(dirpath):
        return
    count = 0
    for fname in sorted(os.listdir(dirpath)):
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(dirpath, fname)
        if os.path.isdir(fpath):
            continue
        if replace_footer(fpath):
            count += 1
    print(f"  {label}: {count} files updated")

process_directory(os.path.join(ROOT, 'tools'), 'Tools')
process_directory(os.path.join(ROOT, 'tools/quarterly-tax-calculator'), 'State pages')
process_directory(os.path.join(ROOT, 'deductions'), 'Deductions')
process_directory(os.path.join(ROOT, 'digital-nomad-tax'), 'Nomad')

print("\nDone!")
