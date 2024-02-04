#!/usr/bin/python3
"""
Opens a command line interpreter and prompts user for a command
"""
import cmd


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


    if __name__ == '__main__':
        HBNBCommand().cmdloop()
