#!/usr/bin/python3
"""
Command interpreter module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all or all <class name>
        """
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg in storage.classes:
            print([str(obj) for obj in objects.values() if type(obj).__name__ == arg])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3].strip("\"'"))
                storage.all()[key].save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        End-of-file (EOF) to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line should not execute anything
        """
        pass

    def help_quit(self):
        """
        Help message for quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help message for EOF command
        """
        print("End-of-file (EOF) to exit the program")

    def help_create(self):
        """
        Help message for create command
        """
        print("Create a new instance of BaseModel, saves it (to the JSON file) and prints the id.")
        print("Usage: create <class name>")

    def help_show(self):
        """
        Help message for show command
        """
        print("Prints the string representation of an instance based on the class name and id.")
        print("Usage: show <class name> <id>")

    def help_destroy(self):
        """
        Help message for destroy command
        """
        print("Deletes an instance based on the class name and id (save the change into the JSON file).")
        print("Usage: destroy <class name> <id>")

    def help_all(self):
        """
        Help message for all command
        """
        print("Prints all string representation of all instances based or not on the class name.")
        print("Usage: all or all <class name>")

    def help_update(self):
        """
        Help message for update command
        """
        print("Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).")
        print("Usage: update <class name> <id> <attribute name> \"<attribute value>\"")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
