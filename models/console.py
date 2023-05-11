#!/usr/bin/python3
"""Class instance that inherits from the Cmd class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple class to build an interpreter
       prompt: custom entry point to the interpreter
    """

    prompt = '(hbnb) '
    def do_EOF(self, arg):
        """Command to handle the EOF"""
        return True
    
    def do_quit(self, arg):
        """Command to exit the program"""
        return True

    def emptyline(self):
        """Command to not execute any empty line entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
