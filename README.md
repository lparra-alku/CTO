# Programa Chief Digital Transformation Officer — Tec de Monterrey

Material del curso, estudiado y sistematizado. Cada módulo se procesa igual: se descarga todo el material de la plataforma, se estudia completo, se investiga la bibliografía citada y se produce un juego fijo de entregables.

> **Uso interno.** Los PDFs y transcripciones son material del Tec de Monterrey / The Learning Gate. Este repositorio es privado y existe para consulta del equipo, no para redistribución.

---

## Cómo está organizado

Una carpeta por módulo. Dentro, el material original tal como viene de la plataforma más los entregables propios.

```
<módulo>/
├── *.pdf                      Material original de la plataforma
├── RESUMEN-modulo-N.md        Resumen de estudio de todas las lecciones
├── GUIA-evaluacion-modulo-N.md  Preparación para el examen
├── mapa-mental-modulo-N.html   Mapa mental (abrir en navegador)
├── Bibliografía/              Resúmenes de las fuentes citadas
├── Reto/                      Rúbrica, formato editable y borradores
├── transcripciones/           Transcripciones de los videos
└── txt/                       Texto plano de los PDFs, para buscar
```

## Los entregables de cada módulo

| Archivo | Para qué sirve |
|---|---|
| **RESUMEN** | Leer una vez para tener el módulo completo. Señala además las erratas del propio curso. |
| **GUIA-evaluacion** | Repasar 45 minutos antes del examen. Sale de los "Pruébate" de cada lección, que son del mismo autor que la evaluación. |
| **mapa-mental** | Repaso visual. Carga los datos memorizables, no solo los títulos. |
| **Bibliografía** | Qué dice cada fuente citada y qué aporta. Incluye ruta de lectura priorizada: de ~70 fuentes, cuáles valen la pena. |
| **Reto** | Rúbrica y borrador del entregable evaluable. |

Ponderación típica: **evaluación 40 %, reto 60 %**.

---

## Módulos

### 1 · Alineando la Mentalidad de Transformación Digital
La tesis de fondo: la transformación digital no empieza en la tecnología, empieza en el modelo operativo y la propuesta de valor. Cubre los sectores industriales, el mundo conectado y la deuda digital, los entornos VUCA y BANI, y la estrategia de transformación dual (A, B y enlace de capacidad C).

### 2 · La Transformación Digital encuentra a las Tecnologías Estratégicas
Diseño de negocios digitales según el CISR del MIT Sloan, los tres tipos de digitalización (procesos, datos y sensores), RPA y automatización cognitiva, IA generativa por industrias, y las herramientas de Gartner para decidir cuándo adoptar una tecnología.

### SC 2.1 y 2.2 · Tecnologías estratégicas de datos y de procesos
Ciencia de datos, IA, *big data* y nube; RPA, *blockchain*, IoT y robótica. Qué es cada una y cuándo conviene adoptarla.

### SC 3.1 a 3.4 · Organización y estrategia
Marcos de referencia, transformación en la organización, visión y estrategia, y mejora continua. Cubre el cómo gobernar el cambio, no solo la tecnología.

### SC 4.1 y 4.2 · Centrado en la persona
Diseño centrado en la persona (entrevistas, mapa de empatía, *journey*) y pruebas piloto: prototipar, probar y medir.

### SC 5.1 y 5.2 · Ejecución y roadmap
Metodologías de ejecución (Design Thinking, Customer Development, agilidad, TI bimodal) y el roadmap de transformación digital de David Rogers en cinco pasos.

### PIDA · Proyecto Integrador
Qué pide la certificación (insignia diamante), sus requisitos y una propuesta para hacerlo en Grupo Infocus. Ver [`PIDA Proyecto Integrador/README-PIDA.md`](PIDA%20Proyecto%20Integrador/README-PIDA.md).

---

## Sitio de estudio

[`index.html`](index.html) reúne los 12 subcursos en una sola página, con un índice lateral y tres vistas por subcurso:
- **Mapa:** el mapa mental.
- **Guía y Reto:** los datos que se preguntan en la evaluación y la rúbrica del Reto, criterio por criterio.
- **Resumen:** el módulo completo, con los errores del curso señalados.

Las páginas de guía y resumen están en `sitio/` y se generan a partir de los `.md` de cada módulo. Para regenerarlas después de editar un `.md`:

```bash
python3 _herramientas/sitio/render_md.py sitio && python3 _herramientas/sitio/build_hub.py repo index.html
```

**Cómo abrirlo:**
- **En local:** clona el repo y abre `index.html` en el navegador.
- **En la web:** GitHub Pages necesita un plan de pago si el repo es privado. Mientras tanto hay una copia publicada como Artifact privado.

---

## Dos cosas que conviene saber antes de estudiar

**El material del módulo 2 tiene un error conceptual.** Invierte las definiciones de *digitización* y *ser digital* respecto a la fuente original de Jeanne Ross. Está documentado en el resumen y en el mapa mental. En la evaluación hay que responder la versión del curso; para aplicarlo en la práctica, la correcta es la de Ross.

**El módulo 1 presenta dos marcos sin atribución.** "VECA" es el VUCA Prime de Bob Johansen (2007) y las respuestas a BANI que enseña no son exactamente las que propone Jamais Cascio. Ambas están rastreadas hasta la fuente en la bibliografía.

---

## Lo que no está en los PDFs

Buena parte del contenido más aprovechable del curso vive en videos y presentaciones interactivas, no en el material descargable. Todo eso está recuperado: las transcripciones completas de los videos están en `transcripciones/` y el contenido de los recursos interactivos quedó integrado en cada resumen.
