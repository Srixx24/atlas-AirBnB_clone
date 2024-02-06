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
    first_name = ""
    last_name = ""

    def __init__(sellf, *args, **kwargs):
        super().__init__(*args, **kwargs)
