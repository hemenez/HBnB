#!/usr/bin/python3
from models.base_model import BaseModel
"""Review Class"""


class Review(BaseModel):
    """Inherits from BaseModel class
    """
    place_id = ""
    user_id = ""
    text = ""
