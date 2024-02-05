#!/usr/bin/env python3
'''
This module is a unit test for the client module.
'''
import unittest
from unittest.mock import patch, PropertyMock
# from unittest.mock
from parameterized import parameterized
from client import GithubOrgClient, get_json
from typing import Dict, List


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
                   return_value={
                       "repos_url": "https://api.github.com/orgs/p/repos"
                   },
                   new_callable=PropertyMock) as mock_property_org:

            # create a new object
            client_obj = GithubOrgClient("p")

            # check if the mocked return value is the same
            self.assertEqual(client_obj._public_repos_url,
                             "https://api.github.com/orgs/p/repos")

    payload = [{
        "login": "ifeO",
        "id": 9173322,
        "url": "https://api.github.com/orgs/ifeO",
        "repos_url": "https://api.github.com/orgs/ifeO/repos",
        "name": "ifebusola",
        }]

    @patch('client.get_json', return_value=payload)
    def test_public_repos(self, mock_get):
        '''
        Testing the public_repos with the get_json method mocked and also
        the _public_repos_url method of the GithubOrgClient class.
        '''
        with patch('client.GithubOrgClient._public_repos_url',
                   return_value=mock_get["repos_url"],
                   new_callable=PropertyMock) as mock_pub_rep_url:
            client_obj = GithubOrgClient('ifeO')
            self.assertEqual(client_obj.public_repos(), ["ifebusola"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(
            self, repo, license_key, expected):
        """
        Testing if the repo has a licence key or not.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected)


# class TestIntegrationGithubOrgClient(unittest.TestCase):
#     """
# Testing with integration Testing with the fixtures in the fixtures module.
#     The only methods that would be mocked, are those that make
#     external requests.
#     """
#     pass
