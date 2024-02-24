#!/usr/bin/python3
"""Base model that defines a class containing all common\
 attributes and methods for other subclasses"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """`BaseModel` class representing common attributes and methods."""

    def __init__(self):
        self.__id = str(uuid4())
        self.__created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    # _____________________________________________________________________________________

    def __str__(self):
        f"""String representation for Object of type {self.__class__.__name__}"""

        obj_repr = f"{self.__class__.__name__}: ({self.id}) - {self.to_dict()}"
        return obj_repr

    # _____________________________________________________________________________________

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, _):
        print("Can't set attribute 'id'")
        pass

    # _____________________________________________________________________________________

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, _):
        print("Can't set attribute 'created_at'")
        pass

    # _____________________________________________________________________________________

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, current_date):
        self.__updated_at = current_date
    
    # _____________________________________________________________________________________

    def save(self):
        """Updates the datetime and saves the instance to the storage."""
        self.updated_at = datetime.utcnow()
    # _____________________________________________________________________________________
        
    def to_dict(self):
        """Returns a clean dictionary representation of an object"""

        date_format = "%d-%m-%YT%I:%M:%S%p"

        obj_dict = {
            key.replace("_BaseModel__", '__'): value 
            for key, value in self.__dict__.items()
        }

        obj_dict['__created_at'] = datetime.strftime(self.created_at, date_format)
        obj_dict['__updated_at'] = datetime.strftime(self.updated_at, date_format)
        obj_dict['__class__'] = self.__class__.__name__

        return obj_dict

    # _____________________________________________________________________________________

    def delete(self):
        """Deletes a record (instance) from the database"""
        pass
