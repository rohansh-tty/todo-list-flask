import os
from flask import Flask

BASE_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(lineno)d",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "detailed",
            "filename": "logs/app2.log",
            "mode": "a"
        }
    },
    "loggers": {
        "flask.app": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False
        },
        "flask.errors": {
            "level": "ERROR",
            "handlers": ["file"],
            "propagate": False
        },
        "werkzeug": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False
        },
        "root": {
            "level": "INFO",
            "handlers": ["console", "file"]
        }
    }
}


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')
    LOGGING_CONFIG = BASE_LOGGING_CONFIG
    DB_NAME = os.getenv('DB_NAME', 'todo-list-dev')

    # Marshmallow configuration
    MARSHMALLOW_STRICT = True
    MARSHMALLOW_INCLUDE_NULLS = False

    
    @classmethod
    def init_app(cls, app: Flask) -> None:
        """Initialize development-specific configurations."""
        app.logger.setLevel(cls.LOGGING_LEVEL, 'DEBUG')


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')

    # MongoDB Development Connection
    MONGO_URI = os.getenv('DEV_DB_URI', 'mongodb://localhost:27017/dev_database')
    
   
    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = 'INFO'
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')

    # MongoDB Production Connection
    MONGO_URI = os.getenv('PROD_MONGO_URI', 'mongodb://localhost:27017/dev_database')
    
   