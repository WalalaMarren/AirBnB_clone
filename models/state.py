#!/usr/bin/python3
from models.BaseModel import BaseModel
"""class state that inherits from BaseModel"""


class State(BaseModel):
    #sets the name attribute to an empty string
    name = ""

    """constructor method for the State class"""
    def __init__(self, name):
        self.name = name
