#!/usr/bin/python3

from models import storage
from models.Food import Food
from pprint import pprint


# food = storage.get_obj_by_id(Food, 'e1745c56-86e4-4f5b-9884-48551bbb1059')
negresco = storage.get_food('e1745c56-86e4-4f5b-9884-48551bbb1059')

pprint(negresco)
