#!/usr/bin/python3
"""This module defines a Food class that will represent the Food table in the database."""
from models.Basemodel import BaseModel, Base as ClassMapper
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.bridges.food_ingredients import Food_Ingredients


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



"""
create Food name=Cheese_Burger category=Beef
create Food name=Crispy_Chicken_Burger category=Chicken
create Recipe content='1-eat.2-it' food_id=aa5653f9-1aca-4168-a709-0370d609aa93
create Recipe content='1-just_eat.2-it' food_id=af693323-aa65-4820-ab2d-28647daedc00
create Ingredient name=Tomato
create Ingredient name=Onion
create Food_Ingredients food_id=273ecf52-0830-4419-a0c4-0139d5555ae6 ingredient_id=111cd477-cb94-47ef-895f-828871abd4c8 quantity=2_pcs
create Food_Ingredients food_id=d07f0902-f199-481d-a4a6-e49c1297de44 ingredient_id=c926bcab-a018-4ab2-a10b-487d9e93fc7b quantity=5_pcs
update Food_Ingredients food_id=d07f0902-f199-481d-a4a6-e49c1297de44 ingredient_id=c926bcab-a018-4ab2-a10b-487d9e93fc7b quantity=3_pcs
"""
