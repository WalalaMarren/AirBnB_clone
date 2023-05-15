#!/usr/bin/python3
'''A module that inherits from BaseModel to create an instance of a user.

Classes:
    User
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Defines the attributes of a user'''

    def __init__(self, *args, **kwargs):
        '''Intialises a user's details like the name, password and email'''
        super().__init__(self, *args, **kwargs)
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""
