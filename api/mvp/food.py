#!/usr/bin/python3
"""This module defines endpoints for the food api"""

from models import storage
from flask import Flask, jsonify, make_response, abort, request as req
from models.Food import Food
from sqlalchemy import inspect


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)

# ________________________________________________________________________________________

@app.route('/api/food', strict_slashes=False)
def get_food():
    """Retrieves all food from the database"""
    food = storage.all_food()
    return jsonify({"food": food, "count": len(food)})

# ________________________________________________________________________________________

@app.route('/api/food', strict_slashes=False, methods=['POST'])
def add_meal():
    """Adds a meal to the food list"""

    # Check if request is valid json
    if not req.is_json:
        abort(400, description="Not a JSON.")
    
    data = req.get_json()
    
    meal = Food(**data)
    
    meal.save()
    if storage.get_meal(meal.id) == {}:
        return make_response(jsonify({"meal": f'"{meal.name}" already exists in the Food table'}), 400)

    return jsonify({"meal": storage.get_meal(meal.id)}), 201

# ________________________________________________________________________________________

@app.route('/api/food/<string:meal_id>', strict_slashes=False, methods=['PUT'])
def update_meal(meal_id):
    """Updates a meal from the food list"""
    if not req.is_json:
        abort(400, description="Not a JSON.")
    
    meal = storage.get_obj_by_id(Food, meal_id)
    
    if not meal:
        abort(404)

    data = req.get_json()
    
    for k, v in data.items():
        if k in inspect(Food).columns.keys():
            setattr(meal, k, v)
    
    meal.save()
    
    return jsonify({"meal": storage.get_meal(meal.id)})

# ________________________________________________________________________________________

@app.route('/api/food/<string:meal_id>', strict_slashes=False, methods=['DELETE'])
def delete_meal(meal_id):
    """Deletes a meal from the Food table"""
    meal = storage.get_obj_by_id(Food, meal_id)
    if not meal:
        abort(404)

    meal.delete()
    return jsonify({'success': f"{meal.name} deleted successfully!"})

# ________________________________________________________________________________________

@app.route('/api/food/<string:meal_id>', strict_slashes=False)
def get_meal(meal_id):
    """Retrieves a meal from the Food table"""
    meal = storage.get_meal(meal_id)

    if not meal:
        abort(404)

    return jsonify({"meal": meal})

# ________________________________________________________________________________________

@app.route('/api/search_food/<string:meal_substr>', strict_slashes=False)
def search_food(meal_substr):
    """Retreives food by searching for its substring"""

    food_list = storage.get_food_by_name(meal_substr)

    if not food_list:
        return jsonify([])
    
    return jsonify({'food': food_list})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
