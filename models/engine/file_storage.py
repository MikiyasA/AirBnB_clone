#!/usr/bin/python3
"""
The method to serialization-deserialization to JSON file
"""
import json
import os


class FileStorage:
    """ The class that serializes instances to a JSON file and
    deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        dic = {}

        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dic, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        dicty = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                 'City': City, 'Amenity': Amenity, 'State': State, 'Review': Review}
        
        if (os.path.exists(self.__file_path) is True):
            with open(self.__file_path, "r") as f:
                for k, v  in json.load(f).items():
                	self.new(dicty[v['__class__']](**v))

