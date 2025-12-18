#!/usr/bin/env python3
"""file contening the tests for client.py file"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, PropertyMock, patch
from client import GithubOrgClient
try:
    from fixtures import org_payload, repos_payload
    from fixtures import expected_repos, apache2_repos
except ImportError:
    org_payload = {"repos_url": "https://api.github.com/orgs/test/repos"}
    repos_payload = [{"name": "repo1"}, {"name": "repo2"}]
    expected_repos = ["repo1", "repo2"]
    apache2_repos = ["repo1"]


class TestGithubOrgClient(unittest.TestCase):
    """class contening the tests of GithubOrgClient.org"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_result = {"name": org_name, "id": 12345}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        result = client.org
        expected_url = f"https: //api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, expected_result)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected URL"""
        known_payload = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = known_payload
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, known_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repos"""
        repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = repos_payload
        expected_repos = ["repo1", "repo2", "repo3"]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_repos_url:
            test_repos_url = "https://api.github.com/orgs/test-org/repos"
            mock_repos_url.return_value = test_repos_url
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            self.assertEqual(result, expected_repos)
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_repos_url)

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected boolean value"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
        "TEST_PAYLOAD": "test_payload"
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """class contening the integration test of GithubOrgClient.org"""
    @classmethod
    def setUpClass(cls):
        """Set up class method to start patching requests.get"""

        def side_effect_function(url):
            """Side effect function to return
            appropriate fixtures based on URL"""
            mock_response = Mock()

            if url == "https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload.get("repos_url"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = {}

            return mock_response

        cls.get_patcher = patch('requests.get',
                                side_effect=side_effect_function)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patching requests.get"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
