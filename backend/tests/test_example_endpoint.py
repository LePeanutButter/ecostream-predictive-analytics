def test_example_returns_200(client):
    response = client.get("/api/example")
    assert response.status_code == 200


def test_example_returns_json(client):
    response = client.get("/api/example")
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["message"] == "EcoStream API"
    assert data["version"] == "1.0"
