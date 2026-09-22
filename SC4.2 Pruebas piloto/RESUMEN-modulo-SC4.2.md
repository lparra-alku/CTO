# SC 4.2 · Pruebas Piloto de Estrategias Centradas en la Persona
### Resumen de estudio

**Competencia 4 — Experiencia del cliente y diseño**
- Experto acreditado: **Jorge Luis Coronel Fuentes**.
- Caso conductor: **Claudia**, gerente de operaciones de una cadena de electrónica. Sus clientes no encuentran lo anunciado en redes o no pueden comprar desde casa por limitaciones físicas, y ella lanza *e-commerce* y una app.

> **La tesis del módulo:** es la continuación de SC 4.1, que llegaba hasta idear. Aquí se **prototipa, se prueba y se mide**. Tiene cinco bloques:
> 1. **Prototipado y pruebas de usabilidad.**
> 2. **Accesibilidad e inclusión** desde el diseño, no como parche.
> 3. **Marcos de ejecución**: OODA, STEP, VSM, *backlog* y SLA.
> 4. **Medición**: heurísticas de Nielsen, KPI de UX y riesgo.
> 5. **Integración en el plan de transformación.**
>
> El mensaje: *prototipar no es solo diseñar, es validar* antes de invertir.

| | |
|---|---|
| **Evaluación** | 25 preguntas · 3 horas · **3 intentos** · 40 % |
| **Reto** | *Solución centrada en la persona* · 2.5 h · **2 intentos** · 60 % |
| **Material estudiado** | 12 lecturas · 29 interactivos · 9 videos — 100 % |

---

## Lección 1 — Prototyping and Testing

### Técnicas de prototipado
| Técnica | Qué es |
|---|---|
| **Baja fidelidad** | Papel, cartulina, post-its. **Materiales sencillos, rápido, fácil de iterar.** |
| **Alta fidelidad** | Cercano al producto final: Adobe XD, Sketch, **Figma**, InVision |
| **Interactivo** | Simula la navegación real |
| **De código** | **HTML, CSS, JS, React, Vue**. Es **la mejor opción para prototipos funcionales de web o app**. |
| **3D** | Blender, SolidWorks, Fusion 360: productos físicos |
| **Storyboards** | Viñetas que narran la interacción |
| **Rápido y en serie** | Impresión 3D, corte láser |
| **VR/AR** | **Experimentar la interacción en un entorno simulado** |
| **De servicio** | *Journey maps* y *service blueprints* |

**La elección depende del tipo de producto, el nivel de detalle, el alcance y los recursos.**

**Matriz de impacto contra complejidad** (Johnson y de Rouw, 2017): **alto impacto y baja complejidad → "¡Hazlo!"** · alto impacto y alta complejidad → arriesgado, planear con cuidado · bajo impacto y baja complejidad → pérdida de esfuerzo · bajo impacto y alta complejidad → **deséchalo**.

**Business Service Design (BSD):** es un **enfoque de prototipado**, no un "concepto".
- **Etapas:** entender el negocio → declaración del diseño de servicio → diseño funcional → construir el MVP → ciclo de vida ágil → instalar y entregar → operación y mantenimiento.
- **Requerimientos:** de negocio, de usuario y de sistema.

### Pruebas de usabilidad: 4 etapas
1. **Objetivos y métricas.**
2. **Participantes** representativos, más escenarios y tareas, y la ejecución con observación.
3. **Recopilación de datos**: cuantitativos (tiempo, errores) y cualitativos.
4. **Iteración y mejora.**

**Son una inversión:** bajan los costos de soporte y aumentan la fidelidad.
**Ejemplo:** un sistema de citas pasa del teléfono y el correo a una plataforma probada en Figma, con meta de **−40 % de llamadas**.

---

## Lección 2 — Diseño para la accesibilidad y la inclusión

### El proceso de producto digital inclusivo: 18 pasos
Ideación → investigación de mercado y **user personas** → alcance y objetivos SMART con KPI → UX/UI con *wireframes* → **planificación técnica y arquitectura** (tecnologías, bases de datos e infraestructura; arquitectura de datos según Microsoft) → QA → escalabilidad y seguridad → desarrollo iterativo → **beta** → contenido → documentación → **pruebas de accesibilidad** → **UAT** → seguridad y cumplimiento → lanzamiento → analítica → marketing → escalar.

**Caso Scytl** (voto electrónico, vía Justinmind): *wireframes* y prototipos interactivos, pruebas con usuarios y Lean UX.

### Consideraciones para ofertas digitales inclusivas
1. **Conocer los estándares: WCAG** y la Sección 508 de EE. UU.
2. **Generar conciencia en el equipo.**
3. Diseñar para todas las plataformas.
4. Diseño centrado en el usuario (Pursell, 2023): *un proceso **iterativo** que dirige sus objetivos a los usuarios y sus necesidades*.
5. **UI accesible:** texto alternativo, navegación por teclado, subtítulos y transcripciones, contraste, diseño responsivo y prueba con lectores de pantalla.
6. Sensibilidad cultural.
7. Mecanismos de retroalimentación.
8. Mejora continua.
9. Documentación y soporte.
10. **Declaración de accesibilidad.**
11. Promover la inclusión y la diversidad.

**Herramientas:** **Axe** · **WAVE** · lectores de pantalla **JAWS, NVDA y VoiceOver** · verificadores de contraste de WebAIM.

### Modelos de diseño inclusivo
| Modelo | Clave |
|---|---|
| **Los 7 principios del Diseño Universal** (NC State) | Equitativo · flexible · simple e intuitivo · información perceptible · **tolerancia al error** · bajo esfuerzo físico · tamaño y espacio |
| **Cooper Hewitt (Smithsonian)** | **Co-creación · empatía · diversidad y equidad · flexibilidad** |
| **Las 4 C de la accesibilidad** | **Contenido · Control** (interactuar y navegar) **· Comunicación · Contexto** |
| **Las 5 dimensiones de la inclusión digital** | Accesibilidad · usabilidad · percepción · cognición · afectividad |
| **HEART (Google)** | **Happiness · Engagement · Adoption · Retention · Task success** |
| **Diseño de servicios centrado en el cliente** | Empatía · co-creación · flexibilidad · iteración · medición · multicanal · fases de vida · calidad |

**Buenas prácticas:** diseño responsivo, WCAG, pruebas de usabilidad, retroalimentación en tiempo real, carga rápida, pruebas en varios navegadores, multilingüe, personalización, SEO y consistencia de marca.

---

## Lección 3 — Implementing User-Centric Design Strategy

**Framework de ejecución de proyectos:**
- **Antes de empezar:** **comprender los objetivos estratégicos** e identificar a las partes interesadas.
- **Los 8 pasos:**
  1. Elegir la metodología (cascada, Scrum, Kanban, Lean).
  2. Procesos y flujos.
  3. Roles.
  4. Herramientas y plantillas.
  5. KPI.
  6. Capacitación y comunicación.
  7. **Piloto** y ajustes.
  8. Documentación y mejora.
- **Las 5 conductas del usuario en línea (Díaz, 2019):** navegar · redes · compras · comunicación · crear contenido.

### Herramientas
| Herramienta | Qué hace |
|---|---|
| **OODA Loop** (John Boyd) | **Observar → Orientar → Decidir → Actuar**, iterativo. **La orientación es la fase más crítica.** Nació en lo militar y se usa en negocios y en conflictos. El ejemplo es una app de súper a domicilio. |
| **STEP** | Factores **Sociales, Tecnológicos, Económicos, Políticos**. PESTEL agrega los ambientales y legales. |
| **Value Stream Mapping** (Lean) | **Visualizar el flujo de valor de principio a fin**, separar valor de desperdicio, flujo de material y de información, mapa actual contra futuro |
| **Interfaz de backlog** (Scrum) | Lista con prioridad, estado y estimación · filtros · detalle · asignación · comentarios · historial · alertas · exportación |
| **SLA** (definición de AWS) | Contrato de nivel de servicio: *uptime*, respuesta, resolución, sanciones. **Tipos: por servicio · por cliente · multinivel.** El **SLO** es la meta de una métrica. |

**Caso Airbnb** (sin nombrarlo): los fundadores subieron fotos de **su propio departamento** a una página básica para validar si la gente pagaría. El curso le atribuye +30 % de conversión y −50 % de *tickets* tras el rediseño.

---

## Lección 4 — Medir el éxito del diseño centrado en el usuario

### Evaluación heurística (Nielsen, 1990)
**Expertos** revisan la interfaz contra **10 heurísticas**:
1. Visibilidad del estado del sistema
2. Correspondencia con el mundo real
3. Control y libertad del usuario
4. Consistencia y estándares
5. **Prevención de errores**
6. **Reconocimiento antes que recuerdo**
7. Flexibilidad y eficiencia
8. Diseño estético y minimalista
9. Ayudar a reconocer, diagnosticar y recuperarse de los errores
10. Ayuda y documentación

**Menos problemas = mejor diseño.**

### Métricas y KPI de UX
- **Retención y abandono · conversión · tiempo por tarea · satisfacción · accesibilidad (WCAG) · negocio (ROI).**
- **KPI:** **tasa de conversión** (% que completa una acción) · tiempo de permanencia · abandono · **SUS o NPS** · tiempo de carga · errores · retención · satisfacción · **tareas completadas** · *engagement* · **NPS** · abandono de carrito.

**Por qué invertir en medición:** decisiones informadas y soluciones funcionales, no solo bonitas.

### Risk Assessment Product Value
Rider et al. (2009): *"evaluar los riesgos sobre el valor del producto"*. **El propio curso admite que no es un concepto estándar.**
- **Riesgos de UX en el ejemplo de una app de salud:** **privacidad y seguridad de datos** · facilidad de uso y accesibilidad · precisión de los datos · relevancia.
- **Cuatro áreas para identificar riesgos:** **Tiempo · Ubicación · Ciclo de vida del producto · Cadena de suministro.**
- **Los tres pasos:** identificar → evaluar (probabilidad e impacto; cartera de alto riesgo) → **plan de acción: Disuasión · Regulación · Cumplimiento**.
- **Programa de protección de marca:** autenticación del producto · seguimiento de la distribución · educación del consumidor.

**Caso Spotify** (sin nombrarlo): retención, NPS, tiempo en pantalla, conversión *free → premium* y éxito en tareas, medidos con Hotjar, UserTesting y A/B.

---

## Lección 5 — Incorporar el DCU en el plan de transformación

**Tendencias:** AR/VR · interfaces conversacionales · personalización en tiempo real · pruebas continuas · colaboración multidisciplinaria · **diseño sostenible** · ética y privacidad · **voz y experiencia multimodal** (combina voz, texto y elementos visuales) · IA y ML.

**Tres ejemplos de plan:**
1. **Rediseño de app bancaria:** investigación → UI/UX → prototipo y pruebas → implementación → lanzamiento → evaluación → mantenimiento.
2. **Portal de atención de una telecom:** investigación → contenido y navegación incluyente, con voz → **funcionalidades clave** (búsqueda, chat, FAQ, **autoayuda accesible**, seguimiento de casos) → chatbot → capacitación → beta → lanzamiento → medición (menos llamadas).
3. **Universidad:** **investigación de estudiantes** (encuestas y *focus groups*) → contenido interactivo → plataforma personalizada → retroalimentación automatizada → seguimiento.

**Caso Iberdrola:** DCU como eje de su transformación, con personalización por perfil y accesibilidad.

**Los tres elementos clave para incorporar el DCU al plan:** **colaboración interdisciplinaria · recopilación de datos significativos · iteración continua.**

---

## Errores y descuidos del curso

| Dónde | Qué dice | Qué es correcto |
|---|---|---|
| OODA | Boyd lo desarrolló *"en la década de 1950 y 1960"* | Boyd lo formuló en los **años 70 y 80**. Su obra es *Patterns of Conflict* (1986). En los 60 hizo la teoría de energía y maniobrabilidad. |
| KPI de UX | *"Usabilidad: SUS o NPS"* | El **NPS mide lealtad o recomendación, no usabilidad**. La usabilidad se mide con **SUS** (Brooke, 1986). |
| Modelos | "4 C de la accesibilidad", "5 dimensiones de la inclusión digital", "modelo Cooper Hewitt" | **No encontré fuentes con estos modelos** tal como se presentan. Parecen síntesis del curso. Los estándares reales son **WCAG 2.2** (POUR: perceptible, operable, comprensible, robusto) y los **7 principios del Diseño Universal**. |
| Risk Assessment | Rider et al. (2009) aplicado a falsificación digital | Rider et al. trata de **seguridad de productos de consumo** (lesiones). La parte de falsificación sale de otra fuente. |
| L2, Parte 2 | *"Plataforma de atención médica digital inclusiva"* | El caso que se describe es **Scytl, de voto electrónico**. El título no corresponde. |
| Bibliografía | Horton, **Quesenbery y Gustafson** (2014) | Los autores de *A Web for Everyone* son **Sarah Horton y Whitney Quesenbery**. No hay tal Gustafson. |
| Formato del Reto | *"La plantilla que propone **Hubsport**"* | **HubSpot**, *Make My Persona* |
| Formato del Reto | Nombre del archivo `_reto_C4SC2`, título *"Diseño de un plan de transformación digital"* | Hay inconsistencia con el nombre del Reto en la plataforma: *"Solución centrada en la persona"* |
| Video L4 | "VESCA a Smerquart-Hvaliou" | Error del reconocimiento de voz: *Risk Assessment Product Value* |

---

## Cómo aterriza en Grupo Infocus y Alku

- **SLA es vocabulario diario de Alku.** El módulo da la estructura formal que debería tener el **contrato de soporte post-implementación de Odoo**: SLO de primera respuesta y de resolución, niveles (por servicio, por cliente o multinivel), sanciones y revisión. **Odoo Helpdesk trae políticas de SLA nativas.**
- **Backlog = Odoo Proyecto** con etapas, prioridades, etiquetas y asignación. La lectura de diseño de interfaz de *backlog* describe lo que Odoo ya hace.
- **La matriz impacto-complejidad sirve para priorizar requerimientos** del cliente en una implementación, las famosas "personalizaciones".
- **Accesibilidad:** el **portal de clientes de Odoo** es la cara digital de las pymes. Una revisión rápida con **WAVE o Axe** del sitio y la tienda de un cliente es un servicio de valor agregado barato.
- **El Reto** (solución centrada en la persona): la rúbrica **solo califica 4 cosas** (situación actual, objetivo, user persona y KPI, 25 puntos cada una), aunque el formato pide más. **Hay que asegurar primero esas cuatro.** Una propuesta natural: un **portal de autoservicio para clientes de Alku** (tickets, facturas y avance del proyecto) sobre Odoo, con SLA, HEART como KPI y OODA como metodología.
