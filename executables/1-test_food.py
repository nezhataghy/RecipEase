#!/usr/bin/python3

from models import storage
from models.Food import Food
from uuid import uuid4
from datetime import datetime


food = Food()
print('-----------------Food id-----------------')
print(food.id)

print('-----------------Change food id-----------------')
food.id = str(uuid4())

print('-----------------Food id check-----------------')
print(food.id)

print('-----------------Food created_at-----------------')
print(food.created_at)

print('-----------------Change food created_at-----------------')
food.created_at = datetime.utcnow()

print('-----------------Food created_at check-----------------')
print(food.created_at)

print('-----------------updated_at-----------------')
print(food.updated_at)

print('-----------------Change food updated_at-----------------')
food.updated_at = datetime.utcnow()

print('-----------------Food updated_at check-----------------')
print(food.updated_at)

food.name = 'Chicken Filler'
food.category = 'Chicken'

print('-----------------STR-----------------')
print(food)

print('-----------------Food dict-----------------')
print(food.to_dict())

food.save()
