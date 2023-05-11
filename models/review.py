#!/usr/bin/python3
"""class Review that inherits from BaseModel"""
from models.BaseModel import BaseModel


class Review(BaseModel):
    '''sets the attributes to empty strings'''

    place_id = ""
    user_id = ""
    text = ""
