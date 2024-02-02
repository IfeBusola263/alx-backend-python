#!/usr/bin/env python3
"""
This is a test Module for the utils module
functions.
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """
    This is the class test for all the expected outputs of the
    get_json method in the utils module.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mocked_req):
        """
        Test for the get_json function.
        """
        mock_response = Mock()
        mock_response.json = lambda: test_payload
        mocked_req.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        self.assertEqual(mock_response.json(), test_payload)
        mocked_req.assert_called_once_with(test_url)
