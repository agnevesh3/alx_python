"""This class will validate the values of rectangle width, height, x and y"""


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


class Rectangle(Base):
    """
    Class representing a rectangle, inheriting from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position. Default is 0.
            y (int, optional): y-coordinate of the rectangle's position. Default is 0.
            id (int, optional): ID for the instance. If not provided, automatically generated.
        """
        Base.__init__(self, id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer.")
        self.__width = width
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer.")
        self.__height = height
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer.")
        self.__x = x
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer.")
        self.__y = y
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method to retrieve the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method to set the x-coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method to retrieve the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method to set the y-coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method will calculate the area of the rectangle by multiplying the width and the hieght"""
        return self.__width * self.__height

    def display(self):
        """This will print in stdout of the Rectangle instance with the character #-"""
        for _ in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """This will return the output format with values in the given place holders"""
        if self.__x is None:
            self.__x = 0
        if self.__y is None:
            self.__y = 0

        return "[{}] ({}) {}/{} - {}/{}".format(
            "Rectangle", self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """This method updates the attributes of the Rectangle instance."""
        # This section will update the values of attributes
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.__width = args[1]
        if num_args >= 3:
            self.__height = args[2]
        if num_args >= 4:
            self.__x = args[3]
        if num_args >= 5:
            self.__y = args[4]
            # This part will update the attributes based on kwargs
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
