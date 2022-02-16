import click
import httpx

from .client import AuthenticatedClient, Client
from .types import Response


class APIRequest:
    # this class should be re-written for each CLI
    TIMEOUT = 5.0
    VERIFY_SSL = False

    def __init__(self, base_url: str, user: str, password: str, verbose: bool):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.verbose = verbose

        self.client = self._get_client()
        self.authenticated_client = self._get_authenticated_client()

    def _get_client(self) -> Client:
        return Client(base_url=self.base_url, timeout=self.TIMEOUT, verify_ssl=self.VERIFY_SSL)

    def _get_authenticated_client(self) -> AuthenticatedClient:
        # Needs further implementation
        response = httpx.post(
            url=f"{self.base_url}/auth/token/create",
            verify=self.VERIFY_SSL,
            auth=(self.user, self.password),
        )

        return AuthenticatedClient(
            base_url=self.base_url,
            token=response.json()["access_token"],
            timeout=self.TIMEOUT,
            verify_ssl=self.VERIFY_SSL,
        )

    @classmethod
    def handle_response(cls, response: Response):
        if response.status_code == 200 and response.parsed:
            click.echo(response.parsed)
        else:
            click.echo(response)


pass_api = click.make_pass_decorator(APIRequest, ensure=True)
