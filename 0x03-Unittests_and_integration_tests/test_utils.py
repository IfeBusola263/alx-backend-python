#!/usr/bin/env python3
"""
This is a test Module for the utils module
functions.
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock


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


class TestMemoize(unittest.TestCase):
    """
    This is the test for the memoize decorator in the utils
    module.
    """

    def test_memoize(self):
        """
        This method test the decorator and all integration necessities expected
        of the decorator.
        """
        class TestClass:
            """
            Test Class for memoize
            """

            def a_method(self):
                """
                A method that returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                A method that invokes the a_method.
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_aMeth:
            test = TestClass()
            mock_aMeth.return_value = 150
            self.assertEqual(test.a_property, 150)
            self.assertEqual(test.a_property, 150)
            mock_aMeth.assert_called_once()
