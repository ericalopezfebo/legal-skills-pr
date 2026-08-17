# Especificación de formato — instrumentos notariales de Puerto Rico

Esta especificación es **obligatoria** para `pr-notarial-instrument-drafting` cuando el usuario pide preparar o redactar un instrumento público final. Su propósito es reproducir el estilo protocolar de los modelos de referencia del proyecto, no entregar un memo ni un documento jurídico genérico.

## Regla de prioridad visual

Cuando exista más de una referencia, aplique este orden:

1. plantilla editable expresamente suministrada por el usuario para ese instrumento;
2. instrumento modelo suministrado por el usuario para ese tipo de negocio;
3. esta especificación;
4. convenciones notariales generales.

El contenido jurídico vigente controla sobre cualquier error sustantivo del modelo, pero **el formato visual del modelo controla** salvo que sea imposible o contrario a una formalidad obligatoria.

## Producto final esperado

Cuando el entorno permita crear archivos y el usuario pida “prepara”, “redacta”, “haz la escritura”, “haz el acta” o equivalente, el resultado preferido es un **DOCX editable** con formato notarial. Si también se solicita PDF, produzca ambos. No sustituya el instrumento por una explicación en Markdown.

Si el entorno no permite crear DOCX, entregue el texto en formato monoespaciado o plano reproduciendo la arquitectura visual, encabezados, guiones, orden y bloques del instrumento.

## Página y composición

- Formato base: **papel legal 8.5 x 14 pulgadas**, salvo que la plantilla del usuario disponga otra cosa.
- El instrumento debe conservar una **zona marginal izquierda / tomo** separada del cuerpo o folio, como en los modelos de referencia.
- El cuerpo principal ocupa el **folio** a la derecha de esa zona marginal.
- No colocar texto sustantivo del negocio en el área reservada para tomo/nota de saca.
- En el primer folio, la **nota de saca** puede ocupar el área marginal izquierda cuando corresponda.
- Mantener espacio suficiente para signos, rúbrica, sello, firmas e iniciales sin comprimir el texto.
- Mantener continuidad de página: no dejar un encabezado aislado al final de una página si puede mantenerse unido al párrafo que sigue.

## Arquitectura visual obligatoria

### 1. Encabezado del instrumento

El instrumento comienza con el número y el título, en mayúsculas, visualmente centrados y flanqueados por guiones:

```text
-----------------------ESCRITURA NÚMERO [___] ([___])-----------------------
-----------------------------[TÍTULO DEL ACTO]------------------------------
```

Para actas puede mantenerse `ESCRITURA NÚMERO ...` si así corresponde al protocolo/modelo utilizado, seguido del título específico del acta.

### 2. Lugar y fecha

Redactar en estilo notarial narrativo, con número en letras y cifra entre paréntesis cuando corresponda:

```text
---En la ciudad de [MUNICIPIO], Puerto Rico, a los [___] ([___]) días del mes de [___] del año [___] ([___]).----------------------------------------------
```

### 3. Encabezados internos

Usar encabezados centrados entre líneas de guiones, en mayúsculas, según corresponda:

```text
-------------------------------------ANTE MÍ-------------------------------------
----------------------------------COMPARECE(N)-----------------------------------
--------------------------------------DOY FE--------------------------------------
-------------------------------------EXPONE(N)------------------------------------
-----------------------------------ADVERTENCIAS----------------------------------
------------------------------------ACEPTACIÓN-----------------------------------
--------------------------LECTURA Y AUTORIZACIÓN-------------------------------
```

No convertir estos encabezados en encabezados Markdown, bullets ni numeración automática de Word.

### 4. Párrafos

- Iniciar los párrafos materiales con guiones, normalmente `---`.
- Usar `PRIMERO`, `SEGUNDO`, `TERCERO`, etc., en mayúsculas cuando el modelo lo haga.
- El final del párrafo debe completar visualmente la línea restante con guiones cuando corresponda.
- No usar listas con viñetas en el instrumento final. Si una cláusula requiere subincisos, usar letras o números en el estilo del modelo (`A:`, `B:`, `(a)`, `(b)`, etc.).
- Conservar las designaciones de partes en mayúsculas (`DONANTE`, `DONATARIO`, `VENDEDORA`, `COMPRADORA`, `PODERDANTE`, `APODERADO`, `REQUIRENTE`, etc.) de manera uniforme.

### 5. Descripciones registrales

- Reproducir la descripción registral **íntegra**, sin resumirla, modernizarla ni reescribir sus colindancias.
- Separarla mediante un encabezado del tipo:

```text
---------------------------DESCRIPCIÓN REGISTRAL-------------------------------
```

- Mantener finca, tomo, folio, inscripción, sección registral y catastro en bloques claros.
- Si un dato no está verificado, usar `[VERIFICAR ...]`; nunca fabricar el dato para completar la apariencia del instrumento.

### 6. Cantidades, fechas y números

Cuando el estilo notarial lo requiera, expresar primero en palabras y luego en cifras entre paréntesis. Ejemplos:

```text
ciento treinta y cinco mil dólares ($135,000.00)
veintinueve punto cinco nueve cinco metros (29.595 mts.)
treinta y uno (31) de marzo de dos mil veintitrés (2023)
```

No cambiar cifras de una descripción registral por razones de estilo.

## Nota de saca

La nota de saca es un bloque separado del cuerpo del instrumento y debe colocarse en la **zona marginal izquierda / tomo**, cuando corresponda. Modelo base:

```text
CERTIFICO que en esta misma
fecha, he expedido primera copia
certificada a favor de [NOMBRE],
quien es parte con interés.
DOY FE.---------------------------

____________________________
NOTARIO/A PÚBLICO/A
```

Reglas:

- No insertar la nota de saca como una cláusula numerada del negocio.
- No duplicarla dentro del cuerpo.
- Ajustar singular/plural, género y legitimación de la persona a cuyo favor se expide.
- No afirmar que se expidió copia si ese hecho no ha ocurrido; en un borrador usar `[NOTA DE SACA — COMPLETAR AL EXPEDIR COPIA]`.

## Folio y tomo

- El **folio** identifica la página del instrumento/protocolo y debe mantenerse en la zona correspondiente del cuerpo.
- El área de **tomo** se mantiene separada visualmente del folio, conforme al modelo protocolar.
- No confundir número de folio del protocolo con número de página de un PDF o DOCX.
- Si no se conoce el folio protocolar real, usar `[FOLIO ___]` o dejar el espacio reservado; no inventarlo.

## Cierre, firmas y autorización

El instrumento final no debe terminar en un simple `[FIRMAS]`. Debe incluir, según los hechos y la ley vigente, el bloque completo de lectura, ratificación, iniciales, firmas y fe notarial.

Modelo visual base:

```text
--------------------------LECTURA Y AUTORIZACIÓN-------------------------------
---[Fórmula de lectura, advertencias, ratificación e iniciales conforme a los hechos y al derecho vigente].--------------------------------------------------------------
---Y de todo lo contenido en este instrumento público, yo, el/la Notario/a, DOY FE.---------------------------------------------------------------------------------

FIRMAS

____________________________          ____________________________
[OTORGANTE]                           [OTORGANTE]

____________________________
NOTARIO/A PÚBLICO/A
```

La fórmula concreta debe corresponder a lo ocurrido realmente; no declarar lectura en alta voz, renuncia a lectura, intervención o renuncia de testigos, identificación, iniciales o firma si no consta.

## Certificación de copia

Cuando se solicite una copia certificada, tratar la certificación como un bloque separado de la matriz y redactarla siguiendo esta arquitectura:

```text
-----------------------------------CERTIFICACIÓN-----------------------------------
---Certifico que en el original aparecen las firmas e iniciales de los comparecientes.--------------------------------------------------------------------------------
---Firmado, rubricado, signado y sellado, [NOMBRE DEL/DE LA NOTARIO/A].-----------
---Tiene adheridos y cancelados los sellos que legalmente correspondan y constan las iniciales requeridas en los folios de la escritura matriz.--------------------------
---Corresponde bien y fielmente con el original de su contenido que obra en mi protocolo correspondiente al año [____], cuyo original consta de [___] folios.-----------
---En fe de lo cual, y para [PERSONA/ENTIDAD], expido la [primera/segunda/etc.] copia certificada, que firmo, rubrico, signo y sello, en [MUNICIPIO], Puerto Rico, hoy [FECHA]. DOY FE.----------------------------------------------------------
```

No afirmar cancelación de sellos, número de folios, protocolo, fecha de expedición o persona legitimada sin datos reales.

## Estilo tipográfico y de Word

Cuando se genere DOCX:

- reproducir el aspecto del modelo más cercano antes que aplicar estilos corporativos modernos;
- usar texto negro, fondo blanco y formato sobrio;
- evitar colores, íconos, cuadros decorativos, encabezados de diseño o estilos de informe;
- no usar tablas visibles para el cuerpo del instrumento;
- se permite usar una tabla **sin bordes visibles** o columnas internas únicamente como mecanismo técnico para separar tomo/nota de saca y folio, si ello reproduce mejor el modelo;
- mantener los encabezados internos en mayúsculas y centrados visualmente mediante guiones;
- no usar listas automáticas si alteran el aspecto notarial;
- desactivar autocorrecciones que sustituyan guiones por rayas largas o listas;
- evitar que Word convierta automáticamente números de cláusulas en listas multinivel.

## Fidelidad al modelo vs. corrección jurídica

La misión es **reproducir el formato, no reproducir errores**.

Si un modelo contiene:

- numeración duplicada;
- términos contradictorios;
- error de género o designación de parte;
- cita legal obsoleta;
- descripción registral inconsistente;
- advertencia que ya no corresponde;

el skill debe conservar la apariencia visual pero corregir o señalar el problema sustantivo antes de producir una versión final.

## Control final de fidelidad visual

Antes de entregar un instrumento final, verificar:

- [ ] papel y orientación coinciden con la plantilla/modelo aplicable;
- [ ] existe separación visual entre tomo/margen y folio cuando el modelo la requiere;
- [ ] número y título aparecen en el estilo de guiones del modelo;
- [ ] `ANTE MÍ`, `COMPARECE(N)`, `DOY FE`, `EXPONE(N)` y demás encabezados mantienen el estilo visual;
- [ ] párrafos comienzan y terminan con los guiones correspondientes;
- [ ] no hay bullets ni estética de memo;
- [ ] descripción registral está completa;
- [ ] nota de saca está en el margen/tomo, no en el cuerpo;
- [ ] folios y espacios marginales están reservados correctamente;
- [ ] cierre contiene fórmula de lectura/autorización y espacios de firma apropiados;
- [ ] certificación de copia, si se solicita, está separada de la matriz;
- [ ] no se inventó ningún hecho para completar el formato.