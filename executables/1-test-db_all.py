#!/usr/bin/python3
from models import storage
from models.Food import Food


food = storage.all()

print('----------------Test all----------------')
for f in food:
    print(f.to_dict())
    
print('----------------Test food by id----------------')

food1 = storage.get_food_by_id("26734a42-e52e-4062-b469-c4ce32ec31b1")
print(food1)

print('----------------Test food by name----------------')

food2 = storage.get_food_by_name("re")
for food in food2:
    print(food.to_dict())
