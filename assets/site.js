// Shared behaviour: theme toggle (light is the default), mobile menu, active nav link.
(function () {
  var root = document.documentElement;

  // Theme toggle
  var btn = document.getElementById('themeBtn');
  function paint() {
    var dark = root.getAttribute('data-theme') === 'dark';
    var knob = document.getElementById('knob');
    if (knob) knob.setAttribute('cx', dark ? 17 : 7);
    if (btn) btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
  }
  if (btn) {
    btn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
      paint();
    });
  }
  paint();

  // Mobile menu
  var toggle = document.getElementById('navToggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Highlight the current page in the nav
  var page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    var href = (a.getAttribute('href') || '').split('#')[0].toLowerCase();
    if (href === page) a.classList.add('active');
  });
})();
