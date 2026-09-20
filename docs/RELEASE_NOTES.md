# Sevens Coaching Form: release notes

Updated 20 Sept 2026. Current release: 17.

## At a glance

Release 17 of the Sevens Coaching Form went live on 20 Sept 2026, at <https://easy-goingcrow.staticdomains.app/>. It is a phone app. Coaches use it to score referees. Organisers use it to rank them.

A coach scores a game, the phone saves it, and the coach uploads it. The app works without signal. An organiser sets up a tournament with one QR code and reviews every referee in one table.

Main changes since the first release:

- A New Zealand rugby look, with a black jersey theme and te reo Māori labels.
- Eight scored areas, score meanings, quick notes and feedback boxes.
- Dictation and voice notes in every comment box.
- Upload, email, share and print options.
- Organiser tools: setup QR code, referee ranking, coach marking, and a demo tournament.

## What is new for coaches

A coach can score a game in about 15 taps. Notes can be typed, spoken, or recorded.

**Scoring**

- Score eight areas from 1 to 5: fitness, foul play, breakdowns, set phase, game awareness, game management, communication, and an overall rating.
- Communication is a new area. "Good position" is a new choice under distance from contest.
- Each score shows a one-line meaning, such as "3. Meets the standard for this level." Open "How to score" to see all five.
- "Tap a score to set it. Tap it again to clear it." is shown on screen above the scores, not just in "How to score".
- Under distance from contest, "Too close" and "In the way" can both apply. "Good position" is a separate choice and clears the other two. A line under the buttons explains this, and "Good position" now sits apart from the other two.

**Notes**

- Quick notes add a ready phrase to a comment box with one tap.
- "Strength to keep" and "One thing to work on" are for the referee.
- Private notes stay out of the summary, the email and the print. The organiser sees them after an upload.
- Dictation: tap the microphone in any comment box and speak. Say "full stop", "comma", "question mark" or "new line" for punctuation.
- Voice notes: tap the wave button. Record up to 2 minutes. Then play, record again, share or delete the clip.
- The microphone and wave buttons are lighter now, so the form reads less cluttered. They still work the same and are still easy to tap.

**Match details**

- Referee, field and time are always on screen. Coach, tournament, date, level, game and role sit under "Match details". The app remembers them.
- Coach sits beside Referee, Field and Time, always on screen. It is needed before the first upload.
- If the organiser has set up a referee list, the app suggests names and checks the spelling.
- Once the referee name and the rating are in, "Start next game" is ready. It copies the tournament, coach and level, and adds one to the game number. It does not need an upload first, so it works with no signal.

**Saving and sending**

- The form saves on the phone as you type. Losing signal loses nothing.
- "Upload results" sends the form. "Upload all waiting" sends every form not yet uploaded. A yellow number on the Saved tab shows how many wait.
- "Share summary", "Copy text", "Email this form" and "Print or save PDF" all work. Share summary also sends voice notes where the phone allows it.
- A coach must enter a name before the first upload.
- On the Saved tab, each form has its own delete button. Deleting no longer means opening the form first.
- "Select forms to delete" ticks off several forms at once and removes them together, with one confirmation.
- If "Upload all waiting" stops partway, the message now names the referee whose form failed, not just "the next one".
- The rating badge on each saved form now labels itself correctly for a screen reader, found in a full accessibility scan of all four tabs.

**Look and feel**

- A black jersey theme, a welcome screen on the first visit, and a compact header after that.
- Four tabs at the top: Form, Saved, Review and Setup.
- Larger buttons and clearer text. The accessibility scan finds no problems.
- Sun mode (white and black, heavy edges) for bright fields. Dark mode follows the phone.
- Te reo Māori labels sit beside the English ones. Dates and times use New Zealand style.

## What is new for organisers

An organiser can set up a tournament with one scan and rank every referee across all games and coaches.

**Setup tab**

- Make a setup link and QR code. It holds the tournament name, tournament code, field names, levels, coaches and referees.
- Coaches scan the QR code in the app, paste the link, or open the link. Their lists fill in.
- The tournament code goes with every upload. Loading a results file skips rows with a wrong or missing code. The code is a filter, not a password.
- Open "Referees and coaches" under "This device" to check the names a setup loaded, without exporting anything.

**Review tab**

- A ranked table shows games, coaches, rating and the seven area averages. Tap a heading to sort. Tap a name to read every comment, private notes included.
- Filters: tournament, role, date range and minimum games.
- A referee with fewer games than the minimum is "provisional" and has no rank.
- "Adjust ratings for coach marking style" corrects for hard and easy markers. It adjusts only coaches with 3 or more forms.
- The coach marking table shows each coach's forms, average and difference from all coaches.
- "Needs more assessments" lists referees below the minimum, including those with no games.
- "Names" finds spellings that look alike and offers to merge them.
- The table fits a laptop screen. On a phone, each referee is a card instead, with a "Sort by" box above the list in place of tapping a heading.

**Results**

- Each upload is one row in the static.app form "sevens-results".
- "Load results file" reads a CSV or JSON export and merges it. "Export ranking table (CSV)" saves the ranking.
- The Saved tab still has the CSV export and the backup file.

**Demo and training**

- Setup, then "Demo and training", loads 45 made-up games. Demo forms are never uploaded. "Remove the demo data" clears them and keeps real forms.

## Release history

There have been 17 releases, newest first. Dates are New Zealand time. The last column helps support tell which release a phone has.

| Date | Release | What changed | How to spot it on a phone |
| --- | --- | --- | --- |
| 20 Sept 2026 | 17. Accessibility fix | A full accessibility scan of all four tabs found one real issue: the rating badge on the Saved tab was not labelled correctly for a screen reader. Fixed. | No visible change. Check with a screen reader on the Saved tab. |
| 20 Sept 2026 | 16. Small fixes | A failed "Upload all waiting" names the referee whose form failed. Setup can show the referee and coach list without exporting. | "Referees and coaches" under "This device" in Setup. A named referee in a failed upload message. |
| 20 Sept 2026 | 15. Review table on phone | On a phone, the referee ranking is a list of cards instead of a sideways-scrolling table, with a "Sort by" box in place of tappable headings. The microphone and wave buttons are lighter. | A "Sort by" box above the ranking. Cards instead of a wide table. Thinner voice buttons. |
| 20 Sept 2026 | 14. Clearer scoring hints | A visible hint above the scores explains tapping a score again clears it. The distance-from-contest buttons show which two can combine and which one is separate. | "Tap a score to set it..." above the score rows. A short line and a gap before "Good position". |
| 20 Sept 2026 | 13. Delete several forms at once | "Select forms to delete" on the Saved tab ticks off several forms and removes them together. | A "Select forms to delete" button above the Saved list. |
| 20 Sept 2026 | 12. Coaching workflow fixes | Coach moved out of "Match details" onto the main screen. "Start next game" no longer waits for an upload. Each Saved form has its own delete button. | Coach sits beside Referee, Field and Time. A bin icon on each row in Saved. |
| 20 Sept 2026 | 11. Dictation | Speak into any comment box and the words are typed in. A switch in Setup turns it off. | A microphone button beside the wave button. A Voice section in Setup. |
| 19 Sept 2026 | 10. Voice notes | Record, play, share and delete voice notes in every comment box. Clips stay on the phone. | A wave button in each comment box. |
| 19 Sept 2026 | 8 and 9. Demo tournament | A demo tournament with 45 made-up games. The review table fits a laptop screen. The Saved tab count is a plain number with a yellow "waiting" badge. | "Demo and training" in Setup. |
| 19 Sept 2026 | 7. Large improvement release | Score meanings, Communication, feedback and private notes, role and level, quick notes, Setup with QR code, referee list, provisional ranks, coach marking, coverage list, tournament code, compact layout, better contrast, "Start next game", sun mode. | A Setup tab and a "Match details" fold. |
| 19 Sept 2026 | 6. Tabs at the top | The tabs moved to the top so the static.app badge no longer covers them. | Tabs at the top of the screen. |
| 19 Sept 2026 | 5. New Zealand rugby look | Black jersey theme, Barlow fonts, te reo Māori labels, New Zealand dates and times, new app icon. | A black header with a large white 7. |
| 19 Sept 2026 | 4. Email | "Email this form" opens the phone's mail app with the summary. The app remembers the addresses. | An "Email a copy to" box. |
| 19 Sept 2026 | 3. Upload | "Upload results", Tournament and Game fields, upload status on each form, "Load results file". | An "Upload results" button. |
| 19 Sept 2026 | 2. Referee review | A Review tab that ranks referees by average rating, with tournament and date filters. | A Review tab. |
| 19 Sept 2026 | 1. First release | The Excel sheet as an installable app that works offline. It has six areas plus a rating, comments, distance from contest, a saved list, CSV and backup export, share, copy and print. | A green theme. |

The release number is also the cache name in `sw.js` (`sevens-form-v11`) up to release 11. From then on the deploy workflow sets the cache name from the commit.

## Update a phone and check its release

A phone gets a new release the second time the app opens after the release goes live. Updating never deletes saved forms.

1. Open the app with signal. The phone loads the new files in the background.
2. Close the app fully.
3. Open the app again. The new release shows.
4. If the app still looks old, close it and open it once more.

The app does not show a release number yet. Use the features on the screen to tell which release a phone has.

| If the phone shows | The release is at least |
| --- | --- |
| A Review tab | 2 |
| An "Upload results" button | 3 |
| An "Email a copy to" box | 4 |
| A black header with a large white 7 | 5 |
| Tabs at the top of the screen | 6 |
| A Setup tab and a "Match details" fold | 7 |
| "Demo and training" in Setup | 8 |
| A wave button in each comment box | 10 |
| A microphone button beside the wave button | 11 |
| A bin icon on each row in Saved | 12 |
| A "Select forms to delete" button above the Saved list | 13 |
| "Tap a score to set it..." shown above the score rows | 14 |
| A "Sort by" box above the referee ranking on a phone | 15 |
| "Referees and coaches" under "This device" in Setup | 16 |

Clearing browser data, or removing the app, deletes saved forms and voice notes. Ask the coach to save a backup file first. Backup files do not hold voice notes.

## Troubleshooting

Most problems come from signal, permissions, or the way iPhone stores data. A form is safe on the phone until the coach deletes it or clears browser data.

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| "Upload did not work" or "No connection" | No signal, or static.app did not answer. | The form is safe. Move to signal and tap Upload again. Or use "Upload all waiting" on the Saved tab. |
| "Add your name first" | The coach name is empty. | Open "Match details", type the name, and upload again. |
| Upload does nothing on a copy of the app hosted elsewhere | Upload only works when static.app serves the page. | Use the static.app address. |
| A yellow number on the Saved tab | Forms are waiting to upload. | Open Saved and tap "Upload all waiting". |
| Saved forms are missing on an iPhone | Safari and the Home Screen icon keep separate storage. | Always open the app from its icon. Restore old forms from a backup file. |
| The phone shows an old release | The update needs two opens. | Close and open the app twice, with signal. |
| Forms and voice notes vanished | Browser data was cleared, or the app was removed. | Restore forms from the latest backup file. Voice notes cannot be restored. |
| "The microphone is blocked" | The coach refused the permission. | Allow the microphone for the site in the phone or browser settings. |
| No dictation button | The browser has no dictation, or dictation is off. | Check Setup, then Voice. Use the microphone on the keyboard. The wave button still works. |
| Dictation says it needs a network | Dictation uses an online speech service. | Get signal, or record a voice note. |
| Dictation gets words or names wrong | The speech service does not know names or te reo Māori. | Check the text and type the names. |
| A voice note will not share | The phone cannot share audio files from a web app. | Share the summary text instead. Note the phone model and browser for support. |
| A voice note is missing on another phone or in a backup | Clips stay on the phone that recorded them. | This is by design. Voice notes are not in backups, uploads or emails. |
| The QR scan does not work | The camera is blocked, the light is low, or the code is very dense. | Allow the camera and hold steady. Or paste the setup link. Long referee lists make dense codes, so share the link. |
| On an iPhone the camera app opens Safari | Safari has separate storage from the Home Screen app. | Scan inside the app: Setup, then "Scan a setup QR code". Or paste the link there. |
| "Load results file" skips rows | The tournament code is wrong or missing. | Check the code in Setup. The message shows how many rows were skipped. |
| A referee is missing from the ranking | Too few games, or a filter hides them. | Lower "Minimum games". Set Role to the right role. Clear the tournament and date filters. |
| The same referee shows twice | Two spellings of one name. | Under "Names", tap "Merge". |
| The page shows "404" just after a release | Static.app needs 1 to 2 minutes to publish. | Wait and reload. |
| A "Hosted for free" badge covers a button | The free static.app plan adds it at the bottom left. | Scroll the page. A paid plan removes the badge. |
| The date box shows the month first | The date box follows the phone's language setting. | Set the phone's region to New Zealand. |
| Demo forms appear on a real phone | Someone loaded the demo. | Setup, then "Demo and training", then "Remove the demo data". Real forms stay. |

## Data and privacy

Forms stay on the phone until the coach uploads, shares, emails or exports them. Dictation is the one feature that sends audio away automatically. Results name real people, so keep the static.app account private and follow your privacy rules.

| Data | Where it goes | When |
| --- | --- | --- |
| Scores and comments | The phone's browser storage. | As the coach types. |
| An uploaded form, including private notes, coach name and tournament code | The static.app form "sevens-results" in the organiser's static.app account. | When the coach taps Upload. |
| Voice notes | The phone only. Not in uploads, backups or emails. | When the coach records. Deleting a form deletes its clips. |
| Dictation audio | The browser's speech service: Google on Android Chrome, Apple on iPhone. | While the coach dictates. A warning shows on first use. A switch in Setup turns it off. |
| A shared or emailed summary | The person the coach picks. Private notes are left out. | When the coach taps Share or Email. |
| Backup and CSV files | Wherever the coach saves them. They include private notes. | When the coach exports. |
| A setup link or QR code | Anyone who has it. It holds the tournament code and the referee and coach names. | When the organiser shares it. |
| Demo data | The phone only. It is never uploaded. | When someone loads the demo. |

## Known limits

The app has not been tested on real phones yet. Everything below is either a design limit or a check still to do.

**Not yet tested**

- Voice notes, dictation and QR scanning were tested in simulated browsers with a fake microphone, a fake camera and a made-up speech service. Real phones may differ, especially an iPhone Home Screen app.
- The free static.app plan may limit form entries. Run a practice event with about 20 uploads before a tournament.

**Design limits**

- The app shows no release number.
- Upload works only when static.app serves the page.
- The organiser cannot read the results table live in the app. Export the entries from static.app, then use "Load results file".
- Voice notes are not uploaded, not in backups and not in emails.
- Dictation needs signal and sends audio to the browser's speech service.
- The tournament code is a filter, not a password.
- The coverage list is a list, not a grid of referees by game.
- Static.app makes a new results table when the list of upload fields changes.

**Content still to check**

- The score meanings and quick-note phrases are drafts. Agree them with the coaches.
- A fluent te reo Māori speaker should check the labels.

## Support reference

| Item | Detail |
| --- | --- |
| Live address | https://easy-goingcrow.staticdomains.app/ (static.app site "Sevenscoaching", site id adrf1y2gis) |
| Results | The static.app form "sevens-results". Read the rows in the static.app account for the site. |
| Results tables | Three tables exist from testing. The newest is the live one. The older ones hold test entries only. |
| Deploy | A GitHub workflow uploads the site to static.app on every push to the main branch. It needs the secret `STATICAPP_API_KEY` and the variable `STATICAPP_PID`. |
| Manual deploy | Upload the site zip to static.app. |
| Offline cache | The cache name in `sw.js` changes on every release. This makes phones fetch the new files. |
| Upload fields | Do not add or rename the hidden upload fields without a plan. Static.app makes a new results table each time. |
| Wording | Score meanings, quick notes and the referee, coach and level lists are set in the app script and the Setup tab. The README explains where. |

**Housekeeping**

- Delete the test entries in static.app: tournaments "ZZ TEST" and "ZZ LIVE TEST", and the table "sevens-test". The delete calls failed from code.
- Delete every API key that was pasted into a chat. Make a new key for the GitHub workflow at static.app, under the account API page.
- Keep the repo private. The results name real people.
