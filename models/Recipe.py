#!/usr/bin/python3
"""Modules that defines Recipe class that will represent the Recipe table in the database."""

from models.Basemodel import BaseModel, Base as ClassMapper
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Recipe(BaseModel, ClassMapper):
    """"Recipe class defines the Recipes table in the database. Inherits from BaseModel
    BaseModel: Representing common attributes and methods for Recipe class."""

    __tablename__ = "Recipes"

    # Define the columns of the table. Each class attribute represents a column in the tables.
    content = Column(String(700), unique=True, nullable=False)
    food_id = Column(String(200), ForeignKey("Food.__id"), unique=True, nullable=False)
