"""
This module defines a storage mechanism for model objects.

Classes:
    Storage: A storage class for managing model objects.

Module-level Variables:
    storage: An instance of the Storage class for easy access.

Usage:
    from models.base_model import BaseModel
    from storage import storage

    my_model = BaseModel()
    storage.new(my_model)  # Add the model to the storage
    storage.save()  # Save the changes made to the stored models
"""

from models.base_model import BaseModel


class Storage:
    """
    The Storage class provides a mechanism to store and manage model objects.
    """
    def new(self, obj):
        """
        Add a model object to the storage.

        Args:
            obj: The model object to be added to the storage.
        """
        pass

    def save(self):
        """
        Save the changes made to the stored model objects.
        """
        pass


storage = Storage()
