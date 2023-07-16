#!/usr/bin/python3
"""
This is the base model unnittest
"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init_with_arguments(self):
        # Test initialization with arguments
        data = {
            "id": "12345",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00",
            "name": "Test Model",
            "my_number": 42
        }
        model = BaseModel(**data)

        self.assertEqual(model.id, "12345")
        self.assertEqual(model.created_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(model.updated_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(model.name, "Test Model")
        self.assertEqual(model.my_number, 42)

    def test_init_without_arguments(self):
        # Test initialization without arguments
        model = BaseModel()

        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        # Test __str__ representation
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42

        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        # Test save method
        model = BaseModel()
        previous_updated_at = model.updated_at

        # Modify the object and save it
        model.name = "Modified Model"
        model.save()

        self.assertNotEqual(model.updated_at, previous_updated_at)

    def test_to_dict(self):
        # Test to_dict method
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())
        self.assertEqual(model_dict["name"], "Test Model")
        self.assertEqual(model_dict["my_number"], 42)
        self.assertEqual(model_dict["__class__"], "BaseModel")

if __name__ == '__main__':
    unittest.main()
