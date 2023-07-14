#!/usr/bin/python3
"""
This module devises a class named City that inherits from
BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the State class that inherits from
    BaseModel

    Attributes:
        state_id (str): empty string: it will be the State.id
        name (str): empty string
    """

    state_id = str()
    name = str()
