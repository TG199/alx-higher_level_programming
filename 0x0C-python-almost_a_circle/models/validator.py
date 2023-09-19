#!/usr/bin/python3

def int_validator(name, value):
        if name in ["width", "height",]:
                if type(value) is not int:
                        raise TypeError(f'{name} must be an intger')
                elif value <= 0:
                        raise ValueError(f'{name} must be > 0')
        if name in ["x", "y"]:
                if type(value) is not int:
                        raise TypeError(f'{name} must be an intger')
                elif value < 0:
                        raise ValueError(f'{name} must be >= 0')
