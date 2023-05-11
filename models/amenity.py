#!/usr/bin/python3
"""class state that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Defines the amenities in a room'''
    name = ""
