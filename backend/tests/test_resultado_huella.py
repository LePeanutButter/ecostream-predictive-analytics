def test_resultado_huella_returns_201(client):
    payload = {
        "tipo_vehiculo": "Diesel",
        "distancia_km": 100,
        "peso_toneladas": 1,
        "factor_eficiencia": 1,
    }
    response = client.post("/api/resultado-huella", json=payload)
    assert response.status_code == 201


def test_resultado_huella_returns_json_with_co2(client):
    payload = {
        "tipo_vehiculo": "Diesel",
        "distancia_km": 100,
        "peso_toneladas": 1,
        "factor_eficiencia": 1,
    }
    response = client.post("/api/resultado-huella", json=payload)
    data = response.json()
    assert "total_co2e_kg" in data
    assert "total_co2e_ton" in data
    assert "_links" in data
    assert isinstance(data["total_co2e_kg"], (int, float))
    assert isinstance(data["total_co2e_ton"], (int, float))


def test_resultado_huella_invalid_tipo_returns_422(client):
    payload = {
        "tipo_vehiculo": "InvalidType",
        "distancia_km": 100,
        "peso_toneladas": 1,
        "factor_eficiencia": 1,
    }
    response = client.post("/api/resultado-huella", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()


def test_resultado_huella_negative_distancia_returns_422(client):
    payload = {
        "tipo_vehiculo": "Diesel",
        "distancia_km": -10,
        "peso_toneladas": 1,
        "factor_eficiencia": 1,
    }
    response = client.post("/api/resultado-huella", json=payload)
    assert response.status_code == 422
