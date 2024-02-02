#!/usr/bin/python3
"""
Class BaseModel that defines all common attributes/methods
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common funtionality for other classes
    """
    def __init__(self):
        """Start of BaseModel instance"""
        # Makes unique id for instance
        self.id = str(uuid.uuid4())
        # Sets created_at to current datetime
        self.created_at = datetime.now()
        # Sets updated_at to current datetime
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints the string representation of attributes"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
            )
        # Returns a str with class name, id, and attribute dict
        # in required format

    def save(self):
        """Updates the current datetime"""
        # Updates with current datetime
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all values of the instance"""
        # Creates a copy of dict
        dictionary = self.__dict__.copy()
        # Adding class name as a key
        dictionary["__class__"] = self.__class__.__name__
        # Converting to ISO format str
        dictionary["created_at"] = self.created_at.isoformat()
        # Converting to ISO format str
        dictionary["update_at"] = self.updated_at.isoformat()
        # Returning dict
        return dictionary
