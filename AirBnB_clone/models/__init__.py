#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {}
classes['BaseModel'] = BaseModel
classes['User'] = User
classes['Place'] = Place
classes['State'] = State
classes['City'] = City
classes['Amenity'] = Amenity
classes['Review'] = Review

storage = FileStorage()
storage.reload()
