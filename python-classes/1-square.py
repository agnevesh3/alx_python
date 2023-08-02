class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer.")
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except (TypeError, ValueError) as e:
            print(e)

    def area(self):
        """
        Calculate the area of a square.

        Parameters:
            size (int): The size of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))
