# ISO Matching Rules

Apply in order. A post gets a draft only when at least one provider passes every applicable filter. Skip quietly when no provider passes. Do not report skipped posts (except on a first manual run the user asked to audit).

Customize the lines marked [CUSTOMIZE]. Everything else is a default that earned its place — change it only with a reason.

## 0. Is it an ISO at all

Pass: the post seeks a therapist for a client ("ISO", "in search of", "looking for", "seeking", "referral", "recommendations", "anyone know").

Skip: self-promotion, job or practicum seeking, seeking a non-therapist professional, medication management only, testing or evaluation only, events, peer or supervision groups, resource lists, and posts asking for a support group as the whole request.

## 1. State

- The provider must be licensed in the client's state.
- The client's state is, in order: a state named in the post, a state implied by a state-specific plan named in the post (for example, "BCBS of Tennessee" implies Tennessee), then the implied state of the group from `config.md`.
- A location-flexible post (telehealth, virtual, online) that names no state passes this filter for all providers in the profile.
- If the named state is one no provider is licensed in, no one fits. Skip.

## 2. Age and population

- If the post names an age group (child, preteen, teen, adolescent) or asks for age-specific care (for example play therapy), keep only providers whose Ages Served includes it.
- A provider documented for adults only is never drafted for a teen or child post, even when every other filter passes.
- If the post names no age group, this filter passes for all.

## 3. Accepting status

- Keep only providers whose profile says accepting new clients: Yes, in those words or the sheet equivalent you defined in the profile.
- No, blank, waitlist, or anything else excludes. No exceptions.
- A dated override in the profile ("not accepting until [date]", "booked out until [month]") excludes the provider until that date, even when the accepting field says Yes.

## 4. Insurance and financial fit

- [CUSTOMIZE] Default: skip the post entirely when it requires Medicare or Medicaid (including Medicare Advantage and state Medicaid names) and no provider in the profile is paneled for them. Most solo and small group practices using this tracker are not, which is why the default is a full skip. If you are paneled, rewrite this bullet to say so and match normally.
- If the post names a plan, the provider's Contracted Panels must include it. Match within plan families: BCBS matches Blue Cross, Blue Shield, and Anthem Blue Cross Blue Shield; Optum matches UHC, UnitedHealthcare, UMR, Oxford, and Oscar.
- State-suffixed panels are state-specific. A panel listed as (for example) BCBS-TX covers posts for clients in Texas only, even when the same brand exists elsewhere.
- Billing route matters when the post raises it. If a provider is paneled with a plan only through a platform (for example Headway, Alma, Grow) and the post requires direct paneling or excludes platform billing, that provider does not fit that post. A post that simply names the plan, with no direct-panel requirement, still fits.
- EAP posts fit only providers on that EAP panel. Note any EAP-specific condition in the profile (for example, no free consultation for a given EAP) and never promise it in a draft.
- Budget and sliding scale:
  - If the post states a budget cap or asks for sliding scale or self-pay, keep only providers whose private pay rate fits or who offer sliding scale.
  - Sliding scale minimum rule: if a provider's profile lists a sliding scale minimum, draft them on a budget post only when the stated budget equals or exceeds that minimum. Below the minimum, exclude that provider for that post entirely. Do not draft an unnumbered "she offers sliding scale" reply to get around it. At or above the minimum, the figure may be stated.
  - For providers with no listed minimum, never quote a sliding scale number in a draft.
- Superbills: a post that requires a superbill is satisfiable by any otherwise-fitting provider, unless the profile says that provider cannot offer one. Never skip a post or exclude a provider over a superbill alone.
- If the post names no insurance or financial constraint, this filter passes for all.

## 5. Setting and level of care

- If the post requires in-person and the provider is telehealth-only, no fit. If the post requires telehealth and the provider is in-person only, no fit.
- Outpatient therapy only, in the types of client the profile lists (individual, couples, family). Skip IOP, PHP, residential, and inpatient requests.
- A provider documented for individual work only is never drafted for a couples or family post, and the reverse holds the same way. "Couples" in a post means the provider's Types of Client must include couples.
- Posts asking for two different referrals (for example, one individual therapist and one couples therapist) are matched per referral. Draft only for the parts a provider genuinely fits, and say in your report to the user that the draft covers only that part.

## 6. Specialty and modality fit

- Prefer the provider whose documented specialties and modalities match the post's primary need. This is a preference among providers who already passed filters 1 to 5, never a reason to waive one of them.
- Never match on insurance, state, or an identity word alone. The clinical need named in the post must appear in the provider's documented specialties or modalities.
- Never infer a specialty, modality, identity, faith, training, or lived experience that the profile does not document. If the post's central ask is undocumented for every provider (for example a named method like ERP, IFS, neurofeedback, or a niche presentation), no one fits, however good the insurance fit looks.
- Hard-skip specialties: [CUSTOMIZE] list here any service no provider in your practice offers (examples from the originating practice: sex therapy, foster care or adoption work, cognitive remediation). A post whose primary ask is on this list is skipped entirely.
- Provider exclusions in the profile always win over a specialty match. Check each candidate provider's "Do NOT recommend for" line before drafting.
- Experience and supervision: a provider under supervision, or documented as early-career, is not drafted for posts requiring an experienced clinician or experienced, specialized work in an area (for example complex trauma) that the profile flags.
- Acuity: posts whose central need is higher-acuity or specialized treatment beyond outpatient scope as documented in the profile (for example suicide-focused treatment or emerging psychosis work, when no provider documents it) are not a fit. When in doubt, skip.
- Availability claims: note evening or weekend availability in your report only when the profile documents it for that provider. Never put an availability claim in a draft that the profile does not support.
- Language: mention a language only under the rule in `config.md` (the post asks for it, or the post is written in it).

## 7. Thread checks (before any draft)

- Comment count: skip when the post has more than 20 comments or replies. Exactly 20 is allowed.
- Already replied: read the comments. Skip when you, the practice, or any provider you would recommend has already been named or has already replied.
- Group-practice requests: if the post explicitly asks for an individual therapist and not a group practice (or the reverse), honor it.

## 8. Selection among fitting providers

- Name at most three providers, and only when they fit comparably. Name one when only one fits well.
- [CUSTOMIZE] When fit is comparable, order by the priority set in `config.md` (for example, availability, referral need, or a fair rotation). If no priority is set, order by closeness of specialty fit.
- [CUSTOMIZE] Last-resort providers named in `config.md` are drafted only when their stated condition is met and no other provider is a good fit. If any other provider survives as a good fit, name them instead.

## The rule behind the rules

When a claim cannot be verified from the profile, the answer is skip, not soften. A draft that hedges an undocumented specialty into a public thread still recommends the provider for that specialty in every reader's eyes.
