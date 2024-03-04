#!/usr/bin/python3
"""This module defines endpoints for the food api"""

from models import storage
from flask import Flask, jsonify, make_response, abort, request as req
from api.mvp.views import app_apis
from models.Food import Food
from sqlalchemy import inspect


@app_apis.route('/food', strict_slashes=False)
def get_food():
    """Retrieves all food from the database"""
    food = storage.all_food()
    return jsonify({"food": food, "count": len(food)})

# ________________________________________________________________________________________

@app_apis.route('/food/<string:meal_id>', strict_slashes=False)
def get_meal(meal_id):
    """Retrieves a meal from the Food table"""
    meal = storage.get_meal(meal_id)

    if not meal:
        abort(404)

    return jsonify({"meal": meal})

# ________________________________________________________________________________________

@app_apis.route('/food', strict_slashes=False, methods=['POST'])
def add_meal():
    """Adds a meal to the food list"""

    json_req = req.get_json()

    # Check if request is valid json
    if not json_req:
        abort(400, description="Not a JSON.")
    
    if 'name' not in json_req and 'category' not in json_req:
        abort(400, description="Missing food name and food category.")

    if 'name' not in json_req:
        abort(400, description="Missing food name.")

    if 'category' not in json_req:
        abort(400, description="Missing food category.")

    meal = Food(**json_req)
    
    meal.save()
    if storage.get_meal(meal.id) == {}:
        return make_response(jsonify({"meal": f'"{meal.name}" already exists in the Food table'}), 400)

    return jsonify({"meal": storage.get_meal(meal.id)}), 201

# ________________________________________________________________________________________

@app_apis.route('/food/<string:meal_id>', strict_slashes=False, methods=['PUT'])
def update_meal(meal_id):
    """Updates a meal from the food list"""
    if req.is_json is False:
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

@app_apis.route('/food/<string:meal_id>', strict_slashes=False, methods=['DELETE'])
def delete_meal(meal_id):
    """Deletes a meal from the Food table"""
    meal = storage.get_obj_by_id(Food, meal_id)
    if not meal:
        abort(404)

    meal.delete()
    return jsonify({'success': f"{meal.name} deleted successfully!"})

# ________________________________________________________________________________________

@app_apis.route('/search_food/<string:meal_substr>', strict_slashes=False)
def search_food(meal_substr):
    """Retreives food by searching for its substring"""

    food_list = storage.get_food_by_name(meal_substr)

    if not food_list:
        return jsonify([])
    
    return jsonify({'food': food_list})
