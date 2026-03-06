#!/usr/bin/env bash
cd "$(dirname "$0")"
python -m venv .venv 2>/dev/null || true
source .venv/bin/activate 2>/dev/null || true
pip install -r requirements.txt -q
uvicorn app.main:app --host 0.0.0.0 --port 8000
