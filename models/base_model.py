#!/usr/bin/python3

"""
this is a module containg the BaseModel class
"""
import models
import uuid
from datetime import datetime

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
        save(): Updates the `updated_at` attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the object.

    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            **kwargs: Keyword arguments to set instance attributes.
                      Keys can be attribute names and values are corresponding values.

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                value = datetime.fromisoformat(value)
            setattr(self, key, value)

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
        Updates the `updated_at` attribute with the current datetime.

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
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

