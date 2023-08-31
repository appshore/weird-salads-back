# ingredients handling

from flask import abort
from database import db
from . import models 


def get_all():
    ingredients = models.Ingredient.query.all()
    ingredients_dicts = map(lambda ingredient: ingredients.to_dict(), ingredients)
    if ingredients is None:
        abort(404, f"Ingredients not found")
    return list(ingredients_dicts)

def get_one(id):
    ingredient = models.Ingredient.query.filter_by(id=id).first()
    if ingredient is None:
        abort(404, f"Ingredient with identifier {id} not found")
    return ingredient.to_dict()


def create_one(body):
    id = body["id"]
    ingredient = models.Ingredient.query.filter_by(id=id).first()
    if ingredient:
        abort(400, f"Ingredient with identifier {id} already exist")
    ingredient = models.Ingredient.from_dict(**body)
    db.session.add(ingredient)
    db.session.commit()
    return 200

def update_one(id, body):
    ingredient = models.Ingredient.query.filter_by(id=id).first()
    if ingredient is None:
        abort(404, f"Ingredient with identifier {id} not found")
    ingredient = models.Ingredient.from_dict(**body)
    ingredient.name = body["name"]
    ingredient.division = body["division"]
    ingredient.salary = body["salary"]
    db.session.commit()
    return 200