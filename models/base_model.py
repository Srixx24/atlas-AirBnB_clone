#!/usr/bin/python3
"""
Class BaseModel that defines all common attributes/methods
"""
import uuid
from datetime import datetime
from file_storage import FileStorage


class BaseModel:
    """
    Defines all common funtionality for other classes
    """
    def __init__(self, *args, **kwargs):
        """Start of BaseModel instance"""
        #Str format for strptime
        strformat = "%Y-%m-%dT%H:%M:%S.%f"
        #check for kwargs
        if kwargs:
            #loop through kwargs
            for key in kwargs:
                #if created at or updated at
                if key == "created_at" or key == "updated_at":
                    #parse the argument to set a datetime object as attr
                    setattr(self, key, datetime.strptime(kwargs[key], strformat))
                #if argument is "__class__" ignore, as is not an actual attr
                elif key == "__class__":
                    #ignore setting the attr
                    pass
                #if key passes all prior checks
                else:
                    #set the attr
                    setattr(self, key, kwargs[key])
            # Saves new instance to storage
            storage.new(self)
        else:
            # Makes unique id for instance
            self.id = str(uuid.uuid4())
            # Sets created_at to current datetime
            self.created_at = datetime.now()
            # Sets updated_at to current datetime
            self.updated_at = datetime.now()
            # Saves new instance to storage
            storage.new(self)

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
        # Saves new instance to storage
        storage.save(self)

    def to_dict(self):
        """Returns a dictionary with all values of the instance"""
        # Creates a copy of dict
        dictionary = self.__dict__.copy()
        # Adding class name as a key
        dictionary["__class__"] = self.__class__.__name__
        # Converting to ISO format str
        dictionary["created_at"] = self.created_at.isoformat()
        # Converting to ISO format str
        dictionary["updated_at"] = self.updated_at.isoformat()
        # Returning dict
        return dictionary
