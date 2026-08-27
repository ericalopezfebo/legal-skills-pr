---
name: pr-filing-readiness
title: Auditoría Final Antes de Presentar en Puerto Rico
description: Realiza una auditoría final de un documento jurídico de Puerto Rico antes de su presentación, verificando jurisdicción, términos, cumplimiento procesal, apoyo en el expediente, citas, remedio solicitado, claridad, consistencia y marcadores pendientes.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.2.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Auditoría Final Antes de Presentar en Puerto Rico

## Propósito

Este skill funciona como control final de calidad. No sustituye investigación jurídica sustantiva ni revisión profesional.

## Auditoría

Verifique:
- tribunal o agencia y epígrafe;
- partes y capacidad representativa;
- jurisdicción y vehículo procesal o de revisión;
- término de presentación y notificación;
- requisitos de la regla, reglamento, orden o formulario oficial aplicable;
- remedio solicitado;
- apoyo fáctico y referencias al expediente;
- referencias a exhibits, anejos o apéndices;
- autoridades jurídicas y citas textuales;
- que cada autoridad sostenga la proposición completa para la cual se cita;
- formato de citación y pincites cuando correspondan;
- firmas y certificaciones;
- información confidencial y necesidad de redacción o protección;
- consistencia interna de fechas, nombres, términos definidos y referencias cruzadas;
- marcadores pendientes como `[POR COMPLETAR]`, `[VERIFICAR]`, `[CITA PENDIENTE]` o similares.

## Auditoría de redacción

Aplicar además una revisión rápida de las tres C:

- **Claridad:** ¿puede el lector identificar la controversia, el argumento y el remedio sin descifrar oraciones innecesariamente complejas?
- **Concisión:** ¿hay repeticiones, antecedentes irrelevantes, formalismos o adjetivos que puedan eliminarse sin perder contenido?
- **Coherencia:** ¿cada sección y párrafo conduce lógicamente al siguiente y la súplica corresponde a lo argumentado?

Verificar también:
- voz activa cuando mejore comprensión;
- encabezados funcionales;
- párrafos con una proposición principal;
- tono profesional y respetuoso;
- ausencia de ataques personales o afirmaciones no sustentadas;
- introducción proporcional al escrito y orientada a la decisión requerida;
- audiencia y propósito del documento.

Cuando existan problemas materiales de redacción, recomendar o ejecutar `pr-legal-writing-review` antes de clasificar el documento como listo.

## Resultado

Devuelva uno de los siguientes estados:
- `LISTO PARA REVISIÓN FINAL DEL ABOGADO`
- `NO LISTO — ASUNTOS MATERIALES`
- `NO LISTO — FALTA INFORMACIÓN`

Enumere primero los asuntos que impiden presentar el documento. Nunca certifique que una presentación es jurídicamente suficiente únicamente porque cumple requisitos de formato.

Cumplir con `pr/CLAUDE.md`.