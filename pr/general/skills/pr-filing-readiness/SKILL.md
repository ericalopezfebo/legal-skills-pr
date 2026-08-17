---
name: pr-filing-readiness
title: Auditoría Final Antes de Presentar en Puerto Rico
description: Realiza una auditoría final de un documento jurídico de Puerto Rico antes de su presentación, verificando jurisdicción, términos, cumplimiento procesal, apoyo en el expediente, citas, remedio solicitado, consistencia y marcadores pendientes.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Auditoría Final Antes de Presentar en Puerto Rico

## Propósito
Este skill funciona como control final de calidad. No sustituye una investigación jurídica sustantiva.

## Auditoría
Verifique:
- tribunal o agencia y epígrafe;
- partes y capacidad representativa;
- jurisdicción y vehículo procesal o de revisión;
- término de presentación y notificación;
- requisitos de la regla procesal aplicable;
- remedio solicitado;
- apoyo fáctico y referencias al expediente;
- referencias a exhibits o apéndices;
- autoridades jurídicas y citas textuales;
- formato de citación;
- firmas y certificaciones, cuando correspondan;
- información confidencial y necesidad de redacción o protección;
- consistencia interna de fechas, nombres, términos definidos y referencias cruzadas;
- marcadores pendientes como `[POR COMPLETAR]` o `[VERIFICAR]`.

## Resultado
Devuelva uno de los siguientes estados:
- `LISTO PARA REVISIÓN FINAL DEL ABOGADO`
- `NO LISTO — ASUNTOS MATERIALES`
- `NO LISTO — FALTA INFORMACIÓN`

Enumere primero los asuntos que impiden presentar el documento. Nunca certifique que una presentación es jurídicamente suficiente únicamente porque cumple con requisitos de formato.
