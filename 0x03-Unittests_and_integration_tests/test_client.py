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


if __name__ == '__main__':
    unittest.main()
