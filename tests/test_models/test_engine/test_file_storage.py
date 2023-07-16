#!/usr/bin/python3
"unnnittest driven"

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    # ... Same setup and teardown methods ...

    def test_save_and_reload_multiple_classes(self):
        # Create instances of different classes
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        # Save the models to the file
        storage = FileStorage()
        storage.new(model1)
        storage.new(model2)
        storage.new(model3)
        storage.save()

        # Clear the objects dictionary to simulate a new instance
        FileStorage._FileStorage__objects.clear()

        # Reload the models from the file
        storage.reload()

        # Check if the objects were reloaded correctly
        self.assertTrue("{}.{}".format(model1.__class__.__name__, model1.id) in storage.all())
        self.assertTrue("{}.{}".format(model2.__class__.__name__, model2.id) in storage.all())
        self.assertTrue("{}.{}".format(model3.__class__.__name__, model3.id) in storage.all())

    def test_save_and_reload_subclasses(self):
        # Create a subclass of BaseModel
        class SubModel(BaseModel):
            def __init__(self):
                super().__init__()

        sub_model = SubModel()
        sub_model.name = "Sub Model"
        sub_model.my_number = 999

        # Save the subclass model to the file
        storage = FileStorage()
        storage.new(sub_model)
        storage.save()

        # Clear the objects dictionary to simulate a new instance
        FileStorage._FileStorage__objects.clear()

        # Reload the models from the file
        storage.reload()

        # Check if the subclass model was reloaded correctly
        self.assertTrue("{}.{}".format(sub_model.__class__.__name__, sub_model.id) in storage.all())
        self.assertEqual(storage.all()["{}.{}".format(sub_model.__class__.__name__, sub_model.id)], sub_model.to_dict())

if __name__ == "__main__":
    unittest.main()
