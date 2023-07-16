#!/usr/bin/python3
"""Basemodel class func"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A base model class that defines common attributes and methods for other classes.

    Attributes:
        id (str): Unique identifier assigned to an instance (UUID).
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance was last updated.

    Methods:
        __init__(**kwargs): Initializes a new instance of the BaseModel class.
        __str__(): Returns a string representation of the object.
        save(): Updates the `updated_at` attribute with the current datetime and saves the instance.
        to_dict(): Returns a dictionary representation of the object.

    """

    def __init__(self, *args, **kwargs):
        """Public instance artributes initialization
        after creation

        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values

        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
    def __str__(self):
        """
        Returns a string representation of the object.

        The string format is: "[<class name>] (<id>) <attribute dictionary>"

        Returns:
            str: String representation of the object.

        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime and saves the instance.

        This method should be called whenever an object is modified.

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        This method returns a dictionary containing all the instance attributes,
        including the '__class__' key with the class name. The 'created_at' and
        'updated_at' attributes are converted to string objects in the ISO format.

        Returns:
            dict: Dictionary representation of the object.

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
