#!/usr/bin/python3
from models import storage
from models.Food import Food


food = storage.all(Food)

print('----------------Test all----------------')
for f in food:
    print(f.to_dict())
    
print('----------------Test food by id----------------')

food1 = storage.get_obj_by_id(Food, '04783b33-52f3-414b-b6b6-047a92557532')
print(food1)

print('----------------Test food by name----------------')

food2 = storage.get_food_by_name("re")
for food in food2:
    print(food.to_dict())
