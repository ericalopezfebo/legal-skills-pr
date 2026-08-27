---
name: pr-motion-drafting
title: Puerto Rico Motion Drafting Engine
description: Redacta, revisa y estructura mociones para tribunales y foros administrativos de Puerto Rico, usando vocabulario forense local, perfiles por foro y una capa de producción DOCX que puede reproducir epígrafes, mayúsculas/negritas, márgenes, líneas laterales y bloques de firma sin confundir estilo de oficina con requisitos oficiales.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 1.0.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Puerto Rico Motion Drafting Engine

## Propósito

Este skill no se limita a “escribir una moción”. Debe producir un escrito que:

1. use el vehículo procesal correcto;
2. emplee la arquitectura y el vocabulario propios de la práctica puertorriqueña;
3. seleccione el perfil de foro correcto;
4. preserve la jerarquía entre formato oficial y estilo de oficina;
5. pueda convertirse a un `.docx` con formato reproducible mediante `motion_docx.py`.

Nunca represente una convención visual observada en modelos privados como requisito oficial del tribunal o agencia.

## Fuente empírica de estilo

El diseño de este skill se apoya en mociones reales y modelos suministrados por abogados puertorriqueños, incluyendo escritos ante CASP, Juntas de Apelaciones y el Tribunal de Primera Instancia. Esas muestras se usan para aprender **arquitectura, vocabulario y convenciones visuales**, no para reutilizar hechos, nombres, argumentos, datos de contacto o conclusiones jurídicas.

Jerarquía de fuentes de formato:

1. formulario, reglamento, orden o instrucción oficial vigente del foro;
2. regla procesal aplicable;
3. muestra reciente del mismo foro;
4. muestra reciente de otro foro puertorriqueño;
5. muestra histórica, solo como referencia estilística.

## Entrada mínima

Recibir o inferir, sin inventar:

- `forum_profile`: `tpi`, `casp`, `aep-ja`, `appellate`, `supreme`, `admin-generic`;
- `motion_type`;
- número de caso y sala cuando aplique;
- partes y designación procesal;
- parte representada;
- orden, controversia o evento activador;
- hechos confirmados y su fuente;
- remedio principal y alterno;
- autoridad jurídica disponible;
- fecha prevista;
- anexos;
- datos de firma y notificación;
- `visual_profile`: `official-neutral` o `pr-litigation-redline`.

Si falta un dato que cambia jurisdicción, término, carga, remedio, certificación o identidad de las partes, usar marcador `[POR COMPLETAR]` y no inventar.

## Perfil por foro

### `tpi` — Tribunal de Primera Instancia

Usar, salvo instrucciones particulares del tribunal:

- encabezado institucional del TPI y sala;
- epígrafe con `Civil Núm.`, sala y `Sobre:`;
- título centrado y descriptivo;
- saludo `AL HONORABLE TRIBUNAL:`;
- comparecencia según postura: `COMPARECE` / `COMPARECEN`;
- cierre dirigido a `este Honorable Tribunal`.

### `casp` — Comisión Apelativa del Servicio Público

Usar, sujeto a modelo oficial vigente:

- `GOBIERNO DE PUERTO RICO`;
- `COMISIÓN APELATIVA DEL SERVICIO PÚBLICO`;
- epígrafe con `Caso Núm.` y `SOBRE:`;
- designaciones `Promovente` / `Promovido` o las que correspondan al expediente;
- saludo `A LA HONORABLE COMISIÓN:` o la variante oficial vigente;
- cierre dirigido a `esta Honorable Comisión`.

### `aep-ja` — Junta de Apelaciones de la AEP

Usar:

- `AUTORIDAD DE EDIFICIOS PÚBLICOS`;
- `JUNTA DE APELACIONES`;
- `SAN JUAN, PUERTO RICO` cuando corresponda al modelo;
- `Caso Núm.` o `CIVIL NÚM.` según el expediente/modelo vigente;
- designaciones `Apelante` / `Apelada`;
- saludo `A LA HONORABLE JUNTA:`;
- cierre dirigido a `esta Honorable Junta`.

### `appellate`, `supreme`, `admin-generic`

No inventar formato. Obtener primero las reglas, instrucciones, orden o muestra oficial del foro. Si no existe, usar estructura puertorriqueña neutral y marcar `[VERIFICAR FORMATO DEL FORO]`.

## Tipos de moción

Clasificar antes de redactar. Entre otros:

- asumiendo representación;
- relevo o renuncia de representación;
- prórroga;
- cumplimiento de orden;
- mostrar causa;
- informativa;
- solicitud de orden;
- solicitud de vista;
- cambio de señalamiento;
- oposición;
- réplica;
- reconsideración;
- desestimación;
- resolución o sentencia sumaria;
- descubrimiento de prueba;
- anotación o relevo de rebeldía.

El título debe construirse dinámicamente cuando el escrito acumule remedios, por ejemplo: `MOCIÓN EN CUMPLIMIENTO DE ORDEN, EN OPOSICIÓN A ... Y EN SOLICITUD DE ...`.

## Arquitectura de contenido

### Moción breve o administrativa

1. encabezado institucional;
2. epígrafe;
3. título;
4. saludo al foro;
5. comparecencia;
6. hechos/proposiciones numeradas;
7. petición (`POR TODO LO CUAL` o `POR LO EXPUESTO`);
8. certificación;
9. `RESPETUOSAMENTE SOMETIDO/A`;
10. lugar y fecha;
11. bloque de firma.

### Moción sustantiva

Cuando el asunto requiera análisis jurídico, añadir solo las secciones necesarias:

- `I. HECHOS`;
- `II. TRÁCTO PROCESAL`;
- `III. DERECHO APLICABLE` o encabezado funcional equivalente;
- `IV. APLICACIÓN A LOS HECHOS`;
- `SÚPLICA` o petición final.

No imponer estas secciones a una moción de una página si no aportan.

## Vocabulario forense puertorriqueño

Puede usar, cuando corresponda y sin abuso:

- `caso de epígrafe` / `caso de autos`;
- `parte promovente`, `parte promovida`, `apelante`, `apelada`, `demandante`, `demandada`;
- `por conducto del abogado que suscribe` / `por conducto de la representación legal que suscribe`;
- `muy respetuosamente EXPONE, ALEGA Y SOLICITA:`;
- `este Honorable Foro`, `esta Honorable Comisión`, `esta Honorable Junta`, `este Honorable Tribunal`;
- `tome conocimiento de lo expuesto`;
- `se dé por cumplida la Orden`;
- `declare HA LUGAR` / `declare NO HA LUGAR`, cuando ese modo de súplica sea apropiado;
- `con cualquier otro pronunciamiento/remedio que en derecho proceda`;
- `dirección de récord`;
- `POR TODO LO CUAL` / `POR LO EXPUESTO`;
- `RESPETUOSAMENTE SOMETIDO`, `SOMETIDA` o `SOMETIDOS`, según corresponda;
- `CERTIFICO` / `CERTIFICACIÓN DE NOTIFICACIÓN`.

### Disciplina de vocabulario

No usar fórmulas ceremoniales por reflejo. Preferir precisión. Evitar:

- repetir `muy respetuosamente` varias veces en la misma súplica;
- `marras`, `ut supra`, `susodicho` u otros arcaísmos si una frase más clara sirve mejor;
- llamar `radicado` a todo escrito cuando `presentado` sea más claro, salvo uso deliberado del foro;
- convertir mayúsculas en sustituto de argumentación.

## Reglas de mayúsculas y negritas

Aplicar como convención visual, no como regla sustantiva:

- encabezado institucional: MAYÚSCULAS + negrita + centrado;
- nombres de partes principales en epígrafe: normalmente MAYÚSCULAS + negrita;
- título de la moción: MAYÚSCULAS + negrita + centrado;
- `AL/A LA HONORABLE ...:`: negrita;
- `COMPARECE`, `EXPONE`, `ALEGA`, `SOLICITA`, `POR TODO LO CUAL`, `POR LO EXPUESTO`, `SÚPLICA`, `CERTIFICO`, `RESPETUOSAMENTE SOMETIDO/A`: negrita y, cuando el modelo lo use, mayúsculas;
- encabezados sustantivos: negrita; preferiblemente números romanos o encabezados funcionales consistentes.

No poner todo el cuerpo en negrita ni mayúsculas.

## Perfil visual `pr-litigation-redline`

Este perfil reproduce un **estilo observado en las muestras DOCX**, no un requisito oficial general de Puerto Rico.

Parámetros empíricos:

- página: Letter, 8.5 × 11 pulgadas;
- margen izquierdo: 1.5 pulgadas;
- margen derecho: 0.5 pulgadas;
- margen superior: aproximadamente 0.625 pulgadas en escritos recientes;
- margen inferior: aproximadamente 0.3125 pulgadas en escritos recientes;
- línea lateral izquierda: roja, doble, 1.5 pt, separada aproximadamente 4 pt del texto;
- línea lateral derecha: roja, sencilla, 1.5 pt, separada aproximadamente 4 pt del texto;
- fuente predominante en las muestras recientes: Times New Roman 12 pt;
- algunas muestras anteriores usan Book Antiqua 12 pt: no mezclar fuentes dentro del mismo escrito;
- epígrafe: tabla de dos columnas sin bordes exteriores visibles, con división vertical central y borde inferior/vertical doble donde corresponda;
- cuerpo: justificado;
- numeración de páginas cuando el escrito exceda una página;
- bloque de firma separado del cuerpo con espacio suficiente para legibilidad.

`motion_docx.py` implementa este perfil de manera reproducible.

## Perfil visual `official-neutral`

Usar cuando exista modelo oficial o cuando no deba imponerse estilo de oficina:

- Letter;
- márgenes y fuente conforme a reglas o formulario del foro;
- sin líneas rojas salvo que el usuario lo pida expresamente;
- epígrafe conforme al modelo oficial;
- título centrado;
- cuerpo legible y consistente.

## Epígrafe

Construir el epígrafe como tabla, no mediante espacios o tabuladores frágiles.

Columna izquierda:

- nombre de parte(s);
- designación procesal;
- `v.` o `vs.` según el modelo seleccionado;
- contraparte;
- designación.

Columna derecha:

- `Caso Núm.` / `Civil Núm.`;
- sala, cuando aplique;
- `SOBRE:`;
- naturaleza del caso.

El epígrafe debe poder sobrevivir cambios de nombre, longitud y tamaño de fuente sin desalinearse.

## Moción en cumplimiento de orden

Cuando responda a una orden:

1. identificar la orden y fecha;
2. enumerar cada mandato material;
3. contestar cada mandato separadamente;
4. indicar qué se cumplió, cómo y con qué anejo;
5. identificar lo que no pueda cumplirse y explicar la razón sustentada;
6. solicitar expresamente que el foro `tome conocimiento` y `dé por cumplida` la orden solo si el récord lo sostiene;
7. no convertir cumplimiento en reconsideración encubierta.

## Control anti-contaminación

De las muestras se puede aprender formato y estilo. No se puede copiar automáticamente:

- nombres;
- hechos;
- direcciones;
- emails;
- teléfonos;
- RUA;
- número de caso;
- citas jurídicas;
- argumentos;
- anexos;
- firmas;
- teorías del caso.

Los errores de un borrador tampoco son precedentes. Si una muestra contiene texto pendiente, errores de edición, nombre incorrecto de agencia o alternativas sin resolver, marcarlos como defecto y no reproducirlos.

## Algoritmo

1. **Clasificar foro y motion_type.**
2. **Verificar fuente oficial de formato.** El modelo oficial prevalece sobre muestras privadas.
3. **Seleccionar visual_profile.** Nunca activar líneas rojas como si fueran requisito oficial.
4. **Verificar marco jurídico.** Regla, estatuto, reglamento, orden, término y carga.
5. **Construir cronología y mapa de fuentes.** Separar hechos confirmados, alegaciones, inferencias y derecho.
6. **Elegir arquitectura breve o sustantiva.**
7. **Redactar con vocabulario puertorriqueño controlado.**
8. **Diseñar la súplica con remedios concretos y congruentes.**
9. **Generar certificación según medio real de notificación.** No afirmar SUMAC, email, correo o notificación automática si no está confirmado.
10. **Aplicar formato.** Usar `FORMAT_PROFILES.md` y, para DOCX, `motion_docx.py`.
11. **Auditar contaminación.** Comparar nombres, contactos y hechos contra las muestras y eliminar cualquier dato heredado.
12. **Auditar presentación.** Revisar encabezado, epígrafe, título, negritas, mayúsculas, numeración, márgenes, bordes, firma, notificación y legibilidad.
13. **Auditar sustancia.** Coordinar con `pr-legal-writing-review`, `pr-citation-verifier` y `pr-filing-readiness`.

## Contrato de salida

Cuando el usuario pida solo el texto, entregar el borrador completo con marcadores mínimos pendientes.

Cuando pida una moción lista para Word, entregar además una especificación estructurada compatible con `motion_docx.py`:

```yaml
forum_profile: casp
visual_profile: pr-litigation-redline
case_number: SA-00-000000
matter: "[SOBRE]"
title: "MOCIÓN ..."
parties:
  left:
    - name: "[PARTE]"
      role: "Promovente"
    - name: "[PARTE]"
      role: "Promovido"
body:
  - "1. ..."
prayer: "POR TODO LO CUAL, ..."
certification: "CERTIFICO: ..."
signature:
  name: "[ABOGADO/A]"
  rua: "[RUA]"
  address: "[DIRECCIÓN]"
  phone: "[TELÉFONO]"
  email: "[EMAIL]"
```

Finalizar con:

- información faltante;
- autoridades pendientes de verificación;
- anexos pendientes;
- `REVISIÓN DE ABOGADO REQUERIDA`.

Cumplir con `pr/CLAUDE.md`. La fidelidad visual nunca sustituye la corrección jurídica.