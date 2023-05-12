#!/usr/bin/python3
"""class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    '''Handles reviews of houses from users'''
    place_id = ""
    user_id = ""
    text = ""
