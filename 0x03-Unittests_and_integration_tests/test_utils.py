#!/usr/bin/env python3
"""
This is a test Module for the utils module
functions.
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    This is the test class where all cases would be tested.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
         ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test method for the access nested map function
        in the utils module.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test method for the exception raised in access nested map
        function in the utils module.
        """
        with self.assertRaises(KeyError, msg=expected) as err:
            access_nested_map(nested_map, path)
