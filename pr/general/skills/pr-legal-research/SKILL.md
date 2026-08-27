---
name: pr-legal-research
title: Puerto Rico Legal Research Workflow
description: Estructura investigación jurídica sobre Puerto Rico desde la definición del problema hasta la verificación de fuentes primarias, vigencia, tratamiento posterior y síntesis, con trazabilidad y controles éticos para investigación asistida por tecnología o IA.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.2.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Puerto Rico Legal Research Workflow

## Cuándo aplicar

- El usuario solicita investigar Derecho de Puerto Rico con autoridad verificable.
- Debe determinarse si una ley, regla, reglamento o precedente aplica a unos hechos.
- Se necesita un memo de investigación para revisión de abogado.
- Se utiliza IA, búsqueda web o plataforma jurídica para apoyar investigación y es necesario verificar el resultado.

No sustituye el juicio profesional ni convierte una respuesta generada por IA en autoridad jurídica.

## Principio rector: investigar es una función profesional

Tratar la investigación como parte de la competencia profesional. Bajo las Reglas de Conducta Profesional vigentes, la preparación adecuada comprende investigar y analizar los hechos y el Derecho, y la competencia tecnológica exige usar responsablemente herramientas digitales, incluidas plataformas de investigación y aplicaciones de IA. Nunca delegar a una herramienta la determinación final de qué es Derecho vigente.

## Las siete piezas operativas

Usar como mapa flexible, no como secuencia rígida:

1. **Definir el problema.** Convertir la consulta en preguntas jurídicas precisas; identificar partes, hechos materiales, foro, fecha relevante y remedio.
2. **Determinar dónde comenzar.** Si el área es desconocida, comenzar con una fuente secundaria fiable para adquirir vocabulario y referencias, pero migrar rápidamente a fuentes primarias. Si se trata de actualizar conocimiento existente, comenzar por vigencia y cambios recientes.
3. **Determinar qué fuentes hacen falta.** Constitución, estatuto, regla, reglamento, jurisprudencia, orden administrativa o autoridad federal según la cuestión.
4. **Localizar la fuente primaria y el estado del Derecho.** Obtener el texto actual y las decisiones controlantes; no descansar en resúmenes cuando el original esté disponible.
5. **Saber cuándo detenerse.** No confundir volumen con exhaustividad. Detener cuando las cuestiones materiales estén cubiertas por autoridad suficiente y actual, se hayan investigado autoridades adversas razonablemente localizables y las búsquedas adicionales produzcan rendimientos decrecientes. Explicar cualquier vacío.
6. **Sintetizar y redactar.** Construir regla, excepciones, estándares, autoridad favorable/adversa y aplicación; no producir un collage de citas.
7. **Auditar ética y tecnología.** Verificar citas, vigencia, confidencialidad, exactitud del resultado automatizado y que el producto refleje investigación real.

## Jerarquía y ruta de fuentes

Priorizar conforme a `pr/CLAUDE.md`:

1. texto constitucional aplicable;
2. estatuto vigente o ley especial;
3. regla procesal o de evidencia aplicable;
4. jurisprudencia del Tribunal Supremo de Puerto Rico;
5. reglamentos y decisiones administrativas cuando corresponda;
6. Tribunal de Apelaciones como autoridad persuasiva según proceda;
7. autoridad federal cuando controle una cuestión federal o se use expresamente como analogía;
8. fuentes secundarias para orientación, nunca como sustituto silencioso de una primaria disponible.

## Workflow de verificación

Para cada autoridad:

- localizar el texto original o fuente primaria fiable;
- verificar cita, fecha, tribunal u organismo y versión;
- comprobar enmiendas, derogación, recodificación o sustitución;
- comprobar tratamiento posterior material cuando se trate de jurisprudencia;
- confirmar que la autoridad sostiene la proposición completa para la cual se cita;
- distinguir holding, dictum, estándar, excepción y hechos;
- identificar autoridad contraria material;
- conservar enlace, pincite o referencia suficiente para reproducir la investigación.

No presentar como Derecho vigente una cita encontrada únicamente en un artículo, blog, resultado de buscador o respuesta de IA.

## IA y herramientas tecnológicas

La IA puede ayudar a formular consultas, generar términos de búsqueda, organizar resultados, detectar cuestiones y resumir documentos. Todo resultado sustantivo debe cotejarse con la fuente jurídica. Nunca inventar una cita, pincite, cita textual, historial procesal, tratamiento posterior o contenido de una autoridad que no esté disponible.

Etiquetar incertidumbre como `[VERIFICAR]`. Si una fuente no pudo localizarse, decirlo expresamente.

## Control de recodificación y cambios

Verificar especialmente áreas sometidas a cambios recientes, incluidos el Código Civil de 2020, la LPAU, reglas procesales, reglamentos y las Reglas de Conducta Profesional vigentes desde 2026. Identificar qué versión gobernaba en la fecha material cuando el cambio temporal importe.

## Contrato de salida

```markdown
# Memo de Investigación — [tema]

## Pregunta presentada
[Pregunta jurídica precisa]

## Respuesta breve
[Conclusión provisional y nivel de certeza]

## Mapa de cuestiones
1. [cuestión]
2. [cuestión]

## Autoridad aplicable
| Fuente | Cita / enlace | Proposición | Estado |
|---|---|---|---|
| [primaria] | [cita] | [qué sostiene] | Vigente / verificar / no localizada |

## Autoridad adversa o limitante
[casos, excepciones, conflictos]

## Análisis
[regla + aplicación + límites]

## Vacíos y asuntos pendientes
[hechos, fuentes o tratamiento por verificar]

## Registro de investigación
[consultas principales, fuentes examinadas y fecha de verificación]

## Próximos pasos
[qué falta antes de confiar profesionalmente en la conclusión]
```

## Fuentes metodológicas del diseño

- Microjuris Puerto Rico, *La investigación jurídica bajo las nuevas Reglas de Conducta Profesional* (competencia, investigación, tecnología e IA como responsabilidades profesionales).
- Microjuris Puerto Rico, *7 piezas para facilitar la investigación legal* (definir problema, punto de partida, selección de fuentes, primarias, criterio de cierre, redacción y dimensión ética).

Cumplir con `pr/CLAUDE.md` y cerrar con su descargo obligatorio.