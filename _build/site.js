(function () {
  'use strict';
  window.__aa = true;
  var root = document.documentElement;
  var body = document.body;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  var motion = root.classList.contains('motion') && !reduce;
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
  var lerp = function (a, b, t) { return a + (b - a) * t; };

  /* ---------- smooth scrolling (Lenis, when it loaded) */
  var lenis = null;
  if (motion && window.Lenis) {
    try {
      lenis = new window.Lenis({ lerp: 0.09, wheelMultiplier: 1 });
      var tick = function (t) { lenis.raf(t); requestAnimationFrame(tick); };
      requestAnimationFrame(tick);
    } catch (e) { lenis = null; }
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="#"]');
    if (!a || a.target === '_blank' || a.getAttribute('href') === '#main') return;
    var url = new URL(a.href, location.href);
    if (url.pathname !== location.pathname || !url.hash) return;
    var target = url.hash === '#top' ? document.getElementById('top') : document.getElementById(url.hash.slice(1));
    if (!target) return;
    e.preventDefault();
    if (lenis) lenis.scrollTo(target, { offset: url.hash === '#top' ? 0 : -8, duration: 1.4 });
    else target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
    if (url.hash !== '#top' && url.hash !== '#main') { try { history.replaceState(null, '', url.hash); } catch (err) {} }
  });

  /* ---------- header: solid after the hero starts to scroll, hides going down, returns going up */
  var head = $('.site-head');
  var bar = $('.progress');
  var lastY = window.scrollY;
  var mark = $('.contact .mark');
  function onScroll() {
    var y = window.scrollY;
    var max = Math.max(1, document.documentElement.scrollHeight - innerHeight);
    if (head) {
      head.classList.toggle('solid', y > 40 || !body.classList.contains('home'));
      if (y > 320 && y > lastY + 4) head.classList.add('away');
      else if (y < lastY - 4 || y < 320) head.classList.remove('away');
    }
    if (bar) bar.style.setProperty('--p', (y / max).toFixed(4));
    if (mark && !reduce) mark.style.setProperty('--r', (y * 0.12 % 360).toFixed(1) + 'deg');
    lastY = y;
  }
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- hero: fit the name, line the outline copy up with the portrait, load sequence, parallax */
  var hero = $('.hero');
  if (hero) {
    var stage = $('.hero-stage', hero);
    var portrait = $('.portrait', hero);
    var lines = $$('h1.name .name-line', hero);
    var cur = { tx: 0, ty: 0, px: 0, py: 0 }, aim = { mx: 0, my: 0 };
    var fit = function () {
      var W = stage.clientWidth, H = stage.clientHeight;
      var stack = getComputedStyle(hero).getPropertyValue('--mode').trim() === 'stack';
      var gutter = parseFloat(getComputedStyle($('.hero-foot', hero)).paddingLeft) || 16;
      var pw = portrait.offsetWidth, ph = portrait.offsetHeight;
      var cx = parseFloat(getComputedStyle(portrait).left) || W / 2;      /* portrait centre in px */
      hero.style.setProperty('--name-size', '100px');
      var widest = Math.max.apply(null, lines.map(function (l) { return l.offsetWidth; }));
      /* side by side: the surname ends a third of the way into the portrait, behind the shoulder;
         stacked (phones, tall screens): the name spans the width across the chest */
      var target = stack ? W - gutter * 2 : (cx - pw / 2 + pw * 0.34) - gutter;
      var size = 100 * target / Math.max(1, widest);
      size = Math.min(size, H * (stack ? 0.2 : 0.3));
      hero.style.setProperty('--name-size', size.toFixed(2) + 'px');
      hero.style.setProperty('--mw', pw + 'px');
      hero.style.setProperty('--mh', ph + 'px');
      hero.style.setProperty('--mx0', (cx - pw / 2).toFixed(1) + 'px');
      hero.style.setProperty('--my0', (H - ph).toFixed(1) + 'px');
    };
    fit();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
    var rt;
    addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(fit, 60); });

    var img = $('img', portrait);
    var go = function () { hero.classList.add('ready'); body.classList.add('ready'); };
    if (!motion) go();
    else {
      var started = false;
      var start = function () { if (started) return; started = true; requestAnimationFrame(function () { requestAnimationFrame(go); }); };
      Promise.all([
        img.complete ? Promise.resolve() : new Promise(function (r) { img.addEventListener('load', r); img.addEventListener('error', r); }),
        document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()
      ]).then(start);
      setTimeout(start, 1600);
    }

    if (motion) {
      if (fine) {
        hero.addEventListener('pointermove', function (e) {
          var r = hero.getBoundingClientRect();
          aim.mx = (e.clientX - r.left) / r.width - 0.5;
          aim.my = (e.clientY - r.top) / r.height - 0.5;
          hero.style.setProperty('--cx', (e.clientX - r.left).toFixed(0) + 'px');
          hero.style.setProperty('--cy', (e.clientY - r.top).toFixed(0) + 'px');
        });
        hero.addEventListener('pointerleave', function () { aim.mx = 0; aim.my = 0; });
      }
      var loop = function () {
        var H = stage.clientHeight, W = stage.clientWidth;
        var p = clamp(window.scrollY / H, 0, 1.2);
        if (p < 1.15) {
          var t = { tx: -aim.mx * 26 - p * W * 0.16, ty: -aim.my * 10 - p * 70, px: aim.mx * 14, py: aim.my * 6 + p * H * 0.16 };
          var changed = false;
          for (var k in t) {
            var v = lerp(cur[k], t[k], 0.09);
            if (Math.abs(v - cur[k]) > 0.02) changed = true;
            cur[k] = v;
          }
          if (changed) {
            hero.style.setProperty('--tx', cur.tx.toFixed(2) + 'px');
            hero.style.setProperty('--ty', cur.ty.toFixed(2) + 'px');
            hero.style.setProperty('--px', cur.px.toFixed(2) + 'px');
            hero.style.setProperty('--py', cur.py.toFixed(2) + 'px');
          }
        }
        requestAnimationFrame(loop);
      };
      requestAnimationFrame(loop);
    }
  } else {
    body.classList.add('ready');
  }

  /* ---------- reveal on scroll */
  var io = null;
  var revealables = $$('.rv, .rv-img, .split, .canvas, .steps');
  if (motion && 'IntersectionObserver' in window) {
    io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
        if (e.target.classList.contains('canvas')) drawIn();
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- the node canvas: wires that draw in, signals that travel, nodes that drag */
  var canvas = $('.canvas');
  var wires = [];
  var drawn = false;
  /* positions ignore the reveal offset (the CSS translate), so wires land where the nodes come to rest */
  function settle(node) {
    var t = (getComputedStyle(node).translate || '').split(' ');
    return { x: parseFloat(t[0]) || 0, y: parseFloat(t[1]) || 0 };
  }
  function portPoint(node, which, box) {
    var r = node.querySelector('.port.' + which).getBoundingClientRect(), o = settle(node);
    return { x: r.left + r.width / 2 - box.left - o.x, y: r.top + r.height / 2 - box.top - o.y };
  }
  function wirePath(i, nodes, rects, box) {
    var a = portPoint(nodes[i], 'out', box), b = portPoint(nodes[i + 1], 'in', box);
    if (b.x > a.x + 16) {
      var dx = Math.max(60, (b.x - a.x) * 0.45);
      return 'M' + a.x + ' ' + a.y + ' C' + (a.x + dx) + ' ' + a.y + ' ' + (b.x - dx) + ' ' + b.y + ' ' + b.x + ' ' + b.y;
    }
    /* back to the next row: down the right side, across the gap between rows, in from the left */
    var above = 0, below = Infinity, k;
    for (k = 0; k <= i; k++) above = Math.max(above, rects[k].bottom);
    for (k = i + 1; k < rects.length; k++) below = Math.min(below, rects[k].top);
    var lane = below > above ? (above + below) / 2 : Math.max(a.y, b.y) - 20;
    var xr = a.x + 28, xl = b.x - 28, r = Math.max(4, Math.min(18, Math.abs(lane - a.y) / 2, Math.abs(b.y - lane) / 2));
    var s1 = lane > a.y ? 1 : -1, s2 = b.y > lane ? 1 : -1;
    return 'M' + a.x + ' ' + a.y + ' H' + (xr - r) + ' Q' + xr + ' ' + a.y + ' ' + xr + ' ' + (a.y + s1 * r) +
           ' V' + (lane - s1 * r) + ' Q' + xr + ' ' + lane + ' ' + (xr - r) + ' ' + lane +
           ' H' + (xl + r) + ' Q' + xl + ' ' + lane + ' ' + xl + ' ' + (lane + s2 * r) +
           ' V' + (b.y - s2 * r) + ' Q' + xl + ' ' + b.y + ' ' + (xl + r) + ' ' + b.y + ' H' + b.x;
  }
  function layoutWires(restartSignals) {
    if (!canvas) return;
    var svg = $('.wires', canvas);
    if (getComputedStyle(svg).display === 'none') return;
    var nodes = $$('.node', canvas);
    var box = canvas.getBoundingClientRect();
    var rects = nodes.map(function (n) { var r = n.getBoundingClientRect(), o = settle(n); return { top: r.top - box.top - o.y, bottom: r.bottom - box.top - o.y }; });
    svg.setAttribute('viewBox', '0 0 ' + box.width + ' ' + box.height);
    if (wires.length !== nodes.length - 1) {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      wires = [];
      for (var i = 0; i < nodes.length - 1; i++) {
        var base = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        var sig = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        base.dataset.from = i; base.dataset.to = i + 1; sig.setAttribute('class', 'sig');
        if (motion && !drawn) { base.style.opacity = '0'; sig.style.opacity = '0'; }
        svg.appendChild(base); svg.appendChild(sig);
        wires.push({ base: base, sig: sig, anim: null });
      }
    }
    wires.forEach(function (w, i) {
      var d = wirePath(i, nodes, rects, box);
      w.base.setAttribute('d', d); w.sig.setAttribute('d', d);
    });
    if (restartSignals && drawn) startSignals();
  }
  function startSignals() {
    if (!motion) { wires.forEach(function (w) { w.sig.style.opacity = '0'; }); return; }
    wires.forEach(function (w, i) {
      var len = w.base.getTotalLength();
      if (w.anim) w.anim.cancel();
      w.sig.style.opacity = '1';
      w.sig.style.strokeDasharray = '16 ' + (len + 16);
      w.anim = w.sig.animate([{ strokeDashoffset: 16 }, { strokeDashoffset: -len }],
        { duration: Math.max(1400, len * 3.2), iterations: Infinity, delay: i * 420, easing: 'cubic-bezier(.6,0,.4,1)' });
    });
  }
  function drawIn() {
    if (drawn || !canvas) return;
    layoutWires(false);
    drawn = true;
    wires.forEach(function (w, i) {
      var len = w.base.getTotalLength();
      w.base.style.opacity = '1';
      w.base.style.strokeDasharray = len + ' ' + len;
      var a = w.base.animate([{ strokeDashoffset: len }, { strokeDashoffset: 0 }], { duration: 1100, delay: 500 + i * 160, easing: 'cubic-bezier(.7,0,.2,1)', fill: 'both' });
      a.onfinish = function () { w.base.style.strokeDasharray = ''; a.cancel(); };
    });
    setTimeout(startSignals, 500 + wires.length * 160 + 900);
  }
  if (canvas) {
    if (!motion) { drawn = true; }
    layoutWires(false);
    if (!motion) startSignals();
    var wt;
    addEventListener('resize', function () { clearTimeout(wt); wt = setTimeout(function () { layoutWires(true); }, 80); });
    addEventListener('load', function () { layoutWires(true); });
    $$('img', canvas).forEach(function (im) { im.addEventListener('load', function () { layoutWires(false); }); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { layoutWires(false); });

    $$('.node', canvas).forEach(function (n, i) {
      var light = function (on) {
        wires.forEach(function (w) { if (+w.base.dataset.from === i || +w.base.dataset.to === i) w.base.classList.toggle('on', on); });
      };
      n.addEventListener('mouseenter', function () { light(true); });
      n.addEventListener('mouseleave', function () { light(false); });
      n.addEventListener('focus', function () { light(true); });
      n.addEventListener('blur', function () { light(false); });

      /* drag (mouse and pen on wide screens) */
      var drag = null;
      n.addEventListener('pointerdown', function (e) {
        if (!fine || e.button !== 0 || innerWidth <= 900) return;
        drag = { x: e.clientX, y: e.clientY, dx: parseFloat(n.style.getPropertyValue('--dx')) || 0, dy: parseFloat(n.style.getPropertyValue('--dy')) || 0, moved: false, id: e.pointerId };
      });
      n.addEventListener('pointermove', function (e) {
        if (!drag) return;
        var mx = e.clientX - drag.x, my = e.clientY - drag.y;
        if (!drag.moved) {
          if (Math.hypot(mx, my) < 6) return;
          drag.moved = true; n.classList.add('dragging');
          try { n.setPointerCapture(drag.id); } catch (err) {}
          cursorLabel('Drag');
        }
        var c = canvas.getBoundingClientRect(), r = n.getBoundingClientRect();
        var nx = drag.dx + mx, ny = drag.dy + my;
        var curx = parseFloat(n.style.getPropertyValue('--dx')) || 0, cury = parseFloat(n.style.getPropertyValue('--dy')) || 0;
        var left0 = r.left - curx, top0 = r.top - cury;
        nx = clamp(nx, c.left - 40 - left0, c.right + 40 - r.width - left0);
        ny = clamp(ny, c.top - 40 - top0, c.bottom + 40 - r.height - top0);
        n.style.setProperty('--dx', nx.toFixed(1) + 'px');
        n.style.setProperty('--dy', ny.toFixed(1) + 'px');
        layoutWires(false);
      });
      var end = function () {
        if (!drag) return;
        var moved = drag.moved;
        drag = null;
        n.classList.remove('dragging');
        if (moved) {
          n.addEventListener('click', function (ev) { ev.preventDefault(); ev.stopImmediatePropagation(); }, { once: true, capture: true });
          layoutWires(true);
          cursorLabel('Open');
        }
      };
      n.addEventListener('pointerup', end);
      n.addEventListener('pointercancel', end);
    });
  }

  /* ---------- cursor label over work */
  var cursor = $('.cursor');
  var cursorText = cursor ? $('span', cursor) : null;
  function cursorLabel(t) { if (cursorText && t) cursorText.textContent = t; }
  if (cursor && fine && motion) {
    var cx = -200, cy = -200, tx = -200, ty = -200, on = false;
    addEventListener('pointermove', function (e) { tx = e.clientX; ty = e.clientY; }, { passive: true });
    document.addEventListener('pointerover', function (e) {
      var t = e.target.closest('[data-cursor]');
      if (t) { if (!t.classList.contains('dragging')) cursorLabel(t.dataset.cursor); if (!on) { cx = tx; cy = ty; } on = true; cursor.classList.add('on'); cursor.classList.toggle('alt', t.classList.contains('next')); }
    });
    document.addEventListener('pointerout', function (e) {
      var t = e.target.closest('[data-cursor]');
      if (t && !(e.relatedTarget && t.contains(e.relatedTarget))) { on = false; cursor.classList.remove('on'); }
    });
    var follow = function () {
      cx = lerp(cx, tx, 0.2); cy = lerp(cy, ty, 0.2);
      cursor.style.setProperty('--x', cx.toFixed(1) + 'px');
      cursor.style.setProperty('--y', cy.toFixed(1) + 'px');
      requestAnimationFrame(follow);
    };
    requestAnimationFrame(follow);
  } else if (cursor) {
    cursor.remove();
  }

  /* ---------- filters on the work index */
  var chips = $$('.chip');
  var cards = $$('.grid .card');
  function setFilter(cat, animate) {
    chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c.dataset.cat === cat)); });
    cards.forEach(function (card, i) {
      var show = cat === 'all' || card.dataset.cat === cat;
      clearTimeout(card._t);
      if (!animate || !motion) { card.hidden = !show; card.classList.remove('out'); return; }
      if (!show && !card.hidden) {
        card.classList.add('out');
        card._t = setTimeout(function () { card.hidden = true; }, 260);
      } else if (show) {
        if (card.hidden) { card.classList.add('out'); card.hidden = false; card.classList.add('in'); }
        card._t = setTimeout(function () { card.classList.remove('out'); }, 280 + (i % 5) * 40);
      }
    });
    try { localStorage.setItem('aa-filter', cat); } catch (e) {}
    if (lenis) setTimeout(function () { lenis.resize(); }, 320);
  }
  chips.forEach(function (c) { c.addEventListener('click', function () { setFilter(c.dataset.cat, true); }); });
  if (chips.length) {
    var saved = 'all';
    try { saved = localStorage.getItem('aa-filter') || 'all'; } catch (e) {}
    if (!$('.chip[data-cat="' + saved + '"]')) saved = 'all';
    setFilter(saved, false);
  }

  /* ---------- lightbox */
  var lb = document.getElementById('lb');
  if (lb && typeof lb.showModal === 'function') {
    var shots = $$('[data-full]');
    var big = $('img', lb), count = $('.lb-count', lb), at = 0;
    var show = function (i, swap) {
      at = (i + shots.length) % shots.length;
      var apply = function () { big.src = shots[at].dataset.full; big.alt = shots[at].alt || ''; count.textContent = (at + 1) + ' of ' + shots.length; big.classList.remove('swap'); };
      if (swap && motion) { big.classList.add('swap'); setTimeout(apply, 180); } else apply();
    };
    shots.forEach(function (s, i) {
      s.setAttribute('tabindex', '0'); s.setAttribute('role', 'button');
      var open = function () { show(i, false); lb.showModal(); if (lenis) lenis.stop(); };
      s.addEventListener('click', open);
      s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
    });
    $('.prev', lb).addEventListener('click', function () { show(at - 1, true); });
    $('.next-img', lb).addEventListener('click', function () { show(at + 1, true); });
    $('.close', lb).addEventListener('click', function () { lb.close(); });
    lb.addEventListener('close', function () { if (lenis) lenis.start(); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(at - 1, true);
      if (e.key === 'ArrowRight') show(at + 1, true);
    });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target === $('.lb-inner', lb)) lb.close(); });
  }

  /* ---------- copy buttons */
  $$('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.dataset.copy, label = b.textContent;
      var done = function (ok) { b.textContent = ok ? 'Copied' : 'Select and copy'; setTimeout(function () { b.textContent = label; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); }, function () { selectVal(b); done(false); });
      } else { selectVal(b); done(false); }
    });
  });
  function selectVal(b) {
    var v = b.parentNode.querySelector('.val');
    if (!v || !window.getSelection) return;
    var r = document.createRange(); r.selectNodeContents(v);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }
})();
