#!/usr/bin/python3
"""Base model that defines a class containing all common\
 attributes and methods for other subclasses"""

from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import inspect


Base = declarative_base()


class BaseModel:
    """`BaseModel` class representing common attributes and methods."""
    
    # Fields that will be inherited by other models
    __id = Column('__id', String(200), primary_key=True)
    __created_at = Column('__created_at', DateTime, nullable=False)
    __updated_at = Column('__updated_at', DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, **kwargs):
        """Constructor function defines the common attributes/methods for each subclass instance"""

        self.id = None
        self.created_at = None
        self.updated_at = datetime.utcnow()

        if kwargs:
            from models.Food import Food
            from models.Ingredient import Ingredient
            from models.Recipe import Recipe
            from models.bridges.food_ingredients import Food_Ingredients

            cls = eval(self.__class__.__name__)
            for k, v in kwargs.items():
                # If the key is a column in the table, set the value to the instance attribute,
                # Otherwise, raise an AttributeError
                if k in inspect(cls).columns.keys():
                    setattr(self, k, v)
                else:
                    raise AttributeError(f"Attribute '{k}' not found in {self.__class__.__name__}")

    # _____________________________________________________________________________________

    def __str__(self):
        f"""String Representation for object of type {self.__class__.__name__}"""

        return f"{self.__class__.__name__}: ({self.id}) - {self.__dict__}"

    # _____________________________________________________________________________________

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, _):
        # If it is new instance set an id otherwise, raise AttributeError
        if self.id is None:
            self.__id = str(uuid4())
        else:
            raise AttributeError

    # _____________________________________________________________________________________

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, _):
        # If it is new instance set a created_at attribute otherwise, raise AttributeError
        if self.created_at is None:
            self.__created_at = datetime.utcnow()
        else:
            raise AttributeError

    # _____________________________________________________________________________________

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, current_date):
        self.__updated_at = current_date
    
    # _____________________________________________________________________________________

    def save(self):
        """
        Updates the datetime and saves the instance to the storage.
        If something changed to the food, it will be saved and updated in the database
        Otherwise, it will be added and saved in the database.
        """
        from models import storage
        from sqlalchemy.exc import IntegrityError
        

        self.updated_at = datetime.utcnow()
        
        try:
            storage.add(self)
            storage.save()
            
        except IntegrityError as err:
            if 'cannot be null' in str(err):
                print('Some attributes are missing in the table')
            elif self.__class__.__name__ == 'Recipe':
                print(f'The recipe already exists in the {self.__class__.__name__}s table')
            else:
                print(f'"{self.name}" already exists in the {self.__class__.__name__} table')
            # reload the storage to prevent the Rollback error.
            storage.reload()
            
    # _____________________________________________________________________________________
        
    def to_dict(self):
        """Returns a clean dictionary representation of an object"""

        date_format = "%d-%m-%YT%I:%M:%S%p"

        # Change the private attribute's default name (from '_BaseModel__.att' to '__.att')
        # and add each attribute in the __dict__ to a new dictionary
        obj_dict = {
            key.replace("_BaseModel__", '__'): value 
            for key, value in self.__dict__.items()
        }

        # Change datetime object to string format
        obj_dict['__created_at'] = datetime.strftime(self.created_at, date_format)
        obj_dict['__updated_at'] = datetime.strftime(self.updated_at, date_format)
        
        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']

        return obj_dict

    # _____________________________________________________________________________________

    def delete(self):
        """Deletes a record (instance) from the database"""
        from models import storage
        storage.delete(self)
        storage.save()
