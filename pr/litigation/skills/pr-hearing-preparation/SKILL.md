---
name: pr-hearing-preparation
title: Preparación de Vistas en Puerto Rico
description: Prepara al abogado para una vista judicial o administrativa en Puerto Rico mediante un bench brief operativo, cronología, teoría, prueba, testigos, exhibits, objeciones, preguntas probables del juzgador, logística y plan de sala, sin inventar hechos ni autoridades.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Preparación de Vistas en Puerto Rico

## Cuándo aplicar

Usar antes de una vista, conferencia, señalamiento evidenciario, vista administrativa o comparecencia oral cuando el abogado necesite convertir el expediente en un plan ejecutable en sala.

## Entrada mínima

- foro, sala/agencia y fecha;
- tipo y propósito de la vista;
- orden o señalamiento;
- postura procesal y remedio;
- controversias y cargas;
- escritos relevantes;
- testigos y exhibits;
- hechos estipulados y controvertidos;
- autoridades aplicables ya verificadas o materiales para investigarlas.

## Algoritmo

1. **Leer la orden primero.** Identificar exactamente qué decidió el foro que ocurrirá en la vista y cualquier requisito previo.
2. **Definir el resultado buscado.** Expresarlo en una oración y formular la orden concreta que se desea obtener.
3. **Construir cronología.** Separar hecho, fuente, relevancia, disputa y laguna.
4. **Construir mapa de elementos/controversias.** Para cada cuestión: carga, hecho necesario, prueba disponible, objeción esperada y autoridad.
5. **Preparar teoría oral.** Crear explicación de 30 segundos, 2 minutos y versión completa. No convertirla en discurso memorizado si la vista exige diálogo con el tribunal.
6. **Preparar testigos.** Para cada testigo: propósito, cinco hechos que debe establecer, riesgos, documentos, directo/cross y puntos de impugnación. Usar `pr-cross-examination` para testigos adversos.
7. **Preparar exhibits.** Número, descripción, fundamento, autenticación, relevancia, posible objeción y momento de uso.
8. **Preparar objeciones y respuestas.** Solo las materialmente previsibles; identificar regla y remedio solicitado.
9. **Preparar preguntas del juzgador.** Generar las preguntas más difíciles sobre jurisdicción, término, carga, prueba, contradicciones, remedio y consecuencias prácticas. Combinar con `pr-litigation-strategy-simulator` cuando sea útil.
10. **Preparar logística.** Hora, lugar/enlace, comparecientes, copias, tecnología, exhibits, intérprete, accesibilidad, citaciones y contactos necesarios. Verificar instrucciones oficiales del foro; no adivinar prácticas de sala.
11. **Preparar plan de contingencia.** Qué hacer si falta un testigo, se excluye un exhibit, surge nueva prueba, el contrario cambia postura o el tribunal limita tiempo.
12. **Auditar la víspera.** Confirmar términos, órdenes, exhibits, autoridades, material confidencial, equipo y próxima acción.

## Disciplina en sala

- Llegar con tiempo suficiente y preparado para esperar sin perder organización.
- Escuchar la pregunta completa del juzgador y contestar primero la pregunta antes de desarrollar.
- Conocer el expediente y poder llevar al foro a la página o exhibit pertinente.
- No discutir personalmente con el tribunal ni con el abogado contrario.
- Cuando no se sepa una respuesta, no improvisar un hecho o autoridad; pedir oportunidad razonable para verificar cuando proceda.
- Mantener una hoja breve con objetivo, tres puntos esenciales, remedio y asuntos que no deben concederse inadvertidamente.

## Contrato de salida

```markdown
# Plan de Vista — [caso]

## 1. Resultado solicitado
[una oración]

## 2. Qué resolverá la vista
[orden + cuestiones]

## 3. Teoría de 30 segundos
[versión oral]

## 4. Cronología crítica
| Fecha | Hecho | Fuente | Disputa/relevancia |

## 5. Mapa de controversias
| Cuestión | Carga | Prueba | Autoridad | Riesgo |

## 6. Testigos
[objetivo + módulos]

## 7. Exhibits
[mapa de uso y fundamento]

## 8. Objeciones previsibles
[objeción → respuesta → autoridad]

## 9. Preguntas difíciles del juzgador
[pregunta → respuesta breve → apoyo]

## 10. Checklist logístico
[lista]

## 11. Plan B
[contingencias]

## 12. Hoja de sala de una página
[objetivo + 3 puntos + remedio + citas clave]
```

## Fuente metodológica

Microjuris Puerto Rico, *Consejos para el nuevo litigante: Cómo prepararte para tu primera vista ante el Tribunal*, utilizado como fuente de técnica práctica de preparación. Las reglas de procedimiento, evidencia, conducta profesional y práctica específica del foro deben verificarse en fuentes primarias vigentes.

Cumplir con `pr/CLAUDE.md`. No inventar hechos, exhibits, órdenes, citas ni prácticas locales.