#!/usr/bin/python3

from sqlalchemy import Table, Column, ForeignKey, String, PrimaryKeyConstraint
from models.Basemodel import Base


Food_Ingredients = Table('Food_Ingredients', Base.metadata,
                         Column('food_id', String(200), ForeignKey('Food.__id')),
                         Column('ingredients_id', String(200), ForeignKey('Ingredients.__id')),
                         Column('quantity', String(15), nullable=False),
                         PrimaryKeyConstraint('food_id', 'ingredients_id'))
