#!/usr/bin/python3
"""
Class BaseModel defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """constructor of a BaseModel"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    my_form = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, k, datetime.strptime(v, my_form))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        name = self.__class__.__name__
        id = self.id
        my_dict = str(self.__dict__)
        return ("[" + name + "] (" + id + ") " + my_dict)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        keys = self.__dict__.copy()
        keys['__class__'] = self.__class__.__name__
        keys["created_at"] = keys["created_at"].isoformat()
        keys["updated_at"] = keys["updated_at"].isoformat()
        return keys
