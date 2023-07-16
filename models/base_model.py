#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This class serves as the base model for all other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty:
            - Each key of the dictionary is an attribute name.
            - Each value of the dictionary is the value of the corresponding attribute.
        If kwargs is empty:
            - Assign a unique id to the 'id' attribute.
            - Assign the current datetime to the 'created_at' attribute.
            - Assign the current datetime to the 'updated_at' attribute.
            - Call models.storage.new() to store the new instance.

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            A string representation in the format:
            "[<class name>] (<self.id>) <self.__dict__>"

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.

        Call models.storage.save() to save the changes.

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            A dictionary containing all keys/values of the instance's __dict__.
            The dictionary also includes '__class__' key with the class name.
            'created_at' and 'updated_at' attributes are converted to string
            objects in ISO format.

        """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
