#!/usr/bin/python3

from models.Food import Food

food1 = Food("Chicken Burger", "Chicken", b"00aysha")


print("-------------str--------------")
print(food1)
print("-------------to_dict()--------------")
print(food1.to_dict())
