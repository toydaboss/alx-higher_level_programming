#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private size
"""


class Square:
    """
    Class Square definition
    Arg:
        size: size of a side in a square
    Function:
        __init__(self, size)
    """

    def __init__(self, size):
        """
        Initializes square
        Attribute:
            size
        """
        self.__size = size
