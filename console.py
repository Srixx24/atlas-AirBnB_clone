#!/usr/bin/python3
"""
Opens a command line interpreter and prompts user for a command
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Start of the class HBNBCommand instance
    """
    # Prompt line
    prompt = "(hbnb) "

    # Global class dict variable, looking ahead we'll need a few
    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
    }

    def do_quit(self, arg):
        """Exit program"""
        return True

    def do_EOF(self, arg):
        """Exit program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        # Split the input arguments into tokens
        toks = arg.split()
        # If none present return error
        if not toks:
            print("** class name missing **")
            return
        
        # Extract the class name from the tokens
        class_name = toks[0]
        # If name isn't in dict return error
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return

        # Create an instance of the desired class
        instance = self.class_dict[class_name]()
        # Save the instance
        instance.save()
        # Print id of new instance
        print(instance.id)

    def do_show(self, arg):
        """Prints an instance"""
        # Split the argument into tokens
        toks = arg.split()

        # If name isn't in dict return error
        if not toks:
            print("** class name missing **")
            return
        # If not enough tokens return error
        if len(toks) < 2:
            print("** instance id missing **")
            return

        # Extract name
        class_name = toks[0]

        # If name is not in dict return error
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return

        # Extract id from tokens
        obj_id = toks[1]
        # Get all obj from storage
        obj = storage.all()

        # Create the key
        key = class_name + "." + obj_id

        # If key exists print obj str and save
        if key in obj:
            print(obj[key])
            storage.save()
        else:
            # Return error otherwise
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        # Split the argument into tokens
        toks = arg.split()

        # If no tokens are present return error
        if len(toks) < 1:
            print("** class name missing **")
            return
        # Extract the class name from the tokens
        class_name = toks[0]
        # If name is not in dict return error
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        #If the object ID is missing return error
        if len(toks) < 2:
            print("** instance id missing **")
            return

        # Extract id from tokens
        obj_id = toks[1]
        # Get all obj from storage
        obj = storage.all()

        # Id for an obj in dict
        key = "{}.{}".format(class_name, obj_id)

        # If id exists in storage delete and update storage
        if key in obj:
            del obj[key]
            storage.save()
        else:
            # Return error otherwise
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances"""
        # Get all obj from storage
        obj = storage.all()

        # Prints all instances
        if len(arg) == 0:
            for obj_id in obj.keys():
                print("{}".format(obj[obj_id]))
        else:
            # Split the argument into tokens
            toks = arg.split()
            if len(toks) > 0:
                # Extract name from toks 
                class_name = toks[0]
                # Prints the instance for the class
                if class_name in self.class_dict:
                    for obj_id in obj.keys():
                        if obj[obj_id].__class__.__name__ == class_name:
                            print("{}".format(obj[obj_id]))
                else:
                    # Return error if name isn't in dictionary
                    print("** class doesn't exist **")
                    return

    def do_update(self, arg):
        """Updates an instance"""
        # Retrieve all instances from the storage
        obj = storage.all()
        # Split the argument into tokens
        toks = arg.split()

        if len(toks) >= 4:
            # Extracts class name
            class_name = toks[0]
            # Extracts id
            obj_id = toks[1]
            # Extracts attribute name
            attributes = toks[2]
            # Extracts attribute value
            value = toks[3]

            if class_name in self.class_dict:
                if obj_id in obj:
                    # Check if the attribute isn't restricted
                    if attribute not in ['id', 'created_at', 'updated_at']:
                        if hasattr(obj[obj_id], attribute):
                            attribute_type = type(getattr(obj[obj_id], attribute))
                            try:
                                # Try to cast value to attribute type
                                casted_value = attribute_type(value)
                                # Update attributes
                                setattr(obj[obj_id], attribute, casted_value)
                                # Save changes
                                obj[obj_id].save()
                            except ValueError:
                                # Value can't be casted
                                print("** invalid value **")
                        else:
                            # Attribute name doesn't exist
                            print("** attribute name missing **")
                    else:
                        # Restricted and can not update
                        print("** attribute cannot be updated **")
                else:
                    # Object id does't exist
                    print("** no instance found **")
            else:
                # Class doesn't exist
                print("** class doesn't exist **")
        
        elif len(toks) == 3:
            # Value is missing
            print("** value missing **")
        elif len(toks) == 2:
            # Attribute name is missing
            print("** attribute name missing **")
        elif len(toks) == 1:
            # Object id is missing
            print("** instance id missing **")
        else:
            # Class name is missing
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
