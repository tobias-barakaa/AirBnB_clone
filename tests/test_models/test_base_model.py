#!/usr/bin/python3
"""
This is the base model unnittest
"""


from models.base_model import BaseModel
import unittest
from datetime import datetime
import os
import sys

class TestBaseModel(unittest.TestCase):
    def test_id_is_unique(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_is_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_str_representation(self):
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_to_dict_returns_dict(self):
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_to_dict_datetime_format(self):
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertEqual(obj_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
