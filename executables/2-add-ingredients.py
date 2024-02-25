#!/usr/bin/python3

from models import storage
from models.Ingredient import Ingredient
from uuid import uuid4
from datetime import datetime


ingredient = Ingredient()
print('-----------------ingredient id-----------------')
print(ingredient.id)

print('-----------------Change ingredient id-----------------')
ingredient.id = str(uuid4())

print('-----------------ingredient id check-----------------')
print(ingredient.id)

print('-----------------ingredient created_at-----------------')
print(ingredient.created_at)

print('-----------------Change ingredient created_at-----------------')
ingredient.created_at = datetime.utcnow()

print('-----------------ingredient created_at check-----------------')
print(ingredient.created_at)

print('-----------------updated_at-----------------')
print(ingredient.updated_at)

print('-----------------Change ingredient updated_at-----------------')
ingredient.updated_at = datetime.utcnow()

print('-----------------ingredient updated_at check-----------------')
print(ingredient.updated_at)

ingredient.name = 'Flour'
ingredient.quantity = '1/8 kg'

print('-----------------STR-----------------')
print(ingredient)

print('-----------------ingredient dict-----------------')
print(ingredient.to_dict())

ingredient.save()
