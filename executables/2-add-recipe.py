#!/usr/bin/python3

from models import storage
from models.Recipe import Recipe
from uuid import uuid4
from datetime import datetime


recipe = Recipe()
print('-----------------recipe id-----------------')
print(recipe.id)

print('-----------------Change recipe id-----------------')
recipe.id = str(uuid4())

print('-----------------recipe id check-----------------')
print(recipe.id)

print('-----------------recipe created_at-----------------')
print(recipe.created_at)

print('-----------------Change recipe created_at-----------------')
recipe.created_at = datetime.utcnow()

print('-----------------recipe created_at check-----------------')
print(recipe.created_at)

print('-----------------updated_at-----------------')
print(recipe.updated_at)

print('-----------------Change recipe updated_at-----------------')
recipe.updated_at = datetime.utcnow()

print('-----------------recipe updated_at check-----------------')
print(recipe.updated_at)

recipe.content = '''1- Preheat the oven to 180°C.
2- In a bowl, mix the flour, sugar, and baking powder.
3- Add the eggs, milk, and melted butter.
4- Mix until smooth.
5- Pour the mixture into a buttered cake pan.
6- Bake for 30 minutes.
7- Let cool before serving.
8- Enjoy!
'''
recipe.food_id = 'b3940ecc-a702-4122-8f7c-ba63c3b9e2d0'

print('-----------------STR-----------------')
print(recipe)

print('-----------------recipe dict-----------------')
print(recipe.to_dict())

recipe.save()
