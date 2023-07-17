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

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when end-of-file character is encountered."""
        print()  # New line before exiting
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for the EOF command."""
        print("Exit the program when end-of-file character is encountered.")

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to the JSON file,
        and prints the id.
        Usage: create <class_name>
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
        """Prints the string representation of an instance based on the
        class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            instance = objects.get(key)
            if instance:
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file).
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            instance = objects.get(key)
            if instance:
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name.
        Usage: all [class_name]
        """
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(instance) for instance in objects.values()])
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            class_objects = [str(instance) for instance in objects.values()
                             if instance.__class__.__name__ == args[0]]
            print(class_objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating an attribute (save the change into the JSON file).
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        args = arg.split()
        objects = storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instance = objects.get(key)
            if instance:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name, attr_value = args[2], args[3]
                    if hasattr(instance, attr_name):
                        attr_value = type(getattr(instance, attr_name))(attr_value)
                        setattr(instance, attr_name, attr_value)
                        instance.save()
                    else:
                        print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def default(self, arg):
        """Default behavior when a command is not recognized."""
        cmd_list = arg.split(".")
        if len(cmd_list) == 2 and cmd_list[0] in storage.classes and cmd_list[1] == "all()":
            self.do_all(cmd_list[0])
        elif len(cmd_list) == 2 and cmd_list[0] in storage.classes and cmd_list[1] == "count()":
            objects = storage.all()
            class_objects = [instance for instance in objects.values()
                             if instance.__class__.__name__ == cmd_list[0]]
            print(len(class_objects))
        else:
            cmd.Cmd.default(self, arg)

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
