#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_id_is_unique(self):
        """
        Test that the 'id' attribute of BaseModel instances is unique.
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_is_datetime(self):
        """
        Test that the 'created_at' attribute of BaseModel instances is a datetime object.
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test that the 'updated_at' attribute of BaseModel instances is a datetime object.
        """
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test that calling the 'save' method updates the 'updated_at' attribute.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_str_representation(self):
        """
        Test the string representation of a BaseModel instance.
        """
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_to_dict_returns_dict(self):
        """
        Test that the 'to_dict' method returns a dictionary.
        """
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        """
        Test that the 'to_dict' method includes all necessary attributes.
        """
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_to_dict_datetime_format(self):
        """
        Test the datetime format in the dictionary returned by the 'to_dict' method.
        """
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertEqual(obj_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
