#!/usr/bin/python3
"""class City that inherits from BaseModel"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    '''Defines a city with a name and id'''
    state_id = State.id
    name = ""
