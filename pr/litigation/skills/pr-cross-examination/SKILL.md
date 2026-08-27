---
name: pr-cross-examination
title: Contrainterrogatorio — Puerto Rico
description: Prepara planes de contrainterrogatorio para vistas y juicios en Puerto Rico a partir del expediente, testimonios previos, descubrimiento y exhibits. Identifica admisiones, contradicciones, lagunas de conocimiento, sesgo e impugnación; genera secuencias sugestivas de un hecho por pregunta, con fundamento documental, respuestas esperadas y rutas de seguimiento, sujeto a las Reglas de Evidencia de Puerto Rico y al foro aplicable.
author: legal-skills-pr
author_url: https://github.com/ericalopezfebo/legal-skills-pr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pr
practice: litigation
language: es
---

# Contrainterrogatorio — Puerto Rico

## Propósito

Convertir el expediente de un caso en un plan oral de contrainterrogatorio, listo para uso por un abogado en Puerto Rico. El skill debe ayudar a obtener admisiones favorables, limitar el relato del testigo, revelar contradicciones y vacíos de conocimiento, y preparar impugnación sin inventar hechos, citas, documentos ni testimonio.

No todo testigo debe ser contrainterrogado. Antes de preparar preguntas, determine si el contrainterrogatorio adelanta una teoría concreta del caso o una impugnación material.

## Regla jurídica base en Puerto Rico

Aplicar como punto de partida las Reglas de Evidencia de Puerto Rico vigentes y verificar siempre la versión actual antes de una vista o juicio.

- **Regla 607(b)(2)**: el contrainterrogatorio es el primer examen por una parte distinta a la que realizó el directo; en general se limita a la materia del interrogatorio directo y a cuestiones que afecten la credibilidad. El tribunal conserva discreción para permitir otras materias como si fueran interrogatorio directo.
- **Regla 607(a)**: el tribunal tiene amplia discreción sobre el modo de interrogar, incluida la protección frente a preguntas impropias, humillantes, insultantes, ofensivas, impertinentes o innecesariamente dilatorias.
- **Regla 608**: considerar medios pertinentes de impugnación, incluidos comportamiento al declarar, naturaleza del testimonio, capacidad para percibir/recordar/comunicar, declaraciones anteriores, prejuicio/interés/motivo de parcialidad, falsedad/ambigüedad/imprecisión y veracidad o mendacidad, sujeto a las reglas aplicables.

Si el asunto está en un foro administrativo, arbitral o federal, identificar además el reglamento, orden procesal o regla específica que controle el alcance y forma del contrainterrogatorio. No asumir que la práctica del Tribunal de Primera Instancia aplica sin cambios.

## Principios de diseño de preguntas

1. **Una meta factual por sección.** Cada bloque debe poder describirse en una oración: “Este bloque demuestra que ___”.
2. **Preguntas sugestivas como regla de trabajo.** Redactar preguntas que propongan el hecho y requieran una respuesta breve, salvo que exista una razón estratégica o procesal para otra forma.
3. **Un hecho nuevo por pregunta.** Evitar preguntas compuestas.
4. **Control antes que conversación.** Preferir hechos verificables sobre opiniones o invitaciones a explicar.
5. **No preguntar sin una base razonable en el expediente.** Si la respuesta es desconocida y puede abrir una explicación dañina, marcar el riesgo.
6. **Construcción antes de destrucción.** Cuando convenga, obtener primero admisiones útiles y no controversiales; luego confrontar contradicciones o credibilidad.
7. **De general a específico.** Construir la secuencia de forma gradual hasta el punto de confrontación.
8. **Las explicaciones pertenecen al alegato, no a la pregunta.** No discutir con el testigo ni convertir la pregunta en un mini-argumento.
9. **Terminar en un punto ganado.** No añadir una pregunta abierta después de obtener una admisión decisiva.
10. **El abogado conserva el juicio profesional.** El outline es un mapa, no un guion obligatorio.

## Fidelidad al expediente — regla estricta

### Citas y hechos

- Toda cita entre comillas debe ser **verbatim** y estar respaldada por una fuente identificable.
- Todo pinpoint debe sostener la proposición completa para la cual se usa.
- No atribuir una declaración a un testigo si el texto exacto no está disponible.
- Si falta fundamento, usar marcadores como:
  - `[VERIFICAR HECHO — fuente pendiente]`
  - `[VERIFICAR CITA EXACTA — p./línea pendiente]`
  - `[AUTORIDAD ACTUAL PENDIENTE]`
- Distinguir claramente entre:
  - hecho probado por el récord;
  - alegación de una parte;
  - inferencia razonable;
  - contradicción aparente;
  - vacío probatorio.

### Descubrimiento y respuestas escritas

Las contestaciones a interrogatorios, admisiones, declaraciones juradas, deposiciones, emails, cartas, memorandos, informes y otros documentos pueden servir como fuente de:

- admisiones;
- identificación de quién posee conocimiento personal;
- limitaciones de conocimiento;
- omisiones;
- contradicciones internas;
- contradicciones entre personas;
- documentos prometidos, entregados, no disponibles o nunca producidos;
- cambios temporales en funciones, versiones o justificaciones.

No tratar una respuesta de descubrimiento de una entidad como conocimiento personal de cualquier testigo individual sin establecer quién proporcionó la información y cuál es la base de su conocimiento.

## Workflow

### Paso 1 — Identificar foro y postura del testigo

Determinar:

- foro y reglas aplicables;
- tipo de vista o juicio;
- nombre y rol del testigo;
- quién lo llamó;
- si es parte, funcionario, perito, custodio, supervisor, investigador u otro;
- relación con los hechos y con las partes;
- posibles intereses, prejuicios o motivos;
- temas abiertos por el interrogatorio directo, si ya ocurrió.

### Paso 2 — Definir objetivos concretos

No empezar redactando preguntas. Definir primero entre 1 y 5 objetivos, por ejemplo:

- obtener una admisión favorable;
- demostrar falta de conocimiento personal;
- fijar una fecha o cronología;
- demostrar que una función no constaba antes de determinada fecha;
- revelar que una decisión se tomó sin determinado documento o análisis;
- mostrar inconsistencia entre versiones del mismo testigo;
- mostrar contradicción entre testigos;
- demostrar sesgo, interés o motivo;
- impugnar por declaración anterior incompatible;
- autenticar o vincular un exhibit.

Si no existe una ganancia concreta, advertir que puede ser mejor no contrainterrogar sobre ese tema.

### Paso 3 — Construir el mapa del expediente

Organizar por **tema del caso**, no por orden de documentos.

Para cada tema preparar:

| Campo | Contenido |
|---|---|
| Posición esperada del testigo | Qué sostiene o probablemente sostendrá |
| Hecho que queremos fijar | Una proposición concreta |
| Fuente de control | Documento, testimonio, admisión, expediente |
| Contradicción | Qué versión incompatible existe |
| Concesión favorable | Hecho que puede admitir sin confrontación |
| Gap de conocimiento | Qué no vio, no hizo, no recuerda o no sabe |
| Exhibit | Documento que puede utilizarse |
| Riesgo | Explicación, rehabilitación, objeción o puerta que podría abrirse |

### Paso 4 — Matriz de inconsistencias

Cuando existan múltiples versiones, crear una tabla comparativa visual. Priorizar comparaciones como:

- mismo testigo / fechas distintas;
- interrogatorio vs. contestación;
- declaración jurada vs. deposición;
- documento contemporáneo vs. testimonio posterior;
- testigo A vs. testigo B;
- descripción formal del puesto vs. funciones alegadamente realizadas;
- expediente histórico vs. justificación creada posteriormente.

Formato recomendado:

| Tema / función / hecho | Versión A | Versión B | Versión C | Inconsistencia o vacío | Fuente exacta |
|---|---|---|---|---|---|

No llamar “contradicción” a una diferencia que pueda coexistir razonablemente. Si solo es tensión o falta de fecha, etiquetarla como `vacío`, `ambigüedad` o `posible inconsistencia`.

### Paso 5 — Seleccionar el tipo de cross por tema

**Constructivo:** usar al testigo adverso para probar hechos favorables a nuestra teoría.

**Deconstructivo:** atacar la fiabilidad de una versión mediante contradicciones, falta de conocimiento, sesgo o evidencia objetiva.

Cuando se utilicen ambos con el mismo testigo, normalmente colocar primero los bloques constructivos y después los de impugnación, para no perder concesiones útiles una vez el testigo adopte una postura defensiva.

### Paso 6 — Redactar secuencias de control

Por cada objetivo, preparar una secuencia breve:

```markdown
## Tema: [nombre]
**Objetivo factual:** [una oración]
**Fuente de control:** [documento/testimonio/página/línea/exhibit]
**Riesgo:** [si aplica]

1. P: [hecho 1, sugestivo, un solo hecho]
   - Base: [fuente]
   - Respuesta esperada: [sí/no/otra]
   - Si evade: [pregunta de control]

2. P: [hecho 2]
   - Base: [fuente]
   - Respuesta esperada: [respuesta]
   - Si niega: [exhibit o declaración previa]

3. P: [punto de cierre]
   - Propósito: [admisión final]
```

Cada pregunta debe poder eliminarse sin destruir las demás. Evitar párrafos disfrazados de preguntas.

### Paso 7 — Preparar impugnación

Para una declaración anterior incompatible o evidencia documental contradictoria, preparar por separado:

1. **Compromiso:** fijar claramente la versión actual del testigo.
2. **Fundamento:** identificar ocasión, documento, autoría, firma, fecha o circunstancia pertinente.
3. **Confrontación:** mostrar o leer solo el segmento exacto necesario, conforme a las reglas aplicables.
4. **Cierre:** terminar con la incompatibilidad; no pedir al testigo que explique salvo que exista una razón estratégica concreta.

Crear una ficha de impugnación:

| Elemento | Contenido |
|---|---|
| Testimonio actual | Cita o paráfrasis fiel |
| Declaración/documento previo | Cita exacta |
| Fecha | |
| Fuente / página / línea | |
| Exhibit | |
| Diferencia material | |
| Fundamento necesario | |
| Pregunta de cierre | |

### Paso 8 — Preparar respuesta a evasión

Para testigos que explican en exceso, preparar pivotes de control, por ejemplo:

- repetir la proposición en términos más estrechos;
- dividir la pregunta;
- regresar al documento;
- fijar que el testigo no contestó la proposición específica;
- solicitar, cuando proceda, instrucción del tribunal para que conteste la pregunta.

Nunca recomendar hostigar, humillar, insultar o discutir con el testigo.

### Paso 9 — Preparar mapa de exhibits

| Exhibit | Qué acredita | Fundamento/autenticación | Contradice o apoya | Tema | Momento de uso |
|---|---|---|---|---|---|

Verificar que el documento realmente contenga el lenguaje o dato que se pretende utilizar.

### Paso 10 — Preparar cierre estratégico

Identificar:

- las 3 admisiones más importantes;
- las 3 contradicciones o vacíos de mayor impacto;
- la mejor última pregunta;
- temas que deben abandonarse si el testigo ya concedió el punto;
- asuntos que se reservan para alegato final.

## Salida por defecto

Entregar, salvo que el usuario pida otra cosa:

1. **Perfil del testigo y objetivo del cross.**
2. **Teoría del contrainterrogatorio en una oración.**
3. **Top 3–5 objetivos.**
4. **Tabla de inconsistencias/vacíos.**
5. **Outline temático de preguntas sugestivas.**
6. **Fichas de impugnación.**
7. **Mapa de exhibits.**
8. **Respuestas a evasión y riesgos.**
9. **Lista de puntos que NO conviene preguntar.**
10. **Checklist de preparación para sala.**

## Checklist para sala

- [ ] Tengo claro qué hecho quiero obtener de cada bloque.
- [ ] Cada pregunta contiene un solo hecho nuevo.
- [ ] Conozco la respuesta esperada o el riesgo de no conocerla.
- [ ] Cada confrontación tiene una fuente de control lista.
- [ ] Verifiqué citas, páginas, líneas y exhibits.
- [ ] Separé contradicción real de ambigüedad o vacío.
- [ ] Sé qué hacer si el testigo niega, evade o explica.
- [ ] Conozco el límite del directo y las materias de credibilidad bajo la regla aplicable.
- [ ] No estoy abriendo una puerta que beneficie innecesariamente a la otra parte.
- [ ] Sé dónde terminar cada tema.

## Controles de calidad

Antes de entregar el outline, revisar:

- ¿Hay alguna pregunta que asuma un hecho no apoyado por el récord?
- ¿Hay preguntas compuestas?
- ¿Hay preguntas abiertas que permitan al testigo reconstruir su historia sin necesidad?
- ¿Alguna cita fue parafraseada dentro de comillas?
- ¿La contradicción es verdaderamente material?
- ¿El punto puede probarse mejor con un documento o con otro testigo?
- ¿El cross repite el interrogatorio directo sin un propósito estratégico?
- ¿La pregunta puede provocar una explicación que repare el caso contrario?
- ¿El tono cumple con la Regla 607(a) y mantiene profesionalismo?

## Fuentes y referencias de diseño

Consultar y verificar según corresponda:

- Reglas de Evidencia de Puerto Rico, Regla 607 (orden, modo y alcance del contrainterrogatorio).
- Reglas de Evidencia de Puerto Rico, Regla 608 (credibilidad e impugnación).
- Donald Milán Guindín, “El ABC del contrainterrogatorio”, Microjuris Puerto Rico (25 junio 2024).
- LexisNexis, “Five Steps to an Effective Cross-Examination” (31 enero 2023).
- LegalAI Guide, “Cross-Examination Question Generation”.
- Family Legal Care, guía de contrainterrogatorio, únicamente como referencia pedagógica general; no sustituye derecho de Puerto Rico.
- CaseMark, `cross-examination-summaries`, como referencia estructural para matrices de impugnación y citas exactas.
- Anthropic, `deposition-prep`, como referencia estructural para fidelidad al récord, postura del testigo y secuencias de control.

## Límites

- No inventar hechos, citas, testimonios, exhibits, fechas, páginas o líneas.
- No asumir que una declaración de una parte prueba por sí sola la verdad del hecho.
- No presentar una predicción de credibilidad como conclusión cierta.
- No atribuir conocimiento personal a un empleado porque la entidad contestó un interrogatorio.
- No sustituir el juicio del abogado sobre estrategia, admisibilidad, objeciones o cuándo detener el contrainterrogatorio.
- Verificar derecho vigente, reglamentos del foro y órdenes particulares antes de usar el material en sala.
