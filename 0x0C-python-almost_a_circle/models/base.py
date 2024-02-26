#!/usr/bin/python3
""" A base module
"""
import json
import os.path
import csv


class Base:
    """"Represents a base class"""
    __nb_objects = 0  # class attribute

    def __init__(self, id=None):
        """ Initialize instance attribute

        Args:
            id: id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ COnverts object to json string
        Args:
            list_dictionaries(list): list of dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object to file
        Args:
            list_objs(list): list of objects
        """
        file_name = f'{cls.__name__}.json'
        list_dic = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        json_string = cls.to_json_string(list_dic)
        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ return json string
        Args:
            json_string
        Returns: json string rep of an object
        """
        if json_string is None:
            return '[]'
        else:
            return json_string.loads(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Convert to json string to Python object
        Args:
            json_String: json string to convert to Python object
        """
        if not json_string:
            pass
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """ Sets all attributes of instance
         Args:
            cls: class
            dictionary: dictionary containing dictionaries
        Returns: An instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
            new.update(**dictionary)
            return new

    def load_from_file(cls):
        file_name = f'{cls.__name__}.json'

        if os.path.exists(file_name) is False:
            return []
        with open(file_name, mode="r", encoding="utf-8") as file:
            list_s = file.read()

        list_cls = cls.from_json_string(list_s)
        list_inst = []

        for i in range(len(list_cls)):
            list_inst.append(cls.create(**list_cls[i]))

        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves a CSV file
        """
        file_name = f'{cls.__name__}.csv'

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []
        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for item in range(len(list_keys)):
                    list_dic[item] = obj.to_dictionary()[list_keys[item]]
                matrix.append(list_dic[:])

        with open(file_name, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from CSV file """

        file_name = f'{cls.__name__}.csv'

        if os.path.exists(file_name) is False:
            return []

        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for item in csv_list:
            dic_csv = {}
            for kv in enumerate(item):
                dic_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dic_csv)

        list_inst = []

        for i in range(len(matrix)):
            list_inst.append(cls.create(**matrix[index]))

        return list_inst
