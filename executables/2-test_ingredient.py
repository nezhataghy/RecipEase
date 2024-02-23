#!/usr/bin/python3

from models.Ingredient import Ingredient

ingred1 = Ingredient("Tomato", "a601f85f-4032-41e9-9f6d-d014eabb6750")


print("-------------str--------------")
print(ingred1)
print("-------------to_dict()--------------")
print(ingred1.to_dict())
