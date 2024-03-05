#!/usr/bin/python3
"""This module defines class that will represent the database management"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import bindparam
from os import getenv
from models.Food import Food
from models.Basemodel import BaseModel
from models.Ingredient import Ingredient
from models.Recipe import Recipe
from models.Basemodel import Base
from models.bridges.food_ingredients import Food_Ingredients


class DBstorage:
    """Database management representation"""
    
    __engine = ''
    __session = ''
    
    def __init__(self):
        usr = getenv('RCP_usr')
        pwd = getenv('RCP_pwd')
        host = getenv('RCP_host')
        db = getenv('RCP_db')
        self.__engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@{host}:3306/{db}')

    # ______________________________________________________________________________________
    
    def add(self, obj):
        """Adds a record to a table.
        obj: instance that will be added to the table.
        """

        self.__session.add(obj)

    # ______________________________________________________________________________________
    
    def all(self, cls):
        """Returns all records of a table.
           Args: 
           cls: class of the table to be queried."""
        return self.__session.query(cls).all()

    # ______________________________________________________________________________________
    
    def all_food(self):
        """Returns a list of dictionaries of all food in the database."""
        food = self.all(Food)

        if not food:
            return None

        food_map = []
        for f in food:
            food_map.append(self.get_meal(f.id))

        return food_map

    # ______________________________________________________________________________________

    def get_meal(self, meal_id):
        """Returns a dictionary of a food object with its recipe and ingredients.
        Args:
            meal_id: id of the food object to be queried."""
        from sqlalchemy import select, Column


        meal = self.get_obj_by_id(Food, meal_id)
        
        if meal is None:
            return {}
        
        # Bind the recipe and ingredients to the food object
        if meal.recipe:
            meal.recipe
        
        if meal.ingredients:
            meal.ingredients

        food_map = meal.to_dict()

        if meal.recipe:
            # add the dict representation of recipe object to the food_map
            food_map['recipe'] = food_map['recipe'].to_dict()
            del food_map.get('recipe')['food_id']

        if meal.ingredients:
            
            for i, ing in enumerate(food_map['ingredients']):
                ing_id = ing.id
                # Get the quantity of each ingredient from the Food_Ingredients table.
                quantity_query = select(Column('quantity')).where(
                    Food_Ingredients.c.food_id == bindparam('meal_id') and 
                    Food_Ingredients.c.ingredients_id == bindparam('ing_id'))

                params = {'meal_id': meal_id, 'ing_id': ing_id}

                query_result = self.__session.execute(quantity_query, params).all()
                # Set the quantity of each ingredient to the __dict__ of the ingredient object
                ing_dict = ing.__dict__
                ing_dict['quantity'] = query_result[i][0]

            # add the dict representation of each ingredient object to the food_map
            food_map['ingredients'] = [ing.to_dict() for ing in meal.ingredients]

        return food_map

    # ______________________________________________________________________________________

    def get_obj_by_id(self, cls, id):
        list_obj = self.all(cls)

        try:
            obj, = [obj for obj in list_obj if obj.id == id]
            return obj
        except ValueError:
            return None
                      

    # ______________________________________________________________________________________

    def get_food_by_name(self, name_substring):
        """Appends each meal to a list if a substring of the name is found in the meal's name.
        Args:
            name_substring: substring to search for in the food name."""
        search_result = []

        food_list = self.all(Food)

        if not food_list:
            return None

        for food in food_list:
            if name_substring in food.name:
                search_result.append(self.get_meal(food.id))

        return search_result
    
    # ______________________________________________________________________________________

    def append_ingredient_to_food(self, food_id, ingredient_id, quantity):
        """
        Appends an ingredient to a food.
        Args:
            food_id: Food id to gets Food object
            ingredient_id: ingredient_id gets an Ingredient object
            quantity: the quantity of the ingredient that should be added to the food
        """


        try:
            ingredient = self.get_obj_by_id(Ingredient, ingredient_id)
            food = self.get_obj_by_id(Food, food_id)
            if not ingredient or not food:
                raise ValueError
        except ValueError:
            if not food:
                print("Food not found in Food table")
                return "food"
            if not ingredient:
                print("Ingredient not found in Ingredients table")
                return "ingredient"
        
        try:
            query = Food_Ingredients.insert().values(food_id=bindparam('food_id'), 
                                                ingredients_id=bindparam('ingredient_id'), 
                                                quantity=bindparam('quantity'))
            params = {'food_id': food_id, 'ingredient_id': ingredient_id, 'quantity': quantity}

            self.__session.execute(query, params)
            food.save()

        except IntegrityError:
            print("The ingredient is already appended to the food!")
            raise
        
        return None

    # ______________________________________________________________________________________

    def update_ingredient_quantity(self, food_id:str, ingredient_id:str, quantity:str):
        """Updates food_ingredient's quantity
        Args: 
            food_id: food id needed to get a quantity of an ingredient
            ingredient_id: needed to get a quantity of an ingredient
            quantity: quantity of the specified ingredient in the specified food to update"""

        try:
            ingredient = self.get_obj_by_id(Ingredient, ingredient_id)
            food = self.get_obj_by_id(Food, food_id)
            if not ingredient or not food:
                raise ValueError
        except ValueError:
            if not food:
                print("Food not found in Food table")
                return 'food'
            if not ingredient:
                print("Ingredient not found in Ingredients table")
                return 'ingredient'

        try:    
            query_update = Food_Ingredients.update().values(quantity=quantity
            ).where(Food_Ingredients.c.food_id == food_id and 
                    Food_Ingredients.c.ingredients_id == ingredient_id)

            self.__session.execute(query_update)
            food.save()

        except IntegrityError:
            print("The ingredient is already appended to the food!")
            raise

        return None

    # ______________________________________________________________________________________

    def save(self):
        """Applies changes to the database."""

        self.__session.commit()

    # ______________________________________________________________________________________
    
    def reload(self):
        """Creates all tables created by the models and starts a session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    # ______________________________________________________________________________________

    def delete(self, obj):
        """Deletes a record from a table.
        obj: instance that will be deleted from the table."""
        self.__session.delete(obj)

    # ______________________________________________________________________________________

    def close(self):
        self.__session.close()
