# Test Checklist — Group Consult Booking Kit

Run in the deployed apps, against your real roster facts (substitute
your own providers/states/panels for the bracketed examples). Test
identities throughout; delete test rows/events afterwards.

## A. Routing (eligibility)

- [ ] **State gate:** [State A] + [panel several providers take] →
      exactly the State-A-licensed providers on that panel appear.
      [State B] → only State-B providers.
- [ ] **State-restricted panel:** a panel a provider holds in one
      state only → they appear for it there and **not** in their
      other licensed state.
- [ ] **EAP-only provider** (on an EAP, not on a commercial panel) →
      appears for that EAP + self-pay, not for the commercial panel.
- [ ] **Language:** a language only one provider offers → only they
      can appear. **For-whom:** "my teen" → only teen-serving
      providers; "couple" → only couples providers.
- [ ] **Sliding scale:** selected → providers with SlidingScale = No
      never appear.
- [ ] **Owner-defined exclusion** (a RoutingRules entry, if any) →
      the excluded provider doesn't appear for that match, appears
      for others.
- [ ] **Preferred clinician + gender:** name a preferred clinician →
      the gender-preference question is hidden; if a gender value was
      picked before going back, it must **not** filter out the named
      clinician (check the stored row: GenderPreference = No
      preference).
- [ ] **No fit:** an impossible combination → no-match message with
      the practice contact email + "mention your preferred clinician"
      guidance; no partial record.
- [ ] **Inactive / not-accepting / no-hours / unconnected providers**
      never appear, for any combination.

## B. Calendar conflicts & availability math

- [ ] Busy event inside a provider's hours → that slot (only) gone.
      Event outside hours → no change.
- [ ] TimeOff row for one provider → their range gone, colleagues
      unaffected. **`ALL` row** → everyone's range gone.
- [ ] New weekly submission in Manage Availability → booking page
      follows the **new** hours/notice/zone, not the Availability
      tab. **Split day** (two blocks) → slots in both, none midday.
- [ ] Manage Availability **time-off** (any Applies-to value) → no
      consult slots in the range. **Date-specific hours** → replace
      that date's hours; "Unavailable" date → no slots; a TimeOff-tab
      row still overrides a date-specific override.
- [ ] Therapy-flag submission (Applies-to = Therapy/Both) → practice
      receipt email carries **MANUAL FOLLOW-UP NEEDED**.
- [ ] Buffer setting → slots adjacent to busy events blocked.
      Minimum notice → sooner slots not offered. **Cap** (set 1/day
      for a test provider, book one) → no more slots that day.
- [ ] **DST week:** a 9:00 AM provider-zone slot stays 9:00 AM local
      across the change. **Panel of zones:** a provider who submitted
      hours in a different zone shows shifted slots, and
      `checkSetup()` reports the new zone with source "Manage
      Availability."

## C. Booking

- [ ] Complete a booking → confirmation shows provider, date/time in
      the browser's zone, booking ID.
- [ ] Event on the **provider's** calendar, correct time, titled
      exactly "Initial Consultation — <BookingID>", description =
      booking ID + phone + language + for-whom only, **no attendee,
      no goals text**.
- [ ] Appointments row complete: Status = Booked, `ManageToken` is a
      64-char hash, `PrivacyConsentAt` set, version = current.
- [ ] Client email: times in client zone (+ provider zone if
      different), .ics correct, manage link present, crisis footer
      present.
- [ ] Practice notification: practice inbox **and** provider's work
      email; triage minimum; **subject has the BookingID, not the
      client's name**.
- [ ] AuditLog gained a BOOKED row (IDs/times only).

## D. Protections

- [ ] Two browsers, same provider + slot, confirm within seconds →
      exactly one succeeds; other gets "just booked" + refreshed
      slots; one event + one row.
- [ ] Book, re-search → slot gone. Same email (new phone) with an
      upcoming booking → refused; same phone (new email, +1 /
      punctuation variants) → refused. Cancel the first → second
      succeeds.
- [ ] Honeypot field set in dev tools → generic failure; no event,
      no row. Per-contact attempt limit temporarily 1 → second
      attempt throttled; restore the setting.

## E. Reschedule / cancel

- [ ] Emailed manage link opens login-free, shows the right booking.
- [ ] Reschedule → old event deleted, new event created, row updated,
      notices sent, **old manage link dead** (rotated). Race two
      manage sessions for one target slot → one wins.
- [ ] Cancel → event deleted, Status = Cancelled + CancelledAt,
      notices sent, slot bookable again.
- [ ] Inside cutoff → refused with contact-us message, untouched.
      Tampered token → "link is not valid," nothing shown/changed.

## F. Permissions & failure handling

- [ ] Test provider's calendar re-shared **free/busy-only** →
      availability displays, booking fails with the clear
      checkSetup message; no row, no orphan event. Restore writer
      sharing.
- [ ] CalendarID set to a nonexistent address → that provider
      silently omitted; reason in the execution log; others book
      normally.
- [ ] `checkSetup()` output: per provider — accessRole, free/busy,
      hours blocks; warnings fire for free/busy-only and zero-hours.
- [ ] Invalid submissions via dev tools (bad email, short phone,
      tampered provider ID / start time) → plain server rejection;
      nothing written.
- [ ] **Cross-provider tampering:** as Provider A (valid token), call
      My Consults / Manage Availability with Provider B's ID → B's
      data is never returned or written. As a provider, call Consult
      Admin functions → nothing returned.
- [ ] PIN lockout: 5 wrong tries → 15-minute lock; if the lock never
      engages, check the lockout-prune rule in the provider-apps
      spec.

## G. Connect Your Calendar

- [ ] Fresh provider: name + PIN (create-PIN path if unset) → pick
      calendar → Connect → status reads back **from the booking
      side** as connected; Providers tab CalendarID updated.
- [ ] Personal-account provider sees the unverified-app screen and
      the in-app warning text matches what they actually see.
- [ ] Disconnect → share removed, registration cleared, provider
      disappears from booking results; `checkSetup()` agrees.
- [ ] Manual fallback: hand-share a calendar at writer level → admin
      sets the ID → identical connected state.
- [ ] Wrong-account authorization (provider authorizes an account
      that doesn't own their schedule calendar) → detectable via a
      test booking landing on the wrong calendar; reconnect correctly.

## H. Reminders, follow-ups, admin

- [ ] Booking ~2h out + run the reminder send by hand → client +
      provider reminders once; markers stamped; re-run sends nothing.
- [ ] After a test consult ends (+ delays), run the sweep → client
      survey email + provider follow-up arrive once; markers stamped.
      A provider on the admin's exclusion list gets **no** follow-up.
- [ ] Mark a past consult **No-show** in My Consults → its follow-up
      never sends. Cancelled bookings trigger neither email.
- [ ] Consult Admin: edit a template → save → read-back matches →
      next send uses it; blank it → built-in default returns. Change
      a booking rule → effective without redeploy.
- [ ] Admin Tools exports: audit CSV + bookings CSV contain **no
      ManageToken values**; audit PDF opens; snapshot numbers match
      the Appointments tab.
- [ ] Admin on-behalf edit: change a provider's hours in Consult
      Admin → booking page + provider's My Current Availability panel
      both reflect it, stamped as admin-entered.

## I. Bilingual (only if enabled)

- [ ] Toggle switches every step with nothing left over / no
      "undefined"; `?lang=` opens directly in that language.
- [ ] Booking in language 2: row stores `UiLanguage`; confirmation /
      reminder / follow-up / manage page all in language 2; provider
      shown by their second-language name; English bookings unchanged.
- [ ] UI language ≠ therapy language still books and emails correctly.

## J. Housekeeping after testing

- [ ] Test events/rows deleted (AuditLog test entries noted as tests).
- [ ] Settings restored (buffer, cutoffs, attempt limits, test caps).
- [ ] Old per-provider booking links still live until cutover.
