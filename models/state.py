#!/usr/bin/python3
"""
This module devises a class named State that inherits from
BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the State class that inherits from
    BaseModel

    Attributes:
        name (str): empty string
    """

    name = str()
