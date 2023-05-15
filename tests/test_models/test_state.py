#!/usr/bin/python3
'''A test for state instances
This tests the functions and functionality of the   module
'''
import uuid as u
import unittest
from models import storage
from models.state import State
from datetime import datetime as d


class TestBaseModel(unittest.TestCase):
    '''A test for the city module'''

    def setUp(self):
        '''Initialises City instances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.city_1 = State()
        self.city_2 = State(**kwargs)

    def test_instance(self):
        '''Tests that a User instance was created'''
        self.assertIsInstance(self.city_1, State)
        self.assertIsInstance(self.city_2, State)

    def test_save(self):
        '''Tests that updated_at is updated when the
        instance is saved'''
        c1_ut1 = self.city_1.updated_at

        c1_id = self.city_1.id
        c1_key = "State." + c1_id

        self.city_1.save()
        c1_ut2 = self.city_1.updated_at
        all_objs = storage.all()

        self.assertNotEqual(c1_ut1, c1_ut2)
        self.assertIn(c1_key, all_objs.keys())
