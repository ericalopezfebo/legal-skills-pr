---
name: pr-motion-drafting
title: Puerto Rico Motion Drafting Engine
description: Redacta mociones para Puerto Rico y, cuando se usa el perfil CASP de oficina, reproduce la arquitectura, vocabulario y formato del modelo attorney-authored de referencia sin añadir hechos o formalidades no presentes.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 1.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion Drafting Engine

## Regla principal
Cuando el usuario provea una moción de referencia hecha por el abogado y pida que el resultado quede como esa muestra, **la muestra attorney-authored controla el estilo, orden, vocabulario y densidad del escrito**, salvo requisito jurídico u orden oficial incompatible. No “mejorar” el estilo sustituyéndolo por lenguaje genérico de IA.

Aprender formato y voz; nunca copiar hechos de otro caso.

## Jerarquía
1. requisito oficial vigente del foro;
2. instrucción expresa del usuario;
3. muestra attorney-authored identificada para ese abogado/foro/tipo de moción;
4. otras muestras recientes del mismo foro;
5. estilo neutral.

## Perfiles
- `tpi`
- `casp`
- `aep-ja`
- `appellate`
- `supreme`
- `admin-generic`

Visuales:
- `official-neutral`
- `pr-litigation-redline`
- `casp-calderon` — perfil de fidelidad al modelo attorney-authored “Asumir Representación”.

## CASP — perfil `casp-calderon`
Usar este perfil cuando el usuario pida el formato del Lcdo. Víctor Calderón o una moción “como Asumir Representación”.

### Arquitectura exacta preferida
1. `GOBIERNO DE PUERTO RICO`
2. `COMISIÓN APELATIVA DEL SERVICIO PÚBLICO`
3. `SAN JUAN, PUERTO RICO`
4. epígrafe de dos columnas;
5. título centrado, mayúsculas, negrita y subrayado;
6. saludo: `A LA HONORABLE COMISIÓN U COMISIONADA ASOCIADA`
7. comparecencia: `COMPARECE LA PARTE [APELADA/APELANTE], [SIGLAS], por conducto del abogado que suscribe, y muy respetuosamente expone y solicita lo siguiente:`
8. párrafos numerados, directos, iniciados con `Que ...` cuando corresponda;
9. súplica en el mismo párrafo iniciada por `POR TODO LO CUAL,`;
10. `RESPETUOSAMENTE SOMETIDO.`
11. `En San Juan, Puerto Rico, a [fecha].`
12. bloque de firma/datos;
13. encabezado centrado, negrita y subrayado `CERTIFICADO DE NOTIFICACIÓN`;
14. certificación en página siguiente cuando el flujo del modelo así resulte: `CERTIFICO: haber enviado copia del presente escrito ...`;
15. firma/nombre al final de la certificación.

### Epígrafe CASP Calderón
- izquierda centrada: nombre de apelante, `Apelante`, `v.`, contraparte, siglas cuando existan, `Apelado/Apelada`;
- derecha: `Caso Núm. [número]`, luego `SOBRE:`, luego materia centrada;
- división vertical central negra; borde inferior en el bloque izquierdo según el modelo;
- no anteponer `Parte` a `Apelante`/`Apelado` si la muestra no lo hace;
- `Caso Núm.` en capitalización normal, no `CASO NÚM.`.

### Voz y vocabulario
Para este perfil, preservar las fórmulas de la muestra aunque exista una alternativa más moderna:
- `abogado que suscribe`, no sustituir automáticamente por `representación legal que suscribe`;
- `Que el abogado que suscribe asume ...`;
- `se solicita copia del expediente de récord`;
- `de tener el expediente digital`;
- `se solicita un término de [X] días`;
- `para poder cumplir con todas las ordenes emitidas, de haber alguna` cuando los hechos lo sostengan;
- `declare CON LUGAR la presente moción`;
- `autorice nuestra representación legal`;
- `en lo sucesivo envíen a nuestra dirección de récord toda notificación futura`.

No introducir lenguaje que el abogado no utilizó solo porque parezca más formal.

## Regla anti-alucinación para mociones breves
**No agregar párrafos jurídicamente plausibles que no estén sustentados por la instrucción o el récord.**

En una moción asumiendo representación NO añadir por defecto:
- que se sustituye a un abogado anterior;
- nombre del abogado anterior;
- que el abogado anterior “cesa su intervención”;
- que no hay anejos;
- método/dirección de notificación aún desconocidos;
- explicaciones sobre la naturaleza de la comparecencia;
- hechos procesales no suministrados.

Si el dato es indispensable, usar `[POR COMPLETAR]`; si no es indispensable para el patrón solicitado, **omitirlo**.

## Regla de fidelidad de contenido
Cuando exista una muestra attorney-authored comparable, hacer primero un `motion skeleton` de la muestra:
- número de párrafos;
- función de cada párrafo;
- fórmulas de apertura/cierre;
- orden de certificación y firma;
- nivel de detalle;
- términos enfatizados.

Redactar el nuevo escrito sobre ese skeleton. No reemplazarlo con una plantilla genérica.

## Tipos de moción
Entre otros: asumir/relevar representación, prórroga, cumplimiento de orden, mostrar causa, informativa, solicitud de orden/vista, cambio de señalamiento, oposición, réplica, reconsideración, desestimación, resolución/sentencia sumaria y descubrimiento.

Para una moción breve, no añadir secciones doctrinales. Para una moción sustantiva, usar solo las secciones que realmente ayuden (`HECHOS`, `TRÁCTO PROCESAL`, `DERECHO`, `APLICACIÓN`, `SÚPLICA`).

## Formato visual
Consultar `FORMAT_PROFILES.md`. Para `casp-calderon`:
- Letter;
- Times New Roman 12 pt;
- líneas laterales rojas en todas las páginas: izquierda doble, derecha sencilla;
- cuerpo justificado;
- título centrado + bold + underline;
- términos seleccionados dentro del cuerpo en bold según la muestra (p. ej. siglas de la parte, `copia del expediente`, email, número de días, `POR TODO LO CUAL`, `CON LUGAR`, `RESPETUOSAMENTE SOMETIDO`, `CERTIFICO`);
- encabezado `CERTIFICADO DE NOTIFICACIÓN` centrado + bold + underline;
- número de página centrado en pie con guiones en páginas subsiguientes según el modelo.

## Algoritmo
1. Identificar foro, tipo de moción y si existe muestra attorney-authored aplicable.
2. Extraer skeleton de la muestra antes de redactar.
3. Separar hechos confirmados de datos faltantes.
4. Eliminar cualquier párrafo “útil” que no aparezca en el skeleton ni sea necesario por el caso.
5. Redactar con la voz de la muestra, manteniendo su nivel de concisión.
6. Construir una súplica que replique la forma de remedio del modelo cuando sea jurídicamente congruente.
7. Certificar únicamente hechos reales de notificación.
8. Renderizar con `motion_docx.py` y el perfil visual correspondiente.
9. Comparar visualmente contra la muestra: encabezado, caption, título, saludo, indentación, espaciado, bold/underline, bordes, firma, certificado y paginación.
10. Revisar que no quede ningún dato de otro asunto.

## Quality gate específico para “Asumiendo Nueva Representación” CASP
Antes de entregar, confirmar:
- ¿dice `SAN JUAN, PUERTO RICO` bajo el encabezado?
- ¿roles dicen `Apelante` / `Apelado(a)` sin `Parte`, si se está imitando la muestra?
- ¿usa `Caso Núm.`?
- ¿título está subrayado además de negrita?
- ¿saludo dice `A LA HONORABLE COMISIÓN U COMISIONADA ASOCIADA`?
- ¿comparecencia usa `abogado que suscribe`?
- ¿los párrafos comienzan con `Que` siguiendo el modelo?
- ¿no se inventó sustitución de abogado, ausencia de anejos u otro hecho?
- ¿`POR TODO LO CUAL` pide `CON LUGAR`, autorización y notificaciones futuras cuando corresponda?
- ¿`RESPETUOSAMENTE SOMETIDO.` aparece antes de lugar/fecha y firma?
- ¿el `CERTIFICADO DE NOTIFICACIÓN` aparece después del bloque principal, como en el modelo?

Si alguna respuesta es no, corregir antes de entregar.

## Salida
Cuando se solicite Word, generar `.docx`; no limitarse a describir el formato. Toda moción requiere revisión final del abogado antes de presentación.
