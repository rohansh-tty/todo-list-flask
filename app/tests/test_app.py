from app.tests.conftest import  app, runner
import random

todo_name = f"test-ci-cd-{random.randint(200,10000)}"
TASK_ID = None

def test_create_todo(client):
    response = client.post("/todos", json={"name": todo_name, "status": "pending"})
    assert (
        response.json["status"] == "success"
        and response.json["data"]["name"] == todo_name
    )


def test_get_todo_by_id(client):
    response = client.get(f"/todos?todo_name={todo_name}")
    assert (
        response.json["status"] == "success"
        and response.json["data"][0]["name"] == todo_name
    )


def test_get_no_todo_by_id(client):
    response = client.get("/todos?todo_name=random_name")
    assert response.json["status"] == "success" and len(response.json["data"]) == 0


def test_update_todo(client):
    response = client.put(
        "/todos", json={"filter": {"name": todo_name}, "data": {"status": "completed"}}
    )
    assert (
        response.json["status"] == "success"
        and response.json["data"]["status"] == "completed"
    )


def test_delete_todo(client):
    response = client.delete("/todos", json={"filter": {"name": todo_name}})
    assert response.json["status"] == "success"


def test_create_task(client):
    response = client.post("/task", json={"filter": {"name": todo_name}})
    global TASK_ID
    if "task_id" in response.json["data"].keys():
        TASK_ID = response.json["data"]["task_id"]
    assert response.json["status"] == "success"


def test_get_task_status(client):
    response = client.get(f"/task/status?task_id={TASK_ID}")
    assert response.json["status"] == "success"
