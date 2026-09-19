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

**Organisers**
- Make a setup link and QR code with the tournament name, a tournament code, and lists of fields, levels, coaches and referees.
- Rank referees, with provisional marks for few games, coach marking style adjustment, a coverage list, and a name merge tool.
- Load a results file (CSV or JSON) and export the ranking as CSV.

**Demo**
- Setup, then Demo and training, loads 45 made-up games. Demo forms are never uploaded.

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
| `.github/workflows/` | Deploys to static.app when you push to `main` |

## Run it on your computer

```
python3 -m http.server 8000
```

Open http://localhost:8000. Service workers and the camera work on `localhost`. Phones need HTTPS.

## Deploy

**Upload results only works when the site is served by static.app.**
The Upload button uses static.app's form service. Static.app adds the form script to the page when it serves it.
On GitHub Pages or another host, everything else works, but Upload does nothing.
The email, share, CSV, backup and print options still work.

1. Make a site at https://static.app and note its site id (`pid`).
2. In this GitHub repo, open Settings, then Secrets and variables, then Actions.
3. Add the secret `STATICAPP_API_KEY`. Make a new key at https://static.app/account/api. Do not paste it in code, chat or issues.
4. Add the variable `STATICAPP_PID` with your site id.
5. Push to `main`. The workflow zips the site and uploads it.

The workflow changes the cache name in `sw.js` on each release, so phones pick up the new files after two opens.
If you deploy by hand, change `CACHE` in `sw.js` first.

## Results and data

- Each game is one row in a static.app form named `sevens-results`. Read the rows in your static.app account.
- Static.app makes a new results table when the list of upload fields changes. Do not add or rename fields in the hidden form (`#up-form`) without a plan. The list is `UP_FIELDS` in `index.html`.
- Static.app's browser rules block live reading of the table from the app. Export the entries, then use Review, then Load results file.
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

## Tests

There is no test suite in the repo. The app was checked with Playwright on phone-size screens, an accessibility scan (axe),
a fake camera for QR scanning, a fake microphone for voice notes, and mocks of the static.app form script and the speech service.
Real speech recognition has not been tested on real phones. Add your own tests if you grow the app.

## Licence

No licence is set for the app code yet. Choose one before you make the repo public.
Third-party code and fonts keep their own licences (see `lib/LICENSES.txt` and `fonts/LICENSE.txt`).
