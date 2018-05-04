#!/usr/bin/python3
class Square:
    """ This is the square class. """
    def __init__(self, size=0, position=(0,0)):
        """ init is called to create an object. self refers to itself
        Args:

            size (int): This is the size of the square.
            position (int, int): These are the coordinates of the square.

        Returns:
            Nothing.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ This retrieves the size.
        Args:
            None.
        Returns:
            This returns the size.
        """
        return self.__size

    @property
    def position(self):
        """ This will retrieve the position of the square.

        Args:
            None.

        Returns:
            This will return the coordinates.

        """
        return self.__position

    @size.setter
    def size(self, value):
        """ This sets the size of the square.
        Args:
            value (int): This is the value size of the square.
        Return:
            Nothing.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0 ")

        self.__size = value

    @position.setter
    def position(self, value):
        """ This sets the position of the square.
        Args:
            value (int): This is the value of the position.

        Returns:
            Nothing.
        """
        if isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int) and value[0] >= 0 and value[1] >= 0 is false:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ This will give us the area of a square.
        Args:
            None.
        Returns:
            The area.
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints in stdout
        Args:
            Nothing.
        Returns:
            Nothing.
        """

        position, ofthemothafuckingtuple = self.__position
        size = self.__size

        if size == 0:
            print("")
        else:
            for x in range(position):
                print("")
            for y in range(size):
                print(" " * position, end="")
                print("#" * size)
