from enum import Enum, auto

import click
import requests


class HandleResponse(Enum):
    PRINT_STDOUT = auto()


class APIRequest:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

        self._set_token()

    def get_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint}"

    def _set_token(self):
        # Needs further implementation
        response = self.session.post(self.get_url('auth/token/create'), auth=('testuser1', 'testuser1'))
        self.token = response.json()['access_token']

    def get_token_header(self):
        return {'Authorization': f"Bearer {self.token}"}

    def delete(self, end_point: str, handle_response: HandleResponse = HandleResponse.PRINT_STDOUT):
        response = self.session.delete(self.get_url(end_point), headers=self.get_token_header())
        self.handle_response(response, handle_response)

    def get(self, end_point: str, handle_response: HandleResponse = HandleResponse.PRINT_STDOUT):
        response = self.session.get(self.get_url(end_point), headers=self.get_token_header())
        self.handle_response(response, handle_response)

    def patch(self, end_point: str, data: dict, handle_response: HandleResponse = HandleResponse.PRINT_STDOUT):
        response = self.session.patch(self.get_url(end_point), json=data, headers=self.get_token_header())
        self.handle_response(response, handle_response)

    def post(self, end_point: str, data: dict, handle_response: HandleResponse = HandleResponse.PRINT_STDOUT):
        response = self.session.post(self.get_url(end_point), json=data, headers=self.get_token_header())
        self.handle_response(response, handle_response)

    @classmethod
    def handle_response(cls, response: requests.Response, handle_method: HandleResponse):
        if handle_method is HandleResponse.PRINT_STDOUT:
            click.echo(response.text)


pass_api = click.make_pass_decorator(APIRequest, ensure=True)
