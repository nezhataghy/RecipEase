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

recipe.content = '''1- heat the oven to 180°C.
2- In a bowl, mix the flour, sugar, and baking powder.
3- Add the eggs, milk, and melted butter.
4- Mix until smooth.
5- Pour the mixture into a buttered cake pan.
6- Bake for 30 minutes.
7- Let cool before serving.
'''



"""
+-----------------+----------+----------+--------------------------------------+---------------------+---------------------+
| name            | category | image    | __id                                 | __created_at        | __updated_at        |
+-----------------+----------+----------+--------------------------------------+---------------------+---------------------+
| Rizo Rice       | Rice     | No image | 04783b33-52f3-414b-b6b6-047a92557532 | 2024-02-27 20:32:21 | 2024-02-27 20:32:21 |
| Chicken Alfredo | Pasta    | No image | 994792b3-24a5-48c8-a0f6-3074fab54216 | 2024-02-27 20:32:40 | 2024-02-27 20:32:40 |
| Chicken Filler  | Chicken  | No image | 9c4806cb-2d95-4ef9-871a-070b4207927a | 2024-02-27 20:31:56 | 2024-02-27 20:31:56 |
| Fried Chicken   | Chicken  | No image | d863ca67-d0f3-4dfe-a512-4fb722d8b8d7 | 2024-02-27 20:32:58 | 2024-02-27 20:32:58 |
| Negresco        | Pasta    | No image | e1745c56-86e4-4f5b-9884-48551bbb1059 | 2024-02-27 20:32:30 | 2024-02-27 20:46:49 |
+-----------------+----------+----------+--------------------------------------+---------------------+---------------------+

"""
recipe.food_id = '00768da3-4576-469a-af70-31e24fb3666d'

print('-----------------STR-----------------')
print(recipe)

print('-----------------recipe dict-----------------')
print(recipe.to_dict())

recipe.save()
