#!/usr/bin/python3
"""
Module 4-square
Defines class Square with private size, and public area
can access and update size
"""


class Square:
    """
    Class Square definition
    Args:
        size (int): size of a side in a square
    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            size (int): default to 0 if None, don't use __size to call setter
        """
        self.size = size

    def area(self):
        """
        Calculates area of square
        Returns: area
        """
        return (self.size) ** 2

    @property
    def size(self):
        """
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value (int): sets size to value if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
