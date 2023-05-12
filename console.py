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
        '''
        Function to call if a class name is verified.
        Creates an instance of the class and returns
        class instance
        '''
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
        '''
        Verifies the argument passed is a valid class, calls
        a function to create an instance of the class and stores
        the instance created to a JSON file
        '''
        if (line == ""):
            print("** class name missing **")
        else:
            class_name = line
            if (class_name not in self.classes):
                print("** class doesn't exist **")
            else:
                class_instance = self.create_class(class_name)
                print(class_instance.id)
                storage.save()

    def verify_args(self, arg_line):
        '''Verifies the number and validity of arguments passed'''
        if (arg_line == ""):
            print("** class name missing **")
            return (0)
        args = arg_line.split()
        class_name = args[0]
        if (class_name not in self.classes):
            print("** class doesn't exist **")
            return (0)
        if (len(args) < 2):
            print("** instance id missing **")
            return (0)
        return (1)

    def verify_key(self, line):
        '''Verifies that an instance with the class name and id exists'''
        if self.verify_args(line):
            class_name, class_id = line.split()
            inst_key = class_name + "." + class_id
            inst_dict = storage.all()
            if (inst_dict.get(inst_key) is None):
                print("** no instance found **")
                return (None)
            return (inst_key, inst_dict)
        return (0)

    def do_show(self, line):
        '''
        Prints the string representation of an
        instance based on the class name and id
        '''
        inst_dict_key = self.verify_key(line)
        if (inst_dict_key):
            inst_key, inst_dict = inst_dict_key
            inst = inst_dict[inst_key]
            print(inst)

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        inst_dict_key = self.verify_key(line)
        if (inst_dict_key):
            inst_key, inst_dict = inst_dict_key
            inst_dict.pop(inst_key)
            storage.save()

    def do_all(self, line):
        '''
        Prints the string representation of all instances of a
        class specified by the class name and id
        '''
        inst_dict = storage.all()
        if (line == ""):
            inst_list = []
            for inst_key in inst_dict.keys():
                inst = inst_dict[inst_key]
                inst_list.append(inst.__str__())
            print(inst_list)
        else:
            if (line in self.classes):
                inst_list = []
                for inst_key in inst_dict.keys():
                    class_name, class_id = inst_key.split(".")
                    if (class_name == line):
                        inst = inst_dict[inst_key]
                        inst_list.append(inst.__str__())
                print(inst_list)
            else:
                print("** class doesn't exist **")

    def check_val_type(self, attr_val, args=None):
        '''Determine what type to store the attribute value as'''
        # Checks for strings with and without spaces
        if (attr_val.startswith('"') & attr_val.endswith('"')):
            if (attr_val.isnumeric() is False):
                attr_val = attr_val[1:-1]
        if (attr_val.startswith('"') & (not attr_val.endswith('"'))):
            try:
                next_val_str = args[4]
                attr_val = attr_val[1:] + " " + args[4][:-1]
            except Exception:
                attr_val = attr_val[1:]
        # Checks for integers
        elif (attr_val.isnumeric() is True):
            attr_val = int(attr_val)
        # Checks for floating point numbers
        else:
            try:
                attr_val_float = float(attr_val)
                return (attr_val_float)
            except ValueError:
                pass
        return (attr_val)

    def verify_attr_name_val(self, args):
        '''Verifies the attribute and and value
        to add to an instance from a list of arguments'''
        inst_dict_key = None
        if (((len(args) <= 2)) or (len(args) > 2)):
            try:
                args_line = " ".join(arg for arg in args[:2])
            except Exception:
                args_line = " ".join(arg for arg in args)
            inst_dict_key = self.verify_key(args_line)
            if (not inst_dict_key):
                return (0)
        if (len(args) < 3):
            print("** attribute name missing **")
            return (0)
        if (len(args) < 4):
            print("** value missing **")
            return (0)
        attr = args[2]
        val = self.check_val_type(args[3], args)
        return (inst_dict_key, attr, val)

    def do_update(self, line):
        '''
        Updates an intance with added or updated
        attributes and saves the changes to a file
        '''
        args = line.split()
        inst_dict_key_attr_val = self.verify_attr_name_val(args)
        if (inst_dict_key_attr_val):
            inst_key, inst_dict = inst_dict_key_attr_val[0]
            inst = inst_dict[inst_key]
            attr, attr_val = inst_dict_key_attr_val[1:]
            inst.__dict__.update({attr: attr_val})
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
