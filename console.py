#!/usr/bin/python3
"""
Opens a command line interpreter and prompts user for a command
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Start of the class HBNBCommand instance
    """
    prompt = "(hbnb) "

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
        boop

    def do_show(self, arg):
        """Prints an instance"""
        boop

    def do_destroy(self, arg):
        """Deletes an instance"""
        boop

    def do_all(self, arg):
         """Prints all instances"""
         boop

    def do_update(self, arg):
        """Updates an instance"""
        boop

if __name__ == '__main__':
    HBNBCommand().cmdloop()
