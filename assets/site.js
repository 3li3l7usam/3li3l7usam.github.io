(function () {
  'use strict';

  /* ---------- wires between nodes on the work canvas */
  var canvas = document.querySelector('.canvas');
  function drawWires() {
    if (!canvas) return;
    var svg = canvas.querySelector('.wires');
    var nodes = Array.prototype.slice.call(canvas.querySelectorAll('.node'));
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    if (getComputedStyle(svg).display === 'none') return;
    var box = canvas.getBoundingClientRect();
    svg.setAttribute('viewBox', '0 0 ' + box.width + ' ' + box.height);
    var rects = nodes.map(function (n) { var r = n.getBoundingClientRect(); return { top: r.top - box.top, bottom: r.bottom - box.top }; });
    for (var i = 0; i < nodes.length - 1; i++) {
      var a = nodes[i].querySelector('.port.out').getBoundingClientRect();
      var b = nodes[i + 1].querySelector('.port.in').getBoundingClientRect();
      var x1 = a.left + a.width / 2 - box.left, y1 = a.top + a.height / 2 - box.top;
      var x2 = b.left + b.width / 2 - box.left, y2 = b.top + b.height / 2 - box.top;
      var d;
      if (x2 > x1 + 16) {
        /* forward: a plain node-editor curve */
        var dx = Math.max(60, (x2 - x1) * 0.45);
        d = 'M' + x1 + ' ' + y1 + ' C' + (x1 + dx) + ' ' + y1 + ' ' + (x2 - dx) + ' ' + y2 + ' ' + x2 + ' ' + y2;
      } else {
        /* back to the next row: run down the right side, across the gap between rows, then in from the left */
        var above = 0, below = Infinity;
        for (var k = 0; k <= i; k++) above = Math.max(above, rects[k].bottom);
        for (k = i + 1; k < rects.length; k++) below = Math.min(below, rects[k].top);
        var lane = below > above ? (above + below) / 2 : Math.max(y1, y2) - 20;
        var xr = x1 + 28, xl = x2 - 28, r = Math.max(4, Math.min(18, (lane - y1) / 2, (y2 - lane) / 2));
        d = 'M' + x1 + ' ' + y1 + ' H' + (xr - r) + ' Q' + xr + ' ' + y1 + ' ' + xr + ' ' + (y1 + r) +
            ' V' + (lane - r) + ' Q' + xr + ' ' + lane + ' ' + (xr - r) + ' ' + lane +
            ' H' + (xl + r) + ' Q' + xl + ' ' + lane + ' ' + xl + ' ' + (lane + r) +
            ' V' + (y2 - r) + ' Q' + xl + ' ' + y2 + ' ' + (xl + r) + ' ' + y2 + ' H' + x2;
      }
      var p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      p.setAttribute('d', d);
      p.dataset.from = i; p.dataset.to = i + 1;
      svg.appendChild(p);
    }
  }
  if (canvas) {
    var nodes = canvas.querySelectorAll('.node');
    Array.prototype.forEach.call(nodes, function (n, i) {
      function light(on) {
        Array.prototype.forEach.call(canvas.querySelectorAll('.wires path'), function (p) {
          if (+p.dataset.from === i || +p.dataset.to === i) p.classList.toggle('on', on);
        });
      }
      n.addEventListener('mouseenter', function () { light(true); });
      n.addEventListener('mouseleave', function () { light(false); });
      n.addEventListener('focus', function () { light(true); });
      n.addEventListener('blur', function () { light(false); });
    });
    var t;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(drawWires, 80); });
    window.addEventListener('load', drawWires);
    Array.prototype.forEach.call(canvas.querySelectorAll('img'), function (img) { img.addEventListener('load', drawWires); });
    drawWires();
  }

  /* ---------- filters on the work index */
  var chips = document.querySelectorAll('.chip');
  var cards = document.querySelectorAll('.grid .card');
  function setFilter(cat) {
    Array.prototype.forEach.call(chips, function (c) { c.setAttribute('aria-pressed', String(c.dataset.cat === cat)); });
    Array.prototype.forEach.call(cards, function (card) { card.hidden = !(cat === 'all' || card.dataset.cat === cat); });
    try { localStorage.setItem('aa-filter', cat); } catch (e) {}
  }
  Array.prototype.forEach.call(chips, function (c) { c.addEventListener('click', function () { setFilter(c.dataset.cat); }); });
  if (chips.length) {
    var saved = 'all';
    try { saved = localStorage.getItem('aa-filter') || 'all'; } catch (e) {}
    if (!document.querySelector('.chip[data-cat="' + saved + '"]')) saved = 'all';
    setFilter(saved);
  }

  /* ---------- lightbox on project pages */
  var lb = document.getElementById('lb');
  if (lb && typeof lb.showModal === 'function') {
    var shots = Array.prototype.slice.call(document.querySelectorAll('[data-full]'));
    var img = lb.querySelector('img'), cap = lb.querySelector('.lb-count'), cur = 0;
    function show(i) {
      cur = (i + shots.length) % shots.length;
      img.src = shots[cur].dataset.full; img.alt = shots[cur].alt || '';
      cap.textContent = (cur + 1) + ' of ' + shots.length;
    }
    shots.forEach(function (s, i) {
      s.setAttribute('tabindex', '0'); s.setAttribute('role', 'button');
      function open() { show(i); lb.showModal(); }
      s.addEventListener('click', open);
      s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
    });
    lb.querySelector('.prev').addEventListener('click', function () { show(cur - 1); });
    lb.querySelector('.next').addEventListener('click', function () { show(cur + 1); });
    lb.querySelector('.close').addEventListener('click', function () { lb.close(); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(cur - 1);
      if (e.key === 'ArrowRight') show(cur + 1);
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  }

  /* ---------- copy buttons */
  Array.prototype.forEach.call(document.querySelectorAll('.copy'), function (b) {
    b.addEventListener('click', function () {
      var text = b.dataset.copy, label = b.textContent;
      function done(ok) { b.textContent = ok ? 'Copied' : 'Select and copy'; setTimeout(function () { b.textContent = label; }, 1600); }
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
