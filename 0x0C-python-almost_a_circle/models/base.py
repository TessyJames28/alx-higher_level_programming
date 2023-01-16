#!/usr/bin/python3
"""Defines class Base"""
import json
import csv
import turtle


class Base:
    """a class Base with private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing the Base class

        instances:
            id (int) - assign the value None

        if id is not None, assign the public instance attribute id
        with this argument value
        otherwise, increment __nb_objects and assign the
        new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list deserialization of the JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Arguments:
            list_objs - list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [objs.to_dictionary() for objs in list_objs]
                file.write(Base.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set

        Arguments:
            **dictionary (dict) - key/value pairs of attributes
        """
        if dictionary and len(dictionary) != {}:
            if cls.__name__ == "Rectangle":
                dum_inst = cls(1, 1)
            else:
                dum_inst = cls(1)
            dum_inst.update(**dictionary)
            return dum_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances depending on the cls"""
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method that serializes CSV

        Arguments:
            list_objs - list of instances who inherits of Base
        """

        filename = str(cls.__name__) + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """class method that serializes CSV

        Arguments:
            list_objs - list of instances who inherits of Base
        """
        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                read_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                read_dicts = [dict([key, int(val)] for key, val in dic.items())
                              for dic in read_dicts]
                return [cls.create(**dic) for dic in read_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draws all the Rectangles and Squares using turtle graphics

        Arguments:
            list_rectangles - list of rectangle coordinates
            list_squares - list of square coordinates
        """
        t = turtle.Turtle()
        t.screen.bgcolor("#FFD700")
        t.pensize(4)
        t.shape("turtle")

        t.color("#324ab2")
        for val in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(val.x, val.y)
            t.down()
            for idx in range(2):
                t.forward(val.width)
                t.left(90)
                t.forward(val.height)
                t.left(90)
            t.hidturtle()

        t.color("#251858")
        for sqval in list_squares:
            t.showturtle()
            t.up()
            t.goto(sqval.x, sqval.y)
            t.down()
            for idx in range(2):
                t.forward(sqval.width)
                t.left(90)
                t.forward(sqval.height)
                t.left(90)
                t.hideturtle()

        turtle.exitonclick()
