---
name: pr-pretrial-report-drafting
title: Informe de Conferencia con Antelación al Juicio o Vista
description: Prepara informes conjuntos o separados para conferencias con antelación al juicio, conferencias preliminares entre abogados y vistas en Puerto Rico a partir de posiciones, estipulaciones, testigos, exhibits, objeciones y órdenes suministradas.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Informe previo a juicio o vista

## Cuándo aplicar

Usar para preparar o revisar:
- informe de conferencia con antelación al juicio;
- informe preliminar entre abogados y abogadas;
- informe conjunto o separado previo a vista;
- plan de juicio o vista exigido por orden.

No asumir que todos estos documentos tienen idénticos requisitos. La orden del caso, la regla vigente y el formulario del foro controlan.

## Algoritmo

1. Identificar foro, orden de calendarización, tipo y fecha de conferencia o vista, término, partes responsables y carácter conjunto o separado.
2. Recuperar y verificar la regla procesal, la orden particular y cualquier formulario vigente. No calcular términos con datos incompletos.
3. Solicitar por cada parte: teoría del caso, reclamaciones y defensas vivas, remedios, estipulaciones propuestas, hechos controvertidos, testigos, peritos, documentos, objeciones, mociones pendientes y duración estimada.
4. Conciliar las aportaciones sin presentar como acuerdo una posición unilateral. Etiquetar claramente `ESTIPULADO`, `POSICIÓN DE [PARTE]`, `OBJETADO` y `PENDIENTE`.
5. Organizar el informe según la orden. En ausencia de una secuencia obligatoria, usar:
   1. epígrafe y título;
   2. comparecencia y cumplimiento;
   3. naturaleza del caso;
   4. reclamaciones y defensas pendientes;
   5. estipulaciones;
   6. controversias de hecho y derecho;
   7. prueba testifical, pericial y documental;
   8. objeciones;
   9. mociones o asuntos pendientes;
   10. remedios y cuantificación;
   11. posibilidad de transacción;
   12. logística, duración, certificaciones y firmas.
6. Para cada testigo, indicar rol, tema limitado y necesidad sin inventar testimonio.
7. Para cada exhibit, asignar identificador estable, descripción neutral, parte proponente, método de autenticación, objeción y estado.
8. Distinguir prueba anunciada, producida, estipulada, objetada y excluida. Detectar conflictos con descubrimiento, listas anteriores u órdenes.
9. Formular controversias jurídicas como preguntas concretas vinculadas con una decisión o prueba; no convertir el informe en un tratado.
10. Usar tablas solo para listas repetibles de testigos, exhibits, estipulaciones o pendientes. Usar prosa para teoría, controversias y remedios.
11. Mantener tono cooperativo y preciso en secciones conjuntas, y firme pero neutral al describir desacuerdos.
12. Auditar contra alegaciones, contestaciones, descubrimiento, órdenes, mociones y prueba disponible. Marcar todo vacío o conflicto.

## Privacidad

Aplicar `pr-legal-document-sanitization` antes de usar informes anteriores como referencia. No copiar identidades, direcciones, contactos, números de caso, firmas, hechos, comentarios ni metadatos de otro asunto.

## Contrato de salida

Entregar:
1. borrador editable completo;
2. matriz de testigos y exhibits cuando proceda;
3. lista separada de información faltante y desacuerdos sin conciliar;
4. autoridades y términos pendientes de verificación;
5. estado `REVISIÓN DE ABOGADO REQUERIDA`.

Cumplir con `pr/CLAUDE.md` y añadir su descargo obligatorio.
