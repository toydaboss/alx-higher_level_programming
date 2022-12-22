#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size, position, and public area
can access and update size and position
can print to stdout the square using #'s
"""


class Square:
    """
    Class Square definition
    Args:
        size (int): size of a side in a square
        position (tuple): position of the square when printing
    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        Attributes:
            size (int): default to 0 if None; don't use __size to call setter
            position (tuple): tuple of two positive integers
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates area of the square
        Returns:
            area
        """

        return (self.__size) ** 2

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

    @property
    def position(self):
        """
        Getter
        Returns: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter
        Args:
            value (tuple): sets position to value if tuple(int, int)
        """
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

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
                if self.position[0] > 0:
                    for j in range(int(self.position[0])):
                        print(" ", end="")
                for k in range(num):
                    print('#', end="")
                print()
                i += 1
