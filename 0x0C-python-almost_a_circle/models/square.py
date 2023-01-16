#!/usr/bin/python3
"""defines class Square"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing new square

        Attribute:
            size (int) - size of the square
            x (int) - x coordinate of the new square
            y (int) - y coordinate of the square
            id (int) - the identity of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/set the size of the new square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of square using specified format"""
        new_str = "[" + str(__class__.__name__) + "] (" + str(self.id) + ") "
        new_str += str(self.x) + "/" + str(self.y) + " - " + str(self.size)
        return new_str

    def update(self, *args, **kwargs):
        """
        update square value with keyword and no-keyword arguments

        *args is the list of arguments - no-keyworded arguments
        **kwargs can be thought of as a double pointer to a dictionary:
        key/value (keyworded arguments)

        Arguments:
            arg0 - id
            arg1 - size
            arg2 - x
            arg3 - y
        """

        if args and len(args) != 0:
            elem = 0

            for arg in args:
                if elem == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif elem == 1:
                    self.size = arg
                elif elem == 2:
                    self.x = arg
                elif elem == 3:
                    self.y = arg

                elem += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y

            }
