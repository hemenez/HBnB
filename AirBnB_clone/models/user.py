#!/usr/bin/python3
from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """Inherits from BaseModel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
