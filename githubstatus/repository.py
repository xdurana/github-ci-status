import logging
import json

import requests


class GithubRepository:
    def __init__(self, repo_name, access_token):
        self.repo_name = repo_name
        self.access_token = access_token

        self.github_base = "https://api.github.com"
        self.github_status_url = "{github_base}/repos/{repo_name}/statuses/{sha}?access_token={access_token}"
        self.github_combined_status_url = "{github_base}/repos/{repo_name}/commits/{sha}/status?access_token={access_token}"
        self.github_pull_request_url = "{github_base}/repos/{repo_name}/pulls?access_token={access_token}"

        self.pull_requests = self.get_pull_requests()
        self.get_pull_request_combined_status(self.pull_requests[0])

    def update_status(self, sha, state, desc=None, target_url=None):
        """Create commit statuses for a given SHA."""

        url = self.github_status_url.format(
            github_base=self.github_base, repo_name=self.repo_name, sha=sha, access_token=self.access_token
        )
        params = dict(state=state, description=desc)

        if target_url:
            params["target_url"] = target_url

        headers = {"Content-Type": "application/json"}

        logging.debug("Setting status on %s %s to %s", self.repo_name, sha, state)

        response = requests.post(url, data=json.dumps(params), headers=headers)
        if response.status_code != 201:
            raise requests.HTTPError(response.reason, response=self)

    def get_pull_requests(self):
        """List pull requests."""

        url = self.github_pull_request_url.format(
            github_base=self.github_base, repo_name=self.repo_name, access_token=self.access_token
        )
        logging.debug("Getting pull request list on %s", self.repo_name)

        response = requests.get(url)
        if response.status_code != 200:
            raise requests.HTTPError(response.reason, response=self)

        return response.json()

    def get_pull_request_combined_status(self, pull_request):
        """Get pull request combined status."""

        url = self.github_combined_status_url.format(
            github_base=self.github_base,
            repo_name=self.repo_name,
            sha=pull_request['head']['sha'],
            access_token=self.access_token
        )
        logging.debug("Getting combined status on pull request %s", pull_request['title'])

        response = requests.get(url)
        if response.status_code != 200:
            raise requests.HTTPError(response.reason, response=self)

        return response.json()
