# Perfiles de formato para mociones de Puerto Rico

Este archivo complementa `SKILL.md`. Documenta convenciones visuales observadas en las muestras suministradas y las separa de requisitos oficiales del foro.

## Regla de prioridad

1. **Modelo, reglamento, orden o instrucciones oficiales vigentes del foro**.
2. **Regla procesal aplicable**.
3. **Muestra reciente del mismo foro**.
4. **Muestra reciente de otro foro puertorriqueño**.
5. **Estilo de oficina**.

Una línea roja, fuente particular o diseño de epígrafe visto en una moción privada no se debe describir como requisito oficial sin autoridad independiente.

## Perfil `pr-litigation-redline`

Perfil de oficina reconstruido de las muestras DOCX recientes.

| Propiedad | Valor observado / recomendado |
|---|---|
| Tamaño de papel | Letter (8.5 × 11) |
| Margen izquierdo | 1.5 in |
| Margen derecho | 0.5 in |
| Margen superior | 0.625 in en muestras recientes |
| Margen inferior | 0.3125 in en muestras recientes |
| Línea izquierda | roja (`FF0000`), doble, 1.5 pt, separación 4 pt |
| Línea derecha | roja (`FF0000`), sencilla, 1.5 pt, separación 4 pt |
| Fuente principal | Times New Roman 12 pt |
| Alternativa histórica observada | Book Antiqua 12 pt |
| Cuerpo | justificado |
| Título | centrado, negrita, mayúsculas |
| Encabezado institucional | centrado, negrita, mayúsculas |
| Paginación | centrada en pie, cuando corresponda |

### Dato técnico de las muestras DOCX

Los bordes rojos se implementan como **page borders de la sección**, no como líneas dibujadas manualmente:

```xml
<w:pgBorders>
  <w:left w:val="double" w:sz="12" w:space="4" w:color="FF0000"/>
  <w:right w:val="single" w:sz="12" w:space="4" w:color="FF0000"/>
</w:pgBorders>
```

`motion_docx.py` reproduce este comportamiento mediante WordprocessingML.

## Epígrafe

Usar una tabla de dos columnas. Evitar crear el epígrafe con espacios o tabuladores.

### Columna izquierda

- parte principal en mayúsculas y negrita;
- designación procesal debajo;
- `v.` entre las partes;
- contraparte y su designación.

### Columna derecha

- `Caso Núm.` o `Civil Núm.`;
- sala, cuando corresponda;
- `SOBRE:`;
- naturaleza del procedimiento.

### Bordes observados

En las muestras recientes:

- sin marco exterior completo;
- división central doble;
- borde inferior doble en la celda izquierda en algunos modelos;
- evitar bordes decorativos si el foro usa otro modelo oficial.

## CASP

Convenciones observadas y consistentes con el modelo aportado:

```text
GOBIERNO DE PUERTO RICO
COMISIÓN APELATIVA DEL SERVICIO PÚBLICO

[EPÍGRAFE]

MOCIÓN ...

A LA HONORABLE COMISIÓN:
```

Designaciones usuales: `Promovente` / `Promovido`.

Cierre frecuente:

```text
POR TODO LO CUAL, ...
RESPETUOSAMENTE SOMETIDO.
CERTIFICO: ...
En San Juan, Puerto Rico, a [FECHA].
[FIRMA / RUA / CONTACTO]
```

El orden entre certificación, `RESPETUOSAMENTE SOMETIDO` y fecha varía entre muestras. Si existe un modelo oficial aplicable, seguirlo.

## Junta de Apelaciones de AEP

Convenciones observadas:

```text
AUTORIDAD DE EDIFICIOS PÚBLICOS
JUNTA DE APELACIONES
SAN JUAN, PUERTO RICO

[EPÍGRAFE]

MOCIÓN ...

A LA HONORABLE JUNTA:
```

Designaciones usuales: `Apelante` / `Apelada`.

## Tribunal de Primera Instancia

Convenciones observadas:

```text
ESTADO LIBRE ASOCIADO DE PUERTO RICO
TRIBUNAL DE PRIMERA INSTANCIA
SALA [SUPERIOR] DE [MUNICIPIO]

[EPÍGRAFE CON CIVIL NÚM., SALA Y SOBRE]

MOCIÓN ...

AL HONORABLE TRIBUNAL:
```

En SUMAC, no copiar al documento generado las leyendas automáticas de `Entrada Núm.`, fecha/hora o `Página X de Y` que aparecen en PDFs ya radicados. Esas marcas son producto del sistema, no parte de la moción original.

## Mayúsculas y negritas

Aplicar negrita a los elementos de navegación y fórmulas clave, no al cuerpo completo:

- encabezado institucional;
- partes principales del epígrafe;
- título;
- saludo al foro;
- encabezados de sección;
- `COMPARECE`, cuando se quiera enfatizar la fórmula de comparecencia;
- `POR TODO LO CUAL` / `POR LO EXPUESTO`;
- `SÚPLICA`;
- `CERTIFICO`;
- `RESPETUOSAMENTE SOMETIDO/A`.

No alterar el contenido jurídico solo para forzar un patrón visual.

## Vocabulario reusable

### Comparecencia

Patrones aceptables, ajustados a número y género:

- `COMPARECE la Parte Promovida, [PARTE], por conducto del abogado que suscribe, y muy respetuosamente EXPONE, ALEGA Y SOLICITA:`
- `Comparece la parte apelada por conducto de la representación legal que suscribe y ante esta Honorable Junta muy respetuosamente expone, alega y solicita:`
- `COMPARECEN las partes ..., representadas por sus respectivas representaciones legales, y muy respetuosamente EXPONEN, ALEGAN Y SOLICITAN:`

### Petición

- `POR TODO LO CUAL, se solicita respetuosamente ...`
- `POR LO EXPUESTO, se solicita ...`
- `EN MÉRITO DE LO ANTERIOR, se solicita ...`

### Remedios frecuentes

- `tome conocimiento de lo expuesto`;
- `dé por cumplida la Orden`;
- `declare HA LUGAR la presente moción`;
- `declare NO HA LUGAR la solicitud ...`;
- `continúe con los procedimientos conforme a derecho`;
- `emita cualquier otro remedio que en derecho proceda`.

## Errores que no se deben aprender de las muestras

- texto de borrador con alternativas sin resolver;
- nombres de agencias pegados o incorrectos;
- inconsistencias entre `promovida`, `apelada` y `demandada`;
- errores tipográficos;
- citas incompletas;
- datos personales de otros asuntos;
- fecha en blanco si el usuario ya suministró la fecha;
- afirmaciones de notificación no verificadas.

## Validación visual mínima

Antes de considerar listo el DOCX:

- el epígrafe no se desborda;
- el número de caso y `SOBRE` quedan en la columna derecha;
- el título está centrado;
- no existen dobles espacios usados para alinear;
- las líneas laterales, si se activaron, aparecen en todas las páginas;
- las mayúsculas/negritas son consistentes;
- ningún dato de una muestra anterior permanece en el documento;
- el bloque de firma no queda aislado de forma absurda en una página nueva;
- las páginas siguientes mantienen legibilidad y numeración.