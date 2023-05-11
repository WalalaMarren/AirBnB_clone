#!/usr/bin/python3
"""class City that inherits from BaseModel"""
from models.BaseModel import BaseModel


class City(BaseModel):
    '''sets the name and state_id attributes to empty strings'''
    
    name = ""
    state_id = ""
