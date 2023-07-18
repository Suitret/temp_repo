#!/usr/bin/python3
"""
This modules devises a class named User
"""
import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class

    Attributes:
        email(string) - empty string
        password(string) - empty string
        first_name(string) - empty string
        last_name (string) - empty string

    """

    email = str()
    password = str()
    first_name = str()
    last_name = str()

    def __init__(self, *args, **kwargs):
        """User's class constructor

        Args:
            None

        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        pass
