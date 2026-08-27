---
name: pr-administrative-hearing
title: Puerto Rico Administrative Hearing Preparation
description: Prepara integralmente una vista administrativa en Puerto Rico desde el informe de conferencia y el expediente: teoría del caso, estipulaciones, testigos, exhibits, directo, contra, objeciones, ofertas de prueba y lagunas. Use para CASP/CASARH y otros foros administrativos, sujeto al reglamento particular aplicable.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: administrative
language: es
---

# Preparación integral de vista administrativa

## Alcance
Este skill cubre la **vista adjudicativa interna**. Para revisión judicial de una resolución final, usar `pr-agency-appeal-lpau`.

## Regla preliminar
Identificar primero el foro, estatuto habilitador, reglamento procesal vigente, órdenes particulares del caso y qué reglas probatorias aplica el adjudicador. No asumir uniformidad entre agencias.

## Workflow
1. **Postura procesal:** foro, número de caso, partes, materia, órdenes vigentes, asuntos pendientes y remedio.
2. **Informe de conferencia:** extraer controversias, estipulaciones, testigos, resumen de testimonio, exhibits, objeciones anunciadas y reservas.
3. **Teoría del caso:** una proposición central y 3-5 hechos que deben probarse.
4. **Burden map:** identificar qué parte debe establecer cada elemento según la fuente jurídica aplicable; si no consta, marcar `[VERIFICAR CARGA]`.
5. **Record map:** invocar metodología de `pr-record-analysis`.
6. **Witness map:** para cada testigo, propósito, conocimiento personal, hechos únicos, documentos y vulnerabilidades.
7. **Exhibit map:** número, descripción, propósito, autenticación, pertinencia, objeción prevista, estado (anunciado/estipulado/admitido/controvertido).
8. **Directos:** usar metodología de `pr-direct-examination`.
9. **Contras e impeachment:** localizar admisiones, contradicciones, omisiones y límites de conocimiento; usar `pr-impeachment`.
10. **Objeciones:** preparar tabla anticipada mediante `pr-evidentiary-objections`.
11. **Lagunas:** enumerar todo hecho material todavía no probado y cómo intentar cubrirlo.
12. **Vista:** crear orden de presentación y checklist operativo.

## Trial notebook / carpeta de vista
### A. Teoría y controversias
| Controversia | Nuestra posición | Prueba | Testigo | Riesgo |
|---|---|---|---|---|

### B. Estipulaciones
[Lista exacta]

### C. Testigos
Para cada testigo:
- objetivo;
- hechos que debe establecer;
- foundation/conocimiento;
- exhibits;
- directo o contra;
- impeachment disponible;
- objeciones previsibles.

### D. Exhibits
| Exh. | Documento | Fecha | Propósito | Foundation | Estado | Objeción |
|---|---|---|---|---|---|---|

### E. Orden de prueba
[Secuencia recomendada con razón estratégica]

### F. Objeciones rápidas
[Tabla de cuestión → objeción → respuesta]

### G. Lagunas y asuntos para proffer
[Lista]

### H. Cierre probatorio
Mapa de cada hecho que quedó probado/no probado y fuente en el récord.

## Reglas prácticas derivadas de expedientes de vista
- No gastar directo en estipulaciones salvo contexto indispensable.
- Preguntar concretamente; el documento no sustituye la pregunta al testigo.
- Diferenciar autenticación del documento, admisión del exhibit y conocimiento personal del testigo.
- Preparar pertinencia antes de introducir documentos temporalmente alejados de los hechos controvertidos.
- Cuando una parte anuncie un testigo comparador, separar lo que el testigo actual sabe personalmente de lo que deberá probar el comparador.
- Una alegación contenida en la apelación/recurso no se convierte en hecho probado por estar en el récord.

## Guardrails
- No inventar estipulaciones, exhibits ni decisiones sobre admisibilidad.
- No asumir que evidencia anunciada fue admitida.
- Marcar claramente asuntos pendientes y órdenes incumplidas sin tratarlos como adjudicados.
- Preservar fechas y versiones del expediente; en controversias de clasificación, distinguir funciones históricas de funciones posteriores.
