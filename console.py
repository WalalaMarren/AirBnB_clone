#!/usr/bin/python3
"""Class instance that inherits from the Cmd class"""
import cmd
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


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
        elif (class_name == "Place"):
            return (Place())
        elif (class_name == "State"):
            return (State())
        elif (class_name == "City"):
            return (City())
        elif (class_name == "Amenity"):
            return (Amenity())
        elif (class_name == "Review"):
            return (Review())

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
                storage.save()
                print(class_instance.id)

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
            class_name, inst_id = line.split()
            inst_key = class_name + "." + inst_id
            inst_objs = storage.all()
            if (inst_objs.get(inst_key) is None):
                print("** no instance found **")
                return (None)
            return (inst_key, inst_objs)
        return (0)

    def do_show(self, line):
        '''
        Prints the string representation of an
        instance based on the class name and id
        '''
        inst_objs_key = self.verify_key(line)
        if (inst_objs_key):
            inst_key, inst_objs = inst_objs_key
            inst = inst_objs[inst_key]
            print(inst)

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        inst_objs_key = self.verify_key(line)
        if (inst_objs_key):
            inst_key, inst_objs = inst_objs_key
            inst_objs.pop(inst_key)
            storage.save()

    def do_all(self, line):
        '''
        Prints the string representation of all instances of a
        class specified by the class name and id
        '''
        inst_objs = storage.all()

        if (line == ""):
            inst_list = []
            for inst_key, inst in inst_objs.items():
                inst_list.append(inst.__str__())
            print(inst_list)

        else:

            if (line in self.classes):
                inst_list = []
                for inst_key in inst_objs.keys():
                    class_name, inst_id = inst_key.split(".")
                    if (class_name == line):
                        inst = inst_objs[inst_key]
                        inst_list.append(inst.__str__())
                print(inst_list)
            else:
                print("** class doesn't exist **")

    def check_val_type(self, attr_val, args=None):
        '''Determine what type to store the attribute value as'''

        print("This is the attriubute we were given \n", attr_val)
        has_dqb = attr_val.startswith('"')
        has_dqe = attr_val.endswith('"')
        has_sqb = attr_val.startswith("'")
        has_sqe = attr_val.endswith("'")

        # Normal arguments
        if ((not has_dqb) & (not has_dqe)):
            return (attr_val)

        # Argument starts and ends with single or double quotes
        if ((has_dqb & has_dqe) or (has_sqb & has_sqe)):
            print("Has all quotes")
            return (attr_val[1:-1])

        # Argument starts with but doesn't end with single or double quotes
        if ((has_dqb or has_sqb) and (not has_dqe or not has_sqe)):
            full_str = attr_val[1:]
            i = 1
            args_exist = True

            while (args_exist):
                try:
                    next_word = args[3 + i]
                except IndexError:
                    return (full_str)
                if (next_word.endswith('"') or next_word.endswith("'")):
                    full_str += " " + next_word[:-1]
                    return (full_str)
                else:
                    full_str += " " + next_word
                    i += 1

        # Check for integer
        try:
            attr_val_int = int(attr_value)
            return (attr_val_int)
        except Exception:
            return (attr_val)

        # Checks for floating point numbers
        if ("." in attr_val):
            try:
                attr_val_float = float(attr_val)
                return (attr_val_float)
            except ValueError:
                return (attr_val)

    def verify_attr_name_val(self, args):
        '''Verifies the attribute and and value
        to add to an instance from a list of arguments'''

        inst_objs_key = None

        if (((len(args) <= 2)) or (len(args) > 2)):
            try:
                args_line = " ".join(arg for arg in args[:2])
            except Exception:
                args_line = " ".join(arg for arg in args)
            inst_objs_key = self.verify_key(args_line)
            if (not inst_objs_key):
                return (0)

        if (len(args) < 3):
            print("** attribute name missing **")
            return (0)

        if (len(args) < 4):
            print("** value missing **")
            return (0)

        attr = args[2]
        val = self.check_val_type(args[3], args)
        return (inst_objs_key, attr, val)

    def do_update(self, line):
        '''
        Updates an intance with added or updated
        attributes and saves the changes to a file
        '''
        args = line.split()
        inst_objs_key_attr_val = self.verify_attr_name_val(args)

        if (inst_objs_key_attr_val):
            inst_key, inst_objs = inst_objs_key_attr_val[0]
            inst = inst_objs[inst_key]
            attr, attr_val = inst_objs_key_attr_val[1:]
            inst.__dict__.update({attr: attr_val})
            storage.save()

    def default(self, line):
        '''Function to call when a strange command is encountered'''

        valid_commands = ["all()", "count()"]
        cls_name, command = line.split(".")

        if (cls_name not in self.classes):
            return (cmd.Cmd.default(self, line))
        if (command not in valid_commands):
            return (cmd.Cmd.default(self, line))

        inst_objs = storage.all()

        if (command == "all()"):
            self.do_all(cls_name)
        elif (command == "count()"):
            inst_count = 0
            for inst_key in inst_objs.keys():
                inst_cls_name = inst_key.split(".")[0]
                if (inst_cls_name == cls_name):
                    inst_count += 1
            print(inst_count)

        # inst_list = []
        # inst_objs = storage.all()

        # for inst_key, inst_obj in inst_objs.items():
            # inst_key = inst_key.split(".")[0]
            # if (inst_key == class_name):
            # inst_list.append(inst_obj.__str__())
        # print(inst_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
