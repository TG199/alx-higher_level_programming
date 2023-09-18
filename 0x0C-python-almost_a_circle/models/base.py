#/usr/bin/python3


class Base:
    # The above class is a base class.

    __nb_objects = 0 # private attribute
    
    def __init__(self, id=None):
        """
        The function initializes an object with an ID, either provided as an argument or generated
        automatically.
        
        :param id: The "id" parameter is used to assign a unique identifier to an instance of the class.
        If an "id" value is provided when creating an instance, it will be assigned to the instance's
        "id" attribute. If no "id" value is provided, a unique identifier will be generated
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id