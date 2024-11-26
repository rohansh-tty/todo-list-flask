from datetime import datetime
from bson import ObjectId

class Todo:
    def __init__(self, id, name, status, created_at, updated_at):
        self.id = id
        self.name = name
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
