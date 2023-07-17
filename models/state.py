#!/usr/bin/python3
"""
class state for put the name
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State instance"""
        super().__init__(*args, **kwargs)

