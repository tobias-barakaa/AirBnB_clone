#!/usr/bin/python3
"""
console.py - Command Line Interpreter for the AirBnB Clone Project.

This module provides a command-line interface for interacting with the AirBnB Clone Project.
It allows users to manage and manipulate objects in the AirBnB clone storage system through a series of commands.

Usage:
    ./console.py

Commands:
    - quit: Exit the program.
    - EOF: Exit the program on End-of-File (Ctrl-D).
    - help: Get information about available commands.
    - create: Creates a new instance of a given class and saves it to the JSON file.
    - show: Prints the string representation of an instance based on the class name and id.
    - destroy: Deletes an instance based on the class name and id.
    - all: Prints the string representation of all instances or instances of a specific class.
    - update: Updates an instance based on the class name and id by adding or updating attributes.
"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Command Line Interpreter class.

    This class provides the implementation for the command-line interpreter.
    It extends the cmd.Cmd class from the cmd module, which provides the basic functionality for a command-line interface.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        quit - Command to exit the program.

        Usage:
            quit

        This command exits the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF - Command to exit the program on End-of-File (Ctrl-D).

        Usage:
            EOF

        This command exits the program when the End-of-File character (Ctrl-D) is encountered.
        """
        print()
        return True

    def emptyline(self):
        """
        emptyline - Command executed when an empty line + ENTER is encountered.

        This command does nothing when an empty line is entered.
        It prevents the last executed command from being repeated when no command is entered.
        """
        pass

    def do_create(self, arg):
        """
        create - Command to create a new instance of a class.

        Usage:
            create <class name>

        This command creates a new instance of the specified class,
        saves it to the JSON file, and prints its ID.
        If the class name is missing, it prints ** class name missing **.
        If the class doesn't exist, it prints ** class doesn't exist **.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        show - Command to print the string representation of an instance.

        Usage:
            show <class name> <id>

        This command prints the string representation of the instance
        specified by the class name and id.
        If the class name is missing, it prints ** class name missing **.
        If the class doesn't exist, it prints ** class doesn't exist **.
        If the id is missing, it prints ** instance id missing **.
        If the instance doesn't exist, it prints ** no instance found **.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        destroy - Command to delete an instance.

        Usage:
            destroy <class name> <id>

        This command deletes the instance specified by the class name and id
        from the JSON file.
        If the class name is missing, it prints ** class name missing **.
        If the class doesn't exist, it prints ** class doesn't exist **.
        If the id is missing, it prints ** instance id missing **.
        If the instance doesn't exist, it prints ** no instance found **.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        all - Command to print the string representation of all instances.

        Usage:
            all [<class name>]

        This command prints the string representation of all instances
        or instances of the specified class.
        If the class name doesn't exist, it prints ** class doesn't exist **.
        """
        if arg:
            class_name = arg
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            instances = [str(obj) for obj in storage.all().values() if type(obj).__name__ == class_name]
        else:
            instances = [str(obj) for obj in storage.all().values()]

        print(instances)

    def do_update(self, arg):
        """
        update - Command to update an instance.

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"

        This command updates an instance specified by the class name and id
        by adding or updating the specified attribute.
        The changes are saved to the JSON file.
        If the class name is missing, it prints ** class name missing **.
        If the class doesn't exist, it prints ** class doesn't exist **.
        If the id is missing, it prints ** instance id missing **.
        If the instance doesn't exist, it prints ** no instance found **.
        If the attribute name is missing, it prints ** attribute name missing **.
        If the value for the attribute name doesn't exist, it prints ** value missing **.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """
        default - Command executed when no matching command is found.

        This command is executed when no matching command is found.
        It checks if the line starts with a class name followed by a dot.
        If so, it splits the line into class name and arguments
        and checks if the class exists.
        If the class exists, it calls the corresponding method with the arguments.
        Otherwise, it prints ** class doesn't exist **.
        """
        class_name, dot, command = line.partition('.')
        if dot == '.':
            if class_name in storage.classes():
                self.onecmd("{} {}".format(command, class_name))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
