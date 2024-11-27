from flask import  request
from app.db.schema import (
    TodoSchema,
    TodoResponseSchema,
    TodoGetResponseSchema,
)
from app.services import collection, log_config
from flask.views import MethodView
from datetime import datetime
import logging
from logging.config import dictConfig

dictConfig(log_config)
logger = logging.getLogger()

class TodoListResource(MethodView):
    def get(self):
        """Retrieve all todos"""
        args = request.args.to_dict()
        response_body = []
        try:
            if "todo_name" not in args.keys():
                todos = collection.find({})
                response_body = TodoSchema().dump(todos, many=True)
            else:
                todo = collection.find_one({"name": args["todo_name"]})
                if todo is not None:
                    response_body = [
                        TodoSchema().dump(todo)
                    ]  # for consistent response schema
        except Exception as e:
            return TodoGetResponseSchema().dump({"status": "error", "error": repr(e)})
        response_ = {"status": "success", "data": response_body}
        return TodoGetResponseSchema().dump(response_)

    def post(self):
        """Create a new todo"""
        payload = request.get_json()
        try:
            payload["created_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            payload["updated_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            data = TodoSchema().load(payload)
            new_document = collection.insert_one(data)
            response_data = {
                "id": str(new_document.inserted_id),
                "name": payload["name"],
                "status": payload["status"],
            }
        except Exception as e:
            return TodoResponseSchema().dump({"status": "error", "error": e})
        response_ = {"status": "success", "data": response_data}
        return TodoResponseSchema().dump(response_)

    def put(self):
        try:
            payload = request.get_json()
            query_filter = payload["filter"]
            update_operation = {"$set": payload["data"]}
            result = collection.update_one(query_filter, update_operation)
        except Exception as e:
            return TodoResponseSchema().dump({"status": "error", "error": repr(e)})
        response_ = {"status": "success", "data": payload["data"]}
        return TodoResponseSchema().dump(response_)

    def delete(self):
        try:
            payload = request.get_json()
            query_filter = payload["filter"]
            result = collection.delete_one(query_filter)
        except Exception as e:
            return TodoResponseSchema().dump({"status": "error", "error": repr(e)})
        response_ = {"status": "success", "data": {}}
        return TodoResponseSchema().dump(response_)
