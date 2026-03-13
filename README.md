# EcoTrack — Entrega Sprint 4

**Proyecto:** EcoStream Predictive Analytics / EcoTrack  
**Sprint:** 4 — Interpretación de lenguaje natural y caja de texto tipo chat  
**Metodología:** Vibe Coding con Cursor y Replit

---

## Portada y datos del estudiante

| Campo                  | Valor                                                                |
| ---------------------- | -------------------------------------------------------------------- |
| **Estudiante**         | Santiago Botero Garcia                                               |
| **Curso / Asignatura** | SWNT                                                                 |
| **Fecha de entrega**   | Marzo 12, 2026                                                       |
| **Repositorio / Repl** | https://github.com/LePeanutButter/ecostream-predictive-analytics.git |

---

## Índice y navegación

1. [Escenario del prototipo en el Sprint 4](#escenario-del-prototipo-en-el-sprint-4)
2. [Instrucciones paso a paso](#instrucciones-paso-a-paso)
3. [Entregables esperados](#entregables-esperados)
4. [Rúbrica de evaluación](#rúbrica-de-evaluación)
5. [Bitácora de prompts — Sprint 4](#bitácora-de-prompts--sprint-4)
6. [Contenido del archivo .cursorrules](#contenido-del-archivo-cursorrules)
7. [Capturas de pantalla](#capturas-de-pantalla)

---

## Escenario del prototipo en el Sprint 4

**EcoTrack** es la interfaz de usuario (frontend) de un MVP que permite a los usuarios **describir en lenguaje natural sus actividades de transporte** y **visualizar la estimación de huella de carbono** asociada.  
El backend **EcoStream** (Python, FastAPI) ya existía con toda la lógica de negocio de cálculo.

- **Objetivo del Sprint 4:**  
  Transformar el flujo de entrada de datos desde un formulario clásico hacia una **experiencia tipo chat**, donde el usuario escribe mensajes como:

  > "Hoy usamos 5 camionetas y 200 kWh de electricidad"

  y el sistema:
  1. Analiza el texto con un modelo de lenguaje.
  2. Extrae datos estructurados (vehículos, electricidad, combustible, etc.).
  3. Los convierte al formato `ActividadRequest` esperado por la lógica actual.
  4. Reutiliza el endpoint de cálculo para devolver un mensaje tipo:  
     **"Con base en tu actividad, tu negocio generó aproximadamente XX kg de CO₂."**

- **Stack:**
  - Frontend: Next.js (App Router), TypeScript, TailwindCSS, Lucide-React.
  - Backend: FastAPI (servicios de cálculo + nueva capa de orquestación AI).
  - Orquestación y despliegue: Replit (`.replit`, `replit.nix`) y tooling existente del monorepo.

- **Flujo principal actualizado:**  
  Mensaje en lenguaje natural en la caja de texto → endpoint AI `/api/chat-resultado-huella` → análisis NLP + conversión a `ActividadRequest` → uso de `CalcularHuellaUseCase` → respuesta en chat + tarjeta de resultado (`ResultCard`).

---

## Instrucciones paso a paso

### 1. Preparación del entorno

- **Cursor:**
  - Abrir el repositorio y asegurarse de que el asistente AI tenga contexto del monorepo (`frontend/` + `backend/`).
  - Mantener las reglas de proyecto en `.cursorrules` para alinear el comportamiento del asistente con la arquitectura EcoTrack/EcoStream y el nuevo flujo de chat.

- **Replit / entorno local:**
  - Backend en puerto `8000` (FastAPI).
  - Frontend en puerto `3000` (Next.js).
  - El script `scripts/start.sh` sigue levantando backend y frontend como en sprints anteriores.

### 2. Implementación del flujo de lenguaje natural (Sprint 4)

#### 2.1 Backend — capa de análisis de lenguaje natural

- **Esquemas Pydantic nuevos** (`backend/app/schemas/huella.py`):

  ```python
  class AnalisisActividadRequest(BaseModel):
      message: str

  class AnalisisActividadResponse(BaseModel):
      electricity_kwh: Optional[float]
      vehicles: Optional[int]
      fuel_liters: Optional[float]
      activity: Optional[str]
      notes: Optional[str]
  ```

## Bitacora de prompts - Sprint 4

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

## Contenido del archivo .cursorrules

A continuación se incluye el contenido completo del archivo `.cursorrules` del proyecto, utilizado para guiar el comportamiento del asistente en Cursor y alinearlo con la arquitectura EcoTrack/EcoStream y la filosofía Vibe Coding.

````markdown
# EcoStream Predictive Analytics — Cursor Rules

You are an expert full-stack developer acting as an **orchestrator**. You don't just write code; you build a frictionless experience from **Text Input** to **CO2 Result**.

---

## The Duo

| Layer        | Name      | Stack                                                       |
| ------------ | --------- | ----------------------------------------------------------- |
| **Frontend** | EcoTrack  | Next.js (App Router), TypeScript, TailwindCSS, Lucide-React |
| **Backend**  | EcoStream | Python-based (calculations, NLP parsing)                    |

---

## The Goal

A simple MVP where:

1. Users input natural language activities (e.g., "I drove 20km", "I ate beef today").
2. EcoStream processes the input and returns a carbon footprint estimation.
3. EcoTrack displays the result visually.

**Core loop:** Natural Language Input → API Call → Visual CO2 Estimation.

---

## Vibe Coding Manifesto

- **Speed & Flow:** Prioritize rapid iteration over manual boilerplate.
- **Auto-Fix:** If an error appears (build, runtime, or API mismatch), **automatically propose the fix** with a full, copy-pasteable solution.
- **Complete Code:** Provide full code blocks, never snippets that leave the user guessing.
- **Beginner-Friendly + Modular:** Code should be readable and well-structured, but avoid over-engineering.

---

## Integration Logic (Critical)

| Responsibility                      | Layer                  | Action                          |
| ----------------------------------- | ---------------------- | ------------------------------- |
| NLP parsing, footprint calculations | **EcoStream (Python)** | All logic stays in the backend. |
| API consumption, UI, state handling | **EcoTrack (Next.js)** | Consume endpoints only.         |

**Rule:** Do **not** replicate calculation or NLP logic in TypeScript. Instead, create **robust TypeScript interfaces** that mirror the Python JSON response schemas. Trust the backend for all computation.

---

## Frontend (EcoTrack) — Standards

### Architecture

- **React Server Components (RSC)** by default.
- Use `'use client'` only when needed: forms, buttons, interactive UI, async state (loading/error).
- Clear folder structure, e.g.:
  - `app/` — routes, layout, pages
  - `components/` — reusable UI
  - `lib/` or `utils/` — API client, helpers, types
  - `types/` — interfaces matching EcoStream responses

### API Consumption

- Handle asynchronous states: `loading`, `error`, `success`.
- Use clear error boundaries and user-facing error messages.
- JSDoc for complex functions; comment the "why," not the "what."

### Styling

- **TailwindCSS** for layout and styling.
- **Lucide-React** for icons.
- **Aesthetic:** Minimalist, eco-friendly — greens, soft neutrals, clean typography.

---

## TypeScript Interfaces for Python Integration

Define interfaces that match EcoStream's JSON responses exactly. Example pattern:

```ts
// types/ecostream.ts — mirrors Python response
export interface FootprintResponse {
  activity: string;
  co2_kg: number;
  unit?: string;
}
export interface EcoStreamError {
  detail: string;
}
```

```

When the backend schema changes, update these interfaces first — never guess response shapes.

---

## Behavioral Rules

1. **Input → Result:** Always optimize for the flow: user types activity → sees footprint.
2. **Auto-Fix First:** On build/runtime/API errors, diagnose and propose the fix immediately.
3. **Modular Logic:** Extract formatting and data helpers into `utils/`; keep components lean.
4. **State Management:** Prefer URL state or simple React Context; avoid heavy libraries for the MVP.

---

## Documentation & Comments

- Comment the **Why:** e.g., why we map activity data in this specific way.
- Avoid redundant comments on obvious operations (e.g., what `map()` does).

---

## Persona Summary

You orchestrate the full stack. You ensure EcoTrack calls EcoStream correctly, handles loading and errors gracefully, and renders results in a clean, eco-friendly UI. You fix issues proactively and deliver copy-pasteable, working code.

**"Code for clarity, design for impact."**
```
````

---

## Referencia rápida del proyecto

### Estructura del monorepo

```text
project-root/
├── frontend/          # Next.js (puerto 3000)
├── backend/           # FastAPI (puerto 8000)
├── scripts/
│   └── start.sh       # Arranque backend + frontend
├── docs/              # frontend-mvp-architecture.md, etc.
├── .replit
├── replit.nix
└── README.md
```

### Comandos útiles

- **Replit:** Run ejecuta `scripts/start.sh` (backend + frontend).
- **Backend (local):**  
  `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8000`
- **Frontend (local):**  
  `cd frontend && npm install && npm run dev`
- **Tests backend:** `cd backend && pytest`
- **Tests frontend:** `cd frontend && npm run test`

### API principal

- `GET /api/health` → `{ "status": "ok" }`
- `GET /api/example` → mensaje de ejemplo
- `POST /api/resultado-huella` → body: `{ tipo_vehiculo, distancia_km, peso_toneladas, factor_eficiencia }` → respuesta: `{ total_co2e_kg, total_co2e_ton, _links }`
- `POST /api/chat-resultado-huella` → body: `{ message }` → respuesta: `{ total_co2e_kg, total_co2e_ton, _links, parsed_activity, result_text }`

---

_Documento generado para la entrega del Sprint 4 — EcoTrack / EcoStream. Metodología Vibe Coding._
