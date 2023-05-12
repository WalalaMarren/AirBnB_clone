'''A module that inherits from BaseModel to create an instance of a user.

Classes:
    User
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Defines the attributes of a user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
