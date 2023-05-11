#!/usr/bin/python3
"""class Place that inherits from BaseModel"""
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    '''Defines the properties and  attributes of a room'''
    city_id = City.id
    user_id = User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
