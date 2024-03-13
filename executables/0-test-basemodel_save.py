#!/usr/bin/python3

from models.Basemodel import BaseModel

base = BaseModel()

print("--------------__dict__--------------")
print(base.__dict__)
print("--------------to_dict()--------------")
print(base.to_dict())
base.save()
print(base.to_dict())
