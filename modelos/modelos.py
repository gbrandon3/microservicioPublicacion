import datetime
from attr import fields 
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Response:
    message = str()
    succeded = bool()
    errors = []
    Estado = str()
    hora_inicio = str()
    hora_fin = str()