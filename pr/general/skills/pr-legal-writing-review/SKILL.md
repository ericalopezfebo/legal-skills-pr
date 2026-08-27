---
name: pr-legal-writing-review
title: Revisión de Redacción Jurídica en Puerto Rico
description: Audita y mejora la estructura, claridad, concisión, coherencia, precisión, tono, organización, citas y fuerza persuasiva de escritos jurídicos de Puerto Rico. Puede operar en modo diagnóstico, edición o reescritura según lo solicite el abogado, sin alterar hechos ni autoridades no verificadas.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Revisión de Redacción Jurídica en Puerto Rico

## Propósito

Revisar escritos jurídicos para que comuniquen con claridad al lector jurídico sin sacrificar precisión. La revisión debe tratar la redacción como parte de la estrategia: cada oración debe tener una función, cada párrafo debe desarrollar una proposición y la estructura debe permitir al juzgador identificar rápidamente la controversia, la regla, la aplicación y el remedio.

## Modos

Identifique cuál solicita el usuario:

1. **Diagnóstico:** señalar problemas y prioridades sin reescribir sustancialmente.
2. **Edición:** corregir y simplificar conservando al máximo la voz del autor.
3. **Reescritura:** producir una versión mejorada cuando el usuario lo pida expresamente.
4. **Auditoría final:** revisar un escrito terminado antes de presentación; combinar con `pr-filing-readiness`.

No transformar automáticamente una solicitud de evaluación en una reescritura.

## Las tres C

Auditar siempre:

- **Claridad:** lenguaje sencillo, proposiciones identificables, oraciones comprensibles y términos definidos.
- **Concisión:** eliminar redundancias, muletillas, duplicación de hechos, frases ceremoniales innecesarias y detalles que no adelanten la cuestión.
- **Coherencia:** asegurar que oraciones, párrafos, secciones y remedio formen una secuencia lógica y que las transiciones expliquen por qué el punto siguiente importa.

## Algoritmo

1. **Identificar audiencia y propósito.** Tribunal, agencia, cliente, abogado contrario, memorando interno u otra audiencia. Determinar qué decisión o comprensión se busca provocar.
2. **Leer completo antes de editar.** Identificar tipo de escrito, teoría central, cuestiones, remedio y estructura existente.
3. **Construir el mapa del escrito.** Resumir en una línea la función de cada sección. Detectar secciones sin función, duplicadas o fuera de orden.
4. **Revisar arquitectura.** Verificar introducción, antecedentes, hechos, derecho, aplicación, conclusión y súplica según corresponda. Usar encabezados funcionales que adelanten la proposición, no rótulos vacíos.
5. **Revisar cada párrafo.** Una idea principal; primera oración orientadora cuando ayude; evidencia o autoridad pertinente; conexión explícita con la conclusión.
6. **Revisar cada oración.** Preferir voz activa cuando resulte natural, verbos concretos, sujeto identificable y oraciones razonablemente cortas. Dividir oraciones que contengan demasiadas proposiciones independientes.
7. **Eliminar ruido.** Quitar repeticiones, adjetivos argumentativos innecesarios, latinismos o tecnicismos evitables, frases de relleno y antecedentes sin valor para la decisión.
8. **Comprobar precisión.** No cambiar un hecho, fecha, posición procesal, cita, estándar jurídico o remedio para hacer la prosa más elegante. Marcar `[VERIFICAR]` cuando la fuente no esté disponible.
9. **Auditar citas.** La autoridad debe apoyar la proposición completa. Detectar citas incompletas, desactualizadas, mal atribuidas, sin pincite o apoyadas únicamente en fuente secundaria cuando haya fuente primaria disponible.
10. **Auditar tono.** Firme, profesional y proporcional. Evitar ataques personales, sarcasmo, exageraciones y afirmaciones de intención o mala fe sin apoyo.
11. **Auditar fluidez.** Verificar transiciones, secuencia temporal, términos definidos, consistencia de nombres y que el lector entienda por qué cada sección sigue a la anterior.
12. **Priorizar cambios.** Distinguir problemas materiales de estructura/análisis de problemas de estilo menores.

## Introducciones jurídicas

Cuando el género lo permita, la introducción debe permitir al lector identificar con rapidez:

- qué determinación, controversia o solicitud está ante el foro;
- por qué el promovente entiende que debe prevalecer; y
- qué remedio concreto solicita.

No convertir la introducción en una repetición extensa del historial procesal.

## Errores frecuentes a detectar

- pensamientos o párrafos sin conexión lógica;
- oraciones excesivamente largas;
- repetición de la misma conclusión con palabras distintas;
- exceso de voz pasiva;
- lenguaje innecesariamente complejo;
- hechos mezclados con argumentos o conclusiones jurídicas;
- citas que no sostienen la proposición;
- señales introductorias o referencias ambiguas;
- párrafos que empiezan sobre un tema y terminan sobre otro;
- encabezados que no ayudan a navegar el argumento;
- conclusión o súplica que solicita algo distinto de lo argumentado.

## Contrato de salida

En **modo diagnóstico**, entregar:

1. evaluación global en 3–5 oraciones;
2. problemas materiales en orden de prioridad;
3. observaciones por sección;
4. ejemplos específicos de claridad, concisión o coherencia;
5. tres cambios de mayor impacto.

En **modo edición o reescritura**, entregar el texto revisado y después una nota breve de cambios materiales. No alterar deliberadamente el contenido sustantivo sin señalarlo.

## Fuentes de técnica utilizadas para el diseño

- Microjuris Puerto Rico, *Las tres “C” para una redacción legal de excelencia* (claridad/concisión/coherencia, planificación, voz activa y revisión).
- Microjuris Puerto Rico, *¿Cómo mejorar mi redacción jurídica?* (organización, precisión, audiencia, tono, citas y edición).
- Microjuris Puerto Rico, *Detallan errores comunes de redacción en la comunidad legal* (coherencia, estructura y problemas recurrentes).
- Microjuris Puerto Rico, *Redacción legal: Lista de cotejo para mejor edición y revisión* (audiencia, encabezados, estructura y flujo lógico).
- Anthropic `legal-writing`, usado únicamente como referencia estructural para separar revisión de estructura, profundidad analítica, claridad y forma de citas; este skill para abogados sí permite edición o reescritura cuando el usuario la pide expresamente.

Cumplir siempre con `pr/CLAUDE.md`. Toda autoridad jurídica sustantiva debe verificarse independientemente de la calidad de la redacción.