#!/usr/bin/python3

from models import storage
from models.bridges.food_ingredients import Food_Ingredients
from uuid import uuid4
from datetime import datetime
from models.Food import Food
from models.Ingredient import Ingredient


storage.append_ingredient_to_food('e1745c56-86e4-4f5b-9884-48551bbb1059',
                                  '8023931f-7980-4f06-ac6e-e44c5aac4b60',
                                  '3 pcs')

food = storage.get_obj_by_id(Food,"e1745c56-86e4-4f5b-9884-48551bbb1059")

food.save()
for ing in food.ingredients:
    print(ing.to_dict())
