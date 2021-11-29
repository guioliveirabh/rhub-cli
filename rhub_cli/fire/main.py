import abc

import fire

from rhub_cli.fire.api_request import APIRequest


class BaseCommand(abc.ABC):
    def __init__(self, api: APIRequest):
        self._api = api


class CowSay(BaseCommand):
    """Cows the API."""

    def get(self):
        """Cows the API."""
        return self._api.get('cowsay')


class Ping(BaseCommand):
    """Pings the API."""

    def get(self):
        """Pings the API."""
        return self._api.get('ping')


class Policy(BaseCommand):
    """Handles policy API."""

    def create(self, name: str, department: str):
        """Creates a policy"""
        return self._api.post('policies', {'name': name, 'department': department})

    def get(self, policy_id: int = None):
        """Gets a policy details"""
        end_point = 'policies'
        if policy_id is not None:
            end_point += f"/{policy_id}"
        return self._api.get(end_point)

    def update(self, policy_id: int, name: str = None, department: str = None):
        """Updates a policy"""
        data = {}
        if name:
            data['name'] = name
        if department:
            data['department'] = department
        if not data:
            raise RuntimeError('Fill the fields')  # TODO

        return self._api.patch(f"policies/{policy_id}", data)

    def remove(self, policy_id: int):
        """Removes a policy"""
        return self._api.delete(f"policies/{policy_id}")


class CLI:
    """CLI example using Python Fire - https://github.com/google/python-fire"""

    def __init__(self, base_url='http://localhost:8081/v0'):
        api = APIRequest(base_url)
        self.cowsay = CowSay(api)
        self.ping = Ping(api)
        self.policies = Policy(api)


def main():
    fire.Fire(CLI)
