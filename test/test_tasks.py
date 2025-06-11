from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Tarefa 1"})
    assert response.status_code == 201
    assert response.json()["title"] == "Tarefa 1"

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    response = client.post("/tasks/", json={"title": "Original"})
    task_id = response.json()["id"]

    updated = client.put(f"/tasks/{task_id}", json={"title": "Atualizada", "completed": True})
    assert updated.status_code == 200
    assert updated.json()["title"] == "Atualizada"
    assert updated.json()["completed"] is True

def test_delete_task():
    response = client.post("/tasks/", json={"title": "Para Deletar"})
    task_id = response.json()["id"]

    deleted = client.delete(f"/tasks/{task_id}")
    assert deleted.status_code == 204

    not_found = client.get(f"/tasks/{task_id}")
    assert not_found.status_code == 200  
