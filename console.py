import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        """Help for EOF command"""
        print("Quit the command interpreter.")
        
    # Additional help functions for other commands can be added here
        
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
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
        """Prints the string representation instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()

        if args and args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        else:
            print([str(obj) for obj in all_objs.values()
                   if args[0] in str(obj)])

    def do_update(self, arg):
        """Updates an instance based on the class name"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = all_objs[key]
        setattr(instance, args[2], args[3].strip("\"'"))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
