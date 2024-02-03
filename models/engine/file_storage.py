#!/bin/usr/python3

"""
The engine that runs file storage, 
with various methods for JSON serialization
"""

class FileStorage:

    #Set filepath to file.json for data storage
    __file_path: 'file.json'
    #Empty dictionary to hold object IDs and objects
    #formatted as such: <classname>.<IDnumber>
    __objects: {}

    #returns a dictionary of objects
    def all(self):
        return(self.__objects)

    #saves new object into the dictionary
    #key - [<classname>.id#]
    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        

    def reload(self):
