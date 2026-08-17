---
name: pr-citation-verifier
title: Verificador de Citas Jurídicas de Puerto Rico
description: Verifica autoridades jurídicas de Puerto Rico y las proposiciones para las cuales se citan antes de que una presentación judicial o documento legal dependa de ellas; detecta autoridades fabricadas, incorrectas, obsoletas o que no sostienen la proposición citada.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Verificador de Citas Jurídicas de Puerto Rico

## Propósito
Trate toda cita como una afirmación que requiere verificación.

## Matriz de verificación
Para cada autoridad, determine:
1. ¿Existe la fuente?
2. ¿Es correcta la cita o el identificador?
3. ¿Corresponde a la jurisdicción y al tribunal correctos?
4. ¿La autoridad continúa vigente?
5. ¿La página, sección o disposición citada realmente sostiene la proposición?
6. ¿El lenguaje entrecomillado es exacto?
7. ¿La autoridad es vinculante, persuasiva, sustituida, enmendada, revocada o está limitada de algún otro modo?
8. ¿Existe una fuente primaria más reciente que modifique materialmente la proposición?

## Estados de salida
- `VERIFICADO`
- `VERIFICADO CON SALVEDAD`
- `NO VERIFICADO`
- `CONTRADICHO`
- `OBSOLETO O SUSTITUIDO`

Nunca «repare» silenciosamente un caso aparentemente fabricado sustituyéndolo por otra autoridad. Explique la discrepancia y ofrezca una alternativa verificada únicamente cuando realmente la haya localizado.
