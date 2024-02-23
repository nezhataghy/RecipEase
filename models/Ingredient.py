#!/usr/bin/python3
"""This module defines an Ingredient class that will represent the Ingredient table in the database."""

from models.Basemodel import BaseModel

class Ingredient(BaseModel):
    """"Class that represents the ingredient table in our db"""

    # Table Columns
    name = ""
    food_id = ""

    def __init__(self, name, food_id):
        """Temporary constructor to simulate the data"""
        super().__init__()
        self.name = name
        self.food_id = food_id
        