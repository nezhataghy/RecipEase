#!/usr/bin/python3

"""This modules defines endpoints for the ingredient API"""

from models import storage
from models.Ingredient import Ingredient
from flask import request, jsonify, make_response, abort
from api.mvp.views import app_apis


@app_apis.route('/ingredients', strict_slashes=False)
def get_ingredients():
    """Retrieves all ingredients from the DB"""
    ingredients = storage.all(Ingredient)
    return jsonify({"count": len(ingredients),
                    "ingredients": [ing.to_dict() for ing in ingredients]
                    })

# _________________________________________________________________________________________

@app_apis.route('ingredients/<string:ingredient_id>', strict_slashes=False)
def get_ingredient(ingredient_id):
    """Retrieves an ingredient by id from the DB"""
    ingredient = storage.get_obj_by_id(Ingredient, ingredient_id)
    if not ingredient:
        abort(404)
    return jsonify({"ingredient": ingredient.to_dict()})

# _________________________________________________________________________________________

@app_apis.route('/ingredients', strict_slashes=False, methods=['POST'])
def create_ingredient():
    """Adds an ingredient to the Ingredient table in the DB"""

    json_request = request.get_json()

    if not json_request:
        abort(400, description="Not a JSON.")
    
    if 'name' not in json_request:
        abort(400, description="Missing ingredient name.")
        
    ingredient = Ingredient(**json_request)
    ingredient.save()

    if not storage.get_obj_by_id(Ingredient, ingredient.id):
        return make_response(jsonify({
            "Ingredient": f'The ingredient already exists in the Ingredient table'
        }), 400)
    
    return jsonify({"Ingredient": ingredient.to_dict()}), 201

# _________________________________________________________________________________________

@app_apis.route('/ingredients', strict_slashes=False, methods=['PUT'])
def update_ingredient():
    """Updates an ingredient from the Ingredients table"""
    json_request = request.get_json()
    
    if not json_request:
        abort(400, description="Not a JSON")

# _________________________________________________________________________________________

@app_apis.route('/ingredients/<string:ingredient_id>', 
                strict_slashes=False, 
                methods=['DELETE'])
def delete_ingredient(ingredient_id):
    """Deletes a ingredient from the ingredients table"""
    ingredient = storage.get_obj_by_id(Ingredient, ingredient_id)
    
    if not ingredient:
        abort(404)

    deleted_id = ingredient.id
    ingredient.delete()
    
    return jsonify({"ingredient": f"ingredient {deleted_id} deleted."})

# _________________________________________________________________________________________

@app_apis.route('/food/ingredient/quantity', 
                strict_slashes=False,
                methods=['POST'])
def append_ingredient_to_meal():
    """Appends an ingredient and ingredient's quantity to a meal"""
    from sqlalchemy.exc import IntegrityError
    
    json_req = request.get_json()

    if not json_req:
        abort(400, description="Not a JSON.")

    if 'food_id' not in json_req and 'ingredient_id' not in json_req\
        and 'quantity' not in json_req:
        abort(400, description='Missing food_id, ingredient_id and quantity')

    if 'food_id' not in json_req:
        abort(400, description='Missing food_id')

    if 'ingredient_id' not in json_req:
        abort(400, description='Missing ingredient_id')

    if 'quantity' not in json_req:
        abort(400, description='Missing ingredient quantity')
    
    food_id = json_req.get('food_id')
    ingredient_id = json_req.get('ingredient_id')
    quantity = json_req.get('quantity')

    try:
        error_msg = storage.append_ingredient_to_food(food_id, ingredient_id, quantity)

    except ValueError:
        if error_msg == 'food':
            return make_response(jsonify({'Error': 'food_id is incorrect!'}), 400)

        if error_msg == 'ingredient':
            return make_response(jsonify({'Error': 'ingredient_id is incorrect!'}), 400)
        
    except IntegrityError:
        return jsonify({"Error": "The ingredient is already appended to the food!"}), 400

    return jsonify({"success": "The ingredient has been successfully appended to the food"}), 201

# _________________________________________________________________________________________


@app_apis.route('/food/ingredient/quantity', 
                strict_slashes=False,
                methods=['PUT'])
def update_ingredient_quantity():
    """Appends an ingredient and ingredient's quantity to a meal"""
    from sqlalchemy.exc import IntegrityError

    json_req = request.get_json()

    if not json_req:
        abort(400, description="Not a JSON.")

    if 'food_id' not in json_req and 'ingredient_id' not in json_req\
        and 'quantity' not in json_req:
        abort(400, description='Missing food_id, ingredient_id and quantity')

    if 'food_id' not in json_req:
        abort(400, description='Missing food_id')

    if 'ingredient_id' not in json_req:
        abort(400, description='Missing ingredient_id')

    if 'quantity' not in json_req:
        abort(400, description='Missing ingredient quantity')
    
    food_id = json_req.get('food_id')
    ingredient_id = json_req.get('ingredient_id')
    quantity = json_req.get('quantity')

    try:
        error_msg = storage.update_ingredient_quantity(food_id, ingredient_id, quantity)

    except ValueError:
        if error_msg == 'food':
            return make_response(jsonify({'Error': 'food_id is incorrect!'}), 400)

        if error_msg == 'ingredient':
            return make_response(jsonify({'Error': 'ingredient_id is incorrect!'}), 400)

    return jsonify({"success": "The ingredient quantity has updated successfully "}), 201
