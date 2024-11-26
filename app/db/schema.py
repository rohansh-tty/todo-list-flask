from app.extensions import db, ma
from sqlalchemy.sql import func

class TodoSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String(required=True)
    status = ma.String()
    created_at = ma.DateTime(format='%Y-%m-%dT%H:%M:%S') #+00:00')
    updated_at = ma.DateTime(format='%Y-%m-%dT%H:%M:%S') #+00:00')


class TodoGetResponseSchema(ma.Schema):
    status = ma.String()
    data = ma.List(ma.Dict(), allow_none=True)
    error = ma.String(allow_none=True)


class TodoResponseSchema(ma.Schema):
    status = ma.String()
    data = ma.Dict(allow_none=True)
    error = ma.String(allow_none=True)

class TodoUpdateSchema(ma.Schema):
    query = ma.Dict()
    data = ma.Dict()