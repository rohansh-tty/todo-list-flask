import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///todos.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

LOGGING_CONFIG = {
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
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": "logs/app.log",
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
            "level": "DEBUG",
            "handlers": ["console", "file"]
        }
    }
}
