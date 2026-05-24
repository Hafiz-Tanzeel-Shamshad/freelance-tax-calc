import os, re

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"

COOKIE_HTML = '''<!-- Cookie Consent -->
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
(function(){
  var banner = document.getElementById('cookie-consent');
  var accept = document.getElementById('cookie-accept');
  var decline = document.getElementById('cookie-decline');
  if(!banner || !accept) return;
  var consent = localStorage.getItem('cookie_consent');
  if(consent !== 'accepted' && consent !== 'declined'){
    banner.style.display = 'block';
  }
  accept.addEventListener('click', function(){
    localStorage.setItem('cookie_consent', 'accepted');
    banner.style.display = 'none';
    if(typeof gtag !== 'undefined'){ gtag('consent', 'update', {'analytics_storage':'granted','ad_storage':'granted'}); }
  });
  decline.addEventListener('click', function(){
    localStorage.setItem('cookie_consent', 'declined');
    banner.style.display = 'none';
    if(typeof gtag !== 'undefined'){ gtag('consent', 'update', {'analytics_storage':'denied','ad_storage':'denied'}); }
  });
})();
</script>'''

def add_cookie_consent(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'cookie-consent' in content or 'cookie_consent' in content:
        # Already has cookie consent
        return False
    
    if '</body>' not in content:
        return False
    
    content = content.replace('</body>', COOKIE_HTML + '\n</body>')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def process_all():
    count = 0
    for root, dirs, files in os.walk(ROOT):
        # Skip assets and _generators
        if 'assets' in root or '_gen' in root or '__pycache__' in root:
            continue
        for fname in files:
            if not fname.endswith('.html') or fname.startswith('_'):
                continue
            fpath = os.path.join(root, fname)
            if add_cookie_consent(fpath):
                count += 1
                rel = os.path.relpath(fpath, ROOT)
                print(f"  ADDED: {rel}")
    print(f"\nTotal: {count} files updated")

process_all()
