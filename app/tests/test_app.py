from app.tests.conftest import client, app, runner
import random

todo_name = f"test-ci-cd-{random.randint(200,10000)}"


def test_create_todo(client):
    response = client.post("/todos", json={"name": todo_name, "status": "pending"})
    assert (
        response.json["status"] == "success"
        and response.json["data"]["name"] == todo_name
    )

def test_get_todo_by_id(client):
    response = client.get(f"/todos?todo_name={todo_name}")
    assert response.json['status'] == "success" and response.json['data']['name'] == todo_name



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
