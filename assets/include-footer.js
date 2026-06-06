(function() {
  var placeholder = document.getElementById('footer-placeholder');
  if (!placeholder) return;

  function injectFooter(html) {
    placeholder.innerHTML = html;
  }

  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/assets/_footer.html', true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      injectFooter(xhr.responseText);
    }
  };
  xhr.onerror = function() {
    // Fallback: try fetch API
    fetch('/assets/_footer.html')
      .then(function(r) { return r.text(); })
      .then(function(html) { injectFooter(html); })
      .catch(function() {});
  };
  xhr.send();
})();
