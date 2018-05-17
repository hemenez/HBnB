#!/usr/bin/python3
"""FileStorage class"""
import json
import os
import models
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """class FileStorage
        __file_path: private; string; path to JSON file
        __objects: private; dictionary; empty; stores all objects
        by <class name>.id -- example: if id=1212, key will be
        BaseModel.1212
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Method returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Method sets in __objects the obj with key <obj
        class name>.id
        """
        key1 = obj.__class__.__name__
        key2 = obj.id
        key = key1 + '.' + key2
        self.__objects[key] = obj
        return self.__objects

    def save(self):
        """Method serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as myFile:
            my_dict = {}
            for k, v in self.__objects.items():
                my_dict[k] = v.to_dict()
            json.dump(my_dict, myFile)

    def reload(self):
        """Method deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                obj_storage = json.load(myFile)
                for k, v in obj_storage.items():
                    store = v['__class__']
                    if '__class__' in v and store in models.classes:
                        self.__objects[k] = models.classes[store](**v)
        else:
            pass






























#                    print(my_dict['__class__'], '\n\n')
#                        print('k:', k, '\n')
#                        print('self.__objects[k]', self.__objects[k], '\n')
##                            print(models.classes[val])
 ##                           print()
  ##                          print(v[key])
   ##                         v[key](**key)
