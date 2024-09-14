#!/usr/bin/env python3
"""Test cases for the file client.py"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


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

    def test_public_repos_url(self):
        """Test the _public_repos_url method of GithubOrgClient"""
        client = GithubOrgClient("google")

        # Check if the result is the mocked return value
        self.assertEqual(client._public_repos_url, client.org["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method"""
        # Mocked payload for the get_json method
        mocked_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}}
        ]
        
        # Mock the return value of get_json
        mock_get_json.return_value = mocked_repos_payload

        # Mock the _public_repos_url to return a fixed URL
        with patch('client.GithubOrgClient._public_repos_url', new_callable=property) as mock_repos_url:
            mock_repos_url.return_value = "https://api.github.com/orgs/test-org/repos"

            # Initialize the GithubOrgClient with an org name
            client = GithubOrgClient("test-org")

            # Call the public_repos method
            result = client.public_repos()

            # Expected list of public repo names
            expected_repos = ["repo1", "repo2", "repo3"]

            # Assert that the result is what we expect
            self.assertEqual(result, expected_repos)

            # Assert that _public_repos_url was called once
            mock_repos_url.assert_called_once()

            # Assert that get_json was called once with the mocked URL
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test-org/repos")

if __name__ == '__main__':
    unittest.main()
