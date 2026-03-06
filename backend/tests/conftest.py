import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Asegurar que el módulo app está en el path
backend_root = Path(__file__).resolve().parent.parent
if str(backend_root) not in sys.path:
    sys.path.insert(0, str(backend_root))

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)
