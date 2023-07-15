import uuid
from datetime import datetime


class BaseModel:
    """
    A base model class that defines common att and methods for other classes.

    Attributes:
        id (str): Unique identifier assigned to an instance (UUID).
        created_at (datetime): Date and time when the instance was created.
        updated_at (dtt): Date and time when the instance was last updated.

    Methods:
        __str__(): Returns a string representation of the object.
        save(): Updates the `updated_at` attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the object.

    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        This constructor sets the `id` attribute to a unique identifier (UUID),
        `created_at` att to the current datetime, and `updated_at` attribute
        to the same value.

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the object.

        The string format is: "[<class name>] (<id>) <attribute dictionary>"

        Returns:
            str: String representation of the object.

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.

        This method should be called whenever an object is modified.

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        This method returns a dictionary contaig all the instance attributes,
        including the '__class__' key with the class name. The 'created_at' and
        'updated_at' att are converted to string objects in the ISO format.

        Returns:
            dict: Dictionary representation of the object.

        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
