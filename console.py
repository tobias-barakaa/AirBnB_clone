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
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("EOF command to exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                # Create an instance of the provided class name
                # Save it to the JSON file
                # Print the instance id
                # Example: $ create BaseModel
                # Output: 49faff9a-6318-451f-87b6-910505c55907
                # Implement your logic here
                pass
            except Exception as e:
                print("** {}".format(str(e)))

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                try:
                    # Print the string representation of the instance
                    # based on the class name and id
                    # Example: $ show BaseModel 1234-1234-1234
                    # Output: [BaseModel] (1234-1234-1234) {'id': '1234-1234-1234'}
                    # Implement your logic here
                    pass
                except Exception as e:
                    print("** {}".format(str(e)))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                try:
                    # Delete the instance based on the class name and id
                    # Save the change to the JSON file
                    # Example: $ destroy BaseModel 1234-1234-1234
                    # Output: None
                    # Implement your logic here
                    pass
                except Exception as e:
                    print("** {}".format(str(e)))

    def do_all(self, arg):
        """Prints all instances or instances of a specific class"""
        if len(arg) == 0:
            try:
                # Print the string representation of all instances
                # Example: $ all
                # Output: ["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234'}"]
                # Implement your logic here
                pass
            except Exception as e:
                print("** {}".format(str(e)))
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                try:
                    # Print the string representation of instances of the specified class
                    # Example: $ all BaseModel
                    # Output: ["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234'}"]
                    # Implement your logic here
                    pass
                except Exception as e:
                    print("** {}".format(str(e)))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                try:
                    # Update the instance based on the class name, id, attribute name, and value
                    # Save the change to the JSON file
                    # Example: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
                    # Output: None
                    # Implement your logic here
                    pass
                except Exception as e:
                    print("** {}".format(str(e)))

    def do_help(self, arg):
        """Help command to display available commands"""
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
