#!/usr/bin/python3

from models import storage
from flask import jsonify, request, abort, make_response
from api.mvp.views import app_apis
from models.Recipe import Recipe
from models.Food import Food
from sqlalchemy import inspect


@app_apis.route('/recipes', strict_slashes=False)
def get_recipes():
    """Retreives all recipes from the database"""
    recipes = storage.all(Recipe)
    return jsonify({"count": len(recipes),
                    "recipes": [recipe.to_dict() for recipe in recipes]
            })

# _______________________________________________________________________________________

@app_apis.route('/recipes/<string:recipe_id>', strict_slashes=False)
def get_recipe(recipe_id):
    """Get a recipe by id"""
    recipe = storage.get_obj_by_id(Recipe, recipe_id)
    if not recipe:
        abort(404)
    return jsonify({"recipe": recipe.to_dict()})

# _______________________________________________________________________________________

@app_apis.route('/recipes', strict_slashes=False, methods=['POST'])
def add_recipe():
    """Adds recipe to the Recipes table in the database"""
    
    json_req = request.get_json()

    # Check if request is valid json
    if not json_req:
        abort(400, description="Not a JSON.")


    if 'content' not in json_req and 'food_id' not in json_req:
        abort(400, description="Missing content and food_id.")

    if 'content' not in json_req:
        abort(400, description="Missing content.")
    
    if 'food_id' not in json_req:
        abort(400, description="Missing food_id.")
        
    food = storage.get_obj_by_id(Food, json_req['food_id'])
    if not food:
        abort(400, description='"food_id" is incorrect!')

    recipe = Recipe(**json_req)
    
    recipe.save()

    if not storage.get_obj_by_id(Recipe, recipe.id):
        return make_response(jsonify({"recipe": f'The recipe already exists in the Recipes table'}), 400)
    
    return jsonify({"recipe": recipe.to_dict()}), 201

# _______________________________________________________________________________________

@app_apis.route('/recipes/<string:recipe_id>', strict_slashes=False, methods=['PUT'])
def update_recipe(recipe_id):
    """Updates a recipe from the Recipes table"""
    if request.is_json is False:
        abort(400, description="Not a JSON.")
    
    recipe = storage.get_obj_by_id(Recipe, recipe_id)
    
    if not recipe:
        abort(404)
    
    data = request.get_json()
    
    if data.get('food_id'):
        food = storage.get_obj_by_id(Food, data['food_id'])

        if food.recipe:
            abort(400, description="This food already has a recipe.")
    
    for k, v in data.items():
        if k in inspect(Recipe).columns.keys():
            setattr(recipe, k, v)
        else:
            abort(404, description=f"Invalid key: {k}")
    
    recipe.save()
    
    return jsonify({"recipe": recipe.to_dict()})

# _______________________________________________________________________________________

@app_apis.route('/recipes/<string:recipe_id>', strict_slashes=False, methods=['DELETE'])
def delete_recipe(recipe_id):
    """Deletes a recipe from the Recipes table"""
    recipe = storage.get_obj_by_id(Recipe, recipe_id)
    
    if not recipe:
        abort(404)

    deleted_id = recipe.id
    recipe.delete()
    
    return jsonify({"recipe": f"Recipe {deleted_id} deleted."})
