#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and public area
can access and update size
can print to stdout the square using #'s
"""


class Square:
    """
    Class Square definition
    Args:
        size (int): size of a side in a square
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        my_print(self)
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
        Calculates area of the square
        Returns:
            area
        """
        return self.__size ** 2

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
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """
        Prints square as #'s
        """
        if self.__size == 0:
            print()
        else:
            i = 0
            num = self.__size
            while (i < num):
                for j in range(num):
                    print('#', end="")
                print()
                i += 1
