---
name: pr-notarial-instrument-drafting
title: Puerto Rico Notarial Instrument Drafting
description: Drafts Puerto Rico public instruments, including escrituras públicas and actas notariales, from verified facts and current Puerto Rico notarial, civil, registry, tax, and professional-conduct law. Use when the user asks to redact, preparar, revisar, adaptar, corregir, or structure a escritura, acta, poder, donación, compraventa, opción, repudiación de herencia, hogar seguro, or another instrumento público for authorization by a Puerto Rico notary.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: notarial
language: es
---

# Puerto Rico Notarial Instrument Drafting

## Purpose
Draft a Puerto Rico notarial instrument that is structurally complete, factually grounded, tailored to the transaction, and ready for review by the authorizing notary. This skill does not replace the notary's personal duties of identification, capacity assessment, legal counseling, impartiality, authorization, protocol custody, registry/tax compliance, or professional judgment.

## Governing-source hierarchy
Before stating that a clause, warning, formality, tax step, registry requirement, or legal consequence is mandatory, verify the current authority. Apply, as relevant:

1. Ley Notarial de Puerto Rico, as amended.
2. Reglamento Notarial de Puerto Rico and current rules/orders of the Tribunal Supremo and ODIN.
3. Código Civil de Puerto Rico de 2020 and applicable special statutes.
4. Ley del Registro de la Propiedad Inmobiliaria del Estado Libre Asociado de Puerto Rico and current registry rules when real property is involved.
5. Puerto Rico tax statutes, Hacienda guidance, CRIM requirements, and applicable municipal/federal law when the transaction requires them.
6. Reglas de Conducta Profesional de Puerto Rico, particularly provisions governing the notarial function, confidentiality, competence, conflicts, impartiality, technological competence, and withdrawal/refusal.
7. Binding Puerto Rico Supreme Court precedent.

Never treat an old model deed or prior instrument as proof that a legal citation, warning, tax rule, registry practice, or statutory requirement remains current.

## Source discipline
- Use supplied prior instruments as **style and issue-spotting references**, not as controlling law.
- Preserve useful Puerto Rico notarial conventions found in the user's models — e.g. instrument number/title, place/date, `ANTE MÍ`, `COMPARECE(N)`, `DOY FE`, `EXPONE(N)`, transaction-specific clauses, `ADVERTENCIAS`, `ACEPTACIÓN`, `OTORGAMIENTO Y LECTURA`, authorization and copy-certification language — only when appropriate to the specific instrument.
- Correct obvious inconsistencies, duplicated numbering, obsolete citations, contradictory clauses, gender/party-label errors, registry mismatches, or legally unsupported boilerplate rather than reproducing them blindly.
- If a supplied model conflicts with current law, current law controls and the discrepancy must be flagged.

## First decision: escritura or acta
Determine the proper notarial vehicle before drafting.

### Escritura pública
Use an escritura when the instrument contains a juridical act, declaration of will, contract, conveyance, acceptance, renunciation, power, constitution/modification/extinction of a right, or another transaction that by law or the parties' intention is formalized in a public deed.

### Acta notarial
Use an acta when the notary is primarily recording facts, circumstances, manifestations, notifications, presence, notoriety, protocolization, or other matters for which the notary gives faith without structuring the document as a bilateral or dispositive juridical transaction, subject to the governing law for the particular act.

If classification is uncertain, do not guess. Explain the issue and identify the legal authority that must be verified before authorization.

## Intake checklist
Obtain or mark as missing the following, to the extent relevant:

### A. Instrument and notary
- type and purpose of instrument;
- protocol instrument number;
- place and exact date of authorization;
- notary's name, status, residence and office information required by current law;
- whether witnesses, interpreters, representatives, corporate officers, fiduciaries, guardians, attorneys-in-fact, or other special participants are involved.

### B. Parties / requirentes
For every person or entity:
- exact legal name and aliases if legally relevant;
- legal age or majority status;
- marital status and matrimonial-property regime when material;
- occupation/profession when required or customarily stated;
- residence/vecindad and jurisdiction;
- capacity in which appearing;
- party label that remains consistent throughout the instrument;
- method of identification actually used by the notary;
- representative authority and documentary source, if applicable;
- capacity/competence facts that the notary must personally assess.

Never invent a driver's-license number, Social Security number, tax ID, RUA number, registry credential, power-of-attorney data, corporate resolution, judicial order, or identity fact.

### C. Transaction facts
- source of title/right or factual basis;
- consideration, value, price, donation value, or no-consideration basis as applicable;
- conditions, terms, reservations, limitations, substitution, revocation, termination, possession, delivery, allocation of expenses, and effective date;
- required acceptances or consents;
- substantive-law elements for the specific juridical act.

### D. Real property, when involved
Require or flag:
- exact registry description;
- finca number and registry section/demarcation;
- inscription/title-source data;
- cadastral number if applicable;
- ownership interests/percentages;
- current charges, liens, mortgages, easements, annotations, conditions, and other encumbrances;
- title-study/certification information and date/source;
- CRIM status and tax matters;
- flood-zone, condominium, horizontal-property, restrictive-covenant, inheritance, community-property, homestead, or other special-law issues when relevant;
- who will present the instrument for registration and any required post-closing steps.

Do not silently reconcile a discrepancy between the registry description, cadastral number, title study, deed of acquisition, party ownership percentage, or encumbrance data. Stop and flag it.

## Drafting algorithm

1. **Identify the juridical act.** State exactly what is being created, transferred, accepted, renounced, authorized, declared, or recorded.
2. **Verify current law.** Identify transaction-specific formalities, capacity rules, indispensable consents, prohibitions, warnings, tax filings, registry consequences, and post-authorization duties.
3. **Validate the parties.** Check names, capacities, marital regimes, representative authority, and internal consistency.
4. **Build a transaction map.** For each legal element, identify the supporting fact or document. If an element lacks support, mark `[FALTA INFORMACIÓN]` rather than inventing it.
5. **Choose escritura vs. acta** and structure the document accordingly.
6. **Draft the opening formalities.** Instrument number/title, place/date, `ANTE MÍ`, notary identification, `COMPARECE(N)`, identification/circumstances, capacity and voluntariness language appropriate to the facts.
7. **Draft the expository section.** State title, background, ownership, registry data, succession facts, corporate authority, family relationship, prior instruments, or other facts needed to understand the transaction.
8. **Draft the dispositive or request section.** Put the legal act itself in clear operative language. Separate material covenants and conditions into numbered clauses.
9. **Draft transaction-specific warnings.** Include only warnings supported by current law and the facts. Do not dump generic boilerplate unrelated to the transaction.
10. **Address registry/tax consequences.** State only verified requirements concerning presentation, recording, CRIM, Hacienda, inheritance/donation tax, stamps/fees, permits, certifications, or other filing obligations.
11. **Draft acceptance/consent.** Include explicit acceptance where the juridical act requires or calls for it.
12. **Draft execution and authorization.** Include the applicable reading, ratification, initials/signatures, witness/interpreter facts, and notarial faith language required for the particular instrument and circumstances.
13. **Copy certification / post-authorization block.** Include a placeholder or draft only if requested and only in a form consistent with current notarial requirements and the actual facts of issuance.
14. **Run a notarial audit.** Check numbering, dates, names, party labels, percentages, property descriptions, money figures, citations, attachments, cross-references, signature lines, warnings, and post-authorization steps.

## Transaction modules
Apply the relevant module in addition to the general algorithm.

### Donación
Check at minimum:
- donor ownership and power to dispose;
- donee identity and acceptance requirements;
- whether the donation is inter vivos or otherwise specially characterized;
- value and description of donated property;
- reservations, conditions, prohibitions on alienation, reversion/revocation provisions, usufruct or other retained rights;
- forced-heirship/legítima issues and substantive limits under current succession law;
- tax reporting and any Hacienda requirements in force on the authorization date;
- registry and CRIM consequences for real property.

Do not reuse an old donation-warning clause without verifying that the cited tax deadlines, exclusions, Civil Code articles, and CRIM statutes remain current.

### Compraventa / option / promise
Check at minimum:
- exact property or interest being sold/optioned;
- ownership percentage;
- price or objectively determinable price mechanism;
- option consideration, if any, and legal effect;
- term and method of exercise;
- financing contingencies;
- allocation of taxes, utilities, closing costs, possession and risk;
- encumbrances to remain or be cancelled;
- registry eligibility and any recordable conditions;
- consistency among all deadlines and clauses.

### Poder / poder duradero
Check at minimum:
- current statutory basis and effect of durability;
- identity of principal(s), agent(s), successor agent(s), and activation/effectiveness terms;
- precise authority granted rather than relying only on generic catch-all language;
- special authority for transactions that require express authorization;
- self-dealing, gifts, trusts, beneficiary changes, litigation, banking, real estate, health-information access, digital assets, tax matters, and delegation/substitution as applicable;
- limitations protecting principal residence or other protected assets;
- termination/revocation and incapacity consequences.

### Repudiación de herencia
Check at minimum:
- identity of decedent and date/place of death;
- basis on which the appearing person is called to inherit;
- whether succession is testate/intestate and any relevant declaration/testament facts;
- current Civil Code formalities for repudiation;
- capacity and representative restrictions;
- indivisibility, conditions, timing/effect, creditor consequences, and irrevocability only as current law actually provides;
- whether any prior conduct may constitute acceptance or otherwise affect the ability to repudiate.

### Hogar seguro
Check at minimum:
- statutory eligibility;
- ownership and principal-residence facts;
- no conflicting homestead designation;
- exact property and registry data;
- current exceptions and effects;
- registry annotation/presentation requirements;
- spouse/family/succession consequences under current law.

## Special notarial safeguards

### Identification
Draft only what the notary actually knows or has verified. Distinguish personal knowledge from identification by legally permissible documentary or witness methods. Never state `DOY FE` of a fact the notary has not personally established as required by law.

### Capacity and voluntariness
The text may state the notary's assessment, but the skill cannot perform that assessment. If capacity, coercion, undue influence, language comprehension, disability accommodations, intoxication, cognitive decline, or voluntariness is in question, flag it for the notary and do not paper over it with boilerplate.

### Impartial notarial advice
When the notary acts in a notarial capacity, draft warnings and explanations neutrally. Do not turn the instrument into advocacy for one appearing party against another where impartiality is required.

### Confidentiality and sensitive data
Do not place confidential or personally identifying information in the draft unless legally necessary. Use placeholders for sensitive identifiers when a redacted working draft is sufficient.

### Real-property title
Never infer that title is clean from silence. If the current registry status is not verified, state `[VERIFICAR ESTADO REGISTRAL Y CARGAS]`.

### Citations
Do not invent statute/article/LPRA citations. When a legal warning is included, cite the verified current source if available. If verification is unavailable, use `[VERIFICAR BASE LEGAL VIGENTE]` rather than an old citation from a model.

## Output modes

### Mode A — Finished draft
When the user asks to redact or prepare the instrument, produce the full instrument in Puerto Rico notarial style, using placeholders only where facts or verified law are missing.

Recommended skeleton:

```text
ESCRITURA/ACTA NÚMERO [___]
[TÍTULO DEL INSTRUMENTO]

En [municipio], Puerto Rico, a [fecha].

ANTE MÍ

[identificación del/de la notario(a)]

COMPARECE(N)

[comparecientes y circunstancias]

DOY FE

[identificación, capacidad, representación y voluntariedad según proceda]

EXPONE(N) / REQUIERE(N)

PRIMERO: ...
SEGUNDO: ...

[CLÁUSULAS DISPOSITIVAS / TÉRMINOS Y CONDICIONES]

[ADVERTENCIAS]

[ACEPTACIÓN / RATIFICACIÓN, si procede]

OTORGAMIENTO, LECTURA Y AUTORIZACIÓN

[texto aplicable]

[FIRMAS]

[CERTIFICACIÓN DE COPIA, si procede y si fue solicitada]
```

### Mode B — Intake before drafting
If essential facts are missing, return a compact checklist grouped by: parties, authority/capacity, transaction, property/registry, tax, warnings, and execution. Do not ask for immaterial details merely because they appeared in a prior model.

### Mode C — Review/redline audit
When reviewing an existing draft, report:
- **fatal/authorization blockers**;
- **substantive-law issues**;
- **notarial-formality issues**;
- **registry/tax/post-authorization issues**;
- **internal inconsistencies/typos**;
- **recommended replacement language**.

## Quality-control checklist
Before finalizing, verify:
- [ ] Correct classification as escritura or acta.
- [ ] Instrument number, title, place and date are consistent.
- [ ] Every party's exact name and role is consistent throughout.
- [ ] Identity method and capacity language match actual facts.
- [ ] Representative authority is identified and verified where applicable.
- [ ] All operative elements of the juridical act are present.
- [ ] All required acceptances/consents are explicit.
- [ ] Property description and registry data are internally consistent.
- [ ] Ownership percentages total correctly.
- [ ] Price/value/consideration and payment terms are coherent.
- [ ] Conditions and deadlines do not contradict one another.
- [ ] Charges/encumbrances are stated from verified information.
- [ ] Transaction-specific warnings are current and fact-specific.
- [ ] Tax/CRIM/registry requirements are verified for the authorization date.
- [ ] Citations are current and not copied blindly from prior forms.
- [ ] Paragraph numbering and cross-references are correct.
- [ ] Reading, ratification, signatures, initials, witnesses/interpreters and authorization language match the actual execution method.
- [ ] No unsupported `DOY FE` statement appears.
- [ ] Post-authorization/presentation/copy steps are identified.

## Hard guardrails
- Never invent facts to make an instrument appear complete.
- Never fabricate a legal citation, registry entry, title-study result, certification, tax status, ID method, signature, witness, notarization, seal, or copy issuance.
- Never state that an instrument is ready to authorize when a required fact, consent, capacity determination, legal formality, registry fact, or current-law requirement remains unresolved.
- Never copy old boilerplate merely because it appears in a supplied model.
- Never impersonate the notary or state that the model itself personally identified a person, witnessed a signature, administered an oath, or authorized the instrument.
- The authorizing Puerto Rico notary must independently review the final instrument and perform all nondelegable notarial duties.

Close with the mandatory disclaimer from `pr/CLAUDE.md`.
