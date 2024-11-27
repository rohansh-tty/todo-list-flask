from flask_marshmallow import Marshmallow
from app.db import MongoConnection
from dotenv import load_dotenv
import os
from app.config import DevelopmentConfig, ProductionConfig

config_map = {"dev": DevelopmentConfig, 'prod': ProductionConfig}

load_dotenv()
CONFIG = os.environ.get("CONFIG", "dedevv")
    
# Initialize MongoDB Connection
config_ = config_map[CONFIG]
mongo_config = {
    'MONGO_URI': config_.MONGO_URI,
    'DATABASE_NAME': config_.DB_NAME
}

log_config = config_.LOGGING_CONFIG
db = MongoConnection(mongo_config)
collection = db.collection
ma = Marshmallow()
