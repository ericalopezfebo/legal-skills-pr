---
name: pr-record-analysis
title: Puerto Rico Administrative Record Analysis
description: Analiza expedientes administrativos de Puerto Rico para construir cronologías, matrices de prueba, lagunas probatorias, inconsistencias y vínculos entre alegaciones, testigos, documentos y declaraciones. Use antes de vista, contrainterrogatorio, mociones o revisión judicial.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: administrative
language: es
---

# Análisis del récord administrativo

## Objetivo
Convertir un expediente voluminoso en un mapa probatorio verificable sin llenar silenciosamente los vacíos del récord.

## Modelo central
`ALEGACIÓN → HECHO MATERIAL → FUENTE → PERSONA CON CONOCIMIENTO → DECLARACIÓN PREVIA → DOCUMENTO → TESTIMONIO → CONSISTENCIA/LAGUNA`

## Algoritmo
1. Inventariar escritos, órdenes, interrogatorios, admisiones, declaraciones, transcripciones, exhibits y estipulaciones.
2. Identificar las controversias de hecho y derecho y el remedio solicitado.
3. Crear cronología con fecha del evento, fecha del documento y fuente. No confundir ambas.
4. Para cada alegación material localizar todas las fuentes que la apoyan, contradicen o no la contestan.
5. Identificar quién posee conocimiento personal y la base de ese conocimiento.
6. Comparar declaraciones del mismo declarante a través del tiempo.
7. Comparar descripciones de funciones, puestos, deberes, fechas y cadena de mando entre documentos.
8. Marcar expresamente `NO CONTESTADO POR EL RÉCORD` cuando ninguna fuente resuelva una pregunta material.
9. Separar contradicción verdadera de: diferencia de detalle, cambio temporal explicable, ambigüedad, documento de distinta fecha o inferencia.
10. Producir líneas de investigación, directo, contra y objeciones derivadas de cada hallazgo.

## Salidas
### Cronología maestra
| Fecha | Evento | Fuente | Persona | Importancia | Disputa |
|---|---|---|---|---|---|

### Matriz de alegaciones y prueba
| Alegación | A favor | En contra | Testigo | Documento | Estado |
|---|---|---|---|---|---|

Estados permitidos: `corroborada`, `controvertida`, `parcialmente corroborada`, `no contestada`, `solo alegada`, `requiere autenticación`.

### Matriz de funciones cuando exista controversia de clasificación
| Función | Documento/fecha A | Documento/fecha B | Comparador | ¿Cuándo comenzó? | Quién la asignó | Hallazgo |
|---|---|---|---|---|---|---|

### Lagunas críticas
Para cada laguna: pregunta exacta que el récord no contesta + documento/testigo que podría contestarla.

## Guardrails
- Nunca convertir ausencia de prueba en prueba de ausencia.
- No afirmar una fecha de comienzo de una función porque aparece por primera vez en un documento posterior.
- No tratar como inconsistencia dos descripciones correspondientes a periodos distintos sin analizar el cambio temporal.
- Mantener cita o referencia exacta a la fuente para cada hallazgo.
