#!/usr/bin/python3
"""
The module that holds the base class BaseModel
that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """ The class BaseModel that defines all common attributes
    /methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ Initializes the instances """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            

    def __str__(self):
        """ The method that return printable string as below
        [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ The method that updates the public instance attribute
        'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """ The method returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dictry = {}
        dictry.update(self.__dict__)
        dictry["__class__"] = self.__class__.__name__
        dictry["created_at"] = dictry["created_at"].isoformat()
        dictry["updated_at"] = dictry["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dictry
        