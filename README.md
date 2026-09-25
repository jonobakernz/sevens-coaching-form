# Sevens Coaching Form

A phone app for rugby referee coaches at sevens tournaments. It began as a one-page Excel scoring sheet.
Coaches score a game, save it on the phone, and upload it. Organisers rank referees across many games and coaches.

It is a progressive web app: plain HTML, CSS and JavaScript, with no build step and no server code. It works offline.

![Demo overview](docs/demo-overview.png)

## What it does

**Coaches**
- Score 8 areas from 1 to 5: fitness, foul play, breakdowns, set phase, game awareness, game management, communication, and an overall rating.
- Tap quick notes, add comments, and write "Strength to keep" and "One thing to work on".
- Write private notes that are left out of the summary, email and print.
- Dictate into any comment box: tap the microphone and speak, and the words are typed in. Say "full stop", "comma", "question mark" or "new line" for punctuation.
- Record a voice note in any comment box (the 8 areas, distance from contest, the two feedback boxes and private notes). Play it back, record again, delete it, or share it.
- Save on the device, upload with one tap, email or share a summary, print or save a PDF.
- Work offline. Forms wait on the phone until there is signal.
- Send feedback about the app from Setup. Goes straight to the organiser through SnapItForms, separately from results upload.

**Organisers**
- Make a setup link and QR code with the tournament name, a tournament code, and lists of fields, levels, coaches and referees.
- Rank referees, with provisional marks for few games, coach marking style adjustment, a coverage list, and a name merge tool.
- Load a results file (CSV or JSON) and export the ranking as CSV.

**Demo**
- Setup, then Demo and training, loads 45 made-up games. Demo forms are never uploaded.

## Release notes

See [docs/RELEASE_NOTES.md](docs/RELEASE_NOTES.md) for what changed in each release, a troubleshooting table for support, and a data and privacy summary.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The whole app: page, styles and script |
| `sw.js` | Service worker for offline use |
| `manifest.webmanifest` | Install details |
| `icons/`, `fonts/` | App icons and the Barlow fonts (SIL Open Font License) |
| `lib/` | QR code maker and QR scanner. Loaded only when used. See `lib/LICENSES.txt` |
| `demo/` | Made-up tournament data: `demo.json`, plus a CSV and a backup file for testing |
| `tools/` | Scripts that make the demo data and the icons |
| `docs/` | Release notes and the demo overview picture |
| `.github/workflows/` | Deploys to static.app when you push to `main` |

## Run it on your computer

```
python3 -m http.server 8000
```

Open http://localhost:8000. Service workers and the camera work on `localhost`. Phones need HTTPS.

## Deploy

**The site is now hosted on GitHub Pages: <https://jonobakernz.github.io/sevens-coaching-form/>.**
This repo had to become public to enable Pages (a private-repo restriction on GitHub's Free plan, not something
this project controls). Nothing sensitive lives in the repo itself -- see "Keeping the repo public safe", below.

GitHub Pages was needed, not just preferred: static.app sends a `Content-Security-Policy` header on every page it
serves (`connect-src 'self' https://*.static.domains https://static.app`) that silently blocks any `fetch()` to a
third-party domain, including SnapItForms. GitHub Pages sends no such header, so results upload and feedback (both
of which call `api.snapitforms.com`) only work when the app is served from Pages, not from static.app.

Pages redeploys automatically a short time after every push to `main` -- no workflow or secret is needed for it.

The old static.app deploy still exists for now (`.github/workflows/deploy-static-app.yml`, needing the secret
`STATICAPP_API_KEY` and the variable `STATICAPP_PID`), and still updates <https://easy-goingcrow.staticdomains.app/>
if you keep those configured. **Do not send coaches to that address** -- results and feedback will silently fail
there because of the CSP header above. Consider removing the static.app workflow and secret once you're confident
GitHub Pages is working well, to avoid the two addresses drifting or confusing anyone.

The workflow that still deploys to static.app changes the cache name in `sw.js` on each release it runs, so phones
pick up the new files after two opens. GitHub Pages does not do this automatically; if you deploy there by hand
outside of a git push, change `CACHE` in `sw.js` yourself first.

## Keeping the repo public safe

- No real coaching data, referee names, or coach names live in this repo -- that data lives in SnapItForms (and,
  for releases 3 to 20, in static.app). The repo only ever held fictional demo data (see `demo/`).
- `SNAPIT_ACCESS_KEY` in `index.html` is visible in the repo now, same as it was already visible to anyone who
  viewed the live page's source -- publishing the repo does not add new exposure for that key. It is still not a
  security secret Anthropic-style, but do not draw attention to it.
- `STATICAPP_API_KEY` was always a GitHub Actions secret, never a file in the repo, so it is not exposed by making
  the repo public.
- Before adding anything else to this repo, re-read `CLAUDE.md`'s rule about never putting real names in it -- that
  rule matters more now that anyone can see the history.

## Upload results and feedback: on trial with SnapItForms

**Coaching-results uploads and in-app feedback are both on trial with [SnapItForms](https://snapitforms.com/), a small
third-party form backend.** It was picked because it works from any static host (GitHub Pages included), not because
it has a track record -- at the time this was set up (Sept 2026), no independent review of it could be found
anywhere (Capterra, G2, Reddit, Hacker News, GitHub). Treat it as unproven. Watch real submissions closely, and be
ready to move to a better-known service (Formspree, Basin, Getform/Forminit) or an in-house option (Power Automate +
SharePoint, an Azure Function) if it does not hold up.

- Both `uploadOne()` (results) and `submitFeedback()` (feedback) post straight to `https://api.snapitforms.com/submit`
  with `fetch`, using the same `SNAPIT_ACCESS_KEY`. Feedback rows are marked `kind: feedback` so they can be told
  apart from results in the dashboard. No vendor script or hidden form is involved for either any more.
- `SNAPIT_ACCESS_KEY`, near the top of the script, must hold a real access key from your SnapItForms account
  (sign in with Google, then copy the key) before either will do anything. `node tools/check.js` fails on the
  placeholder value on purpose, so a deploy with no key configured is caught before it goes out.
- The key is not a secret in the usual sense -- a browser-only app cannot hide it -- but do not publicise it. Anyone
  who has it can send junk into your SnapItForms dashboard.
- If a submission fails for a reason other than "no signal" (SnapItForms down, a CORS block, a rejected key), the
  coach sees a generic failure message with no more detail. The form itself (or the feedback text) is never lost
  either way; it stays on the phone until it sends.
- Both features used to depend on static.app's own injected form script, which only ever worked because static.app
  itself served the page. That stopped being an option once GitHub Pages became the host (see Deploy, above), which
  is why feedback was moved onto the same `fetch` approach as results, in the same change as the hosting move.

## Results and data

- Each game, and each piece of feedback, is one submission in your SnapItForms dashboard (told apart by the `kind`
  field). Export it from there as CSV.
- Whatever the upload backend, do not add or rename fields in `UP_FIELDS` (`index.html`) without a plan -- anyone
  exporting a CSV, or loading an older one, expects the column names to stay put. `node tools/check.js` catches an
  accidental change.
- Nothing in the app reads the results back live. Export the entries, then use Review, then Load results file.
- Forms live in each phone's browser storage. Tell coaches to save a backup file after each event.
- Voice notes are audio clips kept in the phone's IndexedDB. They are **not** uploaded (static.app forms carry text only) and are **not** in backup files. Share summary sends them with the text where the phone allows it. The email button cannot attach files. Clips are limited to 2 minutes (`VN_MAX` in `index.html`). For text the organiser can read, use the microphone on the phone keyboard.
- Deleting a form deletes its voice notes.
- Dictation uses the browser's Web Speech API (`SpeechRecognition`). **It sends the audio to the browser maker's speech service** (Google on Android Chrome, Apple on iPhone). It needs signal, shows a one-time warning, and can be switched off in Setup. It is hidden in browsers without the API (Firefox, and some iPhone Home Screen apps). Te reo Māori words often come out wrong. Voice notes are separate: they stay on the phone.
- Dictation and voice notes both use the microphone, so only one can run at a time.
- On iPhone, Safari and the Home Screen icon keep separate storage. Install first, then always open from the icon.
- The tournament code is a filter, not a password. Anyone who has it can send results.
- Results name real people. Keep the repo, exports and static.app account private, and follow your privacy rules (for example the NZ Privacy Act 2020).

## Change the content

- **Score wording:** `ANCHORS` at the top of the script in `index.html`.
- **Areas and quick notes:** the `SECTIONS` list.
- **Te reo Māori labels:** the `<i lang="mi">` tags in the form. Have a fluent speaker check them.
- **Colours and type:** the CSS variables at the top of the styles. There are light, dark and sun themes.
- **Demo data:** edit and run `python3 tools/generate_demo.py`.

## Checks and Claude Code

- `node tools/check.js` runs quick checks: scripts parse, manifest and cached files exist, the upload fields have not changed by accident, and no keys are in the files. The **Checks** workflow runs it on every pull request. The deploy workflow runs it first.
- `CLAUDE.md` holds the rules for Claude Code. It works on a branch and opens a pull request. You merge it, and the merge deploys.

## Tests

There is no test suite in the repo. The app was checked with Playwright on phone-size screens, an accessibility scan (axe),
a fake camera for QR scanning, a fake microphone for voice notes, a mock of `fetch` for SnapItForms uploads, and a mock of the
static.app form script for feedback and the speech service. Real speech recognition and a real SnapItForms submission have not
been tested. Add your own tests if you grow the app.

## Licence

**No licence is set for the app code, and the repo is now public.** With no licence file, default copyright
applies: the code is visible to anyone, but nobody else has legal permission to copy, modify or reuse it. If that is
not what you want -- for example if you would rather explicitly allow or explicitly forbid reuse -- add a `LICENSE`
file stating your choice. This was not decided as part of making the repo public; it is an open item, not a default.
Third-party code and fonts keep their own licences (see `lib/LICENSES.txt` and `fonts/LICENSE.txt`).
