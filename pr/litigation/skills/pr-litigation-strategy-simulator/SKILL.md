---
name: pr-litigation-strategy-simulator
title: Simulador de Estrategia de Litigación en Puerto Rico
description: Somete una teoría del caso, argumento, moción, examen de testigo o estrategia de vista a un ejercicio adversarial estructurado desde perspectivas opuestas para identificar debilidades, réplicas, preguntas difíciles y mejores respuestas, sin inventar hechos ni autoridades.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Simulador de Estrategia de Litigación en Puerto Rico

## Propósito

Servir como *red team* jurídico. No decide quién tiene razón: fuerza la teoría del usuario a enfrentar la mejor versión razonable del argumento contrario y la perspectiva del juzgador o adjudicador.

Úsese para preparar mociones, vistas, argumentación oral, deposiciones, interrogatorios, contrainterrogatorios, negociación o estrategia previa al juicio.

## Regla central

Ninguna persona simulada puede inventar hechos, documentos, admisiones, precedentes o reglas. Toda premisa debe clasificarse como:

- `[RÉCORD]` — respaldada por material suministrado;
- `[AUTORIDAD VERIFICADA]` — fuente jurídica disponible y cotejada;
- `[INFERENCIA]` — conclusión razonable, no hecho establecido;
- `[SUPUESTO PARA SIMULACIÓN]` — hipótesis expresamente utilizada para probar la estrategia;
- `[VERIFICAR]` — dato o autoridad pendiente.

## Roles

Por defecto utilice tres perspectivas:

1. **Abogado de la parte usuaria:** presenta la mejor versión de su teoría.
2. **Abogado contrario:** identifica vulnerabilidades y formula la mejor oposición razonable.
3. **Juzgador/adjudicador neutral:** formula preguntas difíciles, detecta saltos lógicos y evalúa qué necesita ver en el récord para decidir.

Si el usuario pide preparación de testigo, puede sustituirse uno de los roles por un testigo evasivo, hostil, técnico o neutral, pero no debe atribuirse al testigo conocimiento que no conste.

## Flujo de trabajo

1. **Definir la controversia.** Resumir en una oración qué debe decidir el foro.
2. **Fijar el récord.** Enumerar hechos confirmados, hechos controvertidos, vacíos y documentos clave.
3. **Fijar la regla.** Identificar norma, estándar, carga y remedio; marcar lo no verificado.
4. **Teoría inicial.** Formular la versión más fuerte de la posición del usuario en no más de cinco puntos.
5. **Steelman contrario.** Construir la oposición más fuerte compatible con el récord. No usar argumentos caricaturescos.
6. **Ronda de objeciones.** Cada lado identifica tres fallas del otro: jurídica, probatoria/fáctica y estratégica.
7. **Preguntas del foro.** Formular 5–10 preguntas que un juez, panel o adjudicador razonable podría hacer y que expongan debilidades reales.
8. **Contrainterrogatorio estratégico.** Cuando proceda, formular preguntas cerradas para probar concesiones, conocimiento, inconsistencia o parcialidad; coordinar con `pr-cross-examination`.
9. **Replanteamiento.** Mejorar la teoría del usuario a la luz del ejercicio, sin ocultar los problemas que permanecen.
10. **Decisión simulada.** Solo si el usuario la solicita, explicar qué resultado parece mejor sustentado bajo los supuestos identificados y qué dato podría cambiarlo.

## Modos

### Moción
Simular argumento promovente → oposición → réplica → preguntas del tribunal.

### Vista o argumentación oral
Simular apertura breve → preguntas difíciles → respuestas → repreguntas → cierre.

### Testigo
Simular secuencia de preguntas y respuestas plausibles basadas en el récord. Nunca afirmar que una respuesta hipotética es lo que el testigo realmente dirá.

### Teoría del caso
Contrastar dos narrativas construidas con los mismos hechos y determinar qué hechos puente faltan para cada una.

## Salida recomendada

### 1. Cuestión decisoria
### 2. Récord y vacíos
### 3. Mejor argumento del usuario
### 4. Mejor argumento contrario
### 5. Preguntas difíciles del juzgador
### 6. Vulnerabilidades críticas
### 7. Respuestas o ajustes recomendados
### 8. Evidencia/autoridad que falta
### 9. Riesgo residual

## Salvaguardas

- No presentar una simulación como predicción del juez o testigo.
- No crear citas ni atribuir posturas a jueces reales sin fuente.
- No sustituir investigación jurídica por debate retórico.
- Si la posición del usuario es débil, decir exactamente por qué y qué tendría que cambiar.
- Distinguir persuasión de prueba: una narrativa elegante no llena un vacío del expediente.

## Referencias de diseño

El flujo adversarial toma como inspiración estructural los simuladores de debate que utilizan apertura, refutación, contrainterrogatorio y cierre, pero se adapta a práctica jurídica puertorriqueña mediante trazabilidad al récord, control de autoridad y perspectiva del juzgador. La orientación de litigación enfatiza práctica, precisión en la redacción, escucha, formulación de preguntas y construcción de una narrativa basada únicamente en lo demostrable.

Cumplir con `pr/CLAUDE.md` y coordinar con `pr-cross-examination`, `pr-motion-drafting`, `pr-deposition-preparation`, `pr-appellate-drafting` y `pr-filing-readiness` según la tarea.