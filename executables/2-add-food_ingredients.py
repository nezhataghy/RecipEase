#!/usr/bin/python3

from models import storage
# from models.bridges.food_ingredients import Food_Ingredients
from models.Food import Food


storage.append_ingredient_to_food('00768da3-4576-469a-af70-31e24fb3666d',
                                  '5be1c49f-8e60-4ae0-8c7f-b16099b6d1d7',
                                  '2.5 spoons')

storage.append_ingredient_to_food('00768da3-4576-469a-af70-31e24fb3666d',
                                  'efd949fe-36bd-4874-9767-a045cda05787',
                                  '2 pcs')

storage.append_ingredient_to_food('00768da3-4576-469a-af70-31e24fb3666d',
                                  '0bf89725-c9c0-4982-939a-2b4833474e68',
                                  '2 pcs')

food = storage.get_obj_by_id(Food,"00768da3-4576-469a-af70-31e24fb3666d")

for ing in food.ingredients:
    print(ing.to_dict())
