#!/usr/bin/python3
"""
User class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ The class User holds public attributes of email,
    password, first_name & last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
