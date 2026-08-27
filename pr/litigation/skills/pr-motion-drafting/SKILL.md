---
name: pr-motion-drafting
title: Redacción de Mociones en Puerto Rico
description: Redacta y revisa mociones, oposiciones, réplicas y solicitudes procesales para tribunales o agencias de Puerto Rico a partir de las partes, hechos, postura, remedio y anexos suministrados. Úsese como motor general cuando ningún skill procesal especializado controle completamente el escrito.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.3.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Redacción de mociones en Puerto Rico

## Cuándo aplicar

Usar para redactar o revisar una moción, oposición, réplica, solicitud informativa, moción en cumplimiento de orden o petición de orden. Un skill especializado controla sus requisitos particulares y este skill aporta la estructura, el tono y el ensamblaje final.

## Entrada mínima

Recibir:
- foro y número de caso;
- partes y parte representada;
- etapa procesal;
- orden, controversia o evento activador;
- hechos confirmados y fuente de cada uno;
- remedio principal y alterno;
- fecha prevista y anexos disponibles.

Preguntar solo por datos ausentes que cambien jurisdicción, término, carga, remedio o certificación. Nunca inventar historial, comunicaciones, acuerdos, fechas, entradas, prueba, citas ni anexos.

## Algoritmo

1. **Clasificar el escrito.** Determinar si es solicitud, oposición, réplica, reconsideración, desestimación, descubrimiento, relevo de representación, cumplimiento de orden u otro vehículo.
2. **Verificar el marco.** Confirmar regla, ley especial, reglamento de agencia, orden, estándar, carga, término y requisito de conferencia aplicables. Mantener `[VERIFICAR]` donde falte cotejo.
3. **Buscar formato oficial.** Si el tribunal o agencia publica un formulario, modelo o instrucciones oficiales aplicables, tratarlos como referencia prioritaria de formato. No asumir que un modelo genérico satisface un foro especializado.
4. **Construir la cronología.** Separar hechos confirmados, alegaciones, inferencias, hechos del expediente pendientes de verificación y derecho.
5. **Seleccionar material.** Incluir únicamente hechos pertinentes al remedio y vincular cada afirmación con expediente, anejo, declaración o fuente identificable.
6. **Organizar el escrito.** Respetar primero formulario u orden del foro. En ausencia de formato obligatorio, usar:
   1. epígrafe;
   2. título específico;
   3. comparecencia;
   4. síntesis del remedio solicitado;
   5. antecedentes procesales;
   6. hechos pertinentes numerados;
   7. derecho aplicable;
   8. argumentación;
   9. súplica;
   10. firma, certificación y propuesta de orden cuando corresponda.
7. **Redactar la argumentación.** Presentar cuestión, regla verificada, aplicación, mejor objeción contraria y respuesta. No confundir alegaciones con hechos establecidos.
8. **Precisar la súplica.** Identificar quién solicita qué orden, respecto de qué asunto y qué remedio alterno procede. La súplica debe corresponder a lo realmente argumentado.
9. **Aplicar las tres C.** Claridad, concisión y coherencia. Una proposición principal por párrafo; oraciones manejables; lenguaje sencillo; voz activa cuando sea natural; transiciones que expliquen relevancia; eliminar repeticiones y formalismos que no aporten.
10. **Aplicar tono y narrativa.** Ser firme y respetuoso. Organizar los hechos para que el lector entienda el hilo del caso, pero sin convertir inferencias o narrativa persuasiva en hechos probados.
11. **Aplicar el formato.** Usar texto legible, cuerpo justificado, título centrado y numeración de páginas, salvo que el foro ordene otra cosa. No sacrificar legibilidad para imitar un modelo.
12. **Auditar.** Verificar congruencia entre argumentación y súplica, autoridades, citas al expediente, anexos, firma, notificación, confidencialidad, formato oficial y marcadores.

## Moción en cumplimiento de orden

Cuando la moción responda a una orden del tribunal o agencia:

- identificar con precisión la orden y su fecha;
- enumerar cada mandato material que exige cumplimiento;
- contestar cada mandato de forma separada y trazable;
- indicar qué se cumplió, cómo y con qué anejo o evidencia;
- identificar expresamente lo que no pueda cumplirse y explicar la razón sustentada;
- evitar convertir una moción de cumplimiento en una reconsideración encubierta, salvo que se solicite expresamente el remedio procesal correcto.

## Formularios y modelos externos

Los modelos de agencias, tribunales u organizaciones pueden servir para estructura y campos, pero no deben reutilizarse mecánicamente. Verificar siempre vigencia, foro, regla, firma, certificación, modo de notificación y datos requeridos. Un modelo de litigante por derecho propio o de un tercero no sustituye un formato oficial ni el juicio profesional del abogado.

## Privacidad de modelos

Antes de estudiar un escrito anterior, aplicar `pr-legal-document-sanitization`. No reutilizar nombres, direcciones, contactos, números de caso, firmas, metadatos ni hechos de otro asunto. Para el asunto actual, insertar datos identificativos únicamente cuando el usuario los suministre y autorice; de lo contrario, usar marcadores como `[PARTE]` y `[NÚMERO DE CASO]`.

## Contrato de salida

Entregar el borrador completo, no una explicación genérica, seguido de:
- información faltante;
- autoridades o datos pendientes de verificación;
- anexos o certificaciones pendientes;
- estado `REVISIÓN DE ABOGADO REQUERIDA`.

Coordinar con `pr-legal-writing-review` para edición de claridad y con `pr-filing-readiness` antes de presentar. Cumplir con `pr/CLAUDE.md` y añadir su descargo obligatorio.