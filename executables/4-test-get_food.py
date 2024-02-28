#!/usr/bin/python3

from models import storage
from models.Food import Food
from pprint import pprint


# food = storage.get_obj_by_id(Food, 'e1745c56-86e4-4f5b-9884-48551bbb1059')
negresco = storage.get_meal('00768da3-4576-469a-af70-31e24fb3666d')

print("------------Food object------------")
pprint(negresco)
print('------------Food name------------')
print(negresco.get('name'))
print('------------Food image------------')
print(negresco.get('image'))
print('------------Food category------------')
print(negresco.get('category'))
print('------------Food recipe------------')
print(negresco.get('recipe').get('content'))
print('------------First food ingredient name------------')
print(negresco.get('ingredients')[0].get('name'))
print('------------First food ingredient quantity------------')
print(negresco.get('ingredients')[0].get('quantity'))
