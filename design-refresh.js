/* Ελληνικά navigation and theme enhancement v1. No dependencies and no network requests. */
(function () {
  'use strict';
  if (document.getElementById('ell-global-nav')) return;
  const KEY = 'ellinika.ui.theme.v1';
  const root = document.documentElement;
  let saved = null;
  try { saved = localStorage.getItem(KEY); } catch (_) { /* private browsing */ }
  root.dataset.ellTheme = saved === 'dark' ? 'dark' : 'light';

  const links = [
    ['today', '#today', 'Σήμερα', 'Today', '◷'],
    ['course', '#', 'Μαθήματα', 'Course', 'Α'],
    ['practice', '#practicehub', 'Εξάσκηση', 'Practice', '✎'],
    ['library', '#library', 'Βιβλιοθήκη', 'Library', '▤'],
    ['progress', '#focus', 'Πρόοδος', 'Progress', '◫'],
  ];
  const nav = document.createElement('nav');
  nav.id = 'ell-global-nav';
  nav.className = 'ell-nav';
  nav.setAttribute('aria-label', 'Primary navigation');
  nav.innerHTML = '<div class="ell-nav-inner">' + links.map(([id, hash, el, en, glyph]) =>
    '<a href="' + hash + '" data-ell-dest="' + id + '">' +
    '<span class="ell-nav-mark" aria-hidden="true">' + glyph + '</span>' +
    '<span class="ell-nav-el" lang="el">' + el + '</span>' +
    '<span class="ell-nav-en">' + en + '</span></a>').join('') +
    '<div class="ell-theme-wrap"><button type="button" class="ell-theme" id="ell-theme-toggle"></button></div></div>';
  const main = document.querySelector('main#view');
  if (!main) return;
  main.parentNode.insertBefore(nav, main);

  const toggle = document.getElementById('ell-theme-toggle');
  const describeTheme = () => {
    const dark = root.dataset.ellTheme === 'dark';
    toggle.textContent = dark ? '☼ Light' : '◐ Dark';
    toggle.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    toggle.setAttribute('aria-pressed', String(dark));
  };
  describeTheme();
  toggle.addEventListener('click', () => {
    root.dataset.ellTheme = root.dataset.ellTheme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem(KEY, root.dataset.ellTheme); } catch (_) { /* private browsing */ }
    describeTheme();
  });

  const activeSection = () => {
    const h = decodeURIComponent(location.hash.slice(1)).split('.')[0];
    if (h === 'today') return 'today';
    if (h === 'practicehub' || /^(sheets|drill|exam|mock|writing|listening|expr|mistakes|register|speaking|diagnostic|speakinglab|writingcoach|tetradio)$/.test(h)) return 'practice';
    if (/^(library|stories|classics|news|opinion|ref|search|phrases|argue|pos)$/.test(h)) return 'library';
    if (h === 'focus' || h === 'backup') return 'progress';
    return 'course';
  };
  const updateActive = () => {
    const current = activeSection();
    nav.querySelectorAll('a[data-ell-dest]').forEach((a) => {
      if (a.dataset.ellDest === current) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
  };
  window.addEventListener('hashchange', updateActive);
  updateActive();

  const sections = [
    ['Λέξεις · Vocabulary', 'Recall, expressions and phrases',
      [['Word recall', '#today'], ['Expression trainer', '#expr'], ['Phrasebook', '#phrases']]],
    ['Γραμματική · Grammar', 'Inflection tables, productive practice and written exercises',
      [['Exercise sheets', '#sheets'], ['Paradigm drill', '#drill'], ['Grammar reference', '#ref'], ['Grammar by part of speech', '#pos']]],
    ['Κατανόηση · Comprehension', 'Listening and reading comprehension',
      [['Listening and dictation', '#listening'], ['Graded stories', '#stories']]],
    ['Παραγωγή · Production', 'Write, rehearse speaking and practise register',
      [['Writing workbook', '#tetradio'], ['Writing and speaking workshop', '#writing'], ['Writing coach', '#writingcoach'], ['Speaking studio', '#speakinglab'], ['Register converter', '#register']]],
    ['Πιστοποίηση · Exam preparation', 'Timed practice and full mock assessments',
      [['Exam practice', '#exam'], ['Mock examination', '#mock']]],
    ['Επανεξέταση · Review', 'Revisit mistakes and identify weaker areas',
      [['Mistakes notebook', '#mistakes'], ['Where to focus', '#focus'], ['Placement diagnostic', '#diagnostic']]],
  ];
  const esc = (v) => String(v).replace(/[&<>"']/g, (c) =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const routes = window.EllinikaAddons = window.EllinikaAddons || {};
  routes.practicehub = () => {
    const app = window.Ellinika;
    if (!app?.view) return;
    document.title = 'Practice · Ελληνικά';
    const meta = document.getElementById('bar-meta');
    if (meta) meta.textContent = 'Εξάσκηση · Practice';
    app.view.innerHTML = '<p class="crumbs"><a href="#">← Course</a></p>' +
      '<header class="intro"><span class="eyebrow" lang="el">Εξάσκηση</span><h1>Practice studio</h1>' +
      '<p class="sub">Choose a skill. Your existing exercises and saved progress stay intact.</p></header>' +
      '<div class="ell-practice-grid">' + sections.map(([title, sub, dest]) =>
        '<section class="card ell-practice-group"><h3>' + esc(title) + '</h3>' +
        '<p>' + esc(sub) + '</p><div class="ell-practice-links">' + dest.map(([label, hash]) =>
          '<a href="' + hash + '">' + esc(label) + '</a>').join('') + '</div></section>').join('') + '</div>';
    window.scrollTo(0, 0);
  };
})();
