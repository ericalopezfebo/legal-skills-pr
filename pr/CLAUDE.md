# Cross-cutting context: the Puerto Rico legal system

Orchestrator cold-start for any plugin under `pr/`. Loaded before the plugin-specific `CLAUDE.md` or `SKILL.md`.

## Legal family

Hybrid system. Private law (obligations, contracts, property, family, succession) descends from the Spanish civil-law tradition; criminal and constitutional procedure, and the federal overlay, follow U.S. common-law practice. Puerto Rico has been a U.S. territory since 1898; the Constitution of the Commonwealth of Puerto Rico (1952) operates alongside the U.S. Constitution, and U.S. federal law and the First Circuit's jurisprudence bind on matters within federal jurisdiction.

## Sources of law (by priority)

1. U.S. Constitution and applicable federal statutes/treaties (federal-question and diversity matters; federal agencies).
2. Constitución del Estado Libre Asociado de Puerto Rico (1952).
3. Statutes enacted by the Asamblea Legislativa, codified in **Leyes de Puerto Rico Anotadas (LPRA)**.
4. Agency regulations (reglamentos), filed with the Departamento de Estado.
5. Case law (jurisprudencia) of the **Tribunal Supremo de Puerto Rico** — binding; opinions of the **Tribunal de Apelaciones** are persuasive/intermediate authority. First Circuit and U.S. District Court for the District of Puerto Rico decisions bind on federal-law questions.

## Core codes

- **Código Civil de Puerto Rico**, Ley Núm. 55-2020 (31 LPRA) — replaced the 1930 Civil Code; governs obligations, contracts, property, family, and succession.
- **Reglas de Procedimiento Civil de 2009**, según enmendadas (32 LPRA Ap. V).
- **Reglas de Evidencia de 2009**, según enmendadas (32 LPRA Ap. VI).
- **Código Penal de Puerto Rico**, Ley Núm. 146-2012 (33 LPRA).
- **Ley de Procedimiento Administrativo Uniforme (LPAU)**, Ley Núm. 38-2017 (3 LPRA § 9601 et seq.).
- **Cánones de Ética Profesional**, 4 LPRA Ap. IX (regulate the practice of law; enforced by the Tribunal Supremo through the Oficina de Inspección de Notarías and disciplinary proceedings).

## Language

Spanish is the working language of the Commonwealth courts and most agencies. The U.S. District Court for the District of Puerto Rico and other federal fora operate in English. Confirm which forum governs before drafting.

## Citation discipline (mandatory for every plugin under `pr/`)

- Statutes: cite both the popular name/session-law number and the current LPRA codification where known — e.g., "Art. 1064, Código Civil de PR, Ley Núm. 55-2020, 31 LPRA § [sección]". LPRA sections get renumbered on recodification; **do not assume an old Civil Code (31 LPRA, pre-2020) citation still applies** — confirm which code version governs the facts.
- Tribunal Supremo opinions: "*[Parte] v. [Parte]*, [volumen] DPR [página] ([año])".
- Tribunal de Apelaciones: cite by KLAN/KLRA/KLCE docket number and decision date; these are frequently unpublished/persuasive only — say so.
- **Never invent** a section number, case name, docket number, or page citation. If you cannot verify it from context or a cited source, say so explicitly and prompt the user to confirm against LexJuris, Microjuris, or the official Rama Judicial site before filing or relying on it.

## Working with current law

Puerto Rico statutes and rules are amended frequently, and several major codes were recently replaced (Civil Code in 2020; LPAU in 2017). A skill that depends on a specific article or rule must state the assumed version/date and warn the user to confirm it is still current.

## Mandatory disclaimer in output

> Este contenido es informativo únicamente y no constituye asesoramiento legal. Verifique la ley, regla o reglamento vigente, y las reglas particulares del tribunal o agencia correspondiente, antes de utilizarlo. Un abogado admitido a la práctica en Puerto Rico debe revisar cualquier documento antes de presentarlo o enviarlo.
