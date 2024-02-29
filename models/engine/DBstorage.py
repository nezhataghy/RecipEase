#!/usr/bin/python3
"""This module defines class that will represent the database management"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
        DBstorage.__engine = create_engine(f'mysql+mysqldb://{usr}:{pwd}@{host}:3306/{db}')

    # ______________________________________________________________________________________
    
    def add(self, obj):
        """Adds a record to a table.
        obj: instance that will be added to the table.
        """

        DBstorage.__session.add(obj)

    # ______________________________________________________________________________________
    
    def all(self, cls):
        # food.recipe
        # food.ingredients
        # mapping them to the food object
        # get food
        return DBstorage.__session.query(cls).all()
    
    # ______________________________________________________________________________________
    
    def all_food(self):
        food = self.all(Food)

        food_map = []
        for f in food:
            food_map.append(self.get_meal(f.id))

        return food_map

    # ______________________________________________________________________________________

    def get_meal(self, meal_id):
        from models.bridges.food_ingredients import Food_Ingredients
        from sqlalchemy import select, Column
        from sqlalchemy.sql import bindparam

        meal = self.get_obj_by_id(Food, meal_id)
        
        # Bind the recipe and ingredients to the food object
        # if not meal.recipe or not meal.ingredients:
        #     return meal.to_dict()

        if meal.recipe:
            meal.recipe[0]
        
        if meal.ingredients:
            meal.ingredients

        food_map = meal.to_dict()

        if meal.recipe:
            # Update the recipe property with the dict of recipe object
            food_map['recipe'] = food_map['recipe'][0].to_dict()
            del food_map.get('recipe')['food_id']

        if meal.ingredients:
            # Update ingredients property with the dict of each ingredient object
            for i, ing in enumerate(food_map['ingredients']):
                ing_id = ing.id
                quantity_query = select(Column('quantity')).where(
                    Food_Ingredients.c.food_id == bindparam('meal_id') and 
                    Food_Ingredients.c.ingredients_id == bindparam('ing_id'))
            
                params = {'meal_id': meal_id, 'ing_id': ing_id}

                query_result = DBstorage.__session.execute(quantity_query, params).all()
                ing_dict = ing.__dict__
                ing_dict['quantity'] = query_result[i][0]

            food_map['ingredients'] = [ing.to_dict() for ing in meal.ingredients]

        return food_map

    # ______________________________________________________________________________________

    def get_obj_by_id(self, cls, id):
        Food_list = self.all(cls)

        try:
            food, = [food for food in Food_list if food.id == id]
            return food
        except ValueError:
            return None
                      

    # ______________________________________________________________________________________

    def get_food_by_name(self, name):
        search_result = []

        food_list = self.all(Food)
        
        if not food_list:
            return None

        # search_result = [search_result.append(food) for food in food_list if name in food.name]
        for food in food_list:
            if name in food.name:
                search_result.append(food)
        
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
        from models.bridges.food_ingredients import Food_Ingredients
        from sqlalchemy.sql import bindparam
        from sqlalchemy.exc import IntegrityError

        try:
            ingredient = self.get_obj_by_id(Ingredient, ingredient_id)
            food = self.get_obj_by_id(Food, food_id)
            if not ingredient or not food:
                raise ValueError
        except ValueError:
            if not food:
                print("Food not found in Food table")
            if not ingredient:
                print("Ingredient not found in Ingredients table")
            return
        
        try:
            query = Food_Ingredients.insert().values(food_id=bindparam('food_id'), 
                                                ingredients_id=bindparam('ingredient_id'), 
                                                quantity=bindparam('quantity'))
            params = {'food_id': food_id, 'ingredient_id': ingredient_id, 'quantity': quantity}

            DBstorage.__session.execute(query, params)
            food.save()

        except IntegrityError:
            print("The ingredient is already appended to the food!")

    # ______________________________________________________________________________________

    def update_food_ingredient(self, food_id, ingredient_id, quantity):
        """Updates food_ingredient's ingredient_id or quantity"""
        from sqlalchemy.exc import IntegrityError
        from models.bridges.food_ingredients import Food_Ingredients
        from sqlalchemy import update, Column

        try:
            ingredient = self.get_obj_by_id(Ingredient, ingredient_id)
            food = self.get_obj_by_id(Food, food_id)
            if not ingredient or not food:
                raise ValueError
        except ValueError:
            if not food:
                print("Food not found in Food table")
            if not ingredient:
                print("Ingredient not found in Ingredients table")
            return

        try:    
            query_update = Food_Ingredients.update().values(quantity=quantity
            ).where(Food_Ingredients.c.food_id == food_id and 
                    Food_Ingredients.c.ingredients_id == ingredient_id)

            DBstorage.__session.execute(query_update)
            food.save()

        except IntegrityError:
            print("The ingredient is already appended to the food!")

    # ______________________________________________________________________________________

    def save(self):
        """Applies changes to the database."""
        DBstorage.__session.commit()

    # ______________________________________________________________________________________
    
    def reload(self):
        """Creates all tables created by the models and starts a session"""
        Base.metadata.create_all(DBstorage.__engine)
        Session = sessionmaker(DBstorage.__engine)
        DBstorage.__session = Session()

    # ______________________________________________________________________________________

    def delete(self, obj):
        """Deletes a record from a table.
        obj: instance that will be deleted from the table."""
        DBstorage.__session.delete(obj)

    # ______________________________________________________________________________________

    def close(self):
        DBstorage.__session.close()
