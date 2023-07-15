import uuid
from datetime import datetime

class BaseModel:
    """
    The BaseModel class defines common attributes and methods for other classes.

    Public instance attributes:
        id: string - Assigned with a unique identifier when an instance is created.
        created_at: datetime - Represents the datetime when an instance is created.
        updated_at: datetime - Represents the datetime when an instance is last updated.

    Public instance methods:
        __str__(): Returns a string representation of the instance.
        save(): Updates the `updated_at` attribute with the current datetime.
        to_dict(): Returns a dictionary containing all the instance attributes.

    Usage:
        my_model = BaseModel()
        my_model.save()
        my_model_json = my_model.to_dict()
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
            id: string - Assigned a unique identifier using uuid.uuid4() method.
            created_at: datetime - Set to the current datetime.
            updated_at: datetime - Set to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string in the format [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing all keys/values of __dict__ of the instance.
                It includes the '__class__' key with the class name and
                the 'created_at' and 'updated_at' keys as strings in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
