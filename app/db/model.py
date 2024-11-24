from datetime import datetime
from bson import ObjectId

from flask_bcrypt import generate_password_hash, check_password_hash

class Todo:
    def __init__(self, id, name, status, created_at, updated_at):
        self.id = id 
        self.name = name 
        self.status = status 
        self.created_at = created_at
        self.updated_at = updated_at
        