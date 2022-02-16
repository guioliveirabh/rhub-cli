from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiAuthUserCreateUserResponse200")


@attr.s(auto_attribs=True)
class RhubApiAuthUserCreateUserResponse200:
    """
    Attributes:
        email (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        password (Union[Unset, str]):
        username (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        enabled = self.enabled
        first_name = self.first_name
        last_name = self.last_name
        password = self.password
        username = self.username
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        id = d.pop("id", UNSET)

        rhub_api_auth_user_create_user_response_200 = cls(
            email=email,
            enabled=enabled,
            first_name=first_name,
            last_name=last_name,
            password=password,
            username=username,
            id=id,
        )

        rhub_api_auth_user_create_user_response_200.additional_properties = d
        return rhub_api_auth_user_create_user_response_200

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
