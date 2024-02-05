#!/usr/bin/python3
"""
Class Review that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Start of class Review instance
    """
    place_id = ""
    user_id = ""
    text = ""
