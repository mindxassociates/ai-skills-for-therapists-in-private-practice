# Access and sessions

## Clients and externals — email + one-time code

1. Enter email → server checks the account exists and is Active → sends a **6-digit code** (10-minute expiry).
2. Code is stored **only as a SHA-256 hash** (of record ID + code). 5 attempts; the 5th failure locks the account for 15 minutes.
3. Optional second step: where a **date of birth** is on file, it is required before the session opens — also stored only as a hash; the raw date is never kept.
4. Success issues a **session token** (random, stored as hash, ~12-hour expiry), verified on **every** server call. Disabling the account ends its sessions immediately.
5. A code request for a **disabled** account sends nothing and alerts the admin.

## Providers — name + PIN

- Pick/type your name (type-to-search over the Providers list), enter a **PIN (4–8 digits)**.
- First time: no PIN on file → the flow offers set-PIN (enter + confirm); the hash is stored and the session opens. Nobody — including the admin — ever sets or sees another provider's PIN; the admin console can **reset** (clear the hash) so the provider sets a new one at next sign-in.
- Same 5-try / 15-minute lockout, shared counter discipline with the code surface.

## Lockout bookkeeping (get this exactly right)

One lock state per account across its surfaces (code, DOB, PIN where applicable). Pruning rule: delete an entry only when its **lock has expired** or the counter is stale by age — *never* prune entries merely because `lockedUntil` is 0 or past, while they still hold a live attempt count. The classic bug (`if (until <= cutoff) delete`) wipes counters on every read and the 5-try lockout silently never engages. Test the lockout end-to-end: 5 wrong codes → 6th (even correct) refused until the window passes.

## Terms gate

- Clients and externals acknowledge the practice's terms at first login: not monitored 24/7 · not for emergencies (911 / 988) · replies within one business day · **practice administration can access messages** · messages become part of practice records.
- The acknowledgment stores the **terms version** + timestamp. Bumping the version re-blocks content (threads hidden) until the user re-acknowledges. Never pre-check the box, never bury the admin-access line.

## Sessions

- Tokens are random, hash-stored, expiry-checked per call; an hourly trigger sweeps expired sessions/codes.
- Ending conditions: expiry, account disabled, PIN reset (provider), or the incident-response "clear all session columns" procedure (see `security-and-privacy.md`).
- No "remember me" beyond the session window; no anonymous surfaces of any kind — there is no guest, preview, or emailed-link read path. Nobody sees any part of a conversation without signing in.
