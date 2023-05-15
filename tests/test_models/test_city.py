#!/usr/bin/python3
'''A test for state instances
This tests the functions and functionality of the   state module
'''
import uuid as u
import unittest
from models import storage
from models.city import City
from datetime import datetime as d


class TestBaseModel(unittest.TestCase):
    '''A test for the city module'''

    def setUp(self):
        '''Initialises two State intances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.city_1 = City()
        self.city_2 = City(**kwargs)

    def test_instance(self):
        '''Tests that a User instance was created'''
        self.assertIsInstance(self.city_1, City)
        self.assertIsInstance(self.city_2, City)

    def test_cls_attributes(self):
        '''Tests that the class attribute is correct'''
        self.City = City

        self.assertEqual(self.City.state_id, "")
        self.assertEqual(self.City.name, "")
