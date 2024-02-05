#!/usr/bin/env python3
'''
This module is a unit test for the client module.
'''
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubClient(unittest.TestCase):
    '''
    This is a test for the githuborg client method.
    To check if it has the correct return value.
    '''
    @parameterized.expand([
        ('google',),
        ('abc',),
        ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        '''
        This method test that GithubOrgClient.org returns the correct
        value.
        '''
        mock_get_json.return_value = {"name": org}
        test = GithubOrgClient(org)
        self.assertEqual(test.org, {"name": org})
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org))

    def test_public_repos_url(self):
        '''
        This tests if the result of the _public_repos_url is
        accurate.
        '''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_property_org:
            mock_property_org.return_value = {
                "repos_url": "https://example.com"}
            client_obj = GithubOrgClient("p")
            self.assertEqual(client_obj._public_repos_url,
                             "https://example.com")