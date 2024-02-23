#!/usr/bin/python3

from models.Recipe import Recipe

recipe1 = Recipe("Some content!!!!!", "a601f85f-4032-41e9-9f6d-d014eabb6750")


print("-------------str--------------")
print(recipe1)
print("-------------to_dict()--------------")
print(recipe1.to_dict())
