#!/usr/bin/python3
"""
classamenity
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity instance"""
        super().__init__(*args, **kwargs)
