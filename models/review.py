#!/usr/bin/python3
"""
class review incated place and user and text
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inheritated class Review from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
