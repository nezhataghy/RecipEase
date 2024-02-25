#!/usr/bin/python3

from models import storage
from models.bridges.food_ingredients import Food_Ingredients
from uuid import uuid4
from datetime import datetime
from models.Food import Food
from models.Ingredient import Ingredient


storage.append_ingredient_to_food("b3940ecc-a702-4122-8f7c-ba63c3b9e2d0",
                          "2f4aa9a6-0557-4057-a222-fc5b431649b3",
                          "9a86ef23-2b16-4a27-a8e0-e2085fcabc3d",
                          "abcaded4-b13d-4383-a5c6-67aacede93d1")


filler = storage.get_obj_by_id(Food,"b3940ecc-a702-4122-8f7c-ba63c3b9e2d0")

filler.save()
for ing in filler.ingredients:
    print(ing.to_dict())
