"""This class will validate the values of rectangle width, height, x and y"""


class Base:
    """
    Base class for creating instances with an ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int, optional): ID for the instance. If not provided, automatically generated.
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
        self.__width = width
        self.__height = height
        self.__x = x
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
            raise ValueError("OK")
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
            raise ValueError("OK")
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
        if value <= 0:
            raise ValueError("OK")
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
        if value <= 0:
            raise ValueError("OK")
        self.__y = value
