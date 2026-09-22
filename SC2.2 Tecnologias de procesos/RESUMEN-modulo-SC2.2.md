# SC 2.2 · Tecnologías Estratégicas de Procesos para la Transformación Digital
### Resumen de estudio

**Competencia 2 — Tecnologías Estratégicas para la Transformación Digital · 10 horas**
Experto acreditado: **Marco Otilio Peña Díaz** · Caso conductor: **Daniel** en *Milport*

> **La tesis del módulo:** SC 2.1 trató las tecnologías que se alimentan de datos; este trata las que **cambian cómo se ejecutan los procesos** — RPA, blockchain, realidad extendida e IA generativa. Y el mensaje que cruza las cuatro lecciones es de cautela: **cada una está en una fase distinta de madurez, y casi todas fracasan por la misma razón — no por la tecnología, sino por el proceso, la gente y las expectativas**.

| | |
|---|---|
| **Evaluación** | 25 preguntas · 3 horas · **3 intentos** · 40 % |
| **Reto** | Plan de implementación de una tecnología emergente de procesos · 2.5 h · **2 intentos** · 60 % |
| **Material estudiado** | 10 lecturas · 33 interactivos · 9 videos — 100 % |

---

## Lección 1 — Introducción a las tecnologías emergentes

**Tecnología emergente** (Winston & Strawn, 2023): la que **aún está en desarrollo o estará disponible en los próximos 5 a 10 años**, con potencial de impactar a la sociedad o la economía.

**Sus tres rasgos:** **novedad, rápido crecimiento y potencial efecto transformador** — no solo en lo profesional, también en lo personal y social.

**No tiene que ser digital.** Una tecnología emergente puede venir de cualquier área de la ciencia o la ingeniería. El ejemplo del curso: las **vacunas de ARNm** contra el COVID-19.

**Las seis con impacto directo en la transformación:** cómputo en la nube · IoT · **RPA** · **minería de procesos** · realidad virtual y aumentada · **IA generativa**. *El cómputo personal ya no lo es* — es la trampa recurrente del examen.

**Cómo seguirlas:** el reporte anual de tecnologías emergentes del WEF, y los de Gartner, McKinsey, Forrester e IDC. La herramienta más usada es el **Hype Cycle de Gartner** (5 fases: lanzamiento → pico de expectativas sobredimensionadas → abismo de desilusión → rampa de consolidación → meseta de productividad).

**Roles y responsabilidad:** igual que en SC 2.1 — **el esfuerzo cubre a toda la organización**. Solo **1 de 4** transformaciones logra lo esperado (BCG, 2019).

---

## Lección 2 — Robotic Process Automation (RPA)

**Qué es** (Osman, 2019): herramientas que realizan tareas manuales y repetitivas con **robots de software entrenados** que interactúan con otros sistemas **a través de la misma interfaz de usuario** que usaría una persona. Viéndolo trabajar, parecería alguien manejando la computadora, pero muy rápido.

- El término lo acuñó **Patrick Geary (Blue Prism) en 2012**.
- Su atractivo (Driscoll, 2018): opera **24/7, a menor costo que la mano de obra, con mayor calidad y escalable**.
- Ventajas: menos carga de trabajo · **menos errores humanos** · ahorro de costos. *"Aumentar las tareas del empleado" no es ventaja* — trampa del Pruébate.

**La diferencia técnica que importa:** la RPA opera **solo en la interfaz gráfica (GUI)**, no por API. Por eso **cualquier cambio en la aplicación o el proceso obliga a reconfigurar el robot**, y solo funciona con datos electrónicos en formato estable.

### Las tres condiciones críticas de éxito

1. **Calidad de los datos**
2. **Procesos susceptibles de automatizarse** — basados en reglas, sin juicio humano, repetitivos y estables. Exige **mapear el proceso**: cada paso, excepciones, roles, entradas y salidas, sistemas, volumen, tiempos, restricciones y métricas.
3. **Disponibilidad y selección de la tecnología** — proveedor, soporte, presupuesto, capacidad del equipo de TI.

**Casos (Osman, 2019):**
- **Coca-Cola** — auditoría de RR. HH.; el objetivo explícito no era reemplazar gente sino reentrenarla.
- **Federal Bank (India)** — **250 registros por hora** contra un día completo de un empleado; 15 procesos automatizados, 53 previstos.
- **Australia Post** — **4,000+ oficinas, 25 procesos, 120 bots, 18,000 horas ahorradas al año, −15 % de costos**.

**Minería de procesos:** descubre, monitorea y mejora procesos reales **extrayendo información de las bitácoras de los sistemas** — detecta tiempos, cuellos de botella y **variaciones** (*"el proceso de pago tiene 23 variaciones distintas"*). Es el diagnóstico que debe ir **antes** del bot.

### Los 10 errores más comunes de Gartner (Guttridge & Shotton, 2023)

| Categoría | Errores |
|---|---|
| **Aproximación** | 1. Enamorarse de una sola tecnología · 2. Implementar sin TI · 3. No involucrar a todos los interesados |
| **Implementación** | 4. **Pensar que la automatización siempre es la respuesta** · 5. No dedicar suficiente tiempo a pruebas · 6. Desperdiciar esfuerzo en procesos demasiado complejos · 7. **Tratar la automatización como replicación del proceso** |
| **Impacto** | 8. **Ignorar el impacto en la cultura y el empleado** · 9. **Métricas incorrectas** (solo ahorro de costos) · 10. Descuidar el monitoreo y soporte en producción |

**Los tres que más importan para una consultora:**
- **El #4** — muchas empresas usan RPA para tapar un proceso mal diseñado, lo que **alarga la vida del sistema heredado y retrasa la modernización**. Siempre hay que evaluar *automatizar contra reemplazar*.
- **El #7** — *"pavimentar el camino de la vaca"*: automatizar la ineficiencia en vez de rediseñarla.
- **El #6** — usar **Pareto 80/20** para elegir qué automatizar: costo de implementación contra horas ahorradas.

**La tasa de fracaso** (video): casi **50 %** de las organizaciones que usan RPA no alcanza algunas de sus metas; en 2023 la hiperautomatización estaba en el **abismo de desilusión**. La razón que da el curso es incómoda y cierta: **el experto que conoce el proceso es el que tiene que describirlo para automatizarlo — y si el proyecto sale bien, se vuelve redundante.** Lo resume con Upton Sinclair: *es difícil que un hombre entienda algo cuando su salario depende de no entenderlo.*

---

## Lección 3 — Blockchain

**Qué es:** una estructura de **bloques enlazados** que forman una colección de registros llamada **libro mayor** (*ledger*). Cada participante (**nodo**) tiene una copia completa.

**El ejemplo del curso para entenderlo sin tecnicismos:** un abarrotero, una peluquera, una carnicera y un herrero se pagan entre sí; cada uno anota **todas** las transacciones de todos en su propia libreta. Cada cierto número de transacciones (un **bloque**), alguien valida, firma y **encadena su firma con la del bloque anterior**. Para alterar el historial habría que convencer a todos: por eso es prácticamente **inmutable**.

**Las características:** nodos · bloques encadenados · registro **distribuido** · **sin intermediarios** · **consenso** para modificar · **inmutabilidad** (no absoluta, pero tan difícil de romper que se considera así).

**Historia:** conceptos de **W. Scott Stornetta (1991-1997)**; primera implementación masiva con **Bitcoin (2008, Satoshi Nakamoto)**. **Ethereum** popularizó los **contratos inteligentes**: programas montados en la cadena que se ejecutan solos cuando se cumplen sus condiciones — sin notario ni intermediario.

**NFT:** token no fungible — único, no intercambiable por otro igual. El detonante fue *"EVERYDAYS: THE FIRST 5000 DAYS"* de **Beeple, vendida en 69 millones de dólares en Christie's (2021)**. El mercado se saturó y colapsó después de la pandemia.

**Casos de uso más allá de finanzas:** **cadena de suministro** (procedencia y trazabilidad en minutos, no días) · **bienes raíces** (tokenización) · **sistemas de votación** · **certificados y títulos**.

**Ventajas:** simplifica paradigmas (una libreta compartida en vez de sistemas separados) · liquidación ágil · ahorro sin intermediarios · tenencia inteligente · inmutabilidad · alta disponibilidad · alta seguridad.
**Desventajas:** escalabilidad · **consumo energético** (más de **100 TWh al año**, lo de 10 centrales nucleares) · regulación · dependencia de internet.

**¿Cuándo tiene sentido?** El curso es sensato aquí: **dentro de una sola organización casi nunca**, porque es más compleja y cara que una base de datos centralizada y las reglas internas ya se fijan fácilmente. **Su valor aparece entre organizaciones que no confían entre sí** — y adoptarla toca modelo operativo, diseño organizacional, procesos y gobierno de datos.

---

## Lección 4 — Realidad virtual, aumentada y extendida

**El espectro, de lo real a lo virtual:** ambiente real → **realidad aumentada (AR)** → virtualidad aumentada → **realidad virtual (VR)**. La **realidad extendida (XR)** es el término sombrilla que los abarca.

| | |
|---|---|
| **Realidad virtual** | Ambientes tridimensionales virtuales donde el usuario se percibe **"dentro"** e interactúa por sensores y motores (Fuchs et al., 2011) |
| **Realidad aumentada** | Complementa la vista del mundo real con gráficos, audio o video. **No crea un ambiente nuevo** |
| **Realidad mixta** | **Entre la VR y la AR**: interacción con contenido generado sobre el ambiente real — *Pokémon Go* |

**Historia:** simuladores de vuelo de **Edward Link** (1920-30) · *"The Ultimate Display"* de **Ivan Sutherland (1965)** — el artículo fundacional · **Jaron Lanier** populariza el término en los 80 · **Oculus** (Kickstarter, comprado por Facebook) en los 2010 · **Apple Vision Pro** (2024).

**Dónde está en el Hype Cycle:** en **2023** Gartner puso a la **VR en el abismo de desilusión** y movió la **AR a la rampa de consolidación** — la AR avanzó por su uso empresarial en entrenamiento y flujo de trabajo; la VR se atoró por contenido limitado y **personalización y escalabilidad limitadas**.

**Casos industriales** (Augmented Reality for Enterprise Alliance): **asistencia remota · conciencia situacional · simulación · mantenimiento · inspección**. Ejemplos: **Caterpillar** (mantenimiento apuntando el celular), **Boeing** (ensamble), Cleveland Clinic (neurocirugía).

**Impactos:** menor costo de entrenamiento · menor riesgo al simular · ciclos de diseño más cortos · nuevas formas de colaborar e interactuar con clientes.
**Inhibidores:** poco contenido · usabilidad mejorable · pocas formas de dispositivo · falta de escalabilidad · **mareos y jaquecas** en uso prolongado · falta de estandarización.

**El caso que vale recordar:** transferir el conocimiento de técnicos veteranos que se jubilan sin detener la línea. **VR para entrenar** en situaciones de riesgo; **AR para operar** con instrucciones en el campo visual. *El error clásico: usar VR —que tapa la visión— para tareas donde el técnico necesita ver su entorno.*

**Las 3 recomendaciones de Gartner:** identificar procesos que se beneficien y **medir antes** para calcular el ROI · **pocos pilotos** sobre plataformas empresariales · **evitar soluciones puntuales**.

---

## Lección 5 — Inteligencia artificial generativa

**Qué es:** IA que usa **algoritmos y modelos de aprendizaje profundo para generar contenido** —texto, imágenes, música, código— **datos o soluciones**. Se distingue de la **IA discriminativa**, que clasifica o relaciona.

**Cómo funciona:** *machine learning* — que las computadoras "aprendan" sin ser programadas explícitamente — llevado a **redes neuronales profundas**. Dos hitos: las **redes generativas adversarias (GAN)** de **Ian Goodfellow en 2014**, para imágenes; y los **LLM**, para texto.

**Por qué explotó:** el **enorme tamaño potencial de mercado** y la **generación masiva de datos**. En 2022 hubo **78 rondas de inversión por ~1,370 millones de dólares** — casi lo mismo que en los cinco años previos (PitchBook). ChatGPT llegó a **100 millones de usuarios en dos meses**.

**El potencial (McKinsey, junio 2023):** entre **2.6 y 4.4 billones de dólares anuales**, concentrados en cuatro áreas —operación con clientes, marketing y ventas, ingeniería de software e I+D—. **La banca** es de los sectores con más potencial: **200 a 340 mil millones al año**.

**Casos:** **GitHub Copilot** en programación (pero un estudio encontró vulnerabilidades en **~40 %** del código generado) · finanzas · **salud** (se estima que para 2025 más del 30 % de los fármacos se descubrirán con IA) · **arquitectura** (Zaha Hadid Architects genera ideas con DALL-E y Midjourney).

**El otro lado:** Yann LeCun, escéptico de su impacto a corto plazo · **propiedad intelectual** — en muchos países solo una persona física puede ser autora · **demandas en 2023** de escritores, artistas y periódicos por entrenar con sus obras.

**Los riesgos (Gartner):** **precisión** (*alucinaciones*) · **sesgos** · **seguridad y fraude** (*deepfakes*) · uso malicioso · poca transparencia.

**Dónde está:** para Gartner (2023), casi todo lo relacionado con IA generativa estaba en **lanzamiento o en el pico de expectativas sobredimensionadas**. De ahí la advertencia del curso: distinguir aplicaciones reales de sobreexcitación.

---

## Lo que encontré al estudiarlo

Este módulo tiene **más errores de fondo** que los anteriores. Los primeros cuatro importan si vas a usar estos datos con clientes.

**1. La cifra de gasto en RPA está inflada unas cinco veces.** El curso dice que el gasto global pasó de ~2 mil millones en 2020 a **23 mil millones en 2023**. El mercado real en 2023 rondó los **4.4 mil millones**; las cifras de 13 a 53 mil millones que circulan son **proyecciones a 2030**. Todo indica que alguien leyó mal una gráfica.

**2. "AlphaMind" no existe — es AlphaFold.** El curso dice que DeepMind creó "AlphaMind" para predecir estructuras de proteínas. El sistema es **AlphaFold**, y su base de datos superó las 200 millones de estructuras en julio de 2022.

**3. Los "15.7 billones para 2028" no son el mercado de IA generativa.** El video afirma ese tamaño de mercado para 2028, aclarando que usa *billón* en su sentido español. Esa cifra es la estimación de **PwC de lo que toda la IA aportaría al PIB mundial en 2030** — otra cosa, otro año y otro alcance.

**4. Dos afirmaciones de blockchain envejecieron mal.**
- El curso dice que blockchain **"aún no se ha extendido a transacciones en monedas fiduciarias"**. Hoy es falso: los *stablecoins* están regulados en EE. UU. desde la Ley GENIUS (2025) y **JPMorgan liquida entre 2 y 7 mil millones de dólares diarios** en depósitos tokenizados en dólares sobre su plataforma Kinexys.
- Presenta el consumo energético como si todo blockchain usara el mecanismo intensivo (*prueba de trabajo*). **Ethereum lo abandonó en septiembre de 2022** y redujo su consumo en más de 99 %. El dato de 100 TWh aplica sobre todo a Bitcoin.

*Para el examen responde la versión del curso; para un cliente, la actual.*

**5. Un anacronismo menor:** dice que GitHub Copilot se basó en "una versión especial de ChatGPT". Copilot salió en 2021 sobre **Codex**; ChatGPT es de noviembre de 2022.

**6. Restos de plantilla más visibles que en otros módulos.** Un Pruébate dice literalmente *"ayudes a XXXX a resolver"*, y varios conservan instrucciones internas de Genially. No afecta el contenido.

**7. Transcripciones con nombres deformados:** "Bejenhoe" es **Vision Pro**, "AppTuneSencual" es **Upton Sinclair**, "Karel Chapec" es **Karel Čapek** (quien inventó la palabra *robot* en *R.U.R.*, 1920), el "telar de Yakuar" es el de **Jacquard** y "Peach Book" es **PitchBook**.

---

*Archivos: lecturas y textos en `txt/`, transcripciones en `transcripciones/`, rúbrica y formato en `Reto/`.*
