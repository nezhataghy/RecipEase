#!/usr/bin/python3

"""This modules defines endpoints for the ingredient API"""

from models import storage
from models.Ingredient import Ingredient
from flask import request, jsonify, make_response, abort
from api.mvp.views import app_appis



@app_appis.route('/ingredients', strict_slashes=False)
def get_ingredients():
    """Retrieves all ingredients from the DB"""
    ingredients = storage.all(Ingredient)
    return jsonify({"count": len(ingredients),
                    "ingredients": [ing.to_dict() for ing in ingredients]"
                    })


@app_appis.route('ingredients/<ingredient_id>', strict_slashes=False)
