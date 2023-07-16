#!/usr/bin/python3
"""
json serioulize/deserialize
"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    value["created_at"] = datetime.datetime.strptime(
                        value["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    value["updated_at"] = datetime.datetime.strptime(
                        value["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
