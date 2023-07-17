#!/usr/bin/python3
"""
Console for the AirBnB clone project.
"""
import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is reached"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        # Implementation for create command

    def do_show(self, arg):
        """Print the string representation of an instance"""
        # Implementation for show command

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        # Implementation for destroy command

    def do_all(self, arg):
        """Prints all string representation of instances"""
        # Implementation for all command

    def do_update(self, arg):
        """Updates an instance based on the class name, id, and attribute"""
        # Implementation for update command

if __name__ == '__main__':
    HBNBCommand().cmdloop()
