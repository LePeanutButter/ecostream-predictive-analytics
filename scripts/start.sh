#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Backend: puerto 8000
cd backend
python -m venv .venv 2>/dev/null || true
source .venv/bin/activate 2>/dev/null || true
pip install -r requirements.txt -q
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd "$ROOT"

# Frontend: puerto 3000
cd frontend
npm install
npm run dev &
FRONTEND_PID=$!
cd "$ROOT"

echo "Backend (FastAPI) running on http://localhost:8000 (PID $BACKEND_PID)"
echo "Frontend (Next.js) running on http://localhost:3000 (PID $FRONTEND_PID)"
echo "Press Ctrl+C to stop both."

wait $BACKEND_PID $FRONTEND_PID
