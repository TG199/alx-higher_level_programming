#!/usr/bin/python3

"""Base class module"""


import json


class Base:
    """The above class is a base class."""

    __nb_objects = 0  # private attribute

    def __init__(self, id=None,):
        """
        The function initializes an object with an id,
        either provided as an argument or generated
        automatically.

        Args:
          id: The `id` parameter is used to assign a
          unique identifier to an object. If an `id` value is
        provided when creating an object, it will be assigned
        to the `id` attribute of the object. If no
        `id` value is provided, a unique identifier will
        be generated and assigned
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        The function `to_json_string` converts a list of dictionaries
        into a JSON string.

        Args:
          list_dictionaries: A list of dictionaries that you want to convert
          to a JSON string.

        Returns:
          a JSON string representation of the input list of dictionaries.
          If the input list is None, an
        empty list is returned.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The function `save_to_file` saves a list of objects to a JSON file.

        Args:
          cls: The parameter `cls` refers to the class object. It is used
          to access the class name and
        convert the list of objects to a JSON string.
          list_objs: The parameter `list_objs` is a list of objects
          that you want to save to a file. It
        can be any list of objects, but typically it would be a list of
        instances of a specific class.
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f'{class_name}.json'

        json_string = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])

        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(json_string)
