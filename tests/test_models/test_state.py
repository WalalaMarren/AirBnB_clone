#!/usr/bin/python3
'''A test for state instances
This tests the functions and functionality of the   state module
'''
import uuid as u
import unittest
from models import storage
from models.state import State
from datetime import datetime as d


class TestBaseModel(unittest.TestCase):
    '''A test for the state module'''

    def setUp(self):
        '''Initialises two State intances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.state_1 = State()
        self.state_2 = State(**kwargs)

    def test_instance(self):
        '''Tests that a User instance was created'''
        self.assertIsInstance(self.state_1, State)
        self.assertIsInstance(self.state_2, State)

    def test_cls_attributes(self):
        '''Tests that the class attribute is correct'''
        self.State = State

        self.assertEqual(self.State.name, "")
