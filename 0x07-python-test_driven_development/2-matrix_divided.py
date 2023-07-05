#!/usr/bin/python3
"""Matrix divided"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): Matrix of integers pr floats.
        div (int or float): Divisor

    Returns:
        list of lists: New matrix with elements divided by `div`

    Raises:
        TypeError: If `matrix` is not a matrix of integers or floats,
                    or if `div` is not a number.
        ZeroDivisionError: If `div` is equal to 0.
        TypeError: If each row of the matrix doesn't have the same size.
    """
    
