#!/usr/bin/python3
'''A module to handle serialization and deserialization.

Serialize instances to a JSON file.
Deserialize a JSON file to instances.

Class:
    FileStorage : defines methods and attributes for
                    serialization and deserialation.

Typical Usage:
    storage = FileStorage()

Attributes:
    file_path : path to JSON file (str)
    object : dictionary of instance objects (dict)
'''
import copy
import json


class FileStorage():
    '''Defines methods and attributes for serialiation and
    deserialization.

    Attributes:
        __file_path : path to JSON file (str)
        __object : dictionary of instance objects (dict)

    Methods:
        all() : returns the __object attribute
        new(object) : adds an instance object to __object
        save() : serializes the instance objects in object
        reload() : deserializes the JSON objects to instances objects

    Exceptions : None
    '''
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''Initialises a file path and an object
        dictionary to store all objects'''

    def all(self):
        '''Returns the class __object attribute'''
        return (self.__objects)

    def new(self, inst):
        '''Adds an instance object to __object'''
        class_name = inst.__class__.__name__
        inst_id = inst.id
        inst_key = class_name + "." + inst_id
        self.__objects.update({inst_key: inst})

    def save(self):
        '''Serializes instances to JSON file'''
        json_object = {}
        with open(self.__file_path, "w") as file:
            for inst_key in self.__objects:
                inst = self.__objects[inst_key]
                inst_dict = inst.to_dict()
                json_object[inst_key] = inst_dict
            json.dump(json_object, file)

    def reload(self):
        '''Deserializes objects in JSON file to instances'''
        try:
            with open(self.__file_path, "r") as file:
                json_object = json.load(file)
                self.to_instance(json_object)
        except Exception:
            # Do nothing
            pass

    def to_instance(self, json_obj):
        '''Changes object values to instantiable objects'''

        # Model imported here to prevent circular import error
        try:
            # Get key and dict object from loaded data
            for inst_key, inst_obj in json_obj.items():
                #  Create an instance with each dict object
                inst = self.create_instance(inst_obj)
                # Add key : instance pair to __object
                self.__objects.update({inst_key: inst})
        except Exception:
            # Do nothing
            pass

    def create_instance(self, obj):
        '''Deterimine the right instance to create'''
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import BaseModel

        class_name = obj["__class__"]
        if (class_name == "BaseModel"):
            return (BaseModel(**obj))
        elif (class_name == "User"):
            return (User(**obj))
        elif (class_name == "Place"):
            return (Place(**obj))
        elif (class_name == "State"):
            return (State(**obj))
        elif (class_name == "City"):
            return (City(**obj))
        elif (class_name == "Amenity"):
            return (Amenity(**obj))
        elif (class_name == "Review"):
            return (Review(**obj))
