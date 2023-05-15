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
        inst_id = str(u.uuid4())
        t1 = d.now()
        t2 = d.now()
        kwargs = {"id": inst_id,
                "created_at": t1,
                "updated_at": t2}
        self.model_1 = BaseModel()
        self.model_2 = BaseModel(**kwargs)

    def test_model(self):
        '''Tests that BaseModel instance was created'''
        self.assertIsInstance(self.model_1, BaseModel)
        self.assertIsInstance(self.model_2, BaseModel)

        # def test_save(self):
        # self.model_1.name = "First Model"
        # self.model_1.number = "89"
        #  [BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
        
