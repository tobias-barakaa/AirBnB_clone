import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    The BaseModel class serves as the base model for the AirBnB clone console.

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.

    Methods:
        __init__(*args, **kwargs): Initializes a new instance of the BaseModel class.
        __str__(): Returns a human-readable string representation of the instance.
        save(): Updates the updated_at attribute with the current datetime and saves the instance.
        to_dict(): Returns a dictionary representation of the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not None and not empty, the instance attributes are assigned based on the key-value pairs.
        If the keys are 'created_at' or 'updated_at', the corresponding values are converted to datetime objects.
        If kwargs is None or empty, new values are generated for 'id', 'created_at', and 'updated_at'.
        The new instance is then added to the storage.
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a human-readable string representation of the BaseModel instance.

        Returns:
            str: The formatted string representation of the instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing all the instance attributes.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

