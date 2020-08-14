from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import db

ma = Marshmallow()

class RecipesModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    making_time = db.Column(db.String(100), nullable=False)
    serves = db.Column(db.String(100), nullable=False)
    ingredients  = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, title, making_time, serves, ingredients, cost):
        self.title = title
        self.making_time = making_time
        self.serves = serves
        self.ingredients = ingredients
        self.cost = cost

    def __repr__(self):
        return '<RecipesModel {}:{}>'.format(self.id, self.title)


class RecipesSchema(ma.ModelSchema):
    class Meta:
        model = RecipesModel

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
