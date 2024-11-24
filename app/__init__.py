from flask import Flask
from flask_restful import Api
from app.extensions import db, ma
from app.resources import TodoListResource
from app.config import Config

def init_db(app):
    with app.app_context():
        # Create sample todos
        initial_todos = [
            {"name":"Complete project proposal", "status":"pending"},
            {"name":"Schedule team meeting", "status":"in-progress"},
            {"name":"Review quarterly reports", "status":"pending"},
            {"name":"Prepare marketing strategy", "status":"completed"},
            {"name":"Update client documentation", "status":"completed"},
        ]
        
        # Add and commit todos
        for todo in initial_todos:
            print(db.collection.insert_one(todo))
        print(f"Initialized database with {len(initial_todos)} todos")


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    # db.init_app(app)
    ma.init_app(app)

    # init db with dummy data 
    # init_db(app)
    
    # Create API
    api = Api(app)

    # Add resources
    api.add_resource(TodoListResource, '/todos')      
    # api.add_resource(TodoResource, '/todos/<int:todo_id>')

   
    return app