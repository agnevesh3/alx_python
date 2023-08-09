from rectangle import Rectangle

"""This class inherit from Rectangle class in rectangle.py file"""


class Square(Rectangle):
    """
    Class representing a square, inheriting from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square (width and height).
            x (int, optional): x-coordinate of the square's position. Default is 0.
            y (int, optional): y-coordinate of the square's position. Default is 0.
            id (int, optional): ID for the instance. If not provided, automatically generated.
        """
        super().__init__(
            size, size, x, y, id
        )  # Calling the superclass constructor with size for width and height

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.width  # Size of the square is the same as the width

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        self.width = value
        self.height = value  # Set both width and height to the same value

    def update(self, *args, **kwargs):
        """This method updates the attributes of the Square instance."""
        super().update(*args, **kwargs)  # Call the update method of the superclass

    def __str__(self):
        """This will return the output format with values in the given placeholders"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
