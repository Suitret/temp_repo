#!/usr/bin/python3
"""
This module devises a class named Review that inherits from
BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the State class that inherits from
    Review

    Attributes:
        place_id (str): it will be the Place.id
        user_id (str): it will be the User.id
        text (str): empty string
    """

    place_id = str()
    user_id = str()
    text = str()
