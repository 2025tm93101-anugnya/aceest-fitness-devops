import pytest
from ACEest_Fitness import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["service"] == "ACEest Fitness & Gym API"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"

def test_get_members(client):
    res = client.get("/members")
    assert res.status_code == 200
    assert len(res.get_json()) >= 2

def test_add_member(client):
    res = client.post("/members", json={"name": "Rohan Verma", "plan": "Gold"})
    assert res.status_code == 201
    assert res.get_json()["name"] == "Rohan Verma"

def test_get_workouts(client):
    res = client.get("/workouts")
    assert res.status_code == 200
