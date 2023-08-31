# recipes handling

from flask import abort
from database import db
from . import models 

def check_one(id):
    recipe = models.Recipe.query.filter_by(id=id).first()
    if recipe is None:
        abort(404, f"Recipe with identifier {id} not found")
    return recipe.to_dict()


def create_one(body):
    id = body["id"]
    recipe = models.Recipe.query.filter_by(id=id).first()
    if recipe:
        abort(400, f"Recipe with identifier {id} already exist")
    recipe = models.Recipe.from_dict(**body)
    db.session.add(recipe)
    db.session.commit()
    return 200