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
from datetime import datetime
import json


class BaseModel():
    '''Defines the base attributes and methods for sub-classes'''

    def __init__(self, *args, **kwargs):
        '''Initialise the base class with or without kwargs'''
        if kwargs:
            # Call function to prepare kwargs for instantiation
            self.transform_kwargs(kwargs)
            # Set instance attributes from kwargs items
            self.__dict__.update(kwargs)
        else:
            # Generate a unique identifier for each base object
            self.id = str(uuid.uuid4())
            # Record time instance was created
            self.created_at = datetime.now()
            # Record time and update later when changes are made
            self.updated_at = datetime.now()

    def __str__(self):
        '''Displays a string representation of a base object'''
        return (f"{[self.__class__.__name__]} "
                f"({self.id}) {self.__dict__}")

    def save(self):
        '''Updates "updated_at" every time the object is changed'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Creates a dictionary representation of the a base object.
        This method is the first piece of the serialization and
        deserialization process.
        '''
        # Convert datetime objects to strings
        # and ensure conversion is attempted only once
        if (type(self.created_at) == datetime):
            self.created_at = self.created_at.isoformat()
        if (type(self.updated_at) == datetime):
            self.updated_at = self.updated_at.isoformat()
        self.__dict__.update({"__class__": self.__class__.__name__})
        return (self.__dict__)

    def transform_kwargs(self, instance_dict):
        '''Prepares kwargs for instantiation.
        This method is called at the instantiation
        of a class with kwargs'''
        # Remove the __class__ attribute
        try:
            instance_dict.pop("__class__")
        except:
            pass
        # Convert datetime arguments from string to datetime
        for key in instance_dict.keys():
            if ((key == "created_at") or (key == "updated_at")):
                instance_dict[key] = datetime.fromisoformat(instance_dict[key])
