#!/usr/bin/python3
"""This module defines a Food class that will represent the Food table in the database."""
from models.Basemodel import BaseModel, Base as ClassMapper
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Food(BaseModel, ClassMapper):
    """Food class defines the food table in the database. Inherits from BaseModel
    BaseModel: Representing common attributes and methods for Food class."""

    __tablename__ = 'Food'

    # Define the columns of the table. Each class attribute represents a column in the tables.
    name = Column(String(200), nullable=False, unique=True)
    category = Column(String(200), nullable=False)
    image = Column(String(200), default='No image')
    ingredients = relationship("Ingredient", secondary='Food_Ingredients', 
                               back_populates='food', viewonly=False, 
                               cascade='all, delete-orphan', 
                               single_parent=True)
    recipe = relationship("Recipe", cascade='all, delete-orphan', backref='food')
