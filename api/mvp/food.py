#!/usr/bin/python3
"""This module defines endpoints for the food api"""

from models.Food import Food
from models import storage
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/api/food', strict_slashes=False)
def get_food():
    """"Retrieves all food from the database"""
    food = storage.all_food()
    return jsonify({"results": food, "count": len(food)})

if __name__ == '__main__':
    app.run(debug=True)
