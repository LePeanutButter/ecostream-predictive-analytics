#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Backend: port 8000
cd "$ROOT/backend"
pip install -r requirements.txt -q
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Frontend: port 5000 (required for Replit web preview)
cd "$ROOT/frontend"
npm install --legacy-peer-deps -q
NEXT_PUBLIC_REPLIT_DEV_DOMAIN=$REPLIT_DEV_DOMAIN NEXT_PUBLIC_ECOSTREAM_URL=http://localhost:8000 npm run dev &
FRONTEND_PID=$!

echo "Backend (FastAPI) running on http://localhost:8000 (PID $BACKEND_PID)"
echo "Frontend (Next.js) running on http://localhost:5000 (PID $FRONTEND_PID)"
echo "Press Ctrl+C to stop both."

wait $BACKEND_PID $FRONTEND_PID
