#!/usr/bin/python3
"""
This module devises a class named Place that inherits from
BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the Place class that inherits from
    BaseModel

    Attributes:
        city_id (str) : it will be the City.id
        user_id (str): it will be the User.id
        name (str): empty string
        description (string): empty string
        number_rooms (int): default value 0
        number_bathrooms (int): default value 0
        max_guest (int): default value 0
        price_by_night (int): default value 0
        latitude: (float) - default value 0.0
        longitude: (float) - default value 0.0
        amenity_ids: list of string - empty list: it will be
        the list of Amenity.id later

    """

    city_id = str()
    user_id = str()
    name = str()
    description = str()
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = list()
