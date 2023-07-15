#!/usr/bin/python3
"""
fun class base model do everuthing
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    our code insert here
    """
    def __init__(self, *args, **kwargs):
        """
        constructor of base Model
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dataTime = "%Y-%m-%dT %H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], dataTime)
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """
        method for named
        """
        nameClass = self.__class__.__name__
        return ("[{}] ({}) {}".format(nameClass, self.id, self.__dict__))

    def save(self):
        """
        method for save stuff
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        method for create a dict
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        formatTime = "%Y-%m-%dT %H:%M:%S.%f"
        new_dict["created_at"] = self.created_at.strftime(formatTime)
        new_dict["updated_at"] = self.updated_at.strftime(formatTime)
        return new_dict
