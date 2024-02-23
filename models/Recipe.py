#!/usr/bin/python3
"""Modules that defines Recipe class that will represent the Recipe table in the database."""

from models.Basemodel import BaseModel

class Recipe(BaseModel):
    """"Class that represents the Recipe table in our db"""

    # Table Columns
    content = ""
    food_id = ""

    def __init__(self, content, food_id):
        """Temporary constructor to simulate the data"""
        super().__init__()
        self.content = content
        self.food_id = food_id
