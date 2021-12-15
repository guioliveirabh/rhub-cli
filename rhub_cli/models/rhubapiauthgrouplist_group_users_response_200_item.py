from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapiauthgrouplist_group_users_response_200_item_id import (
    RhubapiauthgrouplistGroupUsersResponse200ItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapiauthgrouplistGroupUsersResponse200Item")


@attr.s(auto_attribs=True)
class RhubapiauthgrouplistGroupUsersResponse200Item:
    """See [Keycloak API: UserRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
    """

    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, RhubapiauthgrouplistGroupUsersResponse200ItemId] = UNSET
    last_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        enabled = self.enabled
        first_name = self.first_name
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        last_name = self.last_name
        password = self.password
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        first_name = d.pop("firstName", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthgrouplistGroupUsersResponse200ItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapiauthgrouplistGroupUsersResponse200ItemId.from_dict(_id)

        last_name = d.pop("lastName", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        rhubapiauthgrouplist_group_users_response_200_item = cls(
            email=email,
            enabled=enabled,
            first_name=first_name,
            id=id,
            last_name=last_name,
            password=password,
            username=username,
        )

        rhubapiauthgrouplist_group_users_response_200_item.additional_properties = d
        return rhubapiauthgrouplist_group_users_response_200_item

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
