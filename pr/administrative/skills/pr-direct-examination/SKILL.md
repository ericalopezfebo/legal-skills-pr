---
name: pr-direct-examination
title: Puerto Rico Administrative Direct Examination
description: Diseña el examen directo de testigos en vistas administrativas de Puerto Rico a partir del expediente, estipulaciones, controversias, documentos y conocimiento personal del testigo. Use para preparar preguntas de directo, organizar testimonio o autenticar documentos durante una vista administrativa.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: administrative
language: es
---

# Examen directo en vista administrativa de Puerto Rico

## Objetivo
Construir un directo útil para adjudicación: breve, cronológico, conectado con las controversias y sustentado por conocimiento personal y el récord. No usar el testimonio como sustituto de prueba documental ni atribuir al testigo conocimiento que el expediente no demuestre.

## Principios derivados de materiales de práctica
- Comenzar con identidad, puesto, experiencia y base de conocimiento.
- Usar las estipulaciones para evitar probar nuevamente hechos admitidos.
- Concentrar el directo en las controversias pendientes.
- Para cada hecho material identificar: qué sabe el testigo, cómo lo sabe, cuándo ocurrió y qué documento lo corrobora.
- Si se utilizará un documento, separar: identificación/autenticación, conocimiento personal, pertinencia y contenido.
- Que un documento esté admitido o estipulado no establece por sí solo que el testigo pueda interpretar hechos fuera de su conocimiento personal.
- Si surge una objeción, identificar qué fundamento falta antes de continuar.

## Algoritmo
1. Extraer controversias, estipulaciones y remedio solicitado.
2. Crear matriz HECHO → ELEMENTO/CONTROVERSIA → TESTIGO → BASE DE CONOCIMIENTO → DOCUMENTO → RIESGO DE OBJECIÓN.
3. Eliminar preguntas sobre hechos ya estipulados salvo transición necesaria.
4. Dividir el directo en módulos: acreditación; contexto; cronología; hechos materiales; documentos; daños/remedio cuando proceda; cierre.
5. Para documentos preparar foundation antes de entrar al contenido cuando sea necesario.
6. Señalar cualquier hecho importante que dependa de inferencia, referencia de terceros o documento no autenticado.
7. Preparar posibles preguntas de rehabilitación sobre puntos previsiblemente atacables en contrainterrogatorio, sin ensayar respuestas falsas.

## Formato de salida
### Teoría probatoria del testigo
[2-5 oraciones]

### Hechos que este testigo debe establecer
| Hecho | Base de conocimiento | Documento | Controversia | Riesgo |
|---|---|---|---|---|

### Guion de examen directo
**I. Identificación y experiencia**
1. ...

**II. Base de conocimiento**
...

**III. Hechos materiales en orden cronológico**
...

**IV. Documentos**
Para cada exhibit: propósito → foundation → pregunta material → posible objeción → respuesta/proffer.

### Puntos que NO deben preguntarse sin fundamento adicional
- ...

## Guardrails
- No inventar fechas, funciones, conversaciones, autores, custodios ni contenido documental.
- Distinguir expresamente hechos del récord, testimonio esperado e inferencias del abogado.
- No redactar preguntas sugestivas como método ordinario del directo salvo que el foro las permita o exista una razón procesal concreta.
- No pedir al testigo conclusiones jurídicas que corresponden al adjudicador.
- Cuando el récord no revele cuándo comenzó una función o quién la asignó, convertir la laguna en pregunta; no completarla por inferencia.
