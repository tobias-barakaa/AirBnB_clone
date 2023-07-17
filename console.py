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
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
