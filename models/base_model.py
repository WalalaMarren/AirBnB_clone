#!/usr/bin/python3
'''A basis that defines common attributes/methods for other classes.

This class is to be used to create sub-classes for the models package.

Class:
    BaseModel

Typical Usage:
    class MyClass(BaseModel):
        pass

Attributes: None
'''

import uuid
import json
from models import storage
from datetime import datetime


class BaseModel():
    '''Defines the base attributes and methods for sub-classes

    Methods:
        to_dict : returns dictionary representation of instance
        save : saves an instance to a file
        to_instance : transforms loaded data to instantiable form
    '''

    def __init__(self, *args, **kwargs):
        '''Initialise the base class with or without kwargs
        Attributes:
            id : the class id (str)
            created_at : time of creation (datetime)
            updated_at : time of latest change (datetime)
        '''
        if kwargs:
            # Call function to prepare kwargs for instantiation
            self.to_instance(kwargs)
            # Set instance attributes from kwargs items

            self.__dict__.update(kwargs)
        else:
            # Generate a unique identifier for each base object
            self.id = str(uuid.uuid4())
            # Record time instance was created
            self.created_at = datetime.now()
            # Record time and update later when changes are made
            self.updated_at = datetime.now()
            # Adds class instance to instance storer
            storage.new(self)

    def __str__(self):
        '''Displays a string representation of a base object'''
        return (f"{[self.__class__.__name__]} "
                f"({self.id}) {self.__dict__}")

    def save(self):
        '''
        Updates "updated_at" every time the object is changed
        and store the instance into a JSON file
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Creates a dictionary representation of the a base object.
        This method is the first piece of the serialization and
        deserialization process.
        '''
        # Convert datetime objects to strings
        # and ensure conversion is attempted only once
        return_dict = self.__dict__.copy()
        if (type(return_dict["created_at"]) == datetime):
            return_dict["created_at"] = return_dict["created_at"].isoformat()
        if (type(return_dict["updated_at"]) == datetime):
            return_dict["updated_at"] = return_dict["updated_at"].isoformat()
        # Add a new attribute containing the name of the class
        if not return_dict.get("__class__"):
            class_name = self.__class__.__name__
            return_dict.update({"__class__": class_name})
        return (return_dict)

    def to_instance(self, ins_dict):
        '''Prepares kwargs in instance dict for instantiation.
           This method is called at the instantiation of a class with kwargs
        '''
        # Remove the __class__ attribute
        try:
            ins_dict.pop("__class__")
        except Exception:
            # Do nothing
            pass
        for key in ins_dict.keys():
            if ((key == "created_at") or (key == "updated_at")):
                time = ins_dict[key]
                ins_dict[key] = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f")
