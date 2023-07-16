#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path

    def tearDown(self):
        # Remove the temporary file after testing
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_and_reload(self):
        # Create a few BaseModel instances
        model1 = BaseModel()
        model1.name = "Test Model 1"
        model1.my_number = 42

        model2 = BaseModel()
        model2.name = "Test Model 2"
        model2.my_number = 100

        # Save the models to the file
        storage = FileStorage()
        storage.new(model1)
        storage.new(model2)
        storage.save()

        # Clear the objects dictionary to simulate a new instance
        FileStorage._FileStorage__objects.clear()

        # Reload the models from the file
        storage.reload()

        # Check if the objects were reloaded correctly
        self.assertTrue("{}.{}".format(model1.__class__.__name__, model1.id) in storage.all())
        self.assertTrue("{}.{}".format(model2.__class__.__name__, model2.id) in storage.all())
        self.assertEqual(storage.all()["{}.{}".format(model1.__class__.__name__, model1.id)], model1.to_dict())
        self.assertEqual(storage.all()["{}.{}".format(model2.__class__.__name__, model2.id)], model2.to_dict())

    def test_save_empty(self):
        # Save an empty dictionary to the file
        storage = FileStorage()
        storage.save()

        # Check if the file was created and is empty
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            self.assertEqual(data, "{}")

if __name__ == "__main__":
    unittest.main()
