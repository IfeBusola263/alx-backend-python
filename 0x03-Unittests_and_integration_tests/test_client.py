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
        mock_get_json.return_value = {
                "url": "https://api.github.com/orgs/{}".format(org)
        }
        # {"name": org}
        test = GithubOrgClient(org)
        url = "https://api.github.com/orgs/{}".format(org)
        # self.assertEqual(test.org, {"name": org})
        self.assertIsInstance(test.org, dict)
        mock_get_json.assert_called_once_with(url)

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
                   return_value="https://api.github.com/orgs/ifeO/repos",
                   new_callable=PropertyMock) as mock_pub_rep_url:
            client_obj = GithubOrgClient('ifeO')
            self.assertEqual(client_obj.public_repos(), ["ifebusola"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected):
        """
        Testing if the repo has a licence key or not.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

# @parameterized_class(
#     ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),[
#         (,,,,),
#         (,,,,),
#         ])
# class TestIntegrationGithubOrgClient(unittest.TestCase):
#     '''
#     Testing public_repos method in clients module
#     in an integration sense. The only code to be mocked
#     are those sending external requests.
#     '''
#     def setUpClass(cls):
#         """
#         Method to run one when each test in the class runs.
#         """
#         self.get_patcher = patch('requests.get')
#         self.get_patcher.start()
#     def tearDownClass(cls):
#         """
#         The final method that runs after all the test is completed.
#         """
#         self.get_patcher.stop()
