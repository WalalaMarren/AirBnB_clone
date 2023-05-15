#!/usr/bin/python3
'''A test for the base model.
This tests the functions and functionality of the
base module
'''
import unittest
import uuid as u
from datetime import datetime as d
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''A test for the base model'''

    def setUp(self):
        '''Initialises BaseModel instances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.model_1 = BaseModel()
        self.model_2 = BaseModel(**kwargs)

    def test_instance(self):
        '''Tests that BaseModel instance was created'''
        self.assertIsInstance(self.model_1, BaseModel)
        self.assertIsInstance(self.model_2, BaseModel)

    def test_attributes(self):
        '''Tests the attributes of instance is correct'''
        self.model_1.name = "First Model"
        self.model_1.number = 89

        self.assertEqual(self.model_1.name, "First Model")
        self.assertEqual(self.model_1.number, 89)

        self.assertEqual(self.model_2.id, self.inst_id)
        self.assertEqual(self.model_2.created_at, self.t1)
        self.assertEqual(self.model_2.updated_at, self.t2)

    def test_save(self):
        m1_ut1 = self.model_1.updated_at
        self.model_1.save()
        m1_ut2 = self.model_1.updated_at
        self.model_2.save()
        m2_ut2 = self.model_2.updated_at
        self.assertNotEqual(m1_ut1, m1_ut2)
        self.assertNotEqual(self.t2, m2_ut2)

    def test_to_dict(self):
        m1_json = self.model_1.to_dict()
        m2_json = self.model_2.to_dict()

        self.assertIn("__class__", m1_json.keys())
        self.assertIn("__class__", m2_json.keys())
        self.assertIs(type(m1_json["created_at"]), str)
        self.assertIs(type(m1_json["updated_at"]), str)
        self.assertIs(type(m2_json["created_at"]), str)
        self.assertIs(type(m2_json["updated_at"]), str)
