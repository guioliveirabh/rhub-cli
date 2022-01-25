from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapiauthuserget_current_user_response_200_id import RhubapiauthusergetCurrentUserResponse200Id
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapiauthusergetCurrentUserResponse200")


@attr.s(auto_attribs=True)
class RhubapiauthusergetCurrentUserResponse200:
    """See [Keycloak API: UserRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

      Example:
          {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True, 'mapRoles': True, 'view': True},
              'createdTimestamp': 1614717256570, 'disableableCredentialTypes': [], 'email': 'testuser1@example.com',
              'emailVerified': False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
              'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username': 'testuser1'}

      Attributes:
          email (Union[Unset, str]):
          enabled (Union[Unset, bool]):
          first_name (Union[Unset, str]):
          id (Union[Unset, RhubapiauthusergetCurrentUserResponse200Id]):
          last_name (Union[Unset, str]):
          password (Union[Unset, str]):
          username (Union[Unset, str]):
    """

    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, RhubapiauthusergetCurrentUserResponse200Id] = UNSET
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
        d = copy(src_dict)
        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        first_name = d.pop("firstName", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthusergetCurrentUserResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapiauthusergetCurrentUserResponse200Id.from_dict(_id)

        last_name = d.pop("lastName", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        rhubapiauthuserget_current_user_response_200 = cls(
            email=email,
            enabled=enabled,
            first_name=first_name,
            id=id,
            last_name=last_name,
            password=password,
            username=username,
        )

        rhubapiauthuserget_current_user_response_200.additional_properties = d
        return rhubapiauthuserget_current_user_response_200

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
