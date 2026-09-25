#!/usr/bin/env node
/*
 * Quick checks for the Sevens Coaching Form. No packages needed.
 * Run from the repo root:  node tools/check.js
 * To accept a deliberate change to the upload fields:  node tools/check.js --update-fields
 */
const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '..');
const read = (p) => fs.readFileSync(path.join(root, p), 'utf8');
const exists = (p) => fs.existsSync(path.join(root, p));
let failed = 0;
const ok = (m) => console.log('ok    ' + m);
const bad = (m) => { failed++; console.log('FAIL  ' + m); };

const html = read('index.html');

/* 1. Every inline script must parse. */
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
scripts.forEach((code, i) => {
  try { new Function(code); ok(`inline script ${i + 1} of ${scripts.length} parses`); }
  catch (e) { bad(`inline script ${i + 1} has a syntax error: ${e.message}`); }
});

/* 2. Manifest and icons. */
try {
  const man = JSON.parse(read('manifest.webmanifest'));
  const missing = (man.icons || []).filter((i) => !exists(i.src));
  missing.length ? bad('manifest icons missing: ' + missing.map((i) => i.src).join(', ')) : ok('manifest is valid and its icons exist');
} catch (e) { bad('manifest.webmanifest is not valid JSON: ' + e.message); }

/* 3. Service worker: cache name and every cached file. */
const sw = read('sw.js');
/^const CACHE = '[^']+';/m.test(sw) ? ok('sw.js has a CACHE name') : bad('sw.js has no "const CACHE = \'...\';" line');
try {
  const arr = sw.match(/const ASSETS = (\[[\s\S]*?\]);/)[1];
  const assets = new Function('return ' + arr)().filter((a) => a !== './');
  const missing = assets.filter((a) => !exists(a));
  missing.length ? bad('sw.js caches files that do not exist: ' + missing.join(', ')) : ok(`sw.js caches ${assets.length} files and all exist`);
} catch (e) { bad('could not read ASSETS from sw.js: ' + e.message); }

/* 4. Fonts named in the CSS exist. */
const fonts = [...new Set([...html.matchAll(/url\((fonts\/[^)]+)\)/g)].map((m) => m[1]))];
const noFont = fonts.filter((f) => !exists(f));
noFont.length ? bad('fonts named in the CSS are missing: ' + noFont.join(', ')) : ok(`all ${fonts.length} font files exist`);

/* 5. Uploads and feedback both go to SnapItForms (a trial third-party backend, see CLAUDE.md).
 * Catch an unset key before it reaches the live site, and catch either of the old static.app
 * form hooks coming back by accident -- they only ever worked when static.app itself served the
 * page, which stopped being true once GitHub Pages became the host. */
html.includes('static-form')
  ? bad('a static.app form hook is back (static-form / static-form-id / id="up-form" / id="fb-form"). This project now uploads and sends feedback to SnapItForms instead -- remove it, or update this check if static.app is hosting again on purpose.')
  : ok('no leftover static.app form hook');
const keyMatch = html.match(/const SNAPIT_ACCESS_KEY = '([^']*)'/);
if (!keyMatch) bad('SNAPIT_ACCESS_KEY is missing from index.html');
else if (keyMatch[1].startsWith('REPLACE_WITH_') || !keyMatch[1]) bad('SNAPIT_ACCESS_KEY is still a placeholder. Uploads will not work until the real SnapItForms access key is put in.');
else ok('SNAPIT_ACCESS_KEY looks like it has been set');

/* 6. Upload fields must not change by accident. Static.app makes a NEW results table when they change. */
try {
  const sec = html.match(/const SECTIONS = \[([\s\S]*?)\n\];/)[1];
  const SECTIONS = new Function('return [' + sec + '\n]')();
  const up = html.match(/const UP_FIELDS = (\[[\s\S]*?\]);/)[1];
  const fields = new Function('SECTIONS', 'return ' + up)(SECTIONS);
  const snap = path.join(root, 'tools', 'upload-fields.json');
  if (process.argv.includes('--update-fields')) {
    fs.writeFileSync(snap, JSON.stringify({ note: 'The upload fields. Whichever backend receives them, an export or a saved CSV expects these exact names. Change it only on purpose.', fields }, null, 2) + '\n');
    ok(`wrote tools/upload-fields.json with ${fields.length} fields`);
  } else if (!fs.existsSync(snap)) {
    bad('tools/upload-fields.json is missing. Run: node tools/check.js --update-fields');
  } else {
    const want = JSON.parse(fs.readFileSync(snap, 'utf8')).fields;
    if (JSON.stringify(want) === JSON.stringify(fields)) ok(`the ${fields.length} upload fields match tools/upload-fields.json`);
    else {
      const added = fields.filter((f) => !want.includes(f)), removed = want.filter((f) => !fields.includes(f));
      bad('THE UPLOAD FIELDS CHANGED. Static.app will start a new results table and old rows will stay in the old one.'
        + (added.length ? ' Added: ' + added.join(', ') + '.' : '') + (removed.length ? ' Removed: ' + removed.join(', ') + '.' : '')
        + (!added.length && !removed.length ? ' The order changed.' : '')
        + ' If this is on purpose, run "node tools/check.js --update-fields" and say so in the pull request.');
    }
  }
} catch (e) { bad('could not read the upload fields from index.html: ' + e.message); }

/* 7. Demo data. */
try {
  const d = JSON.parse(read('demo/demo.json'));
  Array.isArray(d.forms) && d.forms.length && d.config && d.forms.every((f) => String(f.id).startsWith('demo-'))
    ? ok(`demo data has ${d.forms.length} forms and every id starts with "demo-"`)
    : bad('demo/demo.json is not in the expected shape (forms with demo- ids, and a config)');
} catch (e) { bad('demo/demo.json is not valid JSON: ' + e.message); }

/* 8. No keys or tokens in the files. */
const skip = new Set(['.git']);
const binExt = /\.(png|jpg|jpeg|gif|woff2?|zip|ico)$/i;
const patterns = [/sk_[A-Za-z0-9]{20,}/, /gh[pousr]_[A-Za-z0-9]{20,}/, /github_pat_[A-Za-z0-9_]{20,}/, /sk-ant-[A-Za-z0-9_-]{20,}/, /AKIA[0-9A-Z]{16}/];
const hits = [];
(function walk(dir) {
  for (const name of fs.readdirSync(dir)) {
    if (skip.has(name)) continue;
    const full = path.join(dir, name);
    const st = fs.statSync(full);
    if (st.isDirectory()) { walk(full); continue; }
    if (binExt.test(name) || st.size > 2e6) continue;
    const text = fs.readFileSync(full, 'utf8');
    patterns.forEach((re) => { if (re.test(text)) hits.push(path.relative(root, full)); });
  }
})(root);
hits.length ? bad('something that looks like a key or token is in: ' + [...new Set(hits)].join(', ')) : ok('no keys or tokens found in the files');

console.log(failed ? `\n${failed} check(s) failed.` : '\nAll checks passed.');
process.exit(failed ? 1 : 0);
