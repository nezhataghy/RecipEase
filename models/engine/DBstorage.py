#!/usr/bin/python3
"""This module defines class that will represent the database management"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.Food import Food
from models.Basemodel import BaseModel
from models.Ingredient import Ingredient
from models.Recipe import Recipe
from models.bridges import food_ingredients
from models.Basemodel import Base


class DBstorage:
    """Database management representation"""
    
    __engine = ''
    __session = ''
    
    def __init__(self):
        usr = getenv('RCP_usr')
        pwd = getenv('RCP_pwd')
        host = getenv('RCP_host')
        db = getenv('RCP_db')
        DBstorage.__engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@{host}:3306/{db}')

    # ______________________________________________________________________________________
    
    def add(self, obj):
        """Adds a record to a table.
        obj: instance that will be added to the table.
        """
        
        DBstorage.__session.add(obj)

    # ______________________________________________________________________________________
    
    def delete(self, obj):
        """Deletes a record from a table.
        obj: instance that will be deleted from the table."""
        DBstorage.__session.delete(obj)
    
    # ______________________________________________________________________________________
    
    def all(self, cls):
        # food.recipe
        # food.ingredients
        # mapping them to the food object
        # get food
        return DBstorage.__session.query(cls).all()
    
    # ______________________________________________________________________________________
    
    def save(self):
        DBstorage.__session.commit()
