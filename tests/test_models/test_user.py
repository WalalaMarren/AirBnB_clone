#!/usr/bin/python3
'''A test for user instances.
This tests the functions and functionality of the user module
'''
import uuid as u
import unittest
from models import storage
from models.user import User
from datetime import datetime as d


class TestBaseModel(unittest.TestCase):
    '''A test for the user module'''

    def setUp(self):
        '''Initialises BaseModel instances'''
        self.inst_id = str(u.uuid4())
        self.t1 = d.now()
        self.t2 = d.now()
        kwargs = {"id": self.inst_id,
                  "created_at": self.t1,
                  "updated_at": self.t2}
        self.user_1 = User()
        self.user_2 = User(**kwargs)

    def test_instance(self):
        '''Tests that a User instance was created'''
        self.assertIsInstance(self.user_1, User)
        self.assertIsInstance(self.user_2, User)

    def test_attributes(self):
        '''Tests the attributes of instance is correct'''
        self.user_1.first_name = "Betty"
        self.user_1.last_name = "Bar"
        self.user_1.email = "airbnb@mail.com"
        self.user_1.password = "root"
        u1_dict = self.user_1.__dict__

        self.assertIn("Betty", u1_dict.values())
        self.assertIn("Bar", u1_dict.values())
        self.assertIn("airbnb@mail.com", u1_dict.values())
        self.assertIn("root", u1_dict.values())

        self.assertEqual(self.user_2.id, self.inst_id)
        self.assertEqual(self.user_2.created_at, self.t1)
        self.assertEqual(self.user_2.updated_at, self.t2)

    def test_password(self):
        self.User.password = "root"
        self.assertEqual(self.User.password, "root")

    def test_save(self):
        '''Tests that updated_at is updated when the
        instance is saved'''
        u1_ut1 = self.user_1.updated_at

        u1_id = self.user_1.id
        u1_key = "User." + u1_id

        self.user_1.save()
        u1_ut2 = self.user_1.updated_at
        all_objs = storage.all()

        self.assertNotEqual(u1_ut1, u1_ut2)
        self.assertIn(u1_key, all_objs.keys())

    def test_to_dict(self):
        '''Tests that the to_dict() method of the instance.
        It confirms the the to_dict() method returns a
        dictionary with a __class__ attribute, and
        the datetime attributes converted to string format'''
        u1_json = self.user_1.to_dict()
        u2_json = self.user_2.to_dict()

        self.assertIn("__class__", u1_json.keys())
        self.assertIn("__class__", u2_json.keys())
        self.assertIs(type(u1_json["created_at"]), str)
        self.assertIs(type(u1_json["updated_at"]), str)
        self.assertIs(type(u2_json["created_at"]), str)
        self.assertIs(type(u2_json["updated_at"]), str)
