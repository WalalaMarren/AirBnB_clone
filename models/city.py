#!/usr/bin/python3
"""class City that inherits from BaseModel"""
from models.BaseModel import BaseModel


class City(BaseModel):
    '''sets the name and state_id attributes to empty strings'''
    name = ""
    state_id = ""

    """constructor method for the City class"""
    def __init__(self, state_id, name):
        self.name = name
        state_id = State.id
