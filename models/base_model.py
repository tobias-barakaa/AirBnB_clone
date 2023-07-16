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
        __init__(*args, **kwargs): Initializes a new instance of the BaseModel class.
        __str__(): Returns a string representation of the object.
        save(): Updates the `updated_at` attribute with the current datetime and saves the instance.
        to_dict(): Returns a dictionary representation of the object.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Args:
            *args: Variable length argument list.
            **kwargs: Keyword arguments to set instance attributes.
                      Keys can be attribute names, and values are corresponding values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

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
        models.storage.save()

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


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at).__name__)
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key, value in my_model_json.items():
        print("\t{}: ({}) - {}".format(key, type(value).__name__, value))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at).__name__)

    print("--")
    print(my_model is my_new_model)
