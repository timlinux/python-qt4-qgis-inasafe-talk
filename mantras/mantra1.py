"""Mantra 1: Adhere to the principle of least surprise."""

def get_minimum(a, b):
    """Get the minimum value and cast to int..

    :param a: First of the numbers to compare.
    :param b: Second of the numbers to compare.
    :returns: The minimum value.
    :rtype: int
    """
    if a < b:
        return int(a)
    else:
        return int(b)


def get_maximum(a, b):
    """Get the maximum value and cast to int.

    :param a: First of the numbers to compare.
    :param b: Second of the numbers to compare.
    :returns: The maximum value.
    :rtype: int
    """
    if a > b:
        return a
    else:
        return b
