# coding=utf-8
"""Mantra 7: Make it work first, then make it work fast."""
from timeit import Timer


def slow(a, b, c):
    """Add up three numbers.

    :param a: First number to add.
    :type a: int, float
    :param b: Second number to add.
    :type b: int, float
    :param c: Third number to add.
    :type c: int, float
    :returns: A number representing the sum of the three input numbers.
    :rtype : int, float
    """
    x = sum([a, b, c])
    return x


def fast(a, b, c):
    """Add up three numbers.

    :param a: First number to add.
    :type a: int, float
    :param b: Second number to add.
    :type b: int, float
    :param c: Third number to add.
    :type c: int, float
    :returns: A number representing the sum of the three input numbers.
    :rtype : int, float
    """
    return a + b + c

if __name__ == "__main__":
    timer = Timer('slow(10, 20, 30)', setup="from __main__ import slow")
    print 'Slow:', timer.timeit()
    timer = Timer('fast(10, 20, 30)', setup="from __main__ import fast")
    print 'Fast', timer.timeit()
