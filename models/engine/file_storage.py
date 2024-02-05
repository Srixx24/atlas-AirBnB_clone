#!/bin/usr/python3

"""
The engine that runs file storage, 
with various methods for JSON serialization
"""
import json
import os


class FileStorage:
    """
    Start of FileStorage instance 
    """
    # Set filepath to file.json for data storage
    __file_path = 'file.json'
    # Empty dictionary to hold object IDs and objects
    # formatted as such: <classname>.<IDnumber>
    __objects = {}

    # Returns a dictionary of objects
    def all(self):
        """Returns dict objects"""
        return self.__objects

    # Saves new object into the dictionary
    # Key - [<classname>.id#]
    def new(self, obj):
        """Add new obj to dict"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Saves to existing instances"""
        with open(self.__class__.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))
            # # Serialize objects 
            # objects = {key: val.to_dict() for
            #         key, val in self.__objects.items()}
            # # Write serialized obj to file
            # json.dump(objects, file)
        

    def reload(self):
        """Load intance from save"""
        # Check if the JSON file exists
        #   note for future ace: try isfile
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                if os.path.getsize(FileStorage.__file_path) > 0:
                    file_content = file.read()
                    self.__objects = json.loads(file_content)
        else:
            pass



        #     try:
        #         # Open the JSON file
        #         with open(FileStorage.__file_path, mode='r') as jFile:
        #             # Loads the data
        #             obj = json.load(jFile)
        #             # Iterate over the data
        #             for key in obj.keys():
        #                 # Extract class name
        #                 class_name = obj[key]["__class__"]
        #                 # Dynamically import
        #                     # module = __import__('models.' + class_name, fromlist=[class_name])
        #                 # Gets attributes
        #                 obj_class = getattr(module, class_name)
        #                 # Create a new instance of the class
        #                 new_obj = obj_class(**value)
        #                 # Store the new instance in dict
        #                 FileStorage.__objects[key] = new_obj
        #     except FileNotFoundError:return
        #         # Do nothing if file not found
        #         pass
