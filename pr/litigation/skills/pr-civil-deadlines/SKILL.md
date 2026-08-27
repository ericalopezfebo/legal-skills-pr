---
name: pr-civil-deadlines
title: Puerto Rico Civil Litigation Deadlines
description: Calcula y audita términos de litigación civil en Puerto Rico desde eventos activadores y fuentes verificadas, y produce un plan de docketing con recordatorios internos y controles redundantes sin confundirlos con el término jurídico.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.2.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Civil Litigation Deadlines

## Propósito

Calcular términos únicamente desde fuentes y hechos verificados y convertir el resultado en un plan operativo de seguimiento. Este skill no es un calendario basado en memoria.

## Entradas requeridas

- foro y tipo de caso;
- evento activador;
- fecha exacta y, cuando importe, método/fecha de notificación o emplazamiento;
- regla, estatuto u orden aplicable si se conoce;
- prórrogas, stays, órdenes modificadas o procedimiento especial;
- acto o presentación objetivo.

## Workflow jurídico

1. Confirmar que gobierna procedimiento civil de Puerto Rico. Si es federal, apelativo, administrativo, penal, quiebra u otro régimen especial, detener o enrutar.
2. Identificar la fuente jurídica que crea el término.
3. Verificar texto vigente y versión aplicable antes de calcular.
4. Identificar precisamente el evento activador; distinguir presentación, entrada, archivo, notificación, servicio, emplazamiento, vista y sentencia.
5. Aplicar la regla vigente de cómputo, incluidos fines de semana y feriados. No añadir días por método de notificación salvo autoridad vigente.
6. Verificar enmiendas, prórrogas, stays, órdenes, procedimientos especiales y si el término es jurisdiccional o improrrogable.
7. Mostrar cálculo transparente: fuente → evento → fecha → intervalo → regla de cómputo → ajustes → resultado.
8. Expresar incertidumbre y alternativas cuando falte un hecho controlador.

## Docketing defensivo

Después de determinar la fecha jurídica, crear separadamente un **plan interno**. Nunca representar una fecha interna como término legal.

- Registrar el término inmediatamente después de verificarlo.
- Mantener una fuente maestra de calendario por asunto/equipo y evitar calendarios paralelos no sincronizados.
- Para términos de alto riesgo, recomendar verificación independiente por una segunda persona o sistema.
- Crear recordatorios escalonados antes del vencimiento según la complejidad del trabajo.
- Dividir tareas extensas en hitos: investigación, primer borrador, revisión de cliente, exhibits, revisión de abogado, firma y presentación.
- Programar revisión periódica de expedientes sin actividad para que ningún asunto quede sin próxima acción.
- Cuando se espera un evento externo, fijar una fecha de seguimiento en lugar de dejar el expediente sin acción.
- Conservar la fuente y el razonamiento del cómputo para que otra persona pueda reproducirlo.

Los recordatorios internos son salvaguardas de gestión, no alteran ni extienden el término jurídico.

## Términos de alto riesgo

Tratar como alto riesgo: post-sentencia, reconsideración, apelación/revisión, certiorari, remoción/remand, prescripción/caducidad cuando corresponda, términos jurisdiccionales, estatutarios y procedimientos especiales. Requerir verificación actual antes de depender de la fecha.

## Guardrails

- Nunca calcular exclusivamente de memoria.
- Nunca asumir que un tribunal puede prorrogar un término.
- Nunca asumir que una moción interrumpe otro término sin verificar efecto y cumplimiento.
- Nunca inferir notificación de presentación.
- Si el récord contiene fechas conflictivas, mostrar escenarios y explicar qué hecho controla.
- No usar un artículo de práctica como autoridad para la duración del término.

## Contrato de salida

```markdown
# Cómputo de término — [acto]

## Fecha jurídica
- Foro: [foro]
- Fuente: [regla/estatuto/orden]
- Evento activador: [evento]
- Fecha activadora: [fecha]
- Término: [duración]
- Regla de cómputo: [fuente]
- Ajustes: [feriados/orden/etc.]
- Fecha resultante: **[fecha]**
- Nivel de certeza: [alto/condicional/verificar]

## Plan interno de docketing
| Hito interno | Fecha sugerida | Propósito |
|---|---|---|
| Verificación secundaria | [fecha] | Confirmar fuente y cálculo |
| Investigación / documentos | [fecha] | Completar insumos |
| Primer borrador | [fecha] | Evitar trabajo de última hora |
| Revisión final | [fecha] | QA jurídico y factual |
| Vencimiento jurídico | [fecha] | Término controlante |

## Advertencias
[asunciones y riesgos]
```

## Fuente metodológica

Microjuris Puerto Rico, *5 consejos esenciales para que los abogados no pierdan una fecha límite*, utilizado únicamente para prácticas de gestión: calendario central, registro inmediato, recordatorios escalonados, hitos y revisión de asuntos inactivos. La duración y efecto de todo término se determina exclusivamente mediante autoridad jurídica vigente.

Aplicar `pr/CLAUDE.md` y citar la regla, estatuto u orden verificada utilizada.