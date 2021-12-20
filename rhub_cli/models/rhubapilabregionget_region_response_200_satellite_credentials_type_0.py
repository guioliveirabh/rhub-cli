from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabregiongetRegionResponse200SatelliteCredentialsType0")


@attr.s(auto_attribs=True)
class RhubapilabregiongetRegionResponse200SatelliteCredentialsType0:
    """Credentials to store in Vault"""

    password: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)  # TODO: find the bug
        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        rhubapilabregionget_region_response_200_satellite_credentials_type_0 = cls(
            password=password,
            username=username,
        )

        rhubapilabregionget_region_response_200_satellite_credentials_type_0.additional_properties = d
        return rhubapilabregionget_region_response_200_satellite_credentials_type_0

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
