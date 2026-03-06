# EcoStream Predictive Analytics

Monorepo fullstack: **EcoTrack** (Next.js) + **EcoStream** (FastAPI). Cálculo de huella de carbono por actividad de transporte.

## Estructura

```
project-root/
├── frontend/          # Next.js (puerto 3000)
├── backend/            # FastAPI (puerto 8000)
├── scripts/
│   └── start.sh       # Arranque backend + frontend
├── .replit
├── replit.nix
└── README.md
```

## Replit

- **Run:** ejecuta `scripts/start.sh` (levanta backend y frontend).
- Backend: http://localhost:8000 — API en `/api` (health, example, resultado-huella).
- Frontend: http://localhost:3000.

## Desarrollo local

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Configura `NEXT_PUBLIC_ECOSTREAM_URL=http://localhost:8000` si el backend está en otro host.

## API

- `GET /api/health` → `{ "status": "ok" }`
- `GET /api/example` → mensaje de ejemplo
- `POST /api/resultado-huella` → body: `{ tipo_vehiculo, distancia_km, peso_toneladas, factor_eficiencia }` → respuesta: `{ total_co2e_kg, total_co2e_ton, _links }`
