#!/usr/bin/python3
"""Basemodel function"""
import uuid
from datetime import datetime
import models

class BaseModel(object):
    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def to_dict(self):
        d = {}
        for key, value in self.__dict__.items():
            if key != "__class__":
                d[key] = value
        return d
