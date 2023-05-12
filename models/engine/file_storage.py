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
from datetime import datetime


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
    __object = {}

    def all(self):
        '''Returns the class __object attribute'''
        return (self.__object)

    def new(self, class_obj):
        '''Adds an instance object to __object'''
        class_name = class_obj.__class__.__name__
        class_id = class_obj.id
        class_key = class_name + "." + class_id
        self.__object.update({class_key: class_obj})

    def save(self):
        '''Serializes instances to JSON file'''
        json_object = {}
        with open(self.__file_path, "w") as file:
            for class_key in self.__object:
                class_obj = self.__object[class_key]
                class_dict = class_obj.to_dict()
                json_object[class_key] = class_dict
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
            for obj_id in json_obj.keys():
                obj_dict = json_obj[obj_id]
                #  Create an instance with each dict object
                obj_instance = self.create_instance(obj_dict)
                # Add key : instance pair to __object
                self.__object.update({obj_id: obj_instance})
        except Exception:
            # Do nothing
            pass

    def create_instance(self, obj):
        '''Deterimine the right instance to create'''
        from models.base_model import BaseModel
        from models.user import User

        class_name = obj["__class__"]
        if (class_name == "BaseModel"):
            return (BaseModel(**obj))
        elif (class_name == "User"):
            return (User(**obj))
        # elif (class_name == "Place"):
        #     return (Place(**obj))
        # elif (class_name == "State"):
        #     return (State(**obj))
        # elif (class_name == "City"):
        #     return (City(**obj)):
        # elif (class_name == "Amenity"):
        #     return (Amenity(**obj))
        # elif (class_name == "Review"):
        #     return (Review(**obj))
