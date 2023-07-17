#!/usr/bin/python3
"""Command interpreter for the AirBnB project."""
import cmd
import json
import models
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel
        # Add other classes here if needed
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_EOF(self, arg):
        """Exit the console with Ctrl+D (EOF)."""
        print()  # Print a newline before exiting
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for the EOF (Ctrl+D) command."""
        print("Exit the console with Ctrl+D (EOF)")

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.__classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representation of all instances."""
        args = arg.split()
        objs = []
        if not arg:
            for obj in models.storage.all().values():
                objs.append(str(obj))
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key, obj in models.storage.all().items():
                if key.split(".")[0] == args[0]:
                    objs.append(str(obj))
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = models.storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(obj, attr_name):
                    attr_value = cast_attribute(attr_value)
                    setattr(obj, attr_name, attr_value)
                    obj.save()
                else:
                    print("** attribute doesn't exist **")

def cast_attribute(value):
    """Cast the attribute value to its original type."""
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]

    try:
        return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        pass

    return value

if __name__ == '__main__':
    HBNBCommand().cmdloop()
