#!/usr/bin/python3
"""class City that inherits from BaseModel"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    '''sets the name and state_id attributes to empty strings'''

    state_id = State.id
    name = ""
