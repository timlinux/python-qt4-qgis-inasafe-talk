# coding=utf-8
"""Unit tests for half."""
from unittest import TestCase
from half import half


class TestHalf(TestCase):
    """Tests for half."""
    def test_half(self):
        """Check if half returns the correct value."""
        x = 10
        y = half(x)
        self.assertEqual(y, 5)

        x = 11
        y = half(x)
        self.assertEqual(y, 5.5)
