from fastapi.testclient import TestClient
from main import app

test_app = TestClient(app)


def test_route_root():
    response = test_app.get("/")
    assert response.json()["message"] == "Home page"
    assert response.status_code == 200


def test_route_json_res():
    response = test_app.get("/json-test")
    assert response.json()["message"] == "JSON TEST"
    assert response.status_code == 201
