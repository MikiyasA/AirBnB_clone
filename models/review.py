#!/usr/bin/python3
"""
The class Review interit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ The class Review hold 'name' public attributes
    """
    place_id = ""
    user_id = ""
    text = ""
