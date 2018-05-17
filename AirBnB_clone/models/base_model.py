#!/usr/bin/python3
from copy import deepcopy
import models
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class that defines all common attributes/methods for other
    classes
    """
    def __init__(self, *args, **kwargs):
        """Method initializes all basic instance attributes of
        BaseModel class. Includes id, created_at, and update_at.
        """
        self.id = str(uuid.uuid4())
        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()
        else:
            desired_ISO = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if 'created_at' in key:
                    self.created_at = datetime.strptime(value, desired_ISO)
                elif 'updated_at' in key:
                    self.updated_at = datetime.strptime(value, desired_ISO)
                elif 'id' in key:
                    self.id = value
                elif '__class__' not in key:
                    setattr(self, key, value)

    def __str__(self):
        """Method pirnts class name, id, and dictionary of instance
        """
        str1 = '[' + str(self.__class__.__name__) + '] '
        str2 = '(' + str(self.id) + ') ' + str(self.__dict__)
        return str1 + str2

    def __repr__(self):
        """ """
        str1 = '[' + str(self.__class__.__name__) + '] '
        str2 = '(' + str(self.id) + ') ' + str(self.__dict__)
        return str1 + str2

    def save(self):
        """Method updates attribute, 'updated_at,' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method returns a dictionary containing all keys/values of
        __dict__ of instance.
        """
        new_dict = deepcopy(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
