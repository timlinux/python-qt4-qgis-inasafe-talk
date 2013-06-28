# coding=utf-8
"""Mantra 2: Document, test, code."""


def get_minimum(a, b):
    """Get the minimum value and cast to int..

    :param a: First of the numbers to compare.
    :param b: Second of the numbers to compare.
    :returns: The minimumn value.
    :rtype: int
    """
    pass


from unittest import TestCase


class TestMinimum(TestCase):
    """Tests for minimum."""
    def test_get_minimum(self):
        """Check if half returns the correct value."""
        x = 10
        y = 55
        self.assertEqual(get_minimum(x, y), x)
