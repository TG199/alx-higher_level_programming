#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        pass

    for keyy in list(a_dictionary):
        if keyy == key:
            del a_dictionary[keyy]
    return a_dictionary
