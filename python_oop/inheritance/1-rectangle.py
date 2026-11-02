#!/usr/bin/env python3
"""Module that defines a Rectangle class."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
