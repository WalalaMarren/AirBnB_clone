#!/usr/bin/python3
"""Class instance that inherits from the Cmd class"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple class to build an interpreter
       prompt: custom entry point to the interpreter
    """

    classes = ["BaseModel", "User", "Place", "State",
               "City", "Amenity", "Review"]
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

    def create_class(self, class_name):
        '''Function to call if class name is verified'''
        if (class_name == "BaseModel"):
            return (BaseModel())
        elif (class_name == "User"):
            return (User())
        # elif (class_name == "Place"):
        #     return (Place())
        # elif (class_name == "State"):
        #     return (State())
        # elif (class_name == "City"):
        #     return (City()):
        # elif (class_name == "Amenity"):
        #     return (Amenity())
        # elif (class_name == "Review"):
        #     return (Review())

    def do_create(self, line):
        '''Creates a new instance of a Class and stores it to a JSON file'''
        if (line == ""):
            print("** class name missing **")
        else:
            if (line not in self.classes):
                print("** class doesn't exist **")
            else:
                self.create_class(line)
                storage.save()

    def verify_args(self, arg_line):
        if (arg_line == ""):
            print("** class name missing **")
            return (0)
        args = arg_line.split()
        if (args[0] not in self.classes):
            print("** class doesn't exist **")
            return (0)
        if (len(args) != 2):
            print("** instance id missing **")
            return (0)
        return (1)

    def do_show(self, line):
        if self.verify_args(line):
            class_name, id = line.split()
            class_key = class_name + "." + id
            class_obj = storage.all()
            if (class_obj.get(class_key)):
                print(class_obj[class_key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
