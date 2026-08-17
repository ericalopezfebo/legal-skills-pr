---
name: pr-motion-withdraw-representation
title: Puerto Rico Motion to Withdraw Legal Representation
description: Drafts a Puerto Rico motion requesting leave to withdraw as counsel while protecting the client, preserving deadlines, and avoiding disclosure of unnecessary confidential information.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion to Withdraw Legal Representation

## When to apply
- Counsel seeks leave to withdraw from an active Puerto Rico court case.
- A substitution of counsel is underway and prior counsel must be relieved.

## Workflow
1. Obtain the exact case caption, case number, court/sala, represented party and current procedural posture.
2. Identify imminent hearings, trial dates, discovery deadlines, filing deadlines and outstanding court orders.
3. Determine whether substitute counsel has appeared or is expected to appear. Do not state that substitution is complete unless supported by the record.
4. State the basis for withdrawal only to the extent necessary. Protect confidential information and avoid narrating privileged communications or prejudicial client details.
5. Explain, when supported, that withdrawal can occur without materially prejudicing the client's interests and identify any protective transition steps actually taken.
6. Request an order relieving counsel and, if appropriate, directing that future notices be sent to substitute counsel or to the client at an address the user has supplied.
7. Do not state that representation has ended merely because the motion was filed; withdrawal is subject to the tribunal's ruling and other applicable law/rules.
8. Flag any approaching deadline that may require separate relief, such as an extension or continuance.

## Guardrails
- Never invent a reason for withdrawal.
- Do not disclose fee disputes, strategic disagreements, client instructions or confidential facts unless legally necessary and supplied by the user.
- Do not provide the client's address publicly unless the user confirms it should appear in the filing and disclosure is appropriate.
- Do not assume filing the motion automatically terminates counsel's obligations.
- Apply the current Puerto Rico Rules of Civil Procedure, Rules of Professional Conduct, applicable court orders, `pr/CLAUDE.md`, and `pr-filing-readiness`.

## Output structure
Draft, when requested:
- caption;
- `MOCIÓN SOLICITANDO RENUNCIA A REPRESENTACIÓN LEGAL` or equivalent accurate title;
- concise procedural background;
- carefully limited grounds;
- transition/protection facts supported by the user;
- precise prayer for relief;
- signature block; and
- certificate of service when applicable.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
