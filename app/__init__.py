from flask import Flask, request, jsonify
from flask_restful import Api
from app.extensions import db, ma
from app.resources import TodoListResource
from app.config import Config
from celery import Celery 
import time 
import json 

# celery config 
celery_obj = Celery(
        __name__, 
        broker='redis://localhost:6379/1', # this is for message queue
        result_backend='redis://localhost:6379/1', # this is for storing states of background jobs that run using celery
    )

global proxytask_result

def init_db(app):
    with app.app_context():
        # Create sample todos
        initial_todos = [
            {"name":"Complete project proposal", "status":"pending"},
            {"name":"Schedule team meeting", "status":"in-progress"}
        ]
        
        # Add and commit todos
        for todo in initial_todos:
            print(db.collection.insert_one(todo))
        print(f"Initialized database with {len(initial_todos)} todos")

@celery_obj.task
def proxytask():
        time.sleep(5)
        print('running proxy task...')
        time.sleep(5)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    ma.init_app(app)

    # init db with dummy data 
    # init_db(app)
    
    # Create API
    api = Api(app)

    @app.route('/send-mail', methods=["POST"])
    def send_mail_to_client():
        global proxytask_result
        proxytask_result = proxytask.delay()
        return jsonify({"status": "success", "data": {"task_id": proxytask_result.task_id}})
    
    @app.route('/task-status')
    def check_task_status():
        task_id = request.args.to_dict()['task_id']
        return jsonify({"status": "success", "data": {"task_id": task_id, "status": proxytask_result.state}})
        
    # Add resources
    api.add_resource(TodoListResource, '/todos')      

    return app