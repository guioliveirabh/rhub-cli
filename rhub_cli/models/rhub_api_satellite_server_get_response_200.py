from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_satellite_server_get_response_200_credentials_type_0 import (
    RhubApiSatelliteServerGetResponse200CredentialsType0,
)
from ..models.rhub_api_satellite_server_get_response_200_id import RhubApiSatelliteServerGetResponse200Id
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiSatelliteServerGetResponse200")


@attr.s(auto_attribs=True)
class RhubApiSatelliteServerGetResponse200:
    """
    Attributes:
        credentials (Union[RhubApiSatelliteServerGetResponse200CredentialsType0, Unset, str]):
        description (Union[Unset, None, str]):  Example: Satellite server for RDU site..
        hostname (Union[Unset, str]):
        id (Union[Unset, RhubApiSatelliteServerGetResponse200Id]):
        insecure (Union[Unset, bool]):
        name (Union[Unset, str]):  Example: satellite-rdu.
        owner_group_id (Union[Unset, str]):
        owner_group_name (Union[Unset, str]):
    """

    credentials: Union[RhubApiSatelliteServerGetResponse200CredentialsType0, Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, RhubApiSatelliteServerGetResponse200Id] = UNSET
    insecure: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    owner_group_id: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Dict[str, Any], Unset, str]
        if isinstance(self.credentials, Unset):
            credentials = UNSET

        elif isinstance(self.credentials, RhubApiSatelliteServerGetResponse200CredentialsType0):
            credentials = UNSET
            if not isinstance(self.credentials, Unset):
                credentials = self.credentials.to_dict()

        else:
            credentials = self.credentials

        description = self.description
        hostname = self.hostname
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        insecure = self.insecure
        name = self.name
        owner_group_id = self.owner_group_id
        owner_group_name = self.owner_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if description is not UNSET:
            field_dict["description"] = description
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if insecure is not UNSET:
            field_dict["insecure"] = insecure
        if name is not UNSET:
            field_dict["name"] = name
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_credentials(data: object) -> Union[RhubApiSatelliteServerGetResponse200CredentialsType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _credentials_type_0 = data
                credentials_type_0: Union[Unset, RhubApiSatelliteServerGetResponse200CredentialsType0]
                if isinstance(_credentials_type_0, Unset):
                    credentials_type_0 = UNSET
                else:
                    credentials_type_0 = RhubApiSatelliteServerGetResponse200CredentialsType0.from_dict(
                        _credentials_type_0
                    )

                return credentials_type_0
            except:  # noqa: E722
                pass
            return cast(Union[RhubApiSatelliteServerGetResponse200CredentialsType0, Unset, str], data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        description = d.pop("description", UNSET)

        hostname = d.pop("hostname", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiSatelliteServerGetResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiSatelliteServerGetResponse200Id.from_dict(_id)

        insecure = d.pop("insecure", UNSET)

        name = d.pop("name", UNSET)

        owner_group_id = d.pop("owner_group_id", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        rhub_api_satellite_server_get_response_200 = cls(
            credentials=credentials,
            description=description,
            hostname=hostname,
            id=id,
            insecure=insecure,
            name=name,
            owner_group_id=owner_group_id,
            owner_group_name=owner_group_name,
        )

        rhub_api_satellite_server_get_response_200.additional_properties = d
        return rhub_api_satellite_server_get_response_200

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
