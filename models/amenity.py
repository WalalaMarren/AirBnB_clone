#!/usr/bin/python3
"""class state that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''sets the name attribute to an empty string'''

    name = ""
