"""This is a base class to assign an id of any instance"""


class Base:
    """The id is given and intial value of 0"""

    __nb_objects = 0
    """ This module takes attribute of id"""

    def __init__(self, id=None):
        """if the id attribute is None, the id will count progressively
        otherwise the id will set to the number provided as attribute
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        if id is not None:
            self.id = id
