#!/usr/bin/python3
"""This module defines an Ingredient class that will represent the Ingredient table in the database."""

from models.Basemodel import BaseModel, Base as ClassMapper
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship

class Ingredient(BaseModel, ClassMapper):
    """"Ingredient class defines the Ingredients table in the database. Inherits from BaseModel
    BaseModel: Representing common attributes and methods for Ingredient class."""

    __tablename__ = 'Ingredients'

    # Define the columns of the table. Each class attribute represents a column in the tables.
    name = Column(String(200), unique=True, nullable=False)
    food = relationship('Food', secondary='Food_Ingredients', 
                        back_populates='ingredients', viewonly=False)
