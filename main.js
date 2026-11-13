/* Convex - site behaviour (draft v2). Plain JS, no dependencies. */
(function () {
  function init(root) {
    root = root || document;

    // Mobile menu
    var toggle = document.querySelector('.menu-toggle');
    var links = document.querySelector('.nav-links');
    if (toggle && links && !toggle.dataset.bound) {
      toggle.dataset.bound = '1';
      toggle.addEventListener('click', function () {
        var open = links.classList.toggle('active');
        toggle.classList.toggle('active', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      links.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          links.classList.remove('active');
          toggle.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });
    }

    // Pricing toggle - figures come from data attributes so display and toggle can never disagree
    root.querySelectorAll('[data-billing-toggle]').forEach(function (input) {
      if (input.dataset.bound) return;
      input.dataset.bound = '1';
      var scope = input.closest('[data-pricing]') || document;
      function fmt(n) { return Number(n).toLocaleString('en-AU'); }
      function render() {
        var yearly = input.checked;
        scope.querySelectorAll('[data-monthly]').forEach(function (el) {
          el.querySelector('.amt').textContent = fmt(yearly ? el.dataset.yearly : el.dataset.monthly);
          el.querySelector('.per').textContent = yearly ? '/year' : '/month';
        });
        scope.querySelectorAll('[data-note-monthly]').forEach(function (el) {
          el.textContent = yearly ? el.dataset.noteYearly : el.dataset.noteMonthly;
        });
        var m = scope.querySelector('.lbl-m'), y = scope.querySelector('.lbl-y');
        if (m) m.classList.toggle('active', !yearly);
        if (y) y.classList.toggle('active', yearly);
      }
      input.addEventListener('change', render);
      render();
    });

    // FAQ search filter
    root.querySelectorAll('[data-faq-search]').forEach(function (box) {
      if (box.dataset.bound) return;
      box.dataset.bound = '1';
      var scope = box.closest('[data-faq-scope]');
      var empty = scope.querySelector('.faq-empty');
      box.addEventListener('input', function () {
        var q = box.value.trim().toLowerCase();
        var shown = 0;
        scope.querySelectorAll('.faq details').forEach(function (d) {
          var hit = !q || d.textContent.toLowerCase().indexOf(q) !== -1;
          d.hidden = !hit;
          if (hit) shown++;
          if (q && hit) d.open = true;
        });
        scope.querySelectorAll('.faq-group').forEach(function (g) {
          g.hidden = !g.querySelector('details:not([hidden])');
        });
        if (empty) empty.hidden = shown !== 0;
      });
    });

    // Purchaser lens picker (illustrative)
    root.querySelectorAll('[data-picker]').forEach(function (picker) {
      if (picker.dataset.bound) return;
      picker.dataset.bound = '1';
      var data = JSON.parse(picker.querySelector('script[type="application/json"]').textContent);
      var out = picker.querySelector('.picker-out');
      function val(name) { var c = picker.querySelector('input[name="' + name + '"]:checked'); return c ? c.value : ''; }
      function render() {
        var p = val('profile'), dev = val('develop');
        var items = (data.profiles[p] || []).concat(dev === 'yes' ? data.develop.yes : data.develop.no);
        var html = '<h4>' + data.labels[p] + (dev === 'yes' ? ' - intending to develop' : ' - not developing') + '</h4><ul>';
        items.forEach(function (i) { html += '<li>' + i + '</li>'; });
        out.innerHTML = html + '</ul>';
      }
      picker.addEventListener('change', render);
      render();
    });

    // Review economics calculator (illustrative)
    root.querySelectorAll('[data-calc]').forEach(function (calc) {
      if (calc.dataset.bound) return;
      calc.dataset.bound = '1';
      var CREDIT = 30, SAVING = 0.8;
      var presets = { est: { hours: 1, fee: 250 }, otp: { hours: 2.5, fee: 400 } };
      function num(k) { var v = parseFloat(calc.querySelector('[data-k="' + k + '"]').value); return isNaN(v) ? 0 : v; }
      function money(v) { var s = '$' + Math.abs(Math.round(v)).toLocaleString('en-AU'); return v < 0 ? '-' + s : s; }
      function hrs(v) { var m = Math.round(v * 60); return m >= 60 ? (Math.floor(m / 60) + ' h ' + (m % 60 ? (m % 60) + ' min' : '')).trim() : m + ' min'; }
      function set(k, v, neg) { var el = calc.querySelector('[data-o="' + k + '"]'); el.textContent = v; el.classList.toggle('neg', !!neg); }
      function render() {
        var rate = num('rate'), h = num('hours'), fee = num('fee'), n = Math.max(1, num('n'));
        var h2 = h * (1 - SAVING);
        var c1 = rate * h, c2 = rate * h2 + CREDIT;
        var m1 = fee - c1, m2 = fee - c2;
        set('t1', hrs(h)); set('t2', hrs(h2));
        set('c1', money(c1)); set('c2', money(rate * h2));
        set('cr', money(CREDIT));
        set('f1', money(fee)); set('f2', money(fee));
        set('m1', money(m1), m1 < 0); set('m2', money(m2), m2 < 0);
        set('mm1', money(m1 * n), m1 < 0); set('mm2', money(m2 * n), m2 < 0);
        calc.querySelector('[data-o="save"]').textContent = money((m2 - m1) * n);
        calc.querySelector('[data-o="hrs"]').textContent = (Math.round((h - h2) * n * 10) / 10).toLocaleString('en-AU');
      }
      calc.querySelectorAll('input[name="ctype"]').forEach(function (r) {
        r.addEventListener('change', function () {
          var p = presets[r.value];
          calc.querySelector('[data-k="hours"]').value = p.hours;
          calc.querySelector('[data-k="fee"]').value = p.fee;
          render();
        });
      });
      calc.addEventListener('input', render);
      render();
    });

    // Contact form (Formspree, same endpoint as the current site)
    root.querySelectorAll('form[data-ajax]').forEach(function (form) {
      if (form.dataset.bound) return;
      form.dataset.bound = '1';
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var status = form.querySelector('.form-status');
        var btn = form.querySelector('button[type="submit"]');
        if (form.dataset.preview) { status.textContent = 'Preview only - the form is not connected in this draft.'; return; }
        btn.disabled = true; status.textContent = 'Sending...';
        fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (!r.ok) throw new Error();
            status.textContent = 'Thank you - we will be in touch within 1 business day.';
            form.reset();
          })
          .catch(function () { status.textContent = 'That did not send. Please email info@convex.au instead.'; })
          .finally(function () { btn.disabled = false; });
      });
    });
  }

  window.ConvexInit = init;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(); });
  else init();
})();
