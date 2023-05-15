#!/usr/bin/python3
'''A test for FileStorage instances.
This tests the functions and functionality of the
file_storage module
'''
import json
import unittest
import uuid as u
from datetime import datetime as d
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''A test for the file storage'''

    def setUp(self):
        '''Initialises FileStorage instances'''

        self.model_1 = BaseModel()
        self.m1_name = "BaseModel"
        self.m1_id = self.model_1.id
        self.m1_key = self.m1_name + "." + self.m1_id

        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.objs = self.storage._FileStorage__objects

    def test_instance(self):
        '''Tests that BaseModel instance was created
        and added to file"storage's __object attribute'''
        self.assertIsInstance(self.storage, FileStorage)

    def test_attributes(self):
        '''Tests the attributes of instance is correct'''
        self.assertEqual(self.file_path, "file.json")
        self.assertIs(type(self.objs), dict)

    def test_all(self):
        '''Tests that this returns __objects'''
        all_objs = self.storage.all()

        self.assertEqual(all_objs, self.objs)

    def test_new(self):
        '''Tests that a nee obj is added to FileStorge __objects'''
        self.storage.new(self.model_1)
        saved_objs = self.storage.all()

        self.assertIn(self.m1_key, saved_objs.keys())

    def test_save(self):
        '''Tests that updated_at is updated when the
        instance is saved'''
        self.model_1.save()

        with open(self.file_path, "r") as file:
            json_objs = json.load(file)
        self.assertIn(self.m1_key, json_objs.keys())
