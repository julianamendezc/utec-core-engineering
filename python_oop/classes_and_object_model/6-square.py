#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validating it."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after validating it."""
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(x) is int and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        print(str(self))

    def __str__(self):
        """Return the square as a string."""
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i < self.__size - 1:
                result += "\n"

        return result
