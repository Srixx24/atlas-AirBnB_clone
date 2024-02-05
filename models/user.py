#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Start of class User instance
    """
    email = ""
    password = ""
    fird_name = ""
    last_name = ""
