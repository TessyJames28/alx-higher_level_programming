"""This module divides two matrix of equal size"""


def matrix_divided(matrix, div):
    """
    divides two matrix of equal size

    Arguments:
        matrix: `matrix` list of lists
        div: `div` must be a number int or float

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Return:
        a new 'matrix'
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    for x in matrix:
        for y in x:
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

        if not isinstance(x, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda y: round(y / div, 2), row)) for row in matrix])


if __name__ == "__main__":
    doctest.textfile("./tests/2-matrix_divided.txt")
