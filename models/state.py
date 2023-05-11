#!/usr/bin/python3
"""class state that inherits from BaseModel"""
from models.BaseModel import BaseModel


class State(BaseModel):
    #sets the name attribute to an empty string
    name = ""

    """constructor method for the State class"""
    def __init__(self, name):
        self.name = name
