import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
db = SQLAlchemy()

class Publicacion (db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    routeId=db.Column(db.Integer)
    userId=db.Column(db.Integer)
    plannedStartDate=db.Column(db.DateTime)
    plannedEndDate= db.Column(db.DateTime)
    createdAt=db.Column(db.DateTime, default=datetime.datetime.utcnow())


 
class PublicacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Publicacion
        include_relationships = True
        load_instance = True

    plannedStartDate= fields.String()
    plannedEndDate = fields.String()
    createdAt=fields.String()
