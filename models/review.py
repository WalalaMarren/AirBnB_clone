#!/usr/bin/python3
"""class Review that inherits from BaseModel"""
from models.BaseModel import BaseModel


class Review(BaseModel):
    '''sets the attributes to empty strings'''
    place_id = ""
    user_id = ""
    text = ""

    """constructor method for the Amenity class"""
    def __init__(self, place_id, user_id, text):
        self.place_id = Place_id
        self.user_id = User_id
        self.text = text
