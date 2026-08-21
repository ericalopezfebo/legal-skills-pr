---
name: pr-motion-drafting
title: Redacción de Mociones en Puerto Rico
description: Redacta y revisa mociones, oposiciones, réplicas y solicitudes procesales para tribunales o agencias de Puerto Rico a partir de las partes, hechos, postura, remedio y anexos suministrados. Úsese como motor general cuando ningún skill procesal especializado controle completamente el escrito.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.2.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Redacción de mociones en Puerto Rico

## Cuándo aplicar

Usar para redactar o revisar una moción, oposición, réplica, solicitud informativa o petición de orden. Un skill especializado controla sus requisitos particulares y este skill aporta la estructura, el tono y el ensamblaje final.

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

1. **Clasificar el escrito.** Determinar si es solicitud, oposición, réplica, reconsideración, desestimación, descubrimiento, relevo de representación u otro vehículo.
2. **Verificar el marco.** Confirmar regla, ley especial, orden, estándar, carga, término y requisito de conferencia aplicables. Mantener `[VERIFICAR]` donde falte cotejo.
3. **Construir la cronología.** Separar hechos confirmados, alegaciones, inferencias, hechos del expediente pendientes de verificación y derecho.
4. **Seleccionar material.** Incluir únicamente hechos pertinentes al remedio y vincular cada afirmación con expediente, anejo, declaración o fuente identificable.
5. **Organizar el escrito.** Respetar primero formulario u orden del foro. En ausencia de formato obligatorio, usar:
   1. epígrafe;
   2. título específico;
   3. comparecencia;
   4. remedio solicitado;
   5. antecedentes procesales;
   6. hechos pertinentes numerados;
   7. derecho aplicable;
   8. argumentación;
   9. súplica;
   10. firma, certificación y propuesta de orden cuando corresponda.
6. **Redactar la argumentación.** Presentar cuestión, regla verificada, aplicación, mejor objeción contraria y respuesta. No confundir alegaciones con hechos establecidos.
7. **Precisar la súplica.** Identificar quién solicita qué orden, respecto de qué asunto y qué remedio alterno procede.
8. **Aplicar el tono.** Usar español jurídico sobrio, firme y respetuoso; párrafos numerados con una proposición principal; encabezados funcionales; voz activa cuando sea natural; y transiciones que expliquen relevancia.
9. **Aplicar el formato.** Usar texto legible, cuerpo justificado, título centrado y numeración de páginas, salvo que el foro ordene otra cosa. No sacrificar legibilidad para imitar un modelo.
10. **Auditar.** Verificar congruencia entre argumentación y súplica, autoridades, citas al expediente, anexos, firma, notificación, confidencialidad y marcadores.

## Privacidad de modelos

Antes de estudiar un escrito anterior, aplicar `pr-legal-document-sanitization`. No reutilizar nombres, direcciones, contactos, números de caso, firmas, metadatos ni hechos de otro asunto. Para el asunto actual, insertar datos identificativos únicamente cuando el usuario los suministre y autorice; de lo contrario, usar marcadores como `[PARTE]` y `[NÚMERO DE CASO]`.

## Contrato de salida

Entregar el borrador completo, no una explicación genérica, seguido de:
- información faltante;
- autoridades o datos pendientes de verificación;
- anexos o certificaciones pendientes;
- estado `REVISIÓN DE ABOGADO REQUERIDA`.

Cumplir con `pr/CLAUDE.md` y añadir su descargo obligatorio.
