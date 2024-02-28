#!/usr/bin/python3

from models import storage


# food = storage.get_obj_by_id(Food, 'e1745c56-86e4-4f5b-9884-48551bbb1059')
food = storage.all_food()

print("------------all Food------------")
print(food)
