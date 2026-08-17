---
name: pr-notarial-instrument-drafting
title: Redacción de Instrumentos Notariales de Puerto Rico
description: Redacta instrumentos públicos de Puerto Rico —escrituras públicas y actas notariales— con contenido jurídico verificado y con formato protocolar puertorriqueño fiel a los modelos de referencia del proyecto. Utilizar cuando el usuario solicite redactar, preparar, revisar, adaptar, corregir o estructurar una escritura, acta, poder, donación, compraventa, opción, repudiación de herencia, hogar seguro u otro instrumento público para autorización por un notario o notaria de Puerto Rico.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.3.0
execution_mode: open
jurisdiction: pr
practice: notarial
language: es
---

# Redacción de Instrumentos Notariales de Puerto Rico

## Misión

La misión principal de este skill es **producir instrumentos públicos con apariencia, arquitectura y lenguaje notarial puertorriqueño**, no memorandos, bosquejos ni contratos genéricos.

Cuando el usuario pide “redacta”, “prepara”, “haz la escritura”, “haz el acta” o equivalente, el resultado debe parecerse a un instrumento protocolar listo para pasar a revisión notarial y, cuando el entorno permita crear archivos, debe entregarse preferentemente como **DOCX editable**.

El formato visual obligatorio se define en [`pr/notarial/FORMAT_SPEC.md`](../../FORMAT_SPEC.md). **Ese archivo forma parte de este skill y debe aplicarse en todo instrumento final.**

Este skill no sustituye los deberes personales e indelegables del notario o notaria autorizante: identificación de comparecientes, juicio de capacidad, consentimiento, asesoramiento, imparcialidad, unidad de acto cuando corresponda, autorización, signo, firma, rúbrica, sello, custodia del protocolo, expedición de copias, presentación registral y cumplimiento contributivo.

## Regla fundamental: contenido correcto + formato fiel

El instrumento final debe satisfacer simultáneamente dos exigencias:

1. **Corrección jurídica:** el contenido debe responder a los hechos y al derecho vigente.
2. **Fidelidad formal:** la presentación debe seguir la estructura visual de los modelos notariales puertorriqueños del proyecto.

No sacrificar una por la otra. Si un modelo contiene un error, se conserva su **formato**, no el error.

## Jerarquía de fuentes rectoras

Antes de afirmar que una cláusula, advertencia, formalidad, gestión contributiva, requisito registral o consecuencia legal es obligatoria, verificar la autoridad vigente. Aplicar, según corresponda:

1. **Ley Notarial de Puerto Rico**, Ley Núm. 75 de 2 de julio de 1987, según enmendada (4 L.P.R.A. § 2001 et seq.).
2. **Reglamento Notarial de Puerto Rico**, así como reglas y órdenes vigentes del Tribunal Supremo de Puerto Rico y de la Oficina de Inspección de Notarías (ODIN).
3. **Código Civil de Puerto Rico de 2020** y leyes especiales aplicables.
4. **Ley del Registro de la Propiedad Inmobiliaria de Puerto Rico** y normativa registral vigente cuando se trate de bienes inmuebles.
5. Estatutos contributivos de Puerto Rico, determinaciones de Hacienda, requisitos del CRIM y derecho municipal o federal aplicable.
6. **Reglas de Conducta Profesional de Puerto Rico** vigentes.
7. Jurisprudencia vinculante del Tribunal Supremo de Puerto Rico.

No asumir que una cita o advertencia de un instrumento viejo sigue vigente solamente porque aparece en un modelo.

## Regla de prioridad para modelos y plantillas

Cuando existan referencias visuales, utilizar este orden:

1. plantilla editable expresamente suministrada por el usuario para el instrumento específico;
2. instrumento modelo del mismo tipo suministrado por el usuario;
3. `pr/notarial/FORMAT_SPEC.md`;
4. convenciones notariales puertorriqueñas generales.

Si el usuario entrega un PDF de ejemplo, estudiar tanto su texto como su distribución visual antes de redactar.

## Primera decisión: escritura o acta

### Escritura pública

Utilizar escritura cuando se formalice un negocio jurídico, declaración de voluntad, transmisión, aceptación, renuncia, poder, constitución, modificación o extinción de derechos u otro acto dispositivo que corresponda documentar mediante escritura pública.

### Acta notarial

Utilizar acta cuando el notario consigne hechos, circunstancias, manifestaciones, requerimientos, presencia, notoriedad, protocolización u otras materias propias de la fe notarial que no se estructuren como negocio jurídico dispositivo.

Si la clasificación no es clara, detenerse y señalar qué autoridad o dato debe verificarse antes de autorizar.

## Lista de cotejo previa a la redacción

Obtener o marcar como pendiente, según corresponda:

### A. Instrumento y notario

- tipo y propósito del instrumento;
- número de orden en el protocolo;
- lugar y fecha exacta del otorgamiento;
- nombre del notario o notaria y los datos que legalmente deban consignarse;
- necesidad de testigos, intérpretes, representantes, oficiales corporativos, fiduciarios, tutores, apoderados u otros comparecientes especiales;
- si existe un instrumento modelo o plantilla que deba reproducirse.

### B. Comparecientes

Para cada persona o entidad:

- nombre legal exacto;
- mayoría de edad;
- estado civil y régimen económico matrimonial cuando sea material;
- ocupación o profesión cuando corresponda;
- vecindad;
- capacidad en que comparece;
- designación de parte que se mantendrá de forma uniforme;
- método de identificación realmente utilizado;
- autoridad representativa y documento que la acredita, cuando aplique;
- hechos de capacidad y voluntariedad que el notario debe apreciar personalmente.

Nunca inventar número de licencia, seguro social, EIN, RUA, poder, resolución corporativa, orden judicial, identificación o dato personal para “completar” el instrumento.

### C. Negocio jurídico

- acto jurídico exacto que se formaliza;
- título u origen del derecho;
- precio, valor, contraprestación o liberalidad;
- condiciones y términos;
- reservas y limitaciones;
- fecha de efectividad;
- consentimientos y aceptaciones necesarios;
- obligaciones posteriores al otorgamiento.

### D. Bien inmueble

Cuando se trate de inmueble, requerir o señalar como pendiente:

- descripción registral exacta y completa;
- finca, folio, tomo, inscripción y sección/demarcación registral, según corresponda;
- título de adquisición;
- número de catastro;
- porcentajes o cuotas de titularidad;
- cargas y gravámenes;
- hipotecas, servidumbres, anotaciones y condiciones;
- estudio de título o certificación y su fecha;
- estatus CRIM y cuestiones contributivas;
- hogar seguro, zona inundable, condominio, restricciones, sucesiones, comunidad de bienes u otras leyes especiales pertinentes;
- quién presentará el instrumento al Registro y qué gestiones posteriores corresponden.

No conciliar silenciosamente discrepancias entre descripción registral, catastro, estudio de título, escritura de adquisición, porcentajes o cargas.

## Algoritmo de trabajo

1. **Identificar el acto jurídico.** Precisar qué se transmite, constituye, acepta, renuncia, declara, autoriza o hace constar.
2. **Seleccionar el vehículo notarial.** Escritura o acta.
3. **Verificar derecho vigente.** Formalidades, capacidad, consentimiento, advertencias, requisitos registrales, contributivos y posteriores al otorgamiento.
4. **Validar comparecientes.** Nombres, estado civil, representación, autoridad y designaciones.
5. **Construir mapa de hechos.** Cada elemento jurídico debe tener un hecho o documento que lo sostenga.
6. **Seleccionar el modelo visual más cercano.** Identificar la plantilla o instrumento de referencia aplicable.
7. **Redactar en estilo protocolar desde el comienzo.** No redactar primero como memo para “convertirlo” después.
8. **Añadir advertencias específicas.** Solo las pertinentes al acto y al derecho vigente.
9. **Auditar datos registrales y cifras.** No alterar una descripción registral por razones estilísticas.
10. **Redactar cierre notarial completo.** Lectura, ratificación, firmas, iniciales, testigos, autorización y fe según los hechos reales.
11. **Preparar nota de saca y certificación, cuando proceda.** Separadas del cuerpo según `FORMAT_SPEC.md`.
12. **Generar DOCX cuando sea posible.** Aplicar el formato de página y composición obligatoria.
13. **Comparar visualmente contra el modelo.** Corregir cualquier apariencia de memo, contrato privado o documento genérico.
14. **Ejecutar auditoría final de contenido y formato.**

## Formato de salida obligatorio

### Regla de entrega

Cuando el usuario solicite el instrumento final y el entorno permita generar archivos:

- crear **DOCX editable**;
- usar **papel legal 8.5 x 14** salvo que la plantilla disponga otra cosa;
- reproducir la zona marginal izquierda/tomo y el cuerpo/folio;
- incluir los encabezados, guiones y cierres conforme a `FORMAT_SPEC.md`;
- si el usuario pide PDF, generar además una copia PDF sin sustituir el DOCX editable.

No entregar solamente una explicación seguida de un bloque de texto si es posible generar el documento.

### Estructura visual base

La apertura debe seguir la arquitectura:

```text
-----------------------ESCRITURA NÚMERO [___] ([___])-----------------------
-----------------------------[TÍTULO DEL ACTO]------------------------------
---En la ciudad de [MUNICIPIO], Puerto Rico, a [FECHA].---------------------
-------------------------------------ANTE MÍ---------------------------------
---[NOTARIO/A].-------------------------------------------------------------
----------------------------------COMPARECE(N)-------------------------------
---[COMPARECIENTES].--------------------------------------------------------
--------------------------------------DOY FE---------------------------------
---[IDENTIFICACIÓN, CAPACIDAD Y VOLUNTARIEDAD].----------------------------
-------------------------------------EXPONE(N)-------------------------------
---PRIMERO: ...-------------------------------------------------------------
---SEGUNDO: ...-------------------------------------------------------------
```

Los encabezados no deben convertirse en títulos Markdown ni estilos gráficos modernos.

### Guiones

- Utilizar guiones antes y después de los encabezados como en los modelos.
- Iniciar párrafos materiales con `---` cuando corresponda.
- Completar con guiones el remanente de la última línea del párrafo cuando reproduzca el modelo.
- No sustituir automáticamente los guiones por em dash, reglas horizontales, bullets o listas de Word.

### Partes

Usar denominaciones consistentes y en mayúsculas cuando el modelo lo haga: `DONANTE`, `DONATARIO`, `VENDEDORA`, `COMPRADORA`, `PODERDANTE`, `APODERADO`, `REQUIRENTE`, etc.

### Descripción registral

Reproducirla **íntegramente**, sin resumir, parafrasear, modernizar o “corregir” colindancias. Si existe un posible error registral, marcarlo para verificación sin alterar silenciosamente el texto fuente.

### Nota de saca

La nota de saca no es una cláusula del negocio. Debe aparecer en la **zona marginal izquierda/tomo** en el formato del modelo, cuando corresponda.

En borradores, si aún no se ha expedido copia, usar un marcador como:

`[NOTA DE SACA — COMPLETAR AL EXPEDIR COPIA CERTIFICADA]`

Nunca afirmar que se expidió una copia si todavía no ocurrió.

### Certificación de copia

La certificación debe prepararse como bloque separado de la matriz y seguir la arquitectura definida en `FORMAT_SPEC.md`. No inventar número de folios, sellos cancelados, fecha de expedición ni persona con interés.

### Folio y tomo

No confundir el folio protocolar con el número de página de Word/PDF. Reservar el área correspondiente y usar `[FOLIO ___]` cuando el dato real aún no esté disponible.

## Módulos por tipo de instrumento

### Donación

Verificar como mínimo:

- titularidad y capacidad dispositiva del donante;
- identidad y aceptación del donatario;
- bien y valor;
- reservas, usufructo, condiciones, prohibiciones, reversión o revocación;
- legítima y límites sucesorios pertinentes;
- obligaciones contributivas vigentes;
- efectos registrales y CRIM.

No copiar automáticamente advertencias contributivas de una donación antigua.

### Compraventa / opción / promesa

Verificar:

- propiedad o participación exacta;
- porcentaje de titularidad;
- precio o mecanismo objetivo para determinarlo;
- contraprestación de opción, si existe;
- término y forma de ejercicio;
- contingencias de financiamiento;
- contribuciones, utilidades, cierre, posesión y riesgo;
- cargas que se cancelarán o permanecerán;
- inscribibilidad del acuerdo;
- coherencia entre todos los términos y fechas.

Si dos cláusulas establecen plazos incompatibles, no escoger una silenciosamente: señalar y resolver la contradicción antes de producir la versión final.

### Poder / poder duradero

Verificar:

- base legal y efecto del poder;
- poderdantes, apoderados y sustitutos;
- facultades específicas;
- facultades que exijan autorización expresa;
- bienes inmuebles, cuentas, litigios, Hacienda, CRIM, información médica, activos digitales y demás materias pertinentes;
- autocontratación, donaciones o conflictos de interés cuando sean relevantes;
- límites sobre residencia principal u otros bienes protegidos;
- revocación, sustitución, incapacidad y terminación.

### Repudiación de herencia

Verificar:

- causante y fecha/lugar de fallecimiento;
- título por el cual la persona es llamada a heredar;
- sucesión testada o intestada;
- formalidades vigentes de repudiación;
- capacidad;
- efectos, indivisibilidad y consecuencias frente a acreedores;
- posible aceptación previa expresa o tácita.

### Hogar seguro

Verificar:

- elegibilidad;
- titularidad;
- residencia principal;
- inexistencia de designación incompatible;
- descripción registral y catastro;
- excepciones y efectos vigentes;
- anotación registral;
- consecuencias familiares y sucesorias aplicables.

## Identificación, capacidad y fe notarial

### Identificación

Redactar únicamente lo que el notario realmente conoce o verificará conforme al derecho aplicable. Distinguir conocimiento personal de medios supletorios de identificación.

### Capacidad

El skill puede redactar la fórmula notarial, pero no sustituye el juicio personal del notario. Si existe duda sobre capacidad, coerción, influencia indebida, comprensión del idioma o voluntariedad, detenerse y señalarlo.

### `DOY FE`

No afirmar como hecho notarial algo que el modelo no puede presenciar o verificar. En borradores, la fórmula puede quedar preparada para la autorización, pero debe corresponder a hechos que el notario confirmará personalmente.

## Representación

Cuando una persona comparezca en representación de otra:

- identificar representante y representado;
- describir la fuente de autoridad;
- verificar suficiencia de facultades;
- consignar datos del poder, resolución, nombramiento u otra fuente únicamente si están verificados;
- no inventar RUA, número de escritura, fecha, notario o registro de poder.

## Testigos e intérpretes

No incluir renuncia o intervención de testigos de forma mecánica. Determinar primero si la ley y las circunstancias requieren testigos o intérprete y redactar conforme a lo realmente ocurrido.

## Advertencias

Las advertencias deben ser **específicas al acto**, no un depósito de boilerplate.

Antes de insertar una advertencia tomada de un modelo viejo, verificar:

- si la ley citada sigue vigente;
- si el artículo sigue siendo el mismo;
- si el término contributivo cambió;
- si la agencia o procedimiento sigue existiendo bajo ese nombre;
- si la advertencia aplica a los hechos del nuevo instrumento.

## Registro, CRIM y Hacienda

Cuando el instrumento afecte bienes inmuebles:

- verificar cargas y titularidad;
- verificar catastro;
- identificar obligaciones ante CRIM;
- identificar documentos o planillas informativas pertinentes;
- verificar advertencias y deberes registrales;
- identificar quién presentará el instrumento;
- no asumir que un estudio de título cierra el Registro ni que ausencia de información significa ausencia de cargas.

## Sellos, copias y protocolo

No afirmar que existen, fueron adheridos, cancelados o expedidos sellos, copias o certificaciones que no consten realmente.

Cuando el usuario pida una copia certificada, nota de saca o certificación, utilizar `FORMAT_SPEC.md` y los datos reales de expedición.

## Modos de salida

### Modo A — Instrumento final

Activar cuando el usuario pide redactar o preparar el instrumento. Entregar el instrumento, no un memo. Cuando sea posible, crear DOCX.

### Modo B — Intake

Si faltan datos esenciales que impiden una redacción jurídicamente responsable, entregar una lista breve y específica de los datos indispensables que faltan.

No convertir cualquier dato menor en una excusa para no redactar. Puede prepararse un borrador con `[FALTA INFORMACIÓN]` o `[VERIFICAR]` cuando ello permita avanzar sin inventar.

### Modo C — Revisión

Al revisar una escritura o acta existente, separar:

1. impedimentos para autorización;
2. problemas sustantivos;
3. formalidades notariales;
4. problemas registrales/contributivos;
5. inconsistencias internas;
6. errores de formato frente al modelo;
7. lenguaje de reemplazo recomendado.

### Modo D — Conversión a formato protocolar

Si el usuario suministra un borrador jurídicamente completo y pide “ponlo en formato de escritura/acta”, no reescribir innecesariamente el negocio. Convertirlo al formato visual definido por el modelo y `FORMAT_SPEC.md`, preservando el contenido salvo correcciones necesarias.

## Auditoría final obligatoria

Antes de entregar un instrumento final verificar:

### Contenido

- [ ] acto jurídico correctamente identificado;
- [ ] escritura vs. acta correctamente seleccionado;
- [ ] nombres y roles consistentes;
- [ ] representación verificada;
- [ ] datos registrales consistentes;
- [ ] porcentajes correctos;
- [ ] cifras y fechas coherentes;
- [ ] condiciones y términos no se contradicen;
- [ ] advertencias actuales y pertinentes;
- [ ] requisitos CRIM/Hacienda/Registro identificados;
- [ ] ninguna cita legal inventada;
- [ ] ningún hecho inventado.

### Formato

- [ ] aplicado `FORMAT_SPEC.md`;
- [ ] papel legal o plantilla correcta;
- [ ] zona tomo/margen separada del folio cuando corresponda;
- [ ] encabezados centrados con guiones;
- [ ] `ANTE MÍ`, `COMPARECE(N)`, `DOY FE`, `EXPONE(N)` en estilo de modelo;
- [ ] párrafos con estilo notarial de guiones;
- [ ] descripción registral íntegra;
- [ ] sin bullets ni apariencia de memo;
- [ ] nota de saca en margen/tomo, no dentro del negocio;
- [ ] folio reservado correctamente;
- [ ] cierre completo de lectura/autorización;
- [ ] firmas y espacios apropiados;
- [ ] certificación separada cuando aplique;
- [ ] DOCX visualmente comparable al instrumento modelo.

## Guardrails estrictos

- Nunca inventar hechos para completar la apariencia del instrumento.
- Nunca fabricar cita legal, dato registral, resultado de estudio de título, certificación, estatus contributivo, identificación, firma, testigo, sello, nota de saca o expedición de copia.
- Nunca resumir una descripción registral para ahorrar espacio.
- Nunca entregar un “instrumento final” con estética de memorando si el entorno permite aplicar el formato protocolar.
- Nunca copiar un error de un modelo únicamente para lograr fidelidad visual.
- Nunca afirmar que el modelo autorizó, presenció o dio fe de hechos reales.
- El notario o notaria autorizante debe revisar independientemente el instrumento y ejercer los deberes notariales indelegables.

Cerrar con el descargo de responsabilidad obligatorio de `pr/CLAUDE.md` cuando corresponda.