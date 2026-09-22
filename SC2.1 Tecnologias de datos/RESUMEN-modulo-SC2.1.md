# SC 2.1 · Tecnologías Estratégicas de Datos para la Transformación Digital
### Resumen de estudio

**Competencia 2 — Tecnologías Estratégicas para la Transformación Digital · 10 horas**
Experto acreditado: **Marco Otilio Peña Díaz** · Caso conductor: **Paola** en la comercializadora *Mundo Azul*

> **La tesis del módulo:** una tecnología estratégica basada en datos es aquella que usa los datos como componente fundamental de su operación. Cuatro de ellas —ciencia de datos, IA, IoT y nube— habilitan directamente la transformación. Pero ninguna funciona sin tres condiciones que el módulo repite en cada lección: **entender el problema antes que la herramienta, involucrar a toda la organización y que la alta dirección se haga cargo**, en especial de la ciberseguridad.

| | |
|---|---|
| **Evaluación** | 25 preguntas · 3 horas · **3 intentos** · 40 % |
| **Reto** | Plan de identificación e implementación de una tecnología · 2.5 h · **2 intentos** · 60 % |
| **Material estudiado** | 10 lecturas · 33 interactivos · 8 videos — 100 % |

---

## Lección 1 — Introducción a las tecnologías basadas en datos

**Tecnología** es la aplicación del conocimiento científico a objetivos prácticos de la vida humana (Britannica). Una **tecnología estratégica basada en datos** usa los datos como **componente fundamental** de su operación para decidir mejor, ser más eficiente o crear productos y servicios nuevos.

**Qué la distingue de una tecnología común.** El cómputo personal, las hojas de cálculo o el internet ya son bienes de consumo — no son estratégicas. Una tecnología estratégica:
- **Sigue en desarrollo** (no tiene "larga historia")
- **Puede impactar a la organización a mediano plazo**
- **Está alineada con la estrategia** organizacional
- **Genera ventajas competitivas**

**Lo que deben considerar** (cuatro frentes): herramientas para decidir con información · seguridad y privacidad de los datos · recolección, generación, almacenamiento y transmisión · procesamiento.

**Las cuatro con impacto directo en la transformación:** ciencia de datos, inteligencia artificial, internet de las cosas y cómputo en la nube.

**Dónde impactan:** evolución del modelo de negocio con nuevas fuentes de ingreso · satisfacción de clientes con expectativas altas · presión del mercado y los competidores.

**Quién es responsable del éxito — la idea central de la lección.** Históricamente se delegó a sistemas. El módulo insiste en que **el esfuerzo debe cubrir a toda la organización, de la C-suite a quien opera el día a día.**
- **Si decides:** Gartner (*Top 10 Emerging Skills for the C-Suite*, 2019) muestra que las empresas buscan líderes con habilidades duras en IA, ML, ciberseguridad e IoT. No hace falta dominar la minucia técnica, pero sí entender los conceptos para fijar estrategia, medir rentabilidad y conducir el cambio cultural — y **elegir con cuidado al asesor tecnológico**.
- **Si eres técnico o asesor:** además de lo técnico, hay que comunicar alcance, riesgos e impactos, evaluar proveedores y su **deuda técnica**, y no olvidar la **gestión del cambio**.
- **El dato duro:** BCG (2019) — **solo 1 de cada 4 esfuerzos de transformación logra los resultados esperados**, por proyectos mal definidos y mal comunicados que generan miedo y resistencia.

La cita que ancla la lección es de Isaac Sacolick (StarCIO, *Driving Digital*): muchos líderes igualan transformación con inversión en tecnología y pierden la meta real, que es transformar negocio, cultura y operación.

---

## Lección 2 — Ciencia de datos

### Dato → información → Big Data

- **Dato:** hechos y cifras que se recolectan, analizan y resumen. **Cuantitativos** (miden cantidad o tamaño) o **cualitativos** (etiquetan categorías). *"Los datos son el nuevo petróleo"* — frase de **Clive Humby**: valiosos, pero sin refinar no sirven.
- **Información:** datos **organizados, procesados e interpretados** para un propósito — típicamente decidir. El dato de ventas mensuales de un vendedor no dice nada hasta que se compara, se contextualiza y se pregunta si mejoró.
- **Big Data:** cuando el **volumen, la variedad y la velocidad** de los datos superan el ritmo común de la organización. Son las **3 V** (Oracle). Suele implicar datos no estructurados de baja densidad — de decenas de terabytes a cientos de petabytes.
- **Datos abiertos (open data):** disponibles al público para explotarse y compartirse. **Los gobiernos son una de sus mayores fuentes.**

### La disciplina

**Ciencia de datos** (Provost & Fawcett, 2013): principios, procesos y técnicas para entender fenómenos analizando datos, **cuyo fin último es mejorar la toma de decisiones**. Combina matemáticas, estadística, computación, programación e IA. Los modelos pronostican sobre datos históricos — **y su margen de error debe considerarse al decidir**.

### CRISP-DM — la metodología

*Cross-Industry Standard Process for Data Mining.* Seis fases, **no estrictamente secuenciales** (se puede ir y volver):

1. **Business understanding** — conocimiento del dominio
2. Data understanding
3. Data preparation
4. Modeling
5. Evaluation
6. Deployment

**El paso que detona todo es el primero: el conocimiento del dominio** — el trasfondo sobre el campo donde se aplicará la ciencia de datos, también llamado conocimiento del negocio. **Lo técnico se puede delegar; el conocimiento del negocio requiere al tomador de decisiones.** De ahí salen objetivos precisos (no "reducir la deserción", sino "usar el historial de ventas para enlazar artículos relacionados en el sitio"), presupuesto, riesgos, costo/beneficio y si hay datos suficientes.

### El ciclo de vida de la información (NIST, 2018)

1. Recolección · 2. Procesamiento · 3. **Divulgación** · 4. Utilización · 5. Resguardo · 6. Eliminación

**La divulgación es la etapa más visible**: llevar la información a quien decide mediante reportes, gráficas o dashboards. **Si no se usa, el valor generado se pierde.**

### El caso que vale la pena recordar

*"El modelo es 99 % preciso, pero el negocio pierde dinero."* Un equipo de retail construyó un recomendador técnicamente excelente que recomendaba los productos más populares — que el cliente iba a comprar de todos modos. Sin conocimiento del dominio, optimizó **precisión estadística** en vez de **margen**. La corrección: definir con Ventas el objetivo real ("subir 5 % el ticket promedio con productos complementarios") y evaluar el modelo por su impacto en ese KPI, no por su *accuracy*.

**Errores a evitar:** empezar sin pregunta de negocio · creer que los datos hablan solos · medir el éxito por la complejidad técnica del modelo.

---

## Lección 3 — Inteligencia artificial

**Definición operativa:** un sistema que exhibe comportamiento que puede interpretarse como inteligencia humana — como ganarle al ajedrez a un gran maestro (Rose, 2020). No máquinas conscientes suplantando humanos.

**Historia mínima:**
- **1950** — Alan Turing propone la **Prueba de Turing** (un interrogador no distingue a la máquina del humano). Ya no se considera la mejor medida, pero sigue impulsando innovación.
- **1955** — **John McCarthy acuña el término** para organizar la **Conferencia de Dartmouth (1956)**, cuya meta era que las computadoras se comportaran de manera que los humanos las identificaran como inteligentes.
- **1980** — John Searle formula **el Cuarto Chino**: manipular símbolos siguiendo reglas no es entender; la sintaxis no produce semántica.

**IA fuerte vs. IA débil.** La **fuerte** alcanzaría entendimiento y estados cognitivos; la **débil** se comporta de forma inteligente sin comprender. El curso lo resume así: *la IA fuerte no es posible, pero la débil es más que suficiente* — para el negocio, si el sistema cumple los requerimientos, el objetivo se alcanzó.

**Machine learning:** detecta patrones y relaciones en grandes volúmenes de datos y, ante un dato nuevo, determina a cuál se parece más. El proceso de detectar patrones se llama **entrenamiento**. Ejemplos: reconocimiento de voz, detección de fraude en tiempo real, recomendaciones.

**Dónde aporta valor en el negocio** (tres áreas): **toma de decisiones** basada en datos · **experiencia de cliente y personalización** · **eficiencia y reducción de costos** (incluye mantenimiento predictivo). La adopción empresarial **creció ~2.5 veces entre 2017 y 2022** (McKinsey vía Statista). *Desarrollar apps móviles no es una aplicación de la IA* — es la respuesta trampa del Pruébate.

**Los tres requisitos antes de implementar:**
1. **Entender el problema** — el síntoma de un proyecto sin base son los cambios constantes de requerimientos
2. **Calidad de los datos** — su mala calidad o ausencia lleva al fracaso
3. **Expectativas alcanzables** — basta con que el sistema sea mejor que el proceso actual, no perfecto

**Los retos** (Stanford vía Statista; Campos Zabala, 2023): dificultad para **probar el valor** de negocio · **falta de compromiso de la alta dirección** · selección de la tecnología adecuada · **resistencia al cambio** · miedo a lo desconocido · **alineación con la estrategia**.

**Caso:** una planta que gasta millones en mantenimiento **preventivo** por calendario y aun así sufre paros inesperados, mientras reemplaza piezas sanas. La solución es **mantenimiento predictivo** con ML — IA analítica, no generativa, y dependiente de la calidad de los datos del sensor.

---

## Lección 4 — Cómputo en la nube

**Qué es:** **no es una tecnología ni una arquitectura individual**, sino una **mezcla de productos y servicios** —muchos existentes desde hace décadas— ofrecidos por internet. El término se rastrea a **1996, en Compaq**; en **2006** Google y Amazon lo popularizaron y **Eric Schmidt** lo usó en una conferencia.

**Por qué despegó:** avances en cómputo, redes y almacenamiento (Williams, 2012) · **internet de alta velocidad, confiable y resiliente** · economías de escala de los grandes proveedores. AWS opera en 32 regiones y 245 países; Azure y Google Cloud en escala similar.

**Los tres modelos:**

| | El proveedor pone… | El cliente gestiona… | Ejemplo |
|---|---|---|---|
| **IaaS** | Red, servidores, virtualización, almacenamiento | Sistema operativo, datos, aplicaciones | Servidores rentados por hora |
| **PaaS** | Hardware y software como plataforma de desarrollo | Sus aplicaciones | Entornos para construir apps web |
| **SaaS** | La aplicación completa | Solo su uso | **Correo web: Gmail, Outlook** |

*Trampa del Pruébate:* Amazon como tienda **no** es SaaS — el consumidor no contrata nada bajo demanda.

**Ventajas:** escalabilidad y flexibilidad · agilidad y competitividad · colaboración y trabajo remoto · acceso a tecnología de punta · ciberseguridad y cumplimiento.
**Desventajas:** dependencia del proveedor (*vendor lock-in*) y de la conectividad · costos ocultos y complejidad · cumplimiento legal entre jurisdicciones · ciberseguridad (**la responsabilidad final sobre los datos sigue siendo de la empresa**).

### ⭐ Valor duro vs. valor suave — el concepto más importante de la lección

- **Valor duro:** ahorro en gasto operativo o en inversión — el argumento original de **CAPEX vs. OPEX**. El problema: no incluye ineficiencias de aprendizaje, capacitación ni costos de transferir datos. **Los sobrecostos de migración y operación son la norma.**
- **Valor suave:** donde está el valor real — **agilidad** del negocio, **rapidez de comercialización** e **innovación diferenciadora** (Linthicum, 2023). Se llama "suave" porque es difícil de cuantificar.

**Los dos errores cruciales en una migración:** **expectativas irreales** y **métricas mal definidas**.

La nube **niveló la cancha**: PyMEs acceden a infraestructura que antes solo tenían las corporaciones.

---

## Lección 5 — Ciberseguridad

**Criptografía moderna:** el arte y la ciencia de mantener un mensaje seguro con técnicas matemáticas y computacionales (Schneier, 2015). Está en cada transacción bancaria, navegación y firma digital.

**Ciberseguridad** (Touhill & Touhill, 2014): la sinergia deliberada de **tecnologías, procesos y prácticas** para proteger información, sistemas, redes y programas contra ataques, daños y accesos no autorizados. **Es más prevención cotidiana que la escena del hacker encapuchado.**

**Activos informáticos** (Ross et al., 2021): **tangibles** (se inventarían fácil) e **intangibles** — software, servicios, sistemas y **datos** (Ruan, 2019). *Los datos de ventas son un activo intangible* — respuesta del Pruébate. Identificar los intangibles exige coordinar a las áreas que generan la información con sistemas.

**Riesgo** = interacción de **amenazas** (lo que puede actuar), **vulnerabilidades** (la debilidad que lo permite) y su **probabilidad**. Idealmente se mide en dinero para poder priorizar.

**Respuestas al riesgo (NIST, 2011):** aceptar · evitar · mitigar · compartir · transferir · combinarlas. Cada acción es un **control**, y todo control necesita seguimiento: *de nada sirve un sistema contra incendios que no funciona.*

### La tríada CIA

| | |
|---|---|
| **Confidentiality** | La información solo está disponible para las partes **autorizadas** |
| **Integrity** | Los datos mantienen consistencia y confiabilidad todo su ciclo de vida, sin cambios no autorizados |
| **Availability** | La información está disponible para quien está autorizado **cuando la necesita** |

### El papel de la dirección — el mensaje que el módulo más repite

**Lo técnico se delega; la gestión de riesgos, los controles y las políticas son responsabilidad directa del liderazgo, junto con el equipo técnico.** Según el WEF (2022), el 87 % de los directivos planea mejorar su ciberresiliencia.

**ENISA** pide: soporte activo de la alta dirección · un administrador que encabece · recursos asignados · **gestión del cambio**, porque los controles estrictos chocan con la comodidad diaria y **la resistencia es causa común de fallo**.

**Las 5 preguntas clave del DHS para el consejo:**
1. ¿Cómo nos enteramos del nivel actual de ciberriesgo y su impacto?
2. ¿Cuál es ese nivel e impacto, y cuál es nuestro plan?
3. ¿Cómo aplica nuestro programa los estándares de la industria?
4. ¿Cuántos incidentes detectamos en una semana normal y cuál es el umbral para avisar a la dirección?
5. ¿Qué tan completo es nuestro plan de respuesta y qué tan seguido se prueba?

**Los 8 elementos clave del DHS a nivel ejecutivo:** integrar el ciberriesgo en la gestión de riesgos y el gobierno corporativo · escalarlo a la alta dirección · **usar estándares y buenas prácticas, no solo cumplimiento** · evaluar los riesgos propios · supervisar · desarrollar y **probar** planes de respuesta · coordinar la respuesta entre áreas · mantener conciencia situacional.

---

## Lo que encontré al estudiarlo

**1. Un error de fecha en una cita.** El interactivo de nube atribuye el artículo sobre el origen del término a *"Regalado (2014)"*. La propia bibliografía del curso —y el original en MIT Technology Review— lo fechan el **31 de octubre de 2011**. Irrelevante para el examen, útil si citas.

**2. El caso de Target se presenta como hecho y probablemente no lo es.** El curso usa la historia de que Target supo que una adolescente estaba embarazada antes que su padre. El artículo de Forbes resume uno del *New York Times* (Duhigg, 2012), y Eric Siegel documentó después que la anécdota viene de un empleado anónimo y que nunca se demostró que el cupón llegara *por* el modelo. El sistema de Target sí existió —un puntaje de embarazo basado en unos 25 productos—; la anécdota del padre es lo dudoso. Sigue siendo un buen ejemplo de riesgo ético; no lo cites como dato.

**3. CRISP-DM no es de IBM.** El curso dice que IBM es "uno de sus principales impulsores", que es cierto, pero puede dejar la impresión de que es su creador. Lo desarrolló un consorcio en 1996-1999 (DaimlerChrysler, SPSS, NCR); IBM lo heredó al comprar SPSS en 2009.

**4. "La IA fuerte no es posible" es una postura, no un hecho.** Es la conclusión de Searle, y el curso la presenta como cierre. Es filosóficamente debatida. Para el examen, respóndela como la presenta el curso.

**5. Material con restos de plantilla.** Varios interactivos conservan texto de relleno (*"lorem ipsum"*, *"Pregunta larga para quiz de varias líneas"*). No afecta el contenido.

**6. En las transcripciones, Whisper deformó dos nombres:** "John Chucky" es **John Tukey** y "Leo Bramann" es **Leo Breiman**, pioneros de lo que hoy es la ciencia de datos.

---

*Archivos de este módulo: lecturas y textos en `txt/`, transcripciones en `transcripciones/`, rúbrica y formato en `Reto/`.*
