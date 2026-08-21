# Legal Skills — Puerto Rico

> **Biblioteca de código abierto de skills jurídicos de IA para la práctica del Derecho en Puerto Rico**, en formato Anthropic Skills (`SKILL.md`), utilizable por Claude Code, Claude Cowork y otros clientes compatibles con skills o MCP. Incluye verificación de citas, investigación jurídica, redacción de memorandos, mociones de sentencia sumaria bajo la Regla 36, recursos administrativos bajo la LPAU, revisión y redacción contractual conforme al Código Civil de 2020, litigación civil, responsabilidad profesional y práctica notarial. Licencia MIT y abierta a contribuciones.

[![Licencia: MIT](https://img.shields.io/badge/licencia-MIT-yellow.svg)](LICENSE)
![Jurisdicción](https://img.shields.io/badge/jurisdicci%C3%B3n-Puerto%20Rico-005BBB)
![Formato: Anthropic Skills](https://img.shields.io/badge/formato-Anthropic_Skills-orange)
![Idioma](https://img.shields.io/badge/idioma-espa%C3%B1ol-blue)

---

## Tabla de contenido

- [Qué es este repositorio](#qué-es-este-repositorio)
- [Cómo luce un skill](#cómo-luce-un-skill)
- [Skills disponibles](#skills-disponibles)
- [Cómo utilizar estos skills](#cómo-utilizar-estos-skills)
- [Por qué Puerto Rico necesita su propio conjunto](#por-qué-puerto-rico-necesita-su-propio-conjunto)
- [Cómo contribuir](#cómo-contribuir)
- [Descargo de responsabilidad](#descargo-de-responsabilidad)
- [Licencia](#licencia)
- [Proyectos relacionados](#proyectos-relacionados)

---

## Qué es este repositorio

Un **skill jurídico de IA** es un archivo Markdown (`SKILL.md`) que describe una tarea jurídica aplicada —por ejemplo: *«revisa esta cita conforme a LPRA»*, *«prepara una moción de sentencia sumaria bajo la Regla 36»* o *«¿existe un conflicto de interés aquí?»*— mediante instrucciones estructuradas que un agente de IA puede seguir de manera consistente: cuándo debe activarse, qué pasos debe realizar y qué debe contener el producto final.

Cada skill se encuentra bajo:

```text
pr/{area-de-practica}/skills/{slug}/SKILL.md
```

y está diseñado a partir de fuentes y prácticas propias de Puerto Rico: estatutos codificados en LPRA, jurisprudencia del Tribunal Supremo y del Tribunal de Apelaciones, reglas procesales, la LPAU, el Código Civil de 2020, las Reglas de Conducta Profesional vigentes y las normas notariales aplicables. La finalidad es evitar plantillas genéricas de Estados Unidos o España que no reflejan correctamente el Derecho puertorriqueño.

## Cómo luce un skill

```yaml
---
name: pr-summary-judgment-motion
title: Redacción de Moción de Sentencia Sumaria en Puerto Rico (Regla 36)
description: Estructura una moción de sentencia sumaria o su oposición bajo la Regla 36 de Procedimiento Civil de Puerto Rico, incluyendo la relación numerada de hechos materiales incontrovertidos exigida por la práctica puertorriqueña.
license: MIT
jurisdiction: pr
practice: litigation
language: es
---

# Título del skill

## Cuándo aplicar
Disparadores, ejemplos de solicitudes y asuntos fuera de alcance.

## Algoritmo
Instrucciones paso a paso para el agente.

## Contrato de salida
Qué debe contener la respuesta: formato, citas requeridas y el descargo de responsabilidad obligatorio.
```

Consulte [`pr/CLAUDE.md`](pr/CLAUDE.md) para las reglas generales aplicables a todos los skills de Puerto Rico: jerarquía de fuentes, disciplina de citas, idioma de trabajo y descargo de responsabilidad obligatorio.

## Skills disponibles

El repositorio incluye skills para investigación, litigación, apelaciones, asuntos administrativos, contratos, responsabilidad profesional y práctica notarial. El catálogo completo y actualizado se encuentra en [`pr/README.md`](pr/README.md).

| Área de práctica | Ejemplos de skills |
|---|---|
| General | `pr-legal-citation` · `pr-legal-research` · `pr-legal-memo-drafting` · `pr-citation-verifier` · `pr-filing-readiness` · `pr-legal-document-sanitization` · `pr-prescription-analysis` |
| Litigación | `pr-summary-judgment-motion` · `pr-motion-drafting` · `pr-pretrial-report-drafting` · `pr-complaint-drafting` · `pr-answer-drafting` · `pr-motion-dismiss` · `pr-reconsideration-motion` · `pr-civil-deadlines` · `pr-discovery-drafting` · `pr-discovery-response` |
| Apelaciones | `pr-appellate-drafting` |
| Administrativo | `pr-agency-appeal-lpau` |
| Contratos | `pr-contract-review` · `pr-contract-drafting` |
| Laboral y empleo | `pr-worker-classification` · `pr-employment-agreement` · `pr-severance-agreement` · `pr-employee-handbook` |
| Privacidad y ciberseguridad | `pr-data-breach-response` · `pr-incident-response-plan` · `pr-privacy-law-applicability` · `pr-data-retention-policy` |
| Contratación gubernamental | `pr-government-contract-compliance` |
| Propiedad intelectual | `pr-dmca-takedown-analysis` |
| Notarial | `pr-notarial-instrument-drafting` |
| Responsabilidad profesional | `pr-ethics-conflict-check` · `pr-engagement-letter` |

Este proyecto continuará ampliándose con nuevas áreas de práctica puertorriqueña, incluyendo familia, penal, bienes raíces, laboral y empleo, contribuciones y otros campos especializados.

## Cómo utilizar estos skills

Clone el repositorio y dirija Claude Code u otro cliente compatible con skills a la carpeta `pr/`. También puede copiar únicamente la carpeta del skill que desee utilizar.

```bash
git clone https://github.com/ericalopezfebo/legal-skills-pr.git
```

No se requiere servidor ni proceso de compilación: los skills son archivos Markdown.

## Por qué Puerto Rico necesita su propio conjunto

Puerto Rico tiene un ordenamiento jurídico híbrido. El Derecho privado se desarrolla sobre una tradición civilista, hoy articulada en buena medida mediante el Código Civil de 2020, mientras que el Derecho constitucional, federal y diversas áreas procesales se relacionan con el sistema jurídico estadounidense. La práctica cotidiana ocurre mayormente en español ante tribunales y agencias propias, con reglas, términos, organismos y métodos de citación particulares.

Por ello, un skill jurídico genérico para «Estados Unidos» o «España» puede equivocarse en la norma aplicable, el estándar de revisión, la estructura procesal, la cita o incluso el código vigente. Este repositorio pretende ofrecer una base abierta y específicamente puertorriqueña para esas tareas.

## Cómo contribuir

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md). En términos generales:

1. haga un fork del repositorio;
2. añada un nuevo skill bajo `pr/{area-de-practica}/skills/{slug}/SKILL.md`;
3. abra un pull request.

No incluya información confidencial ni contenido identificable de clientes, jueces o casos pendientes. Los skills deben ser de uso general.

## Descargo de responsabilidad

Los skills y sus productos son herramientas de apoyo. No sustituyen el juicio profesional ni la revisión de un abogado admitido a la práctica en Puerto Rico. Todo documento, análisis, cita o conclusión debe cotejarse con la ley y las reglas vigentes antes de utilizarse, presentarse o enviarse.

Consulte el texto completo del descargo y las reglas de citación en [`pr/CLAUDE.md`](pr/CLAUDE.md).

## Licencia

[MIT](LICENSE). Puede utilizar, modificar y distribuir el contenido, incluso con fines comerciales, sujeto a los términos de la licencia.

## Proyectos relacionados

- [Anthropic Skills](https://www.anthropic.com/news/skills) — formato subyacente de archivos `SKILL.md`.
- [`legal-skills-open`](https://github.com/ThomasMoreAI/legal-skills-open) — biblioteca multijurisdiccional que sirvió de referencia estructural.
- [`zubair-trabzada/ai-legal-claude`](https://github.com/zubair-trabzada/ai-legal-claude) y [`joe-shenouda/awesome-cyber-skills`](https://github.com/joe-shenouda/awesome-cyber-skills) — referencias de organización para catálogos especializados de skills.

---

*Proyecto iniciado por [@ericalopezfebo](https://github.com/ericalopezfebo). Se aceptan issues y pull requests.*
