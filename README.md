# Legal Skills — Puerto Rico

> **Open-source library of legal AI skills for practice under Puerto Rico law**, in
> the Anthropic Skills (`SKILL.md`) format — runnable by Claude Code, Claude
> Cowork, and any other MCP/skills-compatible client. Citation checking,
> legal research memos, Regla 36 summary judgment motions, LPAU/CASARH
> agency appeals, Código Civil (2020) contract review, and Cánones de Ética
> conflict screening. MIT, contribution-friendly.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Jurisdiction](https://img.shields.io/badge/jurisdiction-Puerto%20Rico-005BBB)
![Format: Anthropic Skills](https://img.shields.io/badge/format-Anthropic_Skills-orange)
![Language](https://img.shields.io/badge/language-espa%C3%B1ol-blue)

---

## Table of contents

- [What this repository is](#what-this-repository-is)
- [What a skill looks like](#what-a-skill-looks-like)
- [Skills in this repository](#skills-in-this-repository)
- [Using these skills](#using-these-skills)
- [Why Puerto Rico needs its own set](#why-puerto-rico-needs-its-own-set)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Related projects](#related-projects)

---

## What this repository is

A **legal AI skill** is a Markdown file (`SKILL.md`) describing one applied
legal task — *"revisa esta cita conforme a LPRA," "prepara una moción de
sentencia sumaria bajo Regla 36," "hay conflicto de interés aquí?"* — in a
structured format an AI agent can follow deterministically: when to trigger,
what steps to take, what the output must contain.

Every skill lives under:

```
pr/{practice}/skills/{slug}/SKILL.md
```

and is grounded in Puerto Rico primary sources — the LPRA-codified statutes,
Tribunal Supremo and Tribunal de Apelaciones jurisprudence, and the specific
procedural rules (Reglas de Procedimiento Civil, LPAU, Cánones de Ética)
that actually govern practice on the island, not a generic U.S.-mainland or
Spain template with the names swapped.

## What a skill looks like

```yaml
---
name: pr-summary-judgment-motion
title: Puerto Rico Summary Judgment Motion Builder (Regla 36)
description: Structures a moción de sentencia sumaria or its opposition under
  Regla 36 of Puerto Rico's Reglas de Procedimiento Civil, including the
  numbered statement of uncontested material facts the Tribunal Supremo requires.
license: MIT
jurisdiction: pr
practice: litigation
language: es
---

# Skill title

## When to apply
Triggers, example prompts, what's out of scope.

## Algorithm
Step-by-step instructions for the agent.

## Output contract
What the answer must contain — format, citations, the mandatory disclaimer.
```

See [`pr/CLAUDE.md`](pr/CLAUDE.md) for the jurisdiction-wide rules every skill
here follows: sources-of-law priority, citation discipline, and the mandatory
disclaimer.

## Skills in this repository

19 skills across 6 practice areas — enough to run a matter end to end: intake
and engagement, research, prescription/deadline screening, pleadings,
discovery, motion practice, contracts, appeal, and a citation/filing-readiness
QC gate before anything goes out the door. Full table with descriptions:
[`pr/README.md`](pr/README.md).

| Practice area | Skills |
|---|---|
| General | `pr-legal-citation` · `pr-legal-research` · `pr-legal-memo-drafting` · `pr-citation-verifier` · `pr-filing-readiness` · `pr-prescription-analysis` |
| Litigation | `pr-summary-judgment-motion` · `pr-motion-drafting` · `pr-complaint-drafting` · `pr-answer-drafting` · `pr-discovery-drafting` · `pr-discovery-response` · `pr-doctrine-to-facts` |
| Appellate | `pr-appellate-drafting` |
| Administrative | `pr-agency-appeal-lpau` |
| Contracts | `pr-contract-review` · `pr-contract-drafting` |
| Professional responsibility | `pr-ethics-conflict-check` · `pr-engagement-letter` |

This is still a starter set. Practice areas like family, criminal, real
estate, labor/employment beyond LPAU appeals, and tax are open — see
[Contributing](#contributing).

## Using these skills

Clone the repo and point a Claude Code / skills-compatible client at the
`pr/` directory, or copy an individual `{slug}/SKILL.md` folder into your own
skills directory. No server, no build step — it's Markdown.

```bash
git clone https://github.com/ericalopezfebo/legal-skills-pr.git
```

## Why Puerto Rico needs its own set

Puerto Rico is not "Spain with a different flag" and not "another U.S.
state." It runs a hybrid system — a Spanish-derived Código Civil (fully
recodified in 2020) for private law, layered under a U.S. constitutional and
federal-court structure, litigated mostly in Spanish before the Tribunal
Supremo and Tribunal de Apelaciones, with its own procedural rules (Reglas de
Procedimiento Civil de 2009, LPAU de 2017) and its own administrative bodies
(like CASARH, still widely called CASP). Generic "US" or "ES" legal skills
get the citation format, the standard of review, and often the governing
code itself wrong. This repository exists so that gap has an open-source
answer.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: fork, add a
`pr/{practice}/skills/{slug}/SKILL.md`, open a PR. No confidential or
matter-specific content (no real client names, judges, or pending-case
material) — skills here are general-purpose.

## Disclaimer

Every skill in this repository is informational and does not constitute
legal advice. Output must be reviewed by an attorney admitted to practice in
Puerto Rico before being relied on, filed, or sent. See the full disclaimer
and citation-discipline rules in [`pr/CLAUDE.md`](pr/CLAUDE.md).

## License

[MIT](LICENSE). Use, modify, and distribute freely, including commercially —
attribution appreciated.

## Related projects

- [Anthropic Skills](https://www.anthropic.com/news/skills) — the underlying
  `SKILL.md` format.
- [`legal-skills-open`](https://github.com/ThomasMoreAI/legal-skills-open) —
  the multi-jurisdiction legal-skills library this repo's format is modeled on.
- [`zubair-trabzada/ai-legal-claude`](https://github.com/zubair-trabzada/ai-legal-claude)
  and [`joe-shenouda/awesome-cyber-skills`](https://github.com/joe-shenouda/awesome-cyber-skills) —
  inspiration for structuring a domain-specific Claude skills catalogue.

---

*Started by [@ericalopezfebo](https://github.com/ericalopezfebo). Issues and
pull requests welcome.*
