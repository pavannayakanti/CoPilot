from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_fake_data():
    response = client.post("/getfakedata", json={
        "name": "Alice",
        "age": 25,
        "city": "Wonderland"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "data" in response.json()