#!/usr/bin/python3
"unnnittest driven"

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.storage.new(self.base_model)

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'.format(self.base_model.id)], self.base_model)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(new_model.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'.format(new_model.id)], new_model)

    def test_save(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            self.assertIn('BaseModel.{}'.format(new_model.id), data)
            self.assertEqual(data['BaseModel.{}'.format(new_model.id)], new_model.to_dict())

    def test_reload(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(new_model.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'.format(new_model.id)], new_model)

    def test_reload_file_not_exists(self):
        self.assertFalse(os.path.exists(self.storage._FileStorage__file_path))
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'.format(self.base_model.id)], self.base_model)

    def test_save_multiple_objects(self):
        new_model1 = BaseModel()
        new_model2 = BaseModel()
        self.storage.new(new_model1)
        self.storage.new(new_model2)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            self.assertIn('BaseModel.{}'.format(new_model1.id), data)
            self.assertEqual(data['BaseModel.{}'.format(new_model1.id)], new_model1.to_dict())
            self.assertIn('BaseModel.{}'.format(new_model2.id), data)
            self.assertEqual(data['BaseModel.{}'.format(new_model2.id)], new_model2.to_dict())

    def test_reload_invalid_data(self):
        invalid_data = '{"invalid_key": "invalid_value"}'
        with open(self.storage._FileStorage__file_path, 'w') as file:
            file.write(invalid_data)
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)
        self.assertEqual(all_objects['BaseModel.{}'.format(self.base_model.id)], self.base_model)


if __name__ == '__main__':
    unittest.main()
