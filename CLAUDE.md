# Sevens Coaching Form: notes for Claude

A phone app (progressive web app) for rugby referee coaches at sevens tournaments. Coaches score games, save them on the phone, and upload them. Organisers rank referees. Read `README.md` for the full picture and `docs/RELEASE_NOTES.md` for support notes.

## How the project is built
- No build step and no packages. The whole app is in `index.html` (HTML, CSS and JavaScript). Keep it that way unless asked.
- `sw.js` is the offline service worker. `manifest.webmanifest` holds install details.
- `fonts/`, `icons/`, `lib/` (QR code maker and scanner) and `demo/` hold assets. `tools/` holds scripts.
- Hosted on static.app. The deploy workflow uploads the site when a change reaches `main`.

## Rules that matter
1. **Work on a branch and open a pull request.** Never push to `main`. Never merge. A merge to `main` deploys to the live site.
2. **Do not change the upload fields** (`UP_FIELDS` in `index.html`, the hidden form `#up-form`) unless the task says so. Static.app starts a new results table when they change, and old rows stay behind. `node tools/check.js` fails if they change. If a change is on purpose, run `node tools/check.js --update-fields` and say so in the pull request.
3. **Never put keys, tokens or real names in the repo.** The static.app key lives in the GitHub secret `STATICAPP_API_KEY`. Demo data is made up.
4. **Private notes stay private.** They must never appear in the shared summary, the email, or the print. They do go in uploads, backups and CSV exports.
5. **Voice notes stay on the phone.** They are not uploaded, not in backups, and not emailed. Dictation sends audio to the browser's speech service, so it keeps its warning and its switch in Setup.
6. **Do not edit `CACHE` in `sw.js` by hand for a release.** The deploy workflow sets it from the commit.
7. **Keep old data working.** Forms saved by older releases must still open. Add new fields with defaults, as `normalise()` does.
8. Update `docs/RELEASE_NOTES.md` when a change is user-visible.

## Test before you finish
- `node tools/check.js` must pass.
- Run the app: `python3 -m http.server 8000`, then open http://localhost:8000. Test on a phone-size screen (about 390 px wide).
- Upload only works on static.app. Test upload logic with a mock of the static.app form script. It sets `window.sendForm`, listens for the form's `submit` event, sets `data-submitting`, and calls `window.sevensUploaded()` on success.
- Voice and dictation: use a fake microphone in Playwright, and a mock `SpeechRecognition`.
- Keep touch targets at 44 px or more, keep text contrast at 4.5 to 1, and run an accessibility scan (axe) on all four tabs.

## Writing style for the app
- Short sentences and plain words. New Zealand spelling: organise, colour, referee.
- Te reo Māori labels carry macrons. Do not change them without a fluent speaker's check.
- Score meanings (`ANCHORS`), areas and quick notes (`SECTIONS`) are drafts the coaches will agree. Change them only when asked.

## Where things are in `index.html`
`ANCHORS`, `SECTIONS` (areas and quick notes), storage keys (`LS_*`), form records (`blank()`, `normalise()`), upload (`UP_FIELDS`, `payload()`, `uploadOne()`), review table (`collect()`, `renderReview()`), setup link and QR (`makeSetup()`, `startScan()`), voice notes and dictation (search "Voice notes" and "Dictation"), demo (`loadDemo()`).
