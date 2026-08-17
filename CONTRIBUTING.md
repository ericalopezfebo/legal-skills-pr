# Cómo contribuir

Gracias por aportar un skill. Los skills son archivos Markdown breves; no se requiere escribir código.

## Cómo hacer una contribución

1. Haga un fork del repositorio.
2. Añada una carpeta `pr/{area-de-practica}/skills/{slug}/` con un archivo `SKILL.md` dentro. Puede utilizar la plantilla incluida más abajo. Si el área de práctica todavía no existe bajo `pr/`, créela.
3. Abra un pull request.

## Plantilla de `SKILL.md`

```markdown
---
name: mi-skill
title: Mi Skill
description: Descripción en un párrafo de lo que hace el skill y cuándo debe utilizarse. Esta descripción ayuda al agente de IA a decidir cuándo invocarlo, por lo que debe ser específica sobre frases disparadoras y alcance.
author: Su Nombre
author_url: https://github.com/suusuario
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Título del skill

## Cuándo aplicar
Disparadores, ejemplos de solicitudes y asuntos expresamente fuera de alcance.

## Algoritmo
Instrucciones paso a paso que debe seguir el agente.

## Contrato de salida
Qué debe contener la respuesta: formato, citas requeridas y el descargo de responsabilidad obligatorio.
```

## Reglas generales

- **Nunca invente una cita.** Todo skill debe instruir al agente a señalar estatutos, casos, números de expediente, reglas o términos que no hayan sido verificados, en lugar de fabricarlos. Véase [`pr/CLAUDE.md`](pr/CLAUDE.md).
- **Indique la versión del código o regla utilizada.** Puerto Rico ha sustituido y recodificado áreas importantes en años recientes, como el Código Civil de 2020 y la LPAU de 2017. Un skill que aplica una versión incorrecta puede ser peor que no utilizar ninguno.
- **Idioma.** El contenido sustantivo y las instrucciones dirigidas a abogados de Puerto Rico deben redactarse en español, salvo que la naturaleza del foro, una fuente oficial o un término técnico requiera mantener texto en inglés.
- **Licencia.** Las contribuciones deben ser compatibles con la licencia MIT. Al abrir un pull request, usted licencia su contribución bajo la [LICENSE](LICENSE) de este repositorio.
- **Esto no constituye asesoramiento legal.** Todo producto de los skills debe incluir el descargo requerido por `pr/CLAUDE.md`.
- **No incluya contenido confidencial o específico de un asunto real.** Los skills deben ser de uso general. No aporte nombres reales de clientes, jueces ni información identificable de litigios pendientes.

## No exclusividad

Usted conserva sus derechos sobre su skill y puede publicarlo o reutilizarlo en otros lugares sin necesidad de notificar al repositorio.
