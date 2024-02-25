#!/usr/bin/python3

from models import storage
from models.Recipe import Recipe
from uuid import uuid4
from datetime import datetime
from models.Food import Food

alfredo = storage.get_obj_by_id(Food, '78b20428-c663-483a-819f-bde483d0a039')

food_alfredo = {}

food_alfredo.update({
    'name': alfredo.name,
    'image': alfredo.image,
    'category': alfredo.category,
    'recipe': alfredo.recipe[0].content,
    'ingredients': [ing.to_dict() for ing in alfredo.ingredients]
})

print(food_alfredo)
