(function() {
  'use strict';

  if ('ontouchstart' in window) return;

  var cardSelector = [
    '.tool-card',
    '.guide-card',
    '.blog-card',
    '.testimonial-card',
    '.step-card',
    '.persona-card',
    '.tool-item'
  ].join(',');

  var cards = document.querySelectorAll(cardSelector);
  if (!cards.length) return;

  // ---- Staggered float delays ----
  cards.forEach(function(card, i) {
    card.style.setProperty('--float-delay', (i * 0.12) + 's');
  });

  // ---- Apply depth classes to inner elements ----
  cards.forEach(function(card) {
    var icon = card.querySelector(
      '.tool-icon, .step-icon, .persona-icon, .blog-card-icon, .tool-item-icon, .testimonial-avatar'
    );
    var badge = card.querySelector('.tool-badge, .guide-category, .tool-item-tag, .badge');
    var heading = card.querySelector('h3, h2');
    var link = card.querySelector('.tool-link, .guide-link, .read-link, .btn-primary, .btn');
    var desc = card.querySelector(
      '.tool-desc, .guide-excerpt, .excerpt, .testimonial-text, .tool-item-desc, p'
    );

    if (icon) icon.classList.add('tilt-depth-1');
    if (badge) badge.classList.add('tilt-depth-2');
    if (heading) heading.classList.add('tilt-depth-2');
    if (link) link.classList.add('tilt-depth-3');
    if (desc) desc.classList.add('tilt-depth-4');

    // Create shine element
    if (!card.querySelector('.tilt-shine')) {
      var shine = document.createElement('div');
      shine.className = 'tilt-shine';
      card.appendChild(shine);
    }
  });

  // ---- Enhanced 3D Tilt with spring-like easing ----
  var tiltData = new WeakMap();

  cards.forEach(function(card) {
    var data = {
      tx: 0, ty: 0,
      targetTX: 0, targetTY: 0,
      rafId: null,
      strength: card.classList.contains('tool-item') ? 12 : 15
    };
    tiltData.set(card, data);

    card.addEventListener('mousemove', function(e) {
      var rect = this.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      var cx = rect.width / 2;
      var cy = rect.height / 2;
      var s = data.strength;

      data.targetTX = ((y - cy) / cy) * -s;
      data.targetTY = ((x - cx) / cx) * s;

      var sx = (x / rect.width) * 100;
      var sy = (y / rect.height) * 100;
      this.style.setProperty('--sx', sx + '%');
      this.style.setProperty('--sy', sy + '%');

      // Update border angle
      var angle = Math.atan2(y - cy, x - cx) * (180 / Math.PI);
      this.style.setProperty('--border-angle', angle + 'deg');

      if (!data.rafId) {
        data.rafId = requestAnimationFrame(function smoothTilt() {
          data.tx += (data.targetTX - data.tx) * 0.15;
          data.ty += (data.targetTY - data.ty) * 0.15;

          var isResting =
            Math.abs(data.tx) < 0.02 &&
            Math.abs(data.ty) < 0.02 &&
            Math.abs(data.targetTX) < 0.02 &&
            Math.abs(data.targetTY) < 0.02;

          if (isResting) {
            card.style.setProperty('--tx', '0deg');
            card.style.setProperty('--ty', '0deg');
            data.rafId = null;
            return;
          }

          card.style.setProperty('--tx', data.tx + 'deg');
          card.style.setProperty('--ty', data.ty + 'deg');
          data.rafId = requestAnimationFrame(smoothTilt);
        });
      }
    });

    card.addEventListener('mouseleave', function() {
      data.targetTX = 0;
      data.targetTY = 0;
    });
  });

  // ---- Energy Ring on Click ----
  cards.forEach(function(card) {
    card.addEventListener('click', function(e) {
      var rect = this.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;

      var ring = document.createElement('div');
      ring.className = 'energy-ring';
      ring.style.cssText =
        'left:' + x + 'px;top:' + y + 'px;';

      // Ensure position context
      if (getComputedStyle(this).position === 'static') {
        this.style.position = 'relative';
      }

      this.appendChild(ring);

      // Remove after animation
      setTimeout(function() {
        if (ring.parentNode) ring.parentNode.removeChild(ring);
      }, 900);
    });
  });

  // ---- Particle Sparkles on Mouse Enter (enhanced) ----
  cards.forEach(function(card) {
    card.addEventListener('mouseenter', function(e) {
      var rect = this.getBoundingClientRect();
      var container = this.querySelector('.tilt-shine');
      if (!container) return;

      var count = 8 + Math.floor(Math.random() * 8);

      for (var i = 0; i < count; i++) {
        var particle = document.createElement('span');
        particle.className = 'tilt-particle';

        var isGold = Math.random() > 0.6;
        var color = isGold
          ? 'rgba(255, 215, 0, ' + (0.4 + Math.random() * 0.4) + ')'
          : 'rgba(0, 200, 150, ' + (0.3 + Math.random() * 0.5) + ')';

        var size = 2 + Math.random() * 3;
        var x = Math.random() * rect.width;
        var y = Math.random() * rect.height;
        var dx = (Math.random() - 0.5) * 80;
        var dy = -(30 + Math.random() * 70);
        var life = 500 + Math.random() * 500;

        particle.style.cssText =
          'position:absolute;' +
          'width:' + size + 'px;' +
          'height:' + size + 'px;' +
          'background:' + color + ';' +
          'border-radius:50%;' +
          'pointer-events:none;' +
          'z-index:3;' +
          'left:' + x + 'px;' +
          'top:' + y + 'px;';

        container.appendChild(particle);

        var startTime = performance.now();
        function animParticle(now) {
          var elapsed = now - startTime;
          var progress = elapsed / life;
          if (progress >= 1) {
            if (particle.parentNode) particle.parentNode.removeChild(particle);
            return;
          }
          var ease = 1 - Math.pow(1 - progress, 3);
          var xOff = dx * ease;
          var yOff = dy * ease;
          var fade = Math.sin(progress * Math.PI) * (1 - progress * 0.6);
          particle.style.transform = 'translate(' + xOff + 'px, ' + yOff + 'px)';
          particle.style.opacity = fade;
          requestAnimationFrame(animParticle);
        }
        requestAnimationFrame(animParticle);
      }
    });
  });

  // ---- Ambient Particle Backgrounds for Sections ----
  function initAmbientParticles() {
    var sections = document.querySelectorAll(
      '.tools-section, .how-section, .target-section, .testimonial-section, .guides-section'
    );

    sections.forEach(function(section) {
      if (section.querySelector('.section-ambient canvas')) return;

      var container = section.querySelector('.section-ambient');
      if (!container) {
        container = document.createElement('div');
        container.className = 'section-ambient';
        section.insertBefore(container, section.firstChild);
      }

      var canvas = document.createElement('canvas');
      container.appendChild(canvas);

      var ctx = canvas.getContext('2d');
      var w, h;
      var particles = [];

      function resize() {
        var rect = section.getBoundingClientRect();
        w = rect.width;
        h = rect.height;
        canvas.width = w;
        canvas.height = h;
      }

      function createParticles() {
        particles = [];
        var count = Math.min(Math.floor((w * h) / 15000), 40);
        for (var i = 0; i < count; i++) {
          particles.push({
            x: Math.random() * w,
            y: Math.random() * h,
            r: 1 + Math.random() * 2.5,
            dx: (Math.random() - 0.5) * 0.3,
            dy: -(0.1 + Math.random() * 0.2),
            alpha: 0.15 + Math.random() * 0.35,
            phase: Math.random() * Math.PI * 2
          });
        }
      }

      function draw() {
        ctx.clearRect(0, 0, w, h);
        var time = Date.now() * 0.001;

        particles.forEach(function(p) {
          p.x += p.dx;
          p.y += p.dy;
          p.alpha += Math.sin(time + p.phase) * 0.001;

          if (p.alpha < 0.05) p.alpha = 0.05;
          if (p.alpha > 0.5) p.alpha = 0.5;
          if (p.y < -10) { p.y = h + 10; p.x = Math.random() * w; }
          if (p.x < -10) p.x = w + 10;
          if (p.x > w + 10) p.x = -10;

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(0, 200, 150, ' + p.alpha + ')';
          ctx.fill();
        });

        requestAnimationFrame(draw);
      }

      resize();
      createParticles();
      draw();

      // Re-initialize on resize
      var resizeTimer;
      window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
          resize();
          createParticles();
        }, 300);
      });
    });
  }
  initAmbientParticles();

  // ---- Reset tilt on resize ----
  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      cards.forEach(function(card) {
        var data = tiltData.get(card);
        if (data) {
          data.targetTX = 0;
          data.targetTY = 0;
          data.tx = 0;
          data.ty = 0;
          card.style.setProperty('--tx', '0deg');
          card.style.setProperty('--ty', '0deg');
        }
      });
    }, 250);
  });
})();
