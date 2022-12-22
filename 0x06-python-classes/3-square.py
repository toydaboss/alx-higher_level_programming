#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private size, and public area
"""


class Square:
    """
    Class Square definition
    Arg:
        size (int): size of a side in a square
    Function:
        __init__(self, size)
    """

    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            size (int): default to 0 if None, assigns if int and >= 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """
        Calculates area of square
        Returns: area
        """
        return (self.__size) ** 2
