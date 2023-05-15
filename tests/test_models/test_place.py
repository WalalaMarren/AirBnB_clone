#!/usr/bin/python3
'''A test for state instances
This tests the functions and functionality of the   place module
'''
import uuid as u
import unittest
from models import storage
from models.place import Place
from datetime import datetime as d


class TestBaseModel(unittest.TestCase):
    '''A test for the place module'''

    def setUp(self):
        '''Initialises two Place intances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.place_1 = Place()
        self.place_2 = Place(**kwargs)

    def test_instance(self):
        '''Tests that two Place instances were created'''
        self.assertIsInstance(self.place_1, Place)
        self.assertIsInstance(self.place_2, Place)

    def test_cls_attributes(self):
        '''Tests that the class attribute is correct'''
        self.Place = Place

        self.assertEqual(self.Place.city_id, "")
        self.assertEqual(self.Place.user_id, "")
        self.assertEqual(self.Place.name, "")
        self.assertEqual(self.Place.description, "")
        self.assertEqual(self.Place.number_rooms, 0)
        self.assertEqual(self.Place.number_bathrooms, 0)
        self.assertEqual(self.Place.max_guest, 0)
        self.assertEqual(self.Place.price_by_night, 0)
        self.assertEqual(self.Place.latitude, 0.0)
        self.assertEqual(self.Place.longitude, 0)
        self.assertEqual(self.Place.amenity_ids, [])
