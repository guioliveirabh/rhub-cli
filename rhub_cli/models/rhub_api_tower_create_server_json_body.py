from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerCreateServerJsonBody")


@attr.s(auto_attribs=True)
class RhubApiTowerCreateServerJsonBody:
    """
    Attributes:
        credentials (str): Tower credentials path (Vault mount/path)
        name (str):
        url (str):
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        verify_ssl (Union[Unset, bool]): Option to disable SSL certificate verification.
    """

    credentials: str
    name: str
    url: str
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    verify_ssl: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials = self.credentials
        name = self.name
        url = self.url
        description = self.description
        enabled = self.enabled
        verify_ssl = self.verify_ssl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "name": name,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if verify_ssl is not UNSET:
            field_dict["verify_ssl"] = verify_ssl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        credentials = d.pop("credentials")

        name = d.pop("name")

        url = d.pop("url")

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        verify_ssl = d.pop("verify_ssl", UNSET)

        rhub_api_tower_create_server_json_body = cls(
            credentials=credentials,
            name=name,
            url=url,
            description=description,
            enabled=enabled,
            verify_ssl=verify_ssl,
        )

        rhub_api_tower_create_server_json_body.additional_properties = d
        return rhub_api_tower_create_server_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
