#!/usr/bin/python3
"unnnittest driven"

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    # ... Same setup and teardown methods ...

    # ... Existing tests ...

    def test_save_and_reload_update_existing(self):
        # Create a BaseModel instance
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 123

        # Save the model to the file
        storage = FileStorage()
        storage.new(model)
        storage.save()

        # Modify the model attributes
        model.name = "Updated Model"
        model.my_number = 789

        # Save the updated model to the file
        storage.save()

        # Clear the objects dictionary to simulate a new instance
        FileStorage._FileStorage__objects.clear()

        # Reload the model from the file
        storage.reload()

        # Check if the updated model was reloaded correctly
        self.assertTrue("{}.{}".format(model.__class__.__name__, model.id) in storage.all())
        self.assertEqual(storage.all()["{}.{}".format(model.__class__.__name__, model.id)], model.to_dict())

    def test_save_and_reload_delete_object(self):
        # Create a few BaseModel instances
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        # Save the models to the file
        storage = FileStorage()
        storage.new(model1)
        storage.new(model2)
        storage.new(model3)
        storage.save()

        # Delete one of the models
        storage.delete(model2)

        # Save the changes to the file
        storage.save()

        # Clear the objects dictionary to simulate a new instance
        FileStorage._FileStorage__objects.clear()

        # Reload the models from the file
        storage.reload()

        # Check if the deleted model is not reloaded
        self.assertTrue("{}.{}".format(model1.__class__.__name__, model1.id) in storage.all())
        self.assertFalse("{}.{}".format(model2.__class__.__name__, model2.id) in storage.all())
        self.assertTrue("{}.{}".format(model3.__class__.__name__, model3.id) in storage.all())

    def test_save_and_reload_no_file(self):
        # Create a BaseModel instance
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 123

        # Save the model to the file
        storage = FileStorage()
        storage.new(model)
        storage.save()

        # Remove the file
        os.remove(storage._FileStorage__file_path)

        # Clear the objects dictionary to simulate a new instance
        FileStorage._FileStorage__objects.clear()

        # Reload the models from the file (file doesn't exist)
        storage.reload()

        # Check if the object is still in memory, no exception raised
        self.assertTrue("{}.{}".format(model.__class__.__name__, model.id) in storage.all())
        self.assertEqual(storage.all()["{}.{}".format(model.__class__.__name__, model.id)], model.to_dict())

if __name__ == "__main__":
    unittest.main()
