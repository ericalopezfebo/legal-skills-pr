---
name: pr-motion-assume-representation
title: Puerto Rico Motion to Assume Legal Representation
description: Drafts a Puerto Rico trial-court motion entering or assuming legal representation for a party, including joint representation and substitution scenarios, with SUMAC-aware filing instructions.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion to Assume Legal Representation

## When to apply
- A lawyer is entering an existing Puerto Rico Court of First Instance case.
- Additional counsel is joining an existing legal team.
- New counsel is appearing after another attorney has withdrawn or will seek withdrawal.

## Workflow
1. Confirm that the forum is the Puerto Rico Court of First Instance and obtain the exact caption, case number, judicial region/sala and represented party.
2. Determine whether this is: (a) first appearance for the party, (b) co-representation, or (c) substitution. Do not state that prior counsel has been relieved unless an order actually says so.
3. Obtain the appearing lawyer's name, RUA number, mailing address, telephone number and email. Use `[POR COMPLETAR]` for missing data.
4. Draft a short motion identifying the party represented and requesting that counsel be entered as attorney of record and receive future notices.
5. If co-representation is intended, say so expressly and do not imply that existing counsel is being replaced.
6. If substitution is intended, distinguish the new appearance from any separate request by prior counsel to withdraw.
7. For SUMAC matters, remind the user that each additional attorney must complete the electronic appearance process from that attorney's own account and select only the party or parties actually represented. Do not invent a filing event name if the current SUMAC menu has not been verified.
8. Include a certificate of service when required by the filing posture and the applicable rules/order.

## Guardrails
- Never invent a RUA number, address, email, party name, case number or judicial region.
- Do not represent that an attorney has authority to appear for a party unless the user supplies that fact.
- Do not combine an appearance with a withdrawal request unless the user specifically asks for both.
- Confirm current SUMAC and tribunal-specific filing requirements before filing.
- Apply `pr/CLAUDE.md` and `pr-filing-readiness` before final use.

## Output structure
When the user asks for a finished motion, draft a filing-ready Puerto Rico motion with:
1. tribunal caption and case information;
2. title such as `MOCIÓN ASUMIENDO REPRESENTACIÓN LEGAL`;
3. appearance paragraph;
4. identification of the represented party;
5. request that counsel be entered as attorney of record and receive notices;
6. signature block; and
7. certificate of service when applicable.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
