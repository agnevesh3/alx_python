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

        self._validate_and_set_attribute("width", "_width", width)
        self._validate_and_set_attribute("height", "_height", height)
        self._validate_and_set_attribute("x", "_x", x)
        self._validate_and_set_attribute("y", "_y", y)

    def _validate_and_set_attribute(self, name, private_attr, value):
        self._validate_value(name, value, int)
        self.__dict__[private_attr] = value

    def _validate_value(self, name, value, expected_type):
        if not isinstance(value, expected_type):
            raise TypeError("{} must be an integer.".format(name))

    # Getter and setter methods for width
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._validate_and_set_attribute("width", "_width", value)

    # Getter and setter methods for height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._validate_and_set_attribute("height", "_height", value)

    # Getter and setter methods for x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._validate_and_set_attribute("x", "_x", value)

    # Getter and setter methods for y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._validate_and_set_attribute("y", "_y", value)
