#!/usr/bin/python3
"""
The class City inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ The class City holds public attibutes state_id & name
    """
    state_id = ""
    name = ""
