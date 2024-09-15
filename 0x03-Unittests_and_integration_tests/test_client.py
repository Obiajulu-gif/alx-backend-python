#!/usr/bin/env python3
"""Test cases for the file client.py"""
from client import GithubOrgClient

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient"""
        client = GithubOrgClient(org_name)

        mock_get_json.return_value = {"test": "value"}

        result = client.org

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name))

        # Check if the result is the mocked return value
        self.assertEqual(result, {"test": "value"})

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient"""
        payload = [
            {"name": "Google"},
            {"name": "Twitter"}
        ]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = \
                "https://api.github.com/orgs/google/repos"
            client = GithubOrgClient("google")
            result = client.public_repos()

            # Check if the result is the list of repo names
            check = [i["name"] for i in payload]
            self.assertEqual(result, check)

            # Check if the mocked property and the mocked get_json were called
            # once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method of GithubOrgClient"""
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([{"org_payload": org_payload,
                       "repos_payload": repos_payload,
                       "expected_repos": expected_repos,
                       "apache2_repos": apache2_repos}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return MockResponse(cls.org_payload, status_code=200)
            elif url == "https://api.github.com/orgs/google/repos":
                return MockResponse(cls.repos_payload, status_code=200)
            return MockResponse(None, status_code=404)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method of GithubOrgClient"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with license filtering"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(
                license="apache-2.0"),
            self.apache2_repos)


class MockResponse:
    """Mock response class for requests.get"""

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


if __name__ == '__main__':
    unittest.main()
