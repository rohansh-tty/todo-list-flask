from flask import Blueprint, request, jsonify, Response, make_response
from flask_restful import Resource, abort
from app.db.schema import TodoSchema, TodoResponseSchema, TodoUpdateSchema
from app.extensions import db,col
from flask.views import MethodView
import json
from datetime import datetime
import time 

class TodoListResource(MethodView):
    def get(self):
        """Retrieve all todos"""
        args = request.args.to_dict()
        response_body = None
        try:
            if 'todo_name' not in args.keys():
                todos= col.find({})
                response_body = TodoSchema().dump(todos, many=True)
            else:
                todo = col.find_one({'name': args['todo_name']})
                response_body = TodoSchema().dump(todo) 
        except Exception as e:
            return TodoResponseSchema().dump({"status": "error", "error": repr(e)})
        response_ = {"status": "success", "data": response_body}
        return TodoResponseSchema().dump(response_)

    def post(self):
        """Create a new todo"""
        payload = request.get_json()
        try:
            payload['created_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+03:00')
            payload['updated_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+03:00')
            data = TodoSchema().load(payload)
            new_document = col.insert_one(data)
            response_data = {'id': str(new_document.inserted_id), 'name': payload['name'], 'status': payload['status']}
        except Exception as e:
            return TodoResponseSchema().dump({"status": "error", "error": e})
        response_ = {"status": "success", "data": response_data}
        return TodoResponseSchema().dump(response_)
    
    def put(self):
        try:
            payload = request.get_json()
            query_filter =  payload['filter']
            update_operation = { '$set' : 
                payload['data']
            }
            result = col.update_one(query_filter, update_operation)
        except Exception as e:
            return TodoResponseSchema().dump({"status": "error", "error": repr(e)})
        response_ = {'status': "success", "data": payload['data']}
        return TodoResponseSchema().dump(
            response_)

        

    def delete(self):
        try:
            payload = request.get_json()
            query_filter =  payload['filter']
            result = col.delete_one(query_filter)
        except Exception as e:
            return TodoResponseSchema().dump({"status": "error", "error": repr(e)})
        response_ = {'status': "success", "data": {}}
        return TodoResponseSchema().dump(
            response_)
