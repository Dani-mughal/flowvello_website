/**
 * Ridgeline Dither Footer Animation
 * Ported from 21st.dev Ridgeline Dither Footer (glacier preset)
 * 2D Canvas Bayer Ordered Dither with Perlin/FBM noise ridges and drifting mist.
 */
(function () {
  'use strict';

  var scene = document.getElementById('ridgelineScene');
  var canvas = document.getElementById('ridgelineCanvas');
  var alt = document.getElementById('ridgelineAlt');
  var altText = document.getElementById('ridgelineAltText');

  if (!scene || !canvas) return;

  var ctx = canvas.getContext('2d');
  if (!ctx) return;

  var RDF_BAYER = [
    0, 32, 8, 40, 2, 34, 10, 42, 48, 16, 56, 24, 50, 18, 58, 26,
    12, 44, 4, 36, 14, 46, 6, 38, 60, 28, 52, 20, 62, 30, 54, 22,
    3, 35, 11, 43, 1, 33, 9, 41, 51, 19, 59, 27, 49, 17, 57, 25,
    15, 47, 7, 39, 13, 45, 5, 37, 63, 31, 55, 23, 61, 29, 53, 21
  ].map(function (v) { return (v + 0.5) / 64; });

  function rdfHex(hex) {
    var m = /^#?([0-9a-f]{3}|[0-9a-f]{6})$/i.exec((hex || '').trim());
    if (!m) return null;
    var h = m[1].length === 3 ? m[1].split('').map(function (c) { return c + c; }).join('') : m[1];
    return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
  }

  function rdfPack(rgb) {
    return ((255 << 24) | (rgb[2] << 16) | (rgb[1] << 8) | rgb[0]) >>> 0;
  }

  function rdfDither(tone, n, b) {
    var t = tone < 0 ? 0 : tone > 1 ? 1 : tone;
    var v = Math.floor(t * (n - 1) + b);
    return v > n - 1 ? n - 1 : v;
  }

  function rdfHash(x, y, seed) {
    var h = Math.imul(x | 0, 374761393) + Math.imul(y | 0, 668265263) + Math.imul(seed | 0, 1442695041);
    h = Math.imul(h ^ (h >>> 13), 1274126177);
    h ^= h >>> 16;
    return (h >>> 0) / 4294967296;
  }

  function rdfNoise(x, y, seed) {
    var xi = Math.floor(x);
    var yi = Math.floor(y);
    var xf = x - xi;
    var yf = y - yi;
    var u = xf * xf * (3 - 2 * xf);
    var v = yf * yf * (3 - 2 * yf);
    var a = rdfHash(xi, yi, seed);
    var b = rdfHash(xi + 1, yi, seed);
    var c = rdfHash(xi, yi + 1, seed);
    var d = rdfHash(xi + 1, yi + 1, seed);
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
  }

  function rdfFbm(x, y, seed, octaves) {
    var sum = 0;
    var amp = 0.5;
    var norm = 0;
    for (var o = 0; o < octaves; o++) {
      sum += rdfNoise(x, y, seed + o * 31) * amp;
      norm += amp;
      x *= 2.03;
      y *= 2.03;
      amp *= 0.5;
    }
    return norm > 0 ? sum / norm : 0;
  }

  function rdfSmooth(e0, e1, x) {
    var t = e1 === e0 ? (x < e0 ? 0 : 1) : Math.min(1, Math.max(0, (x - e0) / (e1 - e0)));
    return t * t * (3 - 2 * t);
  }

  function rdfEase(t) {
    var c = t < 0 ? 0 : t > 1 ? 1 : t;
    return 1 - Math.pow(1 - c, 3);
  }

  function rdfRidgeline(cols, rows, i, layers, seed, margin) {
    var k = layers > 1 ? i / (layers - 1) : 1;
    var n = cols + margin * 2;
    var out = new Float32Array(n);
    var base = rows * (0.38 + 0.66 * Math.pow(k, 1.4));
    var amp = rows * (0.2 + 0.24 * k);
    var freq = 6 - 3.8 * k;
    var flankL = rows * 0.5 * k * k * k * (0.55 + 0.6 * rdfHash(i, 11, seed));
    var flankR = rows * 0.5 * k * k * k * (0.55 + 0.6 * rdfHash(i, 13, seed));
    var ceil = rows * 0.17;
    var tilt = (rdfHash(i, 7, seed) - 0.5) * rows * 0.34 * (0.4 + k);
    var s = (seed | 0) * 13 + i * 101;
    for (var x = 0; x < n; x++) {
      var u = (x - margin) / cols;
      var r1 = 1 - Math.abs(rdfNoise(u * freq + i * 3.7, 0.5, s) * 2 - 1);
      var r2 = 1 - Math.abs(rdfNoise(u * freq * 2.3, 3.5, s + 1) * 2 - 1);
      var f = rdfFbm(u * freq * 4.1, 9.5, s + 2, 3);
      var h = r1 * r1 * 0.62 + r2 * 0.24 + f * 0.14;
      var e = Math.min(1.2, Math.abs(u * 2 - 1));
      var y = base - h * amp + tilt * (u - 0.5) * 2 - (u < 0.5 ? flankL : flankR) * e * e * Math.sqrt(e);
      out[x] = y < ceil ? ceil - (ceil - y) * 0.25 : y;
    }
    return out;
  }

  function rdfElevation(crest, rows, layer, layers) {
    var up = rows > 0 ? 1 - Math.min(1, Math.max(0, crest / rows)) : 0;
    return Math.round(420 + up * 2600 + (layers - 1 - layer) * 140);
  }

  // Options & Palette
  var tones = ['#ffffff', '#d6e6f4', '#a8cae7', '#6b9ecc', '#34679a', '#1a3e66', '#0b2140'];
  var seed = 23;
  var layers = 7;
  var pixel = 2;
  var mistK = 0.8;
  var driftSpeed = 1;
  var radius = 130;
  var interactive = true;
  var altimeter = true;

  var pal = new Uint32Array(tones.map(function (t) { return rdfPack(rdfHex(t) || [128, 128, 128]); }));
  var nTones = pal.length;

  var p = 2;
  var cols = 1;
  var rows = 1;
  var margin = 2;
  var img = null;
  var buf = new Uint32Array(0);
  var tops = [];
  var pools = [];
  var colTop = new Float32Array(0);
  var colSlope = new Float32Array(0);
  var colPool = new Float32Array(0);
  var fog = new Float32Array(0);
  var fw = 1;
  var fh = 1;
  var ceil = 0;
  var fadeTo = 1;

  var raf = 0;
  var visible = false;
  var awake = true;
  var lastDraw = 0;
  var lastTick = performance.now();
  var revealAt = null;

  var tx = 0;
  var ty = 0;
  var ex = 0;
  var ey = 0;
  var inside = false;
  var clear = 0;
  var pt = 0;
  var pe = 0;
  var windV = 0;
  var windX = 0;
  var altShown = false;
  var altLabel = '';

  function layout() {
    var rect = scene.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) return;
    p = Math.max(1, Math.round(pixel));
    cols = Math.max(8, Math.ceil(rect.width / p));
    rows = Math.max(8, Math.ceil(rect.height / p));
    canvas.width = cols;
    canvas.height = rows;
    canvas.style.width = cols * p + 'px';
    canvas.style.height = rows * p + 'px';
    img = ctx.createImageData(cols, rows);
    buf = new Uint32Array(img.data.buffer);
    margin = Math.ceil(cols * 0.045) + 3;
    ceil = Math.max(rows * 0.17, 92 / p);
    fadeTo = Math.max(rows * 0.3, 128 / p);
    tops = [];
    pools = [];
    for (var i = 0; i < layers; i++) {
      var t = rdfRidgeline(cols, rows, i, layers, seed, margin);
      for (var x = 0; x < t.length; x++) if (t[x] < ceil) t[x] = ceil - (ceil - t[x]) * 0.2;
      var pool = new Float32Array(t.length);
      for (var x = 0; x < t.length; x++) pool[x] = 0.45 + 1.1 * rdfFbm(((x - margin) / cols) * 4, i * 5.3, seed + 9, 2);
      tops.push(t);
      pools.push(pool);
    }
    colTop = new Float32Array(layers * cols);
    colSlope = new Float32Array(layers * cols);
    colPool = new Float32Array(layers * cols);
    fw = (cols >> 1) + 2;
    fh = (rows >> 1) + 2;
    fog = new Float32Array(fw * fh);
    awake = true;
  }

  function draw(now) {
    if (!img) return;
    var dt = Math.min(64, now - lastTick);
    lastTick = now;
    var age = revealAt === null ? -1 : now - revealAt;

    var ease = 1 - Math.pow(0.82, dt / 16.7);
    var slow = 1 - Math.pow(0.93, dt / 16.7);
    ex += (tx - ex) * ease;
    ey += (ty - ey) * ease;
    clear += ((inside && interactive ? 1 : 0) - clear) * slow;
    pe += ((interactive ? pt : 0) - pe) * slow;
    windV *= Math.pow(0.965, dt / 16.7);
    windX += (windV * dt) / 1000;
    var fogT = (now / 1000) * 0.045 * Math.max(0, driftSpeed) + windX;

    var sx = 9 / cols;
    var sy = 4.4 / rows;
    for (var gy = 0; gy < fh; gy++) {
      var ny = gy * sy;
      for (var gx = 0; gx < fw; gx++) {
        var nx = gx * sx + fogT;
        var warp = rdfNoise(nx * 0.45 - fogT * 0.6, ny * 0.8, 77) * 0.6;
        var v = rdfFbm(nx + warp, ny + warp * 0.4, 31, 3);
        fog[gy * fw + gx] = rdfSmooth(0.3, 0.74, v);
      }
    }

    var rev = new Float32Array(layers);
    var k = new Float32Array(layers);
    var toneBase = new Float32Array(layers);
    var fogDepth = new Float32Array(layers);
    for (var i = 0; i < layers; i++) {
      k[i] = i / (layers - 1);
      rev[i] = age < 0 ? 0 : rdfEase((age - 380 - i * 170) / 1300);
      toneBase[i] = 0.16 + 0.76 * Math.pow(k[i], 1.6);
      fogDepth[i] = rows * (0.08 + 0.42 * k[i]);
      var rise = (1 - rev[i]) * rows * 0.09;
      var shift = Math.round(pe * (0.25 + k[i]) * 0.75 * (margin - 3));
      var t = tops[i];
      var last = t.length - 1;
      for (var x = 0; x < cols; x++) {
        var at = x + margin + shift;
        colTop[i * cols + x] = t[at] + rise;
        colSlope[i * cols + x] = t[Math.min(last, at + 2)] - t[Math.max(0, at - 2)];
        colPool[i * cols + x] = fogDepth[i] * pools[i][at];
      }
    }
    var lift = age < 0 ? 1 : 1 - rdfEase((age - 900) / 1800);
    var r = Math.max(1, radius / p);
    var r2 = r * r;

    for (var y = 0; y < rows; y++) {
      var fade = rdfSmooth(0, fadeTo, y);
      var frow = (y >> 1) * fw;
      var by = (y & 7) * 8;
      var dyc = (y - ey) * 1.5;
      for (var x = 0; x < cols; x++) {
        var L = -1;
        for (var i = layers - 1; i >= 0; i--) {
          if (y >= colTop[i * cols + x]) {
            L = i;
            break;
          }
        }
        var tone = 0;
        var mk = 0.3;
        if (L >= 0) {
          var kk = k[L];
          var d = y - colTop[L * cols + x];
          var depth = colPool[L * cols + x];
          var crest = 1 - rdfSmooth(0, depth, d) * (0.88 - 0.45 * kk);
          tone = toneBase[L] * crest;
          var sl = colSlope[L * cols + x] * 0.06;
          tone += (sl < -0.2 ? -0.2 : sl > 0.2 ? 0.2 : sl) * (1 - rdfSmooth(0, depth * 0.5, d));
          tone += (rdfHash(x + Math.round(colTop[L * cols + x] * 7), d | 0, L) - 0.5) * 0.07 * kk;
          tone *= rev[L];
          mk = 0.95 - 0.5 * kk;
        } else {
          tone = 0.05 * rdfSmooth(rows * 0.15, rows * 0.6, y);
        }

        var m = fog[frow + (x >> 1)] * mistK * mk;
        if (clear > 0.01) {
          var dx = x - ex;
          var q = (dx * dx + dyc * dyc) / r2;
          if (q < 4) {
            var c = clear * Math.exp(-q);
            m *= 1 - c * 0.92;
            if (L >= 0) tone += c * 0.16 * rev[L];
          }
        }
        if (tone > 0.93) tone = 0.93;
        m += lift * 0.55;
        if (m > 1) m = 1;
        tone = (tone * (1 - m) + 0.09 * m * (1 - lift)) * fade;

        buf[y * cols + x] = pal[rdfDither(tone, nTones, RDF_BAYER[by + (x & 7)])];
      }
    }
    ctx.putImageData(img, 0, 0);

    // Altimeter readout
    if (alt && altText && altimeter && inside && age > 1600) {
      var cx = Math.max(0, Math.min(cols - 1, Math.round(ex)));
      var show = false;
      for (var i = layers - 1; i >= 0; i--) {
        var crestRow = colTop[i * cols + cx];
        if (ey >= crestRow - 6) {
          show = true;
          alt.style.transform = 'translate(' + (cx * p).toFixed(1) + 'px,' + (crestRow * p).toFixed(1) + 'px)';
          var text = rdfElevation(crestRow, rows, i, layers).toLocaleString('en-US') + ' m';
          if (text !== altLabel) {
            altLabel = text;
            altText.textContent = text;
          }
          break;
        }
      }
      if (show !== altShown) {
        altShown = show;
        alt.style.opacity = show ? '1' : '0';
      }
    } else if (alt && altShown) {
      altShown = false;
      alt.style.opacity = '0';
    }

    var settling =
      Math.abs(tx - ex) + Math.abs(ty - ey) > 0.05 ||
      Math.abs((inside && interactive ? 1 : 0) - clear) > 0.005 ||
      Math.abs((interactive ? pt : 0) - pe) > 0.001 ||
      Math.abs(windV) > 0.002;
    awake = (age >= 0 && age < 3400) || age < 0 || settling || (driftSpeed > 0);
  }

  function loop(now) {
    raf = 0;
    if (!visible) return;
    if (revealAt === null) {
      raf = requestAnimationFrame(loop);
      return;
    }
    if (now - lastDraw > 30) {
      draw(now);
      lastDraw = now;
    }
    if (awake) raf = requestAnimationFrame(loop);
  }

  function wake() {
    awake = true;
    if (!raf && visible) raf = requestAnimationFrame(loop);
  }

  function onMove(e) {
    if (!interactive && !altimeter) return;
    var rect = scene.getBoundingClientRect();
    pt = rect.width > 0 ? ((e.clientX - rect.left) / rect.width) * 2 - 1 : 0;
    var lx = (e.clientX - rect.left) / p;
    var ly = (e.clientY - rect.top) / p;
    var was = inside;
    inside = lx >= 0 && ly >= 0 && lx < cols && ly < rows;
    tx = lx;
    ty = ly;
    if (inside && !was) {
      ex = tx;
      ey = ty;
    }
    wake();
  }

  function onLeave() {
    pt = 0;
    inside = false;
    wake();
  }

  function onDown(e) {
    if (!interactive || !inside) return;
    if (e.target && e.target.closest && e.target.closest('a,button')) return;
    windV += tx < cols / 2 ? 1.4 : -1.4;
    wake();
  }

  layout();

  var ro = new ResizeObserver(function () {
    layout();
    draw(performance.now());
    wake();
  });
  ro.observe(scene);

  var io = new IntersectionObserver(function (entries) {
    var entry = entries[0];
    visible = entry ? entry.isIntersecting : true;
    if (visible) {
      if (revealAt === null) revealAt = performance.now();
      lastTick = performance.now();
      wake();
    }
  }, { threshold: 0.1 });
  io.observe(scene);

  scene.addEventListener('pointermove', onMove);
  scene.addEventListener('pointerleave', onLeave);
  scene.addEventListener('pointerdown', onDown);

})();
