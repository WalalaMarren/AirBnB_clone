#!/usr/bin/python3
'''A test for state instances
This tests the functions and functionality of the   Review module
'''
import uuid as u
import unittest
from models import storage
from models.review import Review
from datetime import datetime as d


class TestBaseModel(unittest.TestCase):
    '''A test for the review module'''

    def setUp(self):
        '''Initialises two Review intances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.review_1 = Review()
        self.review_2 = Review(**kwargs)

    def test_instance(self):
        '''Tests that a User instance was created'''
        self.assertIsInstance(self.review_1, Review)
        self.assertIsInstance(self.review_2, Review)

    def test_cls_attributes(self):
        '''Tests that the class attribute is correct'''
        self.Review = Review

        self.assertEqual(self.Review.place_id,  "")
        self.assertEqual(self.Review.user_id, "")
        self.assertEqual(self.Review.text, "")
