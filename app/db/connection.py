from pymongo import MongoClient

class MongoConnection:
    def __new__(cls, cfg):
        uri = cfg['MONGO_URI']
        database = cfg['DATABASE_NAME']
        connection = MongoClient(uri)
        return connection[database]
