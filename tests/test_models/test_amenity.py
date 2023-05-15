#!/usr/bin/python3
'''A test for city instances
This tests the functions and functionality of the user module
'''
import uuid as u
import unittest
from models import storage
from models.amenity import Amenity
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
        self.city_1 = Amenity()
        self.city_2 = Amenity(**kwargs)

    def test_instance(self):
        '''Tests that a User instance was created'''
        self.assertIsInstance(self.city_1, Amenity)
        self.assertIsInstance(self.city_2, Amenity)

    def test_save(self):
        '''Tests that updated_at is updated when the
        instance is saved'''
        c1_ut1 = self.city_1.updated_at

        c1_id = self.city_1.id
        c1_key = "Amenity." + c1_id

        self.city_1.save()
        c1_ut2 = self.city_1.updated_at
        all_objs = storage.all()

        self.assertNotEqual(c1_ut1, c1_ut2)
        self.assertIn(c1_key, all_objs.keys())
