#!/usr/bin/python3
'''A test for base model instances.
This tests the functions and functionality of the
base module
'''
import unittest
import uuid as u
from models import storage
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
        '''Tests that BaseModel instance was created
        and added to file"storage's __object attribute'''
        self.assertIsInstance(self.model_1, BaseModel)
        self.assertIsInstance(self.model_2, BaseModel)
        saved_objs = storage.all()

        name = "BaseModel"
        m1_key = name + "." + self.model_1.id
        m2_key = name + "." + self.inst_id

        self.assertIn(m1_key, saved_objs.keys())
        self.assertNotIn(m2_key, saved_objs.keys())

    def test_str(self):
        '''Confirms the string representation of the instance'''
        name = self.model_1.__class__.__name__
        m1_id = self.model_1.id
        m1_dict = self.model_1.__dict__

        inst_str = "[{}] ({}) {}".format(name, m1_id, m1_dict)
        self.assertEqual(inst_str, str(self.model_1))

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
        '''Tests that updated_at is updated when the
        instance is saved'''
        m1_ut1 = self.model_1.updated_at
        self.model_1.save()
        m1_ut2 = self.model_1.updated_at

        self.model_2.save()
        m2_ut2 = self.model_2.updated_at

        self.assertNotEqual(m1_ut1, m1_ut2)
        self.assertNotEqual(self.t2, m2_ut2)

        saved_objs = storage.all()
        name = "BaseModel"
        m1_key = name + "." + self.model_1.id
        m2_key = name + "." + self.inst_id

        self.assertIn(m1_key, saved_objs.keys())
        self.assertNotIn(m2_key, saved_objs.keys())

    def test_to_dict(self):
        '''Tests that the to_dict() method of the instance.
        It confirms the the to_dict() method returns a
        dictionary with a __class__ attribute, and
        the datetime attributes converted to string format'''
        m1_json = self.model_1.to_dict()
        m2_json = self.model_2.to_dict()

        self.assertIn("__class__", m1_json.keys())
        self.assertIn("__class__", m2_json.keys())
        self.assertIs(type(m1_json["created_at"]), str)
        self.assertIs(type(m1_json["updated_at"]), str)
        self.assertIs(type(m2_json["created_at"]), str)
        self.assertIs(type(m2_json["updated_at"]), str)
