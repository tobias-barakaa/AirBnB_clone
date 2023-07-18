#!/usr/bin/python3
"""
JSON serialization/deserialization for objects
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """File storage for objects serialization/deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all objects.

        Returns:
            dict: A dictionary containing all objects, where keys are
                  "<object class name>.<object id>" and values are the objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Set the object in the dictionary with the key as "<obj class name>.id".

        Args:
            obj (BaseModel): The object to store in the dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to a JSON file.

        The dictionary of objects (__objects) conv to json fmt
        and stored in a file defined by __file_path.
        """
        data = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, User):
                data[key] = self._serialize_user(obj)
            else:
                data[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.

        If the JSON file exists, it will be read and converted to dict
        of objects (__objects) where keys are "<object class name>.
        values are the objects. If the file doesn't exist, no exp raised.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    if class_name == 'User':
                        obj = self._deserialize_user(value)
                    else:
                        cls = eval(class_name)
                        obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def _deserialize_user(self, obj_dict):
        """Deserializes a User object."""
        obj_dict.pop("__class__")
        obj_dict["__class__"] = "User"
        return User(**obj_dict)

    def _serialize_user(self, user):
        """Serializes a User object."""
        obj_dict = user.to_dict()
        obj_dict.pop("__class__")
        obj_dict["__class__"] = "User"
        return obj_dict


CLASSES = {
    # ...
    "User": User,
}
