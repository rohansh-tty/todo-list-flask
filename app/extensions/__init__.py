from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.db import MongoConnection
import os 
from dotenv import load_dotenv


load_dotenv()
db = MongoConnection('todo-list-dev')
col = db.collection
ma = Marshmallow()