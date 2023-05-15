#!/usr/bin/python3
'''A test for amenity instances
This tests the functions and functionality of the   amenity module
'''
import uuid as u
import unittest
from models import storage
from models.amenity import Amenity
from datetime import datetime as d


class TestBaseModel(unittest.TestCase):
    '''A test for the amenity module'''

    def setUp(self):
        '''Initialises two Amenity intances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.amenity_1 = Amenity()
        self.amenity_2 = Amenity(**kwargs)

    def test_instance(self):
        '''Tests that a Amenity instance was created'''
        self.assertIsInstance(self.amenity_1, Amenity)
        self.assertIsInstance(self.amenity_2, Amenity)

    def test_cls_attributes(self):
        '''Tests that the class attribute is correct'''
        self.Amenity = Amenity

        self.assertEqual(self.Amenity.name, "")
