#!/usr/bin/python3
"""
class city that inherited from base model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits BaseModel"""
    
    state_id = ""
    name = ""
