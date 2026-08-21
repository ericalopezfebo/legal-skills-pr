---
name: pr-legal-document-sanitization
title: Sanitización de Documentos Jurídicos
description: Crea una copia de trabajo desidentificada de mociones, informes, cartas, órdenes y expedientes antes de analizarlos, convertirlos en ejemplos o extraer patrones de tono y formato.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: general
language: es
---

# Sanitización de documentos jurídicos

## Cuándo aplicar

Usar antes de estudiar, compartir o reutilizar como modelo un documento que contenga datos de personas, clientes, terceros, abogados, jueces, empleados o asuntos reales.

## Algoritmo

1. Trabajar siempre sobre una copia y mantener el original fuera de toda carpeta distribuible.
2. Sustituir nombres por roles consistentes como `[PARTE DEMANDANTE]`, `[PARTE QUERELLADA]` o `[TESTIGO 1]`.
3. Sustituir direcciones, teléfonos, correos, números de caso, cuentas, licencias, placas, fechas individualizantes y otros identificadores por marcadores tipados.
4. Generalizar hechos que permitan reidentificación cuando no sean necesarios para estudiar estructura o función retórica.
5. Revisar cuerpo, tablas, encabezados, pies, notas, campos, cuadros de texto, hipervínculos, comentarios, cambios controlados y contenido oculto.
6. Eliminar firmas manuscritas o digitales, iniciales, sellos, códigos, imágenes y propiedades que identifiquen personas o expedientes.
7. Mantener cualquier mapa temporal de sustituciones solo durante la tarea y destruirlo al terminar. Nunca incorporarlo al repositorio.
8. Buscar residuos mediante patrones y revisión visual. Tratar cualquier coincidencia dudosa como bloqueo.
9. Extraer únicamente rasgos abstractos: jerarquía, orden de secciones, alineación, espaciado, numeración, extensión, tono y función.
10. Aplicar una prueba de reidentificación: si un lector razonable puede reconocer el asunto, reducir o eliminar más contenido.
11. Aplicar una prueba de sustitución: no distribuir una reconstrucción que permita recuperar sustancialmente el documento de referencia.
12. Informar únicamente el resultado del control y los patrones abstractos; nunca revelar documento, persona o expediente de procedencia.

## Contrato de salida

Entregar:
- estado `SANITIZADO`, `REQUIERE REVISIÓN` o `BLOQUEADO`;
- categorías de datos eliminadas;
- lugares o capas revisadas;
- riesgos residuales;
- patrones abstractos permitidos.

No incluir la tabla de sustituciones ni datos removidos. Cumplir con `pr/CLAUDE.md`.
