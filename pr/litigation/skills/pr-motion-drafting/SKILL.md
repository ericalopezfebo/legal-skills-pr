---
name: pr-motion-drafting
title: Puerto Rico Motion Drafting Engine
description: Redacta mociones para Puerto Rico y reproduce perfiles attorney-authored cuando existe una muestra canónica, priorizando fidelidad de arquitectura, vocabulario y formato sobre paráfrasis genéricas de IA.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 1.2.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion Drafting Engine

## Regla principal
Cuando exista una muestra attorney-authored canónica para el mismo foro y tipo de moción, **la muestra controla estructura, voz, densidad, fórmulas y orden**, salvo requisito oficial incompatible. El agente NO debe “mejorar”, modernizar, ampliar ni parafrasear innecesariamente el modelo.

Aprender formato y voz; nunca copiar hechos de otro caso.

## Jerarquía
1. requisito oficial vigente del foro;
2. instrucción expresa del usuario;
3. plantilla attorney-authored canónica del mismo foro/tipo;
4. otras muestras attorney-authored del mismo abogado/foro;
5. otras muestras recientes del foro;
6. estilo neutral.

## Selección obligatoria de perfil
Antes de redactar, determinar `forum_profile`, `motion_type` y `attorney_style`.

**Regla automática:** si `forum_profile = casp` y `motion_type = asumir representación` (incluyendo variantes como “asumiendo nueva representación”), usar por defecto `attorney_style = calderon` y `visual_profile = casp-calderon`, salvo que el usuario pida expresamente otro estilo o exista un modelo oficial obligatorio incompatible.

Para ese supuesto, **leer y seguir obligatoriamente**:
`references/casp-calderon-asumir-representacion.md`

No basta con conocer las reglas generales de este SKILL.md. La referencia canónica contiene el texto-esqueleto que debe gobernar la salida.

## Perfiles generales
- `tpi`
- `casp`
- `aep-ja`
- `appellate`
- `supreme`
- `admin-generic`

Visuales:
- `official-neutral`
- `pr-litigation-redline`
- `casp-calderon`

## CASP / Calderón — regla de fidelidad estricta
Para una moción asumiendo representación ante CASP:

1. cargar `references/casp-calderon-asumir-representacion.md`;
2. usar sus cuatro párrafos canónicos como skeleton;
3. sustituir solo datos variables y hacer únicamente las adaptaciones mínimas exigidas por los hechos suministrados;
4. mantener la súplica canónica salvo que el usuario pida un remedio adicional indispensable;
5. mantener el orden del cierre y certificado;
6. ejecutar el quality gate antes de entregar.

### Elementos obligatorios
- `GOBIERNO DE PUERTO RICO`
- `COMISIÓN APELATIVA DEL SERVICIO PÚBLICO`
- `SAN JUAN, PUERTO RICO`
- roles `Apelante` / `Apelado(a)` sin anteponer `Parte` en el epígrafe;
- `Caso Núm.` en capitalización normal;
- título exacto por defecto: `MOCIÓN ASUMIENDO NUEVA REPRESENTACIÓN`;
- título centrado + bold + underline;
- saludo exacto: `A LA HONORABLE COMISIÓN U COMISIONADA ASOCIADA`;
- comparecencia con `abogado que suscribe`;
- párrafos numerados iniciados con `Que`;
- súplica con `declare CON LUGAR`, `autorice nuestra representación legal` y futuras notificaciones a dirección de récord;
- `RESPETUOSAMENTE SOMETIDO.` antes de fecha/firma;
- `CERTIFICADO DE NOTIFICACIÓN` después del bloque principal.

### Prohibiciones específicas
Cuando se usa la plantilla canónica, NO:
- cambiar `Apelante` por `Parte Apelante`;
- cambiar `Apelado` por `Parte Apelada` en el epígrafe;
- usar `CASO NÚM.`;
- añadir `LEGAL` al título;
- acortar el saludo a `A LA HONORABLE COMISIÓN:`;
- sustituir `abogado que suscribe` por `representación legal que suscribe`;
- añadir RUA al primer párrafo si el modelo lo coloca en firma;
- explicar que el expediente es necesario “para ejercer cabalmente” la representación;
- crear un quinto párrafo solo para la dirección de récord;
- convertir la súplica en una lista `(a)-(d)`;
- sustituir `declare CON LUGAR` por `tome conocimiento`;
- colocar `CERTIFICO` antes de `RESPETUOSAMENTE SOMETIDO`;
- añadir hechos sobre abogado anterior, anejos, sustitución, cesación o estado procesal no suministrado.

Si el borrador contiene cualquiera de esos cambios sin instrucción expresa, **falla el perfil y debe regenerarse antes de entregarse**.

## Regla anti-alucinación para mociones breves
No agregar contenido jurídicamente plausible que no esté sustentado por instrucciones, récord o plantilla aplicable. Si un dato indispensable falta, usar `[POR COMPLETAR]`; si no es indispensable, omitirlo.

## Otros tipos de moción
Para mociones sin plantilla canónica, construir primero un `motion skeleton` a partir de la mejor muestra attorney-authored disponible:
- número y función de párrafos;
- apertura y cierre;
- orden de certificación/firma;
- densidad;
- vocabulario;
- énfasis tipográfico.

No imponer secciones doctrinales a mociones breves. En mociones sustantivas usar solo las secciones necesarias (`HECHOS`, `TRÁCTO PROCESAL`, `DERECHO`, `APLICACIÓN`, `SÚPLICA`).

## Formato visual
Consultar `FORMAT_PROFILES.md`. Para `casp-calderon`:
- Letter;
- Times New Roman 12 pt;
- líneas laterales rojas en todas las páginas: izquierda doble, derecha sencilla;
- cuerpo justificado;
- título centrado + bold + underline;
- `CERTIFICADO DE NOTIFICACIÓN` centrado + bold + underline;
- énfasis selectivo consistente con la muestra;
- paginación centrada con guiones cuando corresponda.

Cuando se solicite DOCX y el entorno permita ejecutar el renderer, usar `motion_docx.py`. Si el agente genera el DOCX por otro mecanismo, debe reproducir igualmente el perfil y no degradarlo a un documento genérico.

## Algoritmo
1. Clasificar foro, motion_type y estilo attorney-authored.
2. Activar automáticamente plantilla canónica cuando corresponda.
3. Leer la referencia canónica completa antes de redactar.
4. Separar datos variables de lenguaje fijo del modelo.
5. Redactar sustituyendo datos, no reescribiendo el modelo desde cero.
6. Eliminar cualquier ampliación no requerida.
7. Aplicar formato visual.
8. Comparar salida contra la checklist del perfil.
9. Si falla un elemento obligatorio o incurre en una prohibición, corregir/regenerar.
10. Entregar solo después de pasar el quality gate.

## Quality gate CASP / Asumiendo Representación
La salida NO está lista hasta que todas sean `sí`:
- ¿incluye `SAN JUAN, PUERTO RICO`?
- ¿epígrafe usa `Apelante/Apelado(a)` sin `Parte`?
- ¿usa `Caso Núm.`?
- ¿título es `MOCIÓN ASUMIENDO NUEVA REPRESENTACIÓN` sin `LEGAL` salvo instrucción?
- ¿título está subrayado además de negrita?
- ¿saludo exacto dice `A LA HONORABLE COMISIÓN U COMISIONADA ASOCIADA`?
- ¿comparecencia usa `abogado que suscribe`?
- ¿cuerpo conserva cuatro párrafos canónicos salvo necesidad real?
- ¿párrafos comienzan con `Que`?
- ¿no hay quinto párrafo redundante con dirección?
- ¿súplica usa `declare CON LUGAR` y `autorice nuestra representación legal`?
- ¿súplica no fue convertida en lista de subincisos?
- ¿`RESPETUOSAMENTE SOMETIDO.` precede fecha/firma?
- ¿certificado aparece después del bloque principal?
- ¿no se inventó ningún hecho procesal?

Si cualquiera es `no`, no entregar todavía.

## Salida
Cuando se solicite Word, generar `.docx`; no limitarse a describir formato. Toda moción requiere revisión final del abogado antes de presentación.
