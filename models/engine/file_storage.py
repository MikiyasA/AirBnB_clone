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
        return self.__class__.__objects

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
        if (os.path.exists(self.__file_path) is True):
            with open(self.__file_path, "r") as f:
                json.load(f)

