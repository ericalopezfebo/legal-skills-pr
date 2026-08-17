# Puerto Rico (`pr/`)

Skills for practice under Puerto Rico law. See [`CLAUDE.md`](CLAUDE.md) for the jurisdiction's legal family, sources of law, and mandatory citation/disclaimer conventions — every skill below is written to follow it.

## General

| Skill | What it does |
|---|---|
| [`pr-legal-citation`](general/skills/pr-legal-citation/) | Checks and formats citations to PR statutes, case law, and regulations |
| [`pr-legal-research`](general/skills/pr-legal-research/) | Structures research on a PR legal question into a sourced memo |
| [`pr-legal-memo-drafting`](general/skills/pr-legal-memo-drafting/) | Drafts a formal, objective legal research memorandum |
| [`pr-citation-verifier`](general/skills/pr-citation-verifier/) | Verifies that a cited authority exists, is current, and actually supports the proposition |
| [`pr-filing-readiness`](general/skills/pr-filing-readiness/) | Final pre-filing quality-control audit of a document |
| [`pr-prescription-analysis`](general/skills/pr-prescription-analysis/) | Analyzes limitations/caducity periods through a claim-specific chronology |

## Litigation

| Skill | What it does |
|---|---|
| [`pr-summary-judgment-motion`](litigation/skills/pr-summary-judgment-motion/) | Builds/opposes a moción de sentencia sumaria (Regla 36) |
| [`pr-motion-drafting`](litigation/skills/pr-motion-drafting/) | General-purpose motion/opposition/reply drafting engine |
| [`pr-complaint-drafting`](litigation/skills/pr-complaint-drafting/) | Drafts a civil complaint from verified facts and causes of action |
| [`pr-answer-drafting`](litigation/skills/pr-answer-drafting/) | Drafts a paragraph-by-paragraph answer and supported affirmative defenses |
| [`pr-motion-assume-representation`](litigation/skills/pr-motion-assume-representation/) | Drafts a motion entering or assuming legal representation, including co-representation/substitution scenarios |
| [`pr-motion-withdraw-representation`](litigation/skills/pr-motion-withdraw-representation/) | Drafts a motion to withdraw as counsel while protecting the client and pending deadlines |
| [`pr-motion-extension-time`](litigation/skills/pr-motion-extension-time/) | Drafts a motion for extension of time from verified deadlines and supported good cause |
| [`pr-motion-dismiss`](litigation/skills/pr-motion-dismiss/) | Analyzes and drafts a Puerto Rico Regla 10.2 motion to dismiss |
| [`pr-motion-compel-discovery`](litigation/skills/pr-motion-compel-discovery/) | Drafts a request-by-request motion to compel discovery |
| [`pr-reconsideration-motion`](litigation/skills/pr-reconsideration-motion/) | Drafts a civil reconsideration motion with deadline and appellate-effect screening |
| [`pr-default-relief`](litigation/skills/pr-default-relief/) | Handles entry of default, default judgment, and relief from default under Puerto Rico procedure |
| [`pr-civil-deadlines`](litigation/skills/pr-civil-deadlines/) | Calculates and audits civil litigation deadlines from verified rules, triggers, and orders |
| [`pr-discovery-drafting`](litigation/skills/pr-discovery-drafting/) | Drafts interrogatories, production requests, and admissions |
| [`pr-discovery-response`](litigation/skills/pr-discovery-response/) | Drafts discovery responses and good-faith objections |
| [`pr-doctrine-to-facts`](litigation/skills/pr-doctrine-to-facts/) | Connects citations already in a draft to the case's specific facts |

## Appellate

| Skill | What it does |
|---|---|
| [`pr-appellate-drafting`](appellate/skills/pr-appellate-drafting/) | Drafts an appellate brief/petition after jurisdiction and deadline screening |

## Administrative

| Skill | What it does |
|---|---|
| [`pr-agency-appeal-lpau`](administrative/skills/pr-agency-appeal-lpau/) | Structures an LPAU agency appeal, incl. CASARH/CASP personnel appeals |

## Contracts

| Skill | What it does |
|---|---|
| [`pr-contract-review`](contracts/skills/pr-contract-review/) | Reviews an existing contract against the 2020 Código Civil |
| [`pr-contract-drafting`](contracts/skills/pr-contract-drafting/) | Drafts, revises, or adapts a contract or clause |

## Notarial

| Skill | What it does |
|---|---|
| [`pr-notarial-instrument-drafting`](notarial/skills/pr-notarial-instrument-drafting/) | Drafts and audits Puerto Rico escrituras públicas and actas notariales from verified facts and current notarial/substantive law |

## Professional responsibility

| Skill | What it does |
|---|---|
| [`pr-ethics-conflict-check`](professional-responsibility/skills/pr-ethics-conflict-check/) | Screens conflicts, confidentiality, and communications under the 2025 Puerto Rico Rules of Professional Conduct |
| [`pr-engagement-letter`](professional-responsibility/skills/pr-engagement-letter/) | Drafts a client engagement letter / hoja de encargo |

---

**Composable workflows:**

- Complaint: `pr-legal-research` → `pr-prescription-analysis` → `pr-complaint-drafting` → `pr-citation-verifier` → `pr-filing-readiness`
- Answer: `pr-civil-deadlines` → `pr-answer-drafting` → `pr-citation-verifier` → `pr-filing-readiness`
- Motion: specialized procedural skill (e.g. `pr-motion-dismiss`, `pr-summary-judgment-motion`) → `pr-motion-drafting` → `pr-doctrine-to-facts` → `pr-citation-verifier` → `pr-filing-readiness`
- Discovery dispute: `pr-discovery-response` → `pr-motion-compel-discovery` → `pr-filing-readiness`
- Reconsideration: `pr-civil-deadlines` → `pr-reconsideration-motion` → `pr-citation-verifier` → `pr-filing-readiness`
- Appeal: `pr-appellate-drafting` → `pr-legal-citation` → `pr-citation-verifier` → `pr-filing-readiness`
- Contract: `pr-contract-drafting` → `pr-contract-review` → `pr-citation-verifier` (when legal authorities are stated)
- Notarial instrument: `pr-legal-research` (when current-law verification is needed) → `pr-notarial-instrument-drafting` → `pr-citation-verifier`
- New matter: `pr-ethics-conflict-check` → `pr-engagement-letter`

Want to add a practice area or skill? See the root [`CONTRIBUTING.md`](../CONTRIBUTING.md).
