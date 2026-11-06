# Test Checklist — Solo Consult Booking Kit

Run in the deployed apps. Use a test client identity throughout, and
delete test rows/events afterwards. Adapt the bracketed examples to
the owner's own Config (states, panels, languages).

## A. Fit check (replaces group "routing")

- [ ] **In-state + accepted panel** (e.g. your licensed state + a
      panel from Config) → you appear, with slots.
- [ ] **Unlicensed state** → no-fit message with the practice contact
      email; no form errors, no partial booking, no Appointments row.
- [ ] **Panel you don't take** → no-fit message. **State-restricted
      panel** (a panel you take only in one state, if any) → offered
      in that state, no-fit in another.
- [ ] **Language you don't offer** → no-fit. **Age group you don't
      serve** (e.g. "my child" when you see adults only) → no-fit.
      **Sliding scale** required when Config says No → no-fit.
- [ ] **Outside the U.S.:** location free-text appears and is
      required; payment step shows **only** Self-pay + Sliding scale;
      if Config `ServesInternational` is No → no-fit; if Yes, the
      booking stores State "Outside U.S." with the typed location as
      City, and the calendar event carries the private-pay-only flag
      line.
- [ ] **Accepting off:** toggle AcceptingNewClients off in the
      Console → wizard shows the not-accepting message and no slots;
      toggle back on → slots return.

## B. Calendar conflicts & availability math

- [ ] Put a busy event on your calendar inside your weekly hours →
      that slot disappears (and only that slot).
- [ ] Event **outside** weekly hours changes nothing.
- [ ] Time Off (Console) covering a day you normally work → no slots
      that day. A TimeOff-**tab** row does the same and also beats a
      date-specific override for that date.
- [ ] Submit new weekly hours in the Console → the page follows the
      **new** hours (and their minimum notice + time zone), not the
      Availability-tab fallback.
- [ ] **Split day:** two blocks in one day (e.g. 9 AM–12 PM and
      2–5 PM) → slots in both blocks, none in the midday gap.
- [ ] **Date-specific hours:** pick a workday, set different hours →
      only those hours are offered that day; mark another date
      Unavailable → no slots that day.
- [ ] **Slot increment:** set 30 minutes in the Console → start times
      fall only on :00/:30. **Minimum notice:** a slot sooner than
      the notice period is not offered. **Buffer:** set 15 minutes →
      slots adjacent to a busy event are also blocked.
- [ ] **Consult cap:** set a cap of 1/day in the Console, book one
      consult that day → no further slots that day; clear the cap →
      slots return.
- [ ] **Time zone:** submit weekly hours with a different zone
      selected → offered slots shift accordingly, and `checkSetup()`
      reports the new zone and its source. **DST week:** a 9:00 AM
      slot in your zone still lands at 9:00 AM local after the change.

## C. Booking

- [ ] Complete a booking → confirmation screen shows your name,
      date/time in the browser's zone, and the booking ID.
- [ ] Event exists on **your** calendar at the correct time, titled
      exactly "Initial Consultation — <BookingID>", description with
      booking ID + phone + language + for-whom only — **no goals
      text, no client attendee**.
- [ ] Appointments row has every field, Status = Booked, a
      `ManageToken` **hash** (64 hex chars — not a usable link),
      `PrivacyConsentAt` set and `PrivacyConsentVersion` = the
      current version.
- [ ] Client email received: correct time in the client's zone (+
      your zone if different), .ics opens to the right time, manage
      link present, crisis footer present.
- [ ] Owner notification received: triage minimum only, and the
      **subject contains the BookingID, not the client's name**.
- [ ] AuditLog gained a BOOKED row with IDs/times only.

## D. Booking protections

- [ ] Two browsers pick the **same slot** and confirm within seconds
      → exactly one succeeds; the other gets "that time was just
      booked" and refreshed slots. One event + one row exist.
- [ ] Book a slot, search again immediately → the slot is gone.
- [ ] With an upcoming booking in place, book again with the **same
      email** (different phone) → refused with the existing-consult
      message. Repeat with a different email and the **same phone**
      (including +1 / punctuation variants) → also refused. Cancel
      the first booking → the second booking now succeeds.
- [ ] Set the hidden honeypot field in dev tools before confirming →
      generic failure message; no event, no row.
- [ ] Temporarily set the per-contact attempt limit to 1 → a second
      confirmation attempt inside the window is throttled; restore
      the setting afterwards.

## E. Reschedule / cancel (manage link)

- [ ] The emailed link opens without any login and shows the right
      appointment.
- [ ] Reschedule → old event removed, new event created, row updated
      (times, event ID, note of the old time), both parties emailed,
      and the **old manage link no longer works** (token rotated).
- [ ] Two manage sessions race for the same target slot → only one
      gets it.
- [ ] Cancel → event removed, Status = Cancelled with CancelledAt,
      notices sent, the slot is bookable again.
- [ ] Inside the cutoff (book < cutoff away, or temporarily set the
      cutoff to 72h) → online cancel/reschedule refused with the
      contact-us message; appointment untouched.
- [ ] Tamper with the token in the URL → "link is not valid";
      nothing is shown or changed.

## F. Failure handling & setup checks

- [ ] Point Config `CalendarID` at a nonexistent address → you
      disappear from results (no slots), the reason is in the
      execution log, and the wizard still loads cleanly. Restore the
      ID and re-run `checkSetup()` → `accessRole=owner`,
      `freebusy=OK`, hours blocks ≥ 1.
- [ ] Temporarily share nothing / change nothing else: confirm there
      is **no step in this system where anyone shares a calendar with
      anyone** — if the build added one, it's group-edition residue;
      remove it.
- [ ] Invalid submissions (bad email, short phone, missing city,
      tampered slot/provider values via dev tools) → server rejects
      with a plain error; nothing is written; the raw error text
      appears only in the execution log.

## G. Reminders, follow-ups, no-show

- [ ] Create a booking ~2h out, run the reminder send by hand from
      the editor → one client reminder + one owner reminder arrive;
      markers are stamped; running it again sends nothing.
- [ ] Let a test consult end (+ the follow-up delay), run the sweep
      → the client follow-up arrives with the survey link; marker
      stamped; a second sweep doesn't resend.
- [ ] Mark a past test consult **No-show** in the Console → its
      follow-up never sends.
- [ ] Cancelled appointments trigger **neither** reminder nor
      follow-up.

## H. Console

- [ ] Wrong PIN 5 times → 15-minute lockout message; correct PIN
      after the lock expires works. (If the lockout never triggers,
      check the prune rule in the Console spec.)
- [ ] My Current Availability panel matches the public page's slots
      for the next 7 days.
- [ ] Availability submission emails arrive as receipts; Consult
      Booking Settings changes **auto-save** (no button) and take
      effect on the public page without a redeploy.
- [ ] Settings edit: change a template, save, confirm the read-back
      matches, then trigger that email and verify the new wording.
      Blank the template → the built-in default returns.
- [ ] Exports: audit CSV and bookings CSV download; **no ManageToken
      column or values anywhere in either file**; audit PDF opens.
- [ ] Every Console server call rejects a missing/forged token
      (test by clearing site data and calling a view directly).

## I. Second language (only if enabled)

- [ ] Toggle switches every step's wording with nothing left in the
      other language and no "undefined" text; `?lang=` opens the
      wizard in that language directly.
- [ ] A booking in the second language stores `UiLanguage`, and its
      confirmation / reminder / follow-up / manage page all arrive
      in that language; an English booking is completely unchanged.
- [ ] UI language and therapy language are independent (booking in
      one UI language for therapy in the other still works).

## J. Housekeeping after testing

- [ ] Delete test events from the calendar and test rows from
      Appointments + AuditLog test entries noted as tests.
- [ ] Settings restored (buffer, cutoffs, attempt limits, cap off if
      it was a test).
- [ ] Old booking service still live and untouched until go-live.
