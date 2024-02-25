#!/usr/bin/python3

from models.Basemodel import BaseModel
from datetime import datetime

base = BaseModel()

print("--------------Base object representation--------------")
print(base)

print("--------------Test id--------------")
print(base.id)
base.id = None
print(base.id)

print("--------------Test created_at--------------")
print(base.created_at)
base.created_at = None
print(base.created_at)

print("--------------Updating Attributes--------------")
base.updated_at = datetime.utcnow()
print(base.updated_at)

print("--------------Dict--------------")
print(base.to_dict())
