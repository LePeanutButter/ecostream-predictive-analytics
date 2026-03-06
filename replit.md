# EcoTrack — Huella de Carbono

A carbon footprint calculator for transport activities. Full-stack app with a Next.js frontend and FastAPI Python backend.

## Architecture

- **Frontend**: Next.js 16 (React), Tailwind CSS — runs on port 5000
- **Backend**: FastAPI (Python 3.11), Uvicorn — runs on port 8000

## Project Structure

```
/
├── frontend/          # Next.js application
│   ├── app/           # App router pages
│   ├── components/    # React components
│   ├── services/      # API client (api.ts)
│   ├── lib/           # Utilities (env.ts)
│   └── types/         # TypeScript types
├── backend/           # FastAPI application
│   └── app/
│       ├── main.py    # App entry point (CORS configured)
│       └── routes/    # API routes (health, huella, example)
└── scripts/
    └── start.sh       # Startup script (runs both services)
```

## Running the App

The workflow `Start application` runs `bash scripts/start.sh`, which:
1. Installs Python deps and starts FastAPI on port 8000
2. Installs npm deps and starts Next.js on port 5000 (Replit web preview)

## Environment Variables

- `NEXT_PUBLIC_ECOSTREAM_URL` — Backend URL (set to `http://localhost:8000` in start.sh)
- `ALLOWED_ORIGINS` — Comma-separated CORS allowed origins (defaults to localhost:5000)

## Language Modules Installed

- `python-3.11` — Python runtime + pip
- `nodejs-20` — Node.js + npm

## Security Notes

- CORS is restricted to configured origins (not wildcard `*`)
- `ALLOWED_ORIGINS` env var controls allowed origins
- Next.js updated to latest version (CVE-2025-66478 patched)
