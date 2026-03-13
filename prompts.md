# Bitácora de Prompts

## Sprint 1 - Construcción del Microservicio de Cálculo de Huella de Carbono

Durante el primer sprint se desarrolló el microservicio de cálculo de huella de carbono para transporte de mercancías.
El proceso no fue lineal, sino que se estructuró en cinco fases consecutivas, cada una guiada por un prompt especializado que definía el rol del modelo, el alcance de la tarea y el formato de salida esperado.

Este enfoque permitió mantener coherencia entre el modelo matemático, los requisitos funcionales, la arquitectura y la implementación, evitando desviaciones del dominio del problema.

### Fase 1: Definición del Modelo Conceptual y Matemático

**Técnica utilizada:** Chain-of-Thought Prompting
**Objetivo:** Establecer el modelo matemático del cálculo de emisiones de carbono asociado al transporte de mercancías.

En esta fase se solicitó al modelo actuar como ingeniero ambiental especializado en análisis de huella de carbono, con el fin de definir las fórmulas, variables, unidades de medida y supuestos del modelo.

Este modelo serviría posteriormente como base para los requisitos funcionales y la lógica de cálculo del sistema.

**Prompt utilizado:**

> [Rol del modelo]: Eres un(a) ingeniero/a ambiental especializado/a en sostenibilidad, análisis de ciclo de vida (LCA) y cálculo de huella de carbono corporativa bajo estándares como el GHG Protocol e ISO 14064.
>
> [Tarea]: Tu objetivo es documentar de manera exhaustiva todo el proceso de cálculo de Huella de Carbono asociada al transporte de mercancías. Debes explicar el marco conceptual, las fórmulas matemáticas, los supuestos, las variables involucradas, las unidades de medida, los factores de emisión, ejemplos prácticos de cálculo paso a paso y recomendaciones para mejorar la precisión del modelo. El cálculo debe basarse en las siguientes variables:
>
> - Tipo de vehículo (Eléctrico, Diésel, Híbrido).
> - Peso de la carga (en toneladas).
> - Distancia recorrida (en kilómetros).
> - Factor de eficiencia del combustible/energía (km/l, kWh/km u otra unidad relevante).
>
> Incluye además:
>
> - Conversión de unidades cuando sea necesario.
> - Diferenciación entre emisiones directas (Scope 1) e indirectas (Scope 2).
> - Consideraciones sobre factores de emisión promedio.
> - Fórmula general adaptable.
> - Ejemplo comparativo entre los tres tipos de vehículo.
>
> [Formato]: Devuelve la respuesta estructurada en:
>
> 1. Introducción conceptual.
> 2. Definición de variables.
> 3. Fórmulas matemáticas detalladas.
> 4. Proceso paso a paso.
> 5. Tabla comparativa de ejemplo.
> 6. Ejemplo numérico completo.
> 7. Buenas prácticas y recomendaciones técnicas.
> 8. Conclusión técnica resumida.
>
> Usa tablas cuando sea necesario y expresa resultados en kg CO₂e y toneladas CO₂e.
>
> [Ejemplo(s)]: Incluye un ejemplo práctico con los siguientes datos:
>
> - Distancia: 500 km
> - Carga: 10 toneladas
> - Vehículo diésel con eficiencia de 3 km/l
> - Factor de emisión diésel: 2.68 kg CO₂/l
>   Y muestra el desarrollo completo del cálculo.
>
> [Instrucciones extra]:
>
> - Mantén un tono técnico y profesional.
> - Explica cada fórmula antes de aplicarla.
> - No omitas pasos matemáticos.
> - Justifica los supuestos utilizados.
> - Utiliza notación clara.
> - Evita simplificaciones excesivas.
> - Asegúrate de que el modelo pueda adaptarse a distintos factores de emisión regionales.
> - Si existen diferencias metodológicas entre vehículos eléctricos e híbridos, explícalas claramente.

### Fase 2: Definición de Requisitos Funcionales

**Técnica utilizada:** Role Prompting + Structured Prompt
**Objetivo:** Traducir el modelo matemático en requisitos funcionales testeables.

Una vez definido el modelo de cálculo, se solicitó al modelo asumir el rol de analista funcional, generando casos de uso, historias de usuario y criterios de aceptación en formato Gherkin, alineados con el dominio del microservicio.

**Prompt utilizado:**

> [Rol del modelo]: Eres un(a) Analista Funcional Senior y Experto/a en Ingeniería de Requisitos con experiencia en modelado de sistemas ambientales y definición de historias de usuario bajo metodología ágil (Scrum) y especificación en Gherkin (BDD).
>
> [Tarea]: Tu objetivo es definir casos de uso detallados, historias de usuario y escenarios en formato Gherkin, basándote exclusivamente en el contexto funcional previamente definido en este chat sobre el servicio de Cálculo de Huella de Carbono asociada al transporte de mercancías.
>
> El alcance está estrictamente limitado al microservicio de cálculo de huella de carbono. No debes incluir funcionalidades fuera de este dominio (por ejemplo: registro de usuario, autenticación, gestión administrativa, reportes globales, etc.).
>
> Debes generar:
>
> 1. Lista estructurada de Casos de Uso del servicio de cálculo.
> 2. Historias de Usuario en formato:
>    "Como [tipo de usuario] quiero [acción] para [beneficio]".
> 3. Criterios de aceptación en formato Gherkin (Given / When / Then).
> 4. Escenarios alternativos y de error cuando apliquen.
> 5. Reglas de negocio explícitas.
> 6. Validaciones de datos.
> 7. Supuestos matemáticos asociados al cálculo.
> 8. Cobertura para los siguientes tipos de vehículo:
>    - Eléctrico
>    - Diésel
>    - Híbrido
> 9. Consideración de variables obligatorias:
>    - Tipo de vehículo
>    - Peso de la carga (toneladas)
>    - Distancia recorrida (km)
>    - Factor de eficiencia (km/l, kWh/km u otra unidad)
> 10. Casos de borde (valores negativos, cero, unidades inválidas, etc.).
>
> Las historias deben centrarse en:
>
> - Ejecución del cálculo.
> - Validación de variables.
> - Aplicación de factores de emisión.
> - Conversión de unidades.
> - Generación de resultado en kg CO₂e y toneladas CO₂e.
> - Comparación entre tipos de vehículo.
> - Explicación detallada del cálculo paso a paso.
>
> [Formato]:
> Devuelve la respuesta estructurada en las siguientes secciones:
>
> 1. Resumen del Alcance del Servicio
> 2. Lista de Casos de Uso (tabla con ID, Nombre, Actor, Descripción)
> 3. Historias de Usuario
> 4. Escenarios en Gherkin (cada historia debe tener su bloque Gherkin)
> 5. Reglas de Negocio
> 6. Validaciones y Casos de Error
> 7. Casos de Borde y Escenarios Negativos
>
> Cada escenario Gherkin debe escribirse en este formato:
>
> Feature: [Nombre del caso]
>
> Scenario: [Escenario principal]
> Given ...
> When ...
> Then ...
>
> [Ejemplo(s)]:
> Ejemplo de historia válida dentro del alcance:
> Como analista logístico quiero calcular la huella de carbono de un transporte de mercancía para estimar el impacto ambiental del envío.
>
> Ejemplo de historia NO válida (fuera de alcance):
> Como usuario quiero registrarme en la plataforma para guardar mis datos.
>
> [Instrucciones extra]:
>
> - Mantén un enfoque técnico y profesional.
> - No inventes funcionalidades fuera del microservicio de cálculo.
> - Cada historia debe estar alineada con el modelo matemático del cálculo.
> - No omitas escenarios de error.
> - Incluye validaciones explícitas de unidades y tipos de datos.
> - Asegúrate de que los criterios de aceptación sean testeables.
> - Evita ambigüedades.
> - Mantén coherencia con el contexto previamente definido en el chat.
> - Si es necesario, define el tipo de usuario como “Analista Ambiental”, “Operador Logístico” o “Sistema Externo”.

### Fase 3: Diseño de Arquitectura del Microservicio

**Técnica utilizada:** Role Prompting + Chain-of-Thought
**Objetivo:** Diseñar la arquitectura del sistema alineada con los requisitos funcionales previamente definidos.

El modelo fue instruido para actuar como arquitecto de software senior, proponiendo un stack tecnológico moderno y diseñando el microservicio bajo principios de Clean Architecture y microservicios desacoplados.

Además, se generaron diagramas Mermaid que representaban:

- contexto del sistema
- arquitectura de componentes
- modelo de dominio

**Prompt utilizado:**

> [Rol del modelo]: Eres un(a) Arquitecto/a de Software Senior con experiencia en diseño de sistemas distribuidos, arquitectura de microservicios, modelado basado en dominio (DDD), DevOps y buenas prácticas de ingeniería (Clean Code, SOLID, Clean Architecture y 12-Factor App).
>
> [Tarea]: Tu objetivo es definir un stack tecnológico moderno, actualizado y alineado estrictamente a las historias de usuario y casos de uso previamente definidos en este mismo chat, los cuales delimitan el alcance exclusivamente al microservicio de Cálculo de Huella de Carbono asociada al transporte de mercancías.
>
> Debes asumir que el alcance funcional ahora está completamente gobernado por las historias de usuario generadas anteriormente (enfocadas únicamente en cálculo, validaciones, aplicación de factores de emisión, conversión de unidades y generación de resultados en kg CO₂e y toneladas CO₂e).
>
> Restricción crítica:
> No debes diseñar ni incluir microservicios fuera del dominio de cálculo (por ejemplo: Usuarios, Autenticación, Reportes empresariales generales, Gestión administrativa, etc.).  
> El único dominio permitido es el Microservicio de Cálculo de Huella de Carbono.
>
> Debes:
>
> 1. Analizar las historias de usuario previamente definidas y derivar:
>    - Requisitos funcionales consolidados.
>    - Requisitos no funcionales (rendimiento, precisión matemática, trazabilidad, escalabilidad, testabilidad).
>    - Reglas de negocio implícitas.
> 2. Definir un stack tecnológico óptimo para este microservicio específico.
> 3. Justificar técnicamente cada decisión arquitectónica en función de:
>    - Cálculos matemáticos.
>    - Precisión numérica.
>    - Escalabilidad futura.
>    - Posible integración con otros sistemas.
> 4. Diseñar la arquitectura bajo un enfoque de microservicio independiente.
> 5. Aplicar Clean Architecture o arquitectura hexagonal dentro del microservicio.
> 6. Modelar correctamente:
>    - Entidades de dominio.
>    - Casos de uso.
>    - Servicios de aplicación.
>    - Puertos y adaptadores.
> 7. Incluir validaciones de datos y manejo de errores como parte explícita del diseño.
> 8. Considerar que cada microservicio debe tener su propia base de datos (aunque en este caso solo existe uno).
> 9. Definir estrategia de testing alineada a BDD (dado que las historias están en Gherkin).
>
> [Formato]:
>
> Devuelve la respuesta estructurada en las siguientes secciones:
>
> 1. Análisis del Alcance Derivado de las Historias de Usuario
>    - Requisitos funcionales consolidados
>    - Requisitos no funcionales
>    - Reglas de negocio
> 2. Propuesta de Stack Tecnológico
>    - Backend
>    - Base de Datos
>    - Infraestructura
>    - DevOps
>    - Testing
>    - Justificación técnica basada en el dominio matemático del sistema
> 3. Estándares de Codificación y Arquitectura
>    - Aplicación de SOLID en el dominio de cálculo
>    - Separación por capas (Domain, Application, Infrastructure)
>    - Organización de carpetas
>    - Manejo de dependencias
>    - Estrategia de validación y manejo de errores
>    - Estrategia de pruebas (unitarias, integración, BDD)
> 4. Diagrama de Contexto (en bloque Mermaid)
>    - Debe mostrar únicamente:
>      - Actor (ej. Analista Ambiental / Sistema Externo)
>      - Microservicio de Cálculo
>      - Base de Datos local
> 5. Diagrama de Componentes (en bloque Mermaid)
>    - Debe representar arquitectura hexagonal o Clean Architecture
>    - Incluir:
>      - API Controller
>      - Application Service
>      - Domain Layer
>      - Repository Interface
>      - Infraestructura (DB Adapter)
>    - Relaciones claras y coherentes
> 6. Diagrama de Clases (en bloque Mermaid)
>    - Debe extender el diagrama de componentes
>    - Basado en arquitectura de microservicio
>    - Tipado fuerte (UUID, float, Decimal, str, date)
>    - Incluir:
>      - Entidad ActividadTransporte
>      - Entidad FactorEmision
>      - Servicio CalculadoraCarbono
>      - ResultadoHuella
>      - Value Objects si aplican (Distancia, PesoCarga, Eficiencia)
>    - Separación por dominio
>    - Métodos representativos
>    - Relaciones correctas
>    - Aplicación de principios SOLID
>    - Manejo explícito de validaciones
>
> IMPORTANTE:
>
> - Cada diagrama debe estar en su propio bloque `mermaid`.
> - No incluir texto dentro del bloque Mermaid.
> - El Diagrama de Clases debe ser coherente con el de Componentes.
> - No incluir microservicios adicionales.
> - Mantener bajo acoplamiento y alta cohesión.
> - El diseño debe estar listo para producción.
> - Si usas Python + FastAPI como ejemplo, justificar por qué es adecuado para cálculos matemáticos y servicios REST livianos.
> - Priorizar precisión numérica (ej. uso de Decimal si aplica).
>
> [Instrucciones extra]:
>
> - Mantén un tono técnico y profesional.
> - No inventes funcionalidades fuera de las historias de usuario.
> - Justifica cada decisión con base en el dominio del cálculo de huella de carbono.
> - Evita arquitectura innecesariamente compleja.
> - Diseña pensando en extensibilidad futura (ej. nuevos tipos de actividad).
> - Asegura coherencia total entre requisitos, arquitectura y diagramas.

### Fase 4: Desarrollo de Pruebas Unitarias (TDD)

**Técnica utilizada:** Test-Driven Development Prompting
**Objetivo:** Generar pruebas unitarias antes de la implementación del sistema.

El modelo fue configurado para actuar como ingeniero especializado en TDD, generando una suite completa de pruebas unitarias que validaban:

- cálculos de emisiones
- validaciones de datos
- manejo de errores
- casos de borde

Esto permitió garantizar que la implementación posterior cumpliera los requisitos funcionales definidos.

**Prompt utilizado:**

> [Rol del modelo]: Eres un(a) Desarrollador/a Senior especializado/a en pruebas unitarias y TDD (Test-Driven Development) con experiencia en arquitecturas de microservicios, Clean Architecture y MVC.
>
> [Tarea]: Tu objetivo es generar un conjunto completo de pruebas unitarias usando TDD para el microservicio de Cálculo de Huella de Carbono, siguiendo **estrictamente la arquitectura, diagramas de componentes y diagramas de clases previamente definidos** en este chat. Las pruebas deben cubrir:
>
> 1. Todos los casos funcionales derivados de las historias de usuario y diagramas de clases.
> 2. Casos de borde y de error, incluyendo:
>    - Distancia = 0
>    - Peso de la carga negativo o cero
>    - Tipos de vehículo no soportados
>    - Factores de eficiencia nulos o inválidos
> 3. Validaciones de entrada y tipos de datos de cada entidad (Actividades, Factores de Emisión, ResultadoHuella, etc.).
> 4. Resultados esperados en kg CO₂e y toneladas CO₂e.
> 5. Escenarios combinando distintos tipos de vehículos y variables.
> 6. Uso de la infraestructura definida (repositorios locales, servicios de dominio, adaptadores) según los diagramas de componentes y clases.
> 7. Manejo explícito de errores y excepciones definidos en el dominio.
>
> El entorno será **local**, sin despliegue, y la base de datos será **quemada (“hardcoded”)** para pruebas, garantizando consistencia y reproducibilidad.
>
> [Formato]: Devuelve la respuesta en **bloques de código del lenguaje que corresponda al stack definido anteriormente**, con:
>
> - Funciones de prueba nombradas de manera descriptiva (`test_<clase>_<escenario>`).
> - Setup y teardown utilizando los repositorios locales definidos en la arquitectura.
> - Uso de asserts o verificaciones de salida coherentes con la arquitectura de dominio.
> - Comentarios explicativos de cada prueba, referenciando las entidades y servicios de los diagramas de clases/componentes.
> - Cada prueba debe reflejar la estructura de capas (Controller -> Application Service -> Domain -> Repository) según los diagramas previos.
>
> [Ejemplo(s)]:
> Ejemplo conceptual siguiendo la arquitectura definida (pseudocódigo):
>
> ```pseudo
> test CalculadoraCarbono_calculo_vehiculo_desconocido:
>     Dado una ActividadTransporte con tipo_vehiculo = "gasolina_inexistente"
>     Cuando se ejecuta CalculadoraCarbono.calcular(actividad)
>     Entonces se lanza ExcepcionTipoVehiculoNoSoportado
> ```
>
> [Instrucciones extra]:
>
> - Asegúrate de cubrir todos los tipos de vehículo soportados (Eléctrico, Diésel, Híbrido) y combinaciones de variables.
> - Mantén coherencia estricta con los diagramas de clases y componentes.
> - Incluye escenarios principales, alternativos y de error.
> - Explica brevemente cada prueba antes de definirla.
> - Prioriza claridad y reproducibilidad.
> - No incluyas dependencias externas innecesarias ni supuestos que no estén en los diagramas previos.
> - La arquitectura del microservicio debe reflejarse en la forma en que se escriben las pruebas.

### Fase 5: Implementación del Microservicio

**Técnica utilizada:** Role Prompting + Code Generation
**Objetivo:** Implementar el microservicio completo respetando la arquitectura y las pruebas previamente definidas.

En esta fase final se solicitó al modelo implementar el sistema completo siguiendo:

- principios SOLID
- Clean Architecture
- endpoints REST nivel de madurez 2
- compatibilidad con las pruebas TDD generadas previamente

**Prompt utilizado:**

> [Rol del modelo]: Eres un(a) Desarrollador/a Senior y Arquitecto/a de Software experto/a en microservicios, Clean Architecture, principios SOLID, TDD y diseño modular.
>
> [Tarea]: Tu objetivo es realizar la **implementación final del microservicio de Cálculo de Huella de Carbono**, siguiendo estrictamente:
>
> 1. La arquitectura previamente definida (Clean Architecture / MVC / diagramas de componentes y clases).
> 2. Los principios SOLID y buenas prácticas de programación.
> 3. Manejo robusto de errores y validaciones de dominio (tipos de vehículo, distancia, peso, factor de eficiencia, unidades).
> 4. Modularidad y separación clara de capas (Controller / Application Service / Domain / Repository / Infrastructure).
> 5. Que **todos los casos de prueba TDD previamente desarrollados pasen**, incluyendo escenarios principales, alternativos y casos de borde.
> 6. Que los **endpoints REST cumplan con madurez nivel 2**, incluyendo:
>    - URIs consistentes y centradas en recursos (`/actividades`, `/resultado-huella`).
>    - Uso correcto de métodos HTTP (`GET`, `POST`, etc.).
>    - Uso adecuado de códigos de estado HTTP según resultado.
>    - Representación consistente de recursos en JSON.
>    - Hipermedios opcionales o referencias a recursos relacionados según necesidad.
>
> El código debe ser **reproducible en un entorno local**, usando la base de datos quemada definida anteriormente para el microservicio.
>
> [Formato]: Devuelve la respuesta en **bloques de código completos** en el lenguaje o stack previamente definido, con:
>
> - Clases y módulos separados según la arquitectura.
> - Métodos con tipado fuerte y validaciones de entrada.
> - Manejo de excepciones consistente y documentado.
> - Comentarios explicativos de cada módulo y función, referenciando el dominio (ActividadTransporte, FactorEmision, CalculadoraCarbono, ResultadoHuella, etc.).
> - Endpoints REST diseñados con madurez nivel 2.
> - Código listo para pasar todas las pruebas TDD existentes.
>
> [Ejemplo(s)]:  
> Ejemplo conceptual de método de cálculo robusto:
>
> ```pseudo
> class CalculadoraCarbono:
>     metodo calcular(actividad):
>         si tipo_vehiculo no soportado:
>             lanzar ExcepcionTipoVehiculoNoSoportado
>         validar distancia, carga y eficiencia
>         aplicar factor de emisión correspondiente
>         retornar ResultadoHuella(total_co2e)
>
> Controller POST /calcular-huella:
>     request JSON:
>         {
>             "tipo_vehiculo": "Diesel",
>             "distancia_km": 100,
>             "peso_toneladas": 5,
>             "factor_eficiencia": 3.0
>         }
>     response JSON:
>         {
>             "total_co2e_kg": 893.0,
>             "total_co2e_ton": 0.893
>         }
> ```
>
> [Instrucciones extra]:
>
> - Asegúrate de que la implementación sea **modular, escalable y mantenible**.
> - Cada módulo debe reflejar la **arquitectura y diagramas de clases/componentes previamente definidos**.
> - No inventes funcionalidades adicionales fuera del microservicio de cálculo.
> - Incluye manejo de errores robusto y validación de todos los datos de entrada.
> - Explica brevemente cómo cada módulo o clase cumple con los principios SOLID y la arquitectura.
> - Los endpoints REST deben cumplir madurez nivel 2 y devolver códigos HTTP apropiados.
> - Todos los resultados deben ser coherentes con los cálculos de huella de carbono previamente especificados (kg CO₂e y toneladas CO₂e).
> - Prioriza claridad, consistencia con los tests TDD anteriores y reproducibilidad en entorno local.

## Sprint 2 - Extensión Predictiva del Sistema

El segundo sprint tuvo como objetivo extender el microservicio existente mediante un módulo predictivo, capaz de estimar emisiones futuras a partir de actividades de transporte proyectadas.

El desarrollo se organizó en cuatro fases principales.

### Fase 1: Análisis y Planificación

**Técnica:** System Prompt & Few-Shot Prompting.
**Objetivo:** Definir el comportamiento del agente y generar requisitos precisos basados en ejemplos.

**Prompt:**

> [Rol del modelo]: Eres un(a) Analista de Negocios Senior en EcoStream.
> [Tarea]: Generar 5 requisitos funcionales para el nuevo Módulo Predictivo que complemente el actual microservicio de cálculo de transporte.
> [Formato]: Lista numerada.
> [Ejemplo(s)]:
>
> 1. El sistema debe predecir el impacto de cambiar la flota de vehículos DIESEL a ELÉCTRICO basándose en los factores de emisión actuales (2.68 vs 0.12).
> 2. El módulo debe alertar cuando la eficiencia real reportada se desvíe más de un 15% del `factor_eficiencia` promedio histórico.
>    [Instrucciones extra]: Asegúrate de que los requisitos mencionen las entidades existentes como `ActividadTransporte` y `TipoVehiculo`.

### Fase 2: Arquitectura y Diseño

**Técnica:** Chain-of-Thought (CoT).
**Objetivo:** Desglosar el razonamiento arquitectónico para garantizar escalabilidad y seguridad.

**Prompt:**

> [Rol del modelo]: Eres un(a) Arquitecto/a de Software Cloud.
> [Tarea]: Diseñar la expansión de la arquitectura actual para integrar el módulo predictivo.
> [Formato]: Explicación lógica CoT y diagrama Mermaid.
> [Instrucciones extra]:
>
> 1. Analiza cómo el nuevo servicio predictivo consumirá el `RepositorioFactoresEmisionLocal`.
> 2. Propón una capa de persistencia para guardar los `ResultadoHuella` históricos.
> 3. Mantén el patrón de Inyección de Dependencias manual observado en tu punto de entrada (`app.py` o `main.py`).
> 4. Explica cómo desacoplar el cálculo en tiempo real de las proyecciones a largo plazo.

### Fase 3: Generación de Código y Refactorización

**Técnica:** Role Play y Delimitadores.
**Objetivo:** Obtener código limpio y optimizar fragmentos existentes.

**Prompt de Generación (Boilerplate):**

> [Rol del modelo]: Eres un(a) Desarrollador/a Backend Senior.
> [Tarea]: Crear el caso de uso `PredecirHuellaMensualUseCase` siguiendo la estructura del código actual.
> [Formato]: Bloque de código Python.
> [Instrucciones extra]:
>
> - Usa la entidad `ActividadTransporte` y el servicio `CalculadoraCarbono` ya definidos.
> - Implementa la lógica para recibir un listado de actividades proyectadas y devolver un acumulado.
> - Respeta el uso de `dataclasses` y el manejo de excepciones como `ValorInvalidoException`.

**Prompt de Refactorización:**

> [Rol del modelo]: Eres un(a) Especialista en Clean Code.
> [Tarea]: Refactorizar el método `calcular` de la clase `CalculadoraCarbono` para soportar cálculos masivos.
> [Formato]: Código original vs Refactorizado.
> [Instrucciones extra]: Actualmente el código hace el cálculo uno a uno. Optimízalo para recibir una lista de `ActividadTransporte` y devolver una lista de `ResultadoHuella` usando listas por comprensión o Map/Reduce para mejorar el rendimiento.

### Fase 4: Testing, Seguridad y Documentación

**Técnica:** Red Teaming y Adversarial Prompting.
**Objetivo:** Garantizar la calidad del software y la protección contra ataques.

**Prompt de Testing (Unit Tests):**

> [Rol del modelo]: Eres un(a) Ingeniero/a de QA Automation.
> [Tarea]: Crear pruebas unitarias para el nuevo endpoint de predicción.
> [Formato]: Bloque de código Pytest.
> [Instrucciones extra]:
>
> - Utiliza la clase `FakeRepositorioFactores` que ya existe en los tests actuales.
> - Asegúrate de probar la validación de `distancia_km` negativa, verificando que se lance la `ValorInvalidoException` definida en el dominio.

**Prompt de Red Teaming (Seguridad):**

> [Rol del modelo]: Eres un(a) Auditor de Seguridad.
> [Tarea]: Auditar el controlador `calcular_huella` en `presentation/controllers.py`.
> [Formato]: Tabla de vulnerabilidades y mitigaciones.
> [Instrucciones extra]:
>
> - Analiza el riesgo de que el `request_data` en el Use Case no esté tipado (usa un `dict` genérico).
> - Evalúa el impacto de que el repositorio sea "hardcoded" y si esto expone lógica de negocio sensible.
> - Revisa si el manejo de excepciones genéricas (`Exception`) en el controlador podría filtrar trazas de error internas al cliente.

## Sprint 3 - Desarrollo del Frontend MVP y Suite de Testing Integrada

En el tercer sprint se centró en construir la interfaz de usuario mínima viable para registrar actividades y visualizar la huella de carbono, así como en generar la infraestructura completa de testing para garantizar la calidad del producto. Se mantuvo la coherencia con el microservicio de cálculo previamente desarrollado, evitando reimplementar la lógica del backend.

El proceso se estructuró en tres fases:

### Fase 1: Diseño del Frontend MVP

**Técnica utilizada:** Role Prompting + Structured Prompting
**Objetivo:** Crear un frontend minimalista que consuma la API existente de cálculo de huella de carbono, mostrando resultados claros y permitiendo la entrada de actividades en lenguaje natural.

**Prompt utilizado:**

> [Rol del modelo]: Eres un arquitecto de software senior especializado en desarrollo asistido por IA y Vibe Coding. Actúas como orquestador del sistema completo y priorizas experiencia de usuario, rapidez de iteración y claridad técnica.
>
> [Tarea]: Tu objetivo es ayudar a construir la capa de frontend de un MVP que permita a los usuarios registrar actividades diarias en lenguaje natural y visualizar su estimación de huella de carbono.
>
> IMPORTANTE (CRÍTICO):
>
> - TODO el backend ya existe y está implementado en Python.
> - Los endpoints de cálculo de huella de carbono ya están disponibles.
> - NO debes reimplementar lógica de cálculo ni procesamiento de lenguaje natural.
> - El frontend únicamente debe consumir los endpoints existentes y mostrar los resultados.
> - El objetivo es hacer que el sistema sea utilizable mediante una interfaz web simple.
>
> Debes:
>
> - Diseñar una interfaz mínima donde el usuario pueda escribir actividades en lenguaje natural.
> - Conectar la interfaz con los endpoints existentes del backend.
> - Proponer la arquitectura del frontend.
> - Definir interfaces de datos que representen las respuestas JSON del backend en Python.
> - Proponer prompts de alto nivel para que un agente de programación genere el código.
> - Optimizar el flujo principal: texto del usuario → llamada API → visualización de resultado.
>
> [Formato]: Devuelve la respuesta en Markdown con las siguientes secciones:
>
> 1. Arquitectura del MVP
> 2. Flujo completo del usuario (Input → API → Resultado)
> 3. Estructura recomendada del proyecto frontend
> 4. Interfaces de datos que representen las respuestas del backend Python
> 5. Componentes principales de la interfaz
> 6. Prompts recomendados para generar el frontend con un agente de programación
> 7. Manejo de estados (loading, error, success)
> 8. Estrategia de integración con el backend existente
> 9. Recomendaciones para mantener el frontend desacoplado del backend
>
> [Ejemplo(s)]:
> Ejemplo de interacción esperada del usuario:
>
> Usuario escribe:
> "Hoy manejé 20km y comí carne."
>
> Flujo esperado:
>
> 1. El texto se envía al endpoint del backend.
> 2. El backend procesa el lenguaje natural.
> 3. El backend devuelve una estimación de CO2.
> 4. El frontend muestra el resultado en una tarjeta visual clara.
>
> [Instrucciones extra]:
>
> - NO inventes lógica de cálculo.
> - NO simules resultados.
> - NO dupliques funcionalidad del backend Python.
> - Asume que el backend es la fuente de verdad para todos los cálculos.
> - Prioriza simplicidad y rapidez para un MVP funcional.
> - Propón código modular y fácil de mantener.
> - El flujo principal del producto siempre debe ser: actividad escrita → resultado de huella de carbono visible.

### Fase 2: Generación del Scaffolding Fullstack en Replit

**Técnica utilizada:** Role Prompting + Code Generation
**Objetivo:** Generar la estructura completa del proyecto fullstack (Next.js + FastAPI) dentro de un monorepo optimizado para Replit, incluyendo scripts de orquestación.

**Prompt utilizado:**
[Rol del modelo]:
Eres un arquitecto de software senior y programador fullstack experto en Python, Next.js, FastAPI y despliegue en Replit. Sabes diseñar monorepos fullstack optimizados para desarrollo y despliegue en Replit sin usar Docker.

[Tarea]:

> Tu objetivo es generar el scaffolding completo y el código necesario para una aplicación fullstack que se ejecutará completamente en Replit.
>
> La aplicación tendrá:
>
> - Frontend en Next.js
> - Backend en Python usando FastAPI
> - Ambos viviendo dentro del mismo repositorio (monorepo)
> - Orquestación mediante `.replit` y `replit.nix`
> - Un script de arranque que levante backend y frontend simultáneamente
>
> El frontend debe ser generado completamente basándose en el documento `frontend-mvp-architecture.md` previamente definido en el proyecto.
>
> Debes asumir que ese documento contiene:
>
> - estructura de carpetas
> - páginas
> - componentes
> - hooks
> - estado
> - layout
> - rutas
>
> y debes implementarlo fielmente.
>
> [Formato]:
> Devuelve la respuesta en formato de **estructura de proyecto + archivos completos**.
>
> Usa este formato:
>
> 1. Estructura del proyecto (tree)
> 2. Archivos de configuración
> 3. Código completo de cada archivo
>
> Cada archivo debe mostrarse así:
>
> FILE: path/to/file.ext
>
> ```code
> contenido completo
> ```
>
> No omitas archivos importantes.
>
> [Arquitectura requerida]:
>
> El proyecto debe usar esta base:
>
> project-root/
> │
> ├── frontend/
> │ ├── app/ # Next.js App Router
> │ ├── components/
> │ ├── hooks/
> │ ├── services/
> │ ├── styles/
> │ ├── public/
> │ ├── package.json
> │ └── next.config.js
> │
> ├── backend/
> │ ├── app/
> │ │ ├── main.py
> │ │ ├── routes/
> │ │ ├── services/
> │ │ ├── models/
> │ │ └── schemas/
> │ │
> │ ├── requirements.txt
> │ └── start_backend.sh
> │
> ├── scripts/
> │ └── start.sh
> │
> ├── .replit
> ├── replit.nix
> └── README.md
>
> [Requisitos importantes]:
>
> 1. El backend FastAPI debe correr en puerto 8000.
> 2. El frontend Next.js debe correr en puerto 3000.
> 3. Next.js debe consumir la API Python mediante `/api`.
> 4. Debe existir un endpoint de prueba `/api/health`.
>
> Ejemplo respuesta:
>
> GET /api/health →
> { "status": "ok" }
>
> [Orquestación en Replit]:
>
> Debes crear:
>
> replit.nix
> que instale:
>
> - nodejs
> - python311
> - pip
>
> El archivo `.replit` debe ejecutar:
>
> bash scripts/start.sh
>
> El script `start.sh` debe:
>
> 1. iniciar backend
> 2. iniciar frontend
> 3. mantener ambos procesos corriendo
>
> Ejemplo comportamiento esperado:
>
> start.sh
>
> - inicia FastAPI con uvicorn
> - inicia Next.js con npm run dev
>
> [Frontend]:
>
> Debes implementar completamente el frontend usando:
>
> - Next.js App Router
> - React
> - fetch para consumir el backend
> - estructura definida en `frontend-mvp-architecture.md`
>
> Incluye:
>
> - layout global
> - página principal
> - servicios de API
> - componentes base
> - manejo de estado si el documento lo define
>
> [Backend]:
>
> Implementar backend con:
>
> - FastAPI
> - estructura modular
> - router `/api`
> - endpoint `/api/health`
> - endpoint `/api/example`
>
> [Instrucciones extra]:
>
> Asegúrate de:
>
> - escribir código limpio y listo para ejecutar
> - evitar pseudocódigo
> - incluir todos los imports
> - incluir dependencias necesarias
> - que el proyecto funcione al presionar **Run en Replit**
> - mantener una arquitectura escalable
>
> No expliques el código.
> Solo devuelve la estructura del proyecto y los archivos completos.

### Fase 3: Configuración de la Suite de Testing Fullstack

**Técnica utilizada:** Role Prompting + Structured Prompting + Code Generation
**Objetivo:** Implementar la infraestructura de pruebas para backend y frontend, asegurando que todos los endpoints y componentes se puedan testear fácilmente en Replit.

**Prompt utilizado:**

> [Rol del modelo]:
> Eres un ingeniero senior de QA y testing automation experto en pruebas para aplicaciones fullstack con Python (FastAPI) y Next.js. Tienes amplia experiencia configurando suites de testing para monorepos y entornos de desarrollo en Replit.
>
> [Tarea]:
> Tu objetivo es **generar y ajustar toda la infraestructura de testing del proyecto** para una aplicación fullstack que corre completamente en Replit.
>
> Debes crear los **tests necesarios para frontend y backend**, configurar las herramientas de testing, y asegurar que las pruebas puedan ejecutarse fácilmente en el entorno del proyecto.
>
> El proyecto ya tiene esta arquitectura base:
>
> project-root/
> │
> ├── frontend/
> │ ├── app/
> │ ├── components/
> │ ├── hooks/
> │ ├── services/
> │ ├── styles/
> │ └── tests/
> │
> ├── backend/
> │ ├── app/
> │ │ ├── routes/
> │ │ ├── services/
> │ │ ├── models/
> │ │ └── schemas/
> │ │
> │ └── tests/
> │
> ├── scripts/
> ├── .replit
> ├── replit.nix
> └── README.md
>
> Debes **analizar la arquitectura existente y generar la suite completa de pruebas** acorde a ella.
>
> [Formato]:
> Devuelve la respuesta en formato de **estructura de proyecto + archivos completos**.
>
> Primero muestra la estructura de carpetas de testing actualizada.
>
> Luego muestra cada archivo usando el formato:
>
> FILE: path/to/file.ext
>
> ```code id="tests1"
> contenido completo
> ```
>
> No omitas archivos de configuración.
>
> [Testing Backend]:
>
> Configura testing del backend Python usando:
>
> - pytest
> - httpx para testing de endpoints
> - pytest-asyncio para endpoints async
>
> Debes crear:
>
> backend/tests/
> ├── conftest.py
> ├── test_health.py
> ├── test_example_endpoint.py
>
> Los tests deben:
>
> - levantar la app de FastAPI en modo testing
> - verificar endpoints HTTP
> - validar status codes
> - validar respuestas JSON
>
> Ejemplo esperado:
>
> GET /api/health →
> status_code = 200
> response.json() = {"status": "ok"}
>
> [Testing Frontend]:
>
> Configura testing del frontend Next.js usando:
>
> - Jest
> - React Testing Library
>
> Debes crear:
>
> frontend/tests/
> ├── setupTests.ts
> ├── HomePage.test.tsx
> ├── apiService.test.ts
>
> Los tests deben verificar:
>
> - renderizado de componentes
> - comportamiento de hooks
> - consumo de API
> - manejo de estados básicos
>
> [Configuración requerida]:
>
> Debes incluir también los archivos de configuración necesarios:
>
> Frontend:
>
> - jest.config.js
> - package.json scripts de testing
>
> Backend:
>
> - pytest.ini
> - dependencias adicionales en requirements.txt
>
> Scripts esperados:
>
> Frontend:
>
> npm run test
>
> Backend:
>
> pytest
>
> [Integración con el proyecto]:
>
> Los tests deben funcionar con la arquitectura existente:
>
> - frontend consume backend
> - backend expone rutas `/api/*`
>
> Debes usar **mocks cuando el frontend consuma APIs**.
>
> [Instrucciones extra]:
>
> Asegúrate de:
>
> - escribir tests funcionales y ejecutables
> - incluir imports completos
> - usar buenas prácticas de testing
> - evitar pseudocódigo
> - mantener una estructura clara y mantenible
> - que los tests puedan ejecutarse dentro del entorno de Replit sin configuraciones externas
>
> No expliques el código.
>
> Devuelve únicamente:
>
> 1. estructura de tests
> 2. archivos completos
> 3. configuraciones necesarias.

## Sprint 4

En el cuarto sprint se añadió una capa de interpretación de lenguaje natural y una interfaz tipo chat sobre la lógica de huella de carbono que ya existía.

El foco estuvo en: extraer datos estructurados desde texto libre, mapearlos al formato ya usado por el backend y actualizar la experiencia de usuario para que gire en torno a una conversación.

El proceso se estructuró en tres fases.

### Fase 1: Diseño de la interpretación de lenguaje natural

**Técnica utilizada:** Role Prompting + Structured Prompting
**Objetivo:** Definir cómo el modelo de lenguaje debe extraer datos estructurados de mensajes escritos en lenguaje natural por el usuario.

**Prompt utilizado:**

> [Rol del modelo]: Eres un ingeniero de software senior especializado en interfaces conversacionales y mejora de aplicaciones existentes.
>
> [Tarea]: Tu objetivo es transformar el formulario actual del proyecto en una interfaz tipo chat donde el usuario pueda describir sus actividades empresariales en lenguaje natural. Debes reutilizar la lógica existente que actualmente envía datos al backend y adaptarla para que funcione con mensajes de chat.
>
> [Formato]: Devuelve los cambios necesarios en el código existente indicando:
>
> - qué componentes modificar
> - qué nuevos componentes crear
> - cómo manejar el estado de los mensajes
> - cómo enviar el mensaje del usuario al endpoint existente del backend
>
> [Ejemplo(s)]: Usuario: "Hoy usamos 5 camionetas de reparto y gastamos 200kWh de electricidad"
>
> Sistema:
> "Analizando tu actividad..."
>
> Sistema:
> "Resultado estimado de emisiones: 48 kg de CO₂."
>
> [Instrucciones extra]:
> Asegúrate de:
>
> - reutilizar la estructura actual del proyecto
> - no eliminar la lógica existente del formulario sino adaptarla
> - mostrar los mensajes del usuario y del sistema en burbujas de chat
> - mostrar un indicador de "analizando actividad" mientras llega la respuesta

### Fase 2: Integración del JSON extraído con la lógica actual

**Técnica utilizada:** Role Prompting + Code Generation
**Objetivo:** Integrar el resultado del análisis de lenguaje natural con la lógica actual del backend que calcula emisiones, sin duplicar funcionalidad.

**Prompt utilizado:**

> [Rol del modelo]: Eres un especialista en procesamiento de lenguaje natural aplicado a aplicaciones empresariales.
>
> [Tarea]: Tu objetivo es analizar mensajes escritos por el usuario que describen actividades empresariales y extraer datos estructurados que puedan ser utilizados por la lógica existente del backend para calcular emisiones.
>
> [Formato]: Devuelve la respuesta siempre en formato JSON con los siguientes campos:
>
> - electricity_kwh
> - vehicles
> - fuel_liters
> - activity
> - notes
>
> [Ejemplo(s)]: Input: "Hoy usamos 3 camionetas y consumimos 150kWh de electricidad"
>
> Output:
> {
> "electricity_kwh": 150,
> "vehicles": 3,
> "fuel_liters": null,
> "activity": "delivery",
> "notes": "uso de vehículos y consumo eléctrico"
> }
>
> [Instrucciones extra]:
> Asegúrate de:
>
> - no inventar datos que el usuario no mencione
> - devolver null cuando un valor no esté presente
> - generar siempre un JSON válido
> - mantener el formato consistente para que el backend pueda procesarlo

### Fase 3: Transformación del formulario en interfaz tipo chat

**Técnica utilizada:** Role Prompting + Code Generation
**Objetivo:** Sustituir el formulario tradicional por una experiencia de chat, respetando la lógica de negocio y los servicios ya existentes.

**Prompt utilizado:**

> [Rol del modelo]: Eres un arquitecto de software especializado en integración de funcionalidades dentro de sistemas existentes.
>
> [Tarea]: Tu objetivo es integrar el resultado del análisis de lenguaje natural con la lógica actual del backend que calcula emisiones. Debes reutilizar los servicios o funciones que ya existen para realizar el cálculo.
>
> [Formato]: Devuelve:
>
> 1. el flujo lógico completo
> 2. las modificaciones necesarias en el endpoint que recibe el mensaje del chat
> 3. cómo convertir el JSON extraído del mensaje en el formato que espera la lógica actual de cálculo
>
> [Ejemplo(s)]:
>
> Mensaje del usuario:
> "Hoy usamos 5 camionetas y 200kWh de electricidad"
>
> Datos extraídos:
> {
> "vehicles": 5,
> "electricity_kwh": 200
> }
>
> Resultado del sistema:
> "Con base en tu actividad, tu negocio generó aproximadamente 48 kg de CO₂."
>
> [Instrucciones extra]:
> Asegúrate de:
>
> - reutilizar la lógica actual del backend
> - no duplicar funcionalidades que ya existen
> - mantener el flujo simple y fácil de mantener
