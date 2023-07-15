import json
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_json(self):
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = type(self).__name__
        for key, value in model_dict.items():
            if isinstance(value, datetime):
                model_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return model_dict

    def __str__(self):
        return "[{0}] ({1}) {2}".format(self.__class__.__name__, self.id, self.__dict__)

