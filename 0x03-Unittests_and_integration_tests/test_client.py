#!/usr/bin/env python3
'''
This module is a unit test for the client module.
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubClient(unittest.TestCase):
    '''
    This is a test for the githuborg client method.
    '''
    @parameterized.expand([
        ('google',),
        ('abc',),
        ])
    @patch('client.get_json')
    def test_org(self, org, mock_get):
        '''
        This method test that GithubOrgClient.org returns the correct
        value.
        '''
        mock_get.return_value = {'name': org}
        #     mock_org.return_value = mock_get()
        #     test = GithubOrgClient(org)
        #     self.assertEqual(test.org, {'name': org})
        #     mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")
        test = GithubOrgClient(org)
        self.assertEqual(test.org, {'name': org})
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")
