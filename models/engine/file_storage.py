#!/usr/bin/python3
"""
This module defines the FileStorage class, which serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class represents the file storage for serializing and deserializing instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve the dictionary of all objects.

        Returns:
            A dictionary representing all objects.

        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: The object to be added.

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize the objects to the JSON file.

        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize the JSON file to objects.

        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key] = eval(class_name)(**value)
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass

