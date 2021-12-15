from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.rhubapitowerget_server_response_200_id import RhubapitowergetServerResponse200Id
from typing import cast
from typing import Union
from ..types import UNSET, Unset
from typing import Dict




T = TypeVar("T", bound="RhubapitowergetServerResponse200")

@attr.s(auto_attribs=True)
class RhubapitowergetServerResponse200:
    """  """
    credentials: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, RhubapitowergetServerResponse200Id] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    verify_ssl: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        credentials = self.credentials
        description = self.description
        enabled = self.enabled
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name
        url = self.url
        verify_ssl = self.verify_ssl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if verify_ssl is not UNSET:
            field_dict["verify_ssl"] = verify_ssl

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credentials = d.pop("credentials", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapitowergetServerResponse200Id]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = RhubapitowergetServerResponse200Id.from_dict(_id)




        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        verify_ssl = d.pop("verify_ssl", UNSET)

        rhubapitowerget_server_response_200 = cls(
            credentials=credentials,
            description=description,
            enabled=enabled,
            id=id,
            name=name,
            url=url,
            verify_ssl=verify_ssl,
        )

        rhubapitowerget_server_response_200.additional_properties = d
        return rhubapitowerget_server_response_200

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
