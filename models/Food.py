#!/usr/bin/python3
"""This module defines a Food class that will represent the Food table in the database."""
from models.Basemodel import BaseModel


class Food(BaseModel):
    """"Food class defines the food table in the database"""

    # Table Columns
    name = ""
    category = ""
    image = b""
    
    def __init__(self, name, category, image):
        super().__init__()
        self.name = name
        self.category = category
        self.image = image
        """Temporary constructor to simulate the data"""
