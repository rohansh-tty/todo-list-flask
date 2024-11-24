from pymongo import MongoClient
from dotenv import load_dotenv
import os 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

config={
    "host":"localhost",
    "port":27017,
    "username":os.environ.get('DB_USER'),
    "password":os.environ.get('DB_PASSWORD')
}



uri = os.environ.get('DB_URI')

class MongoConnection:
    def __new__(cls, database):
        connection=MongoClient(uri)
        return connection[database]