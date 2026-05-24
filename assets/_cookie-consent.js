/**
 * COOKIE CONSENT BANNER — FreelanceTaxCalc
 *
 * Paste this into the <script> section just before </body> on EVERY page.
 * - Shows banner on first visit
 * - Stores preference in localStorage
 * - Respects EEA/UK consent requirements
 * - "Cookie Settings" link in footer reopens the banner
 *
 * Dependencies: None (vanilla JS, no external libraries)
 */

(function() {
  'use strict';

  var COOKIE_KEY = 'ftc_cookie_consent';
  var EEA_COUNTRIES = ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','GB','CH','NO','IS','LI'];

  // ── Detect EEA/UK visitor via broad timezone hints ──
  function isEEAVisitor() {
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
      var eeaZones = ['Europe','London','Lisbon','Dublin','Berlin','Paris','Rome','Madrid','Amsterdam','Brussels','Vienna','Prague','Warsaw','Budapest','Stockholm','Copenhagen','Oslo','Helsinki','Zurich','Reykjavik'];
      for (var i = 0; i < eeaZones.length; i++) {
        if (tz.indexOf(eeaZones[i]) !== -1) return true;
      }
    } catch(e) {}
    return false;
  }

  // ── Create banner HTML ──
  function createBanner() {
    var banner = document.createElement('div');
    banner.id = 'ftc-cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.setAttribute('aria-modal', 'true');

    var isEEA = isEEAVisitor();

    banner.innerHTML =
      '<div class="ftc-cookie-inner">' +
        '<div class="ftc-cookie-text">' +
          '<p><strong>&#127850; Cookie Settings</strong></p>' +
          '<p>We use cookies to improve your experience, analyze site traffic, and serve personalized ads. By clicking "Accept All," you consent to our use of cookies. See our <a href="/privacy-policy.html" target="_blank">Privacy Policy</a> for details.</p>' +
        '</div>' +
        '<div class="ftc-cookie-actions">' +
          '<button class="ftc-btn ftc-btn-accept" data-action="accept">Accept All</button>' +
          '<button class="ftc-btn ftc-btn-reject" data-action="reject">Reject Non-Essential</button>' +
          (isEEA ? '<button class="ftc-btn ftc-btn-settings" data-action="settings">Customize</button>' : '') +
        '</div>' +
      '</div>';

    document.body.appendChild(banner);

    // ── Event listeners ──
    banner.querySelector('[data-action="accept"]').addEventListener('click', function() {
      setConsent('all');
      hideBanner();
    });

    banner.querySelector('[data-action="reject"]').addEventListener('click', function() {
      setConsent('essential');
      hideBanner();
    });

    var settingsBtn = banner.querySelector('[data-action="settings"]');
    if (settingsBtn) {
      settingsBtn.addEventListener('click', function() {
        // For now this functions like "reject" — you can wire up a CMP here
        setConsent('essential');
        hideBanner();
        // Open Google's consent UI if available
        if (typeof window.__tcfapi !== 'undefined') {
          window.__tcfapi('showUi');
        }
      });
    }
  }

  // ── Store consent in localStorage ──
  function setConsent(value) {
    try {
      localStorage.setItem(COOKIE_KEY, JSON.stringify({
        value: value,
        timestamp: new Date().toISOString(),
        eea: isEEAVisitor()
      }));
    } catch(e) {}
  }

  // ── Get stored consent ──
  function getConsent() {
    try {
      var data = JSON.parse(localStorage.getItem(COOKIE_KEY));
      return data ? data.value : null;
    } catch(e) { return null; }
  }

  // ── Show/hide banner ──
  function showBanner() {
    var banner = document.getElementById('ftc-cookie-banner');
    if (banner) banner.classList.add('ftc-visible');
  }

  function hideBanner() {
    var banner = document.getElementById('ftc-cookie-banner');
    if (banner) {
      banner.classList.remove('ftc-visible');
      setTimeout(function() { if (banner.parentNode) banner.parentNode.removeChild(banner); }, 400);
    }
  }

  // ── Initialize ──
  function init() {
    // Don't show if already consented
    if (getConsent()) return;

    // Don't show on legal pages (optional, but polite)
    var legalPages = ['privacy-policy','terms','about','contact'];
    var path = window.location.pathname.replace('.html','');
    for (var i = 0; i < legalPages.length; i++) {
      if (path.indexOf(legalPages[i]) !== -1) return;
    }

    createBanner();
    // Small delay for page paint
    setTimeout(showBanner, 500);

    // Wire up "Cookie Settings" links in footer
    document.querySelectorAll('a[href="#cookie-preferences"], a[href*="cookie"]').forEach(function(link) {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        // Remove existing consent and re-show banner
        try { localStorage.removeItem(COOKIE_KEY); } catch(e) {}
        if (!document.getElementById('ftc-cookie-banner')) {
          createBanner();
        }
        showBanner();
      });
    });
  }

  // ── Styles injected via JS ──
  function injectStyles() {
    var style = document.createElement('style');
    style.textContent =
      '#ftc-cookie-banner{' +
        'position:fixed;bottom:0;left:0;right:0;z-index:999999;' +
        'background:#0A1628;color:#D1D5DB;padding:16px 24px;' +
        'font-family:"DM Sans",sans-serif;font-size:14px;line-height:1.6;' +
        'transform:translateY(100%);opacity:0;' +
        'transition:all 0.4s cubic-bezier(0.4,0,0.2,1);' +
        'box-shadow:0 -4px 24px rgba(0,0,0,0.3);' +
      '}' +
      '#ftc-cookie-banner.ftc-visible{transform:translateY(0);opacity:1}' +
      '.ftc-cookie-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}' +
      '.ftc-cookie-text p{margin:0;font-size:13px}' +
      '.ftc-cookie-text p:first-child{font-size:14px;margin-bottom:4px}' +
      '.ftc-cookie-text a{color:#00C896;text-decoration:underline}' +
      '.ftc-cookie-actions{display:flex;gap:8px;flex-shrink:0;flex-wrap:wrap}' +
      '.ftc-btn{border:none;padding:8px 18px;border-radius:8px;font-family:"DM Sans",sans-serif;font-size:13px;font-weight:600;cursor:pointer;transition:all 0.2s ease}' +
      '.ftc-btn-accept{background:#00C896;color:#fff}' +
      '.ftc-btn-accept:hover{background:#00B085}' +
      '.ftc-btn-reject{background:transparent;color:#B0B8C4;border:1px solid #4B5563}' +
      '.ftc-btn-reject:hover{background:rgba(255,255,255,0.05);color:#fff}' +
      '.ftc-btn-settings{background:transparent;color:#B0B8C4;border:1px solid #4B5563}' +
      '.ftc-btn-settings:hover{background:rgba(255,255,255,0.05);color:#fff}' +
      '@media(max-width:600px){' +
        '#ftc-cookie-banner{padding:16px}' +
        '.ftc-cookie-actions{width:100%}' +
        '.ftc-btn{flex:1;text-align:center;font-size:12px;padding:10px 12px}' +
      '}';
    document.head.appendChild(style);
  }

  // ── Boot ──
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      injectStyles();
      init();
    });
  } else {
    injectStyles();
    init();
  }
})();
