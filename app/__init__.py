from flask import Flask, request, jsonify, Response
from flask_restful import Api
from app.extensions import db, ma
from app.resources import TodoListResource
from app.config import Config
from celery import Celery 
import time 
import json 
import redis 
import threading
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_sock import Sock


# redis config 
pub = redis.Redis(host='localhost', port=6379)
sub = redis.Redis(host='localhost', port=6379)


global proxytask_result

# celery config 
celery_obj = Celery(
        __name__, 
        broker='redis://localhost:6379/1', # this is for message queue
        result_backend='redis://localhost:6379/1', # this is for storing states of background jobs that run using celery
    )

def message_listener():
    pubsub = sub.pubsub()
    pubsub.subscribe('my_channel')
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received: {message['data'].decode('utf-8')}")
    

# create Subscriber Thread
subscriber_thread = threading.Thread(target=message_listener)
subscriber_thread.daemon = True
subscriber_thread.start()

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
    
    # socketize app 
    sock = Sock(app)
    
    # socketio config 
    # socketio = SocketIO(app, cors_allowed_origins="*")
    @sock.route('/echo')
    def echo(ws):
        while True:
            data = ws.receive()
            ws.send({"message":"this works..."})
    

    @app.route('/send-mail', methods=["POST"])
    def send_mail_to_client():
        global proxytask_result
        proxytask_result = proxytask.delay()
        return jsonify({"status": "success", "data": {"task_id": proxytask_result.task_id}})
    
    @app.route('/task-status')
    def check_task_status():
        task_id = request.args.to_dict()['task_id']
        return jsonify({"status": "success", "data": {"task_id": task_id, "status": proxytask_result.state}})
        
            
    @app.route('/publish-json')
    def publish_json():
        payload = {
            'event': 'user_signup',
            'user_id': 12345,
            'timestamp': '2024-01-01T00:00:00Z'
        }
        pub.publish('my_channel', json.dumps(payload))
        return "JSON message published"
    
    @app.route('/publish/<msg>')
    def publish_msg(msg):
        pub.publish('my_channel', msg)
        return f'published: {msg}'
    
   
    # Add resources
    api.add_resource(TodoListResource, '/todos')      

    return app