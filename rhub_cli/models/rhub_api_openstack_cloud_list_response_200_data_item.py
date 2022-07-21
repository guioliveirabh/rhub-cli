from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_openstack_cloud_list_response_200_data_item_credentials_type_0 import (
    RhubApiOpenstackCloudListResponse200DataItemCredentialsType0,
)
from ..models.rhub_api_openstack_cloud_list_response_200_data_item_id import (
    RhubApiOpenstackCloudListResponse200DataItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackCloudListResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiOpenstackCloudListResponse200DataItem:
    """
    Attributes:
        credentials (Union[RhubApiOpenstackCloudListResponse200DataItemCredentialsType0, Unset, str]):  Example:
            kv/openstack/rhub-rdu.
        description (Union[Unset, None, str]):  Example: Private cloud for RHub located in RDU..
        domain_id (Union[Unset, str]):  Example: default.
        domain_name (Union[Unset, str]):  Example: Default.
        id (Union[Unset, RhubApiOpenstackCloudListResponse200DataItemId]):
        name (Union[Unset, str]):  Example: rhub-rdu.
        networks (Union[Unset, List[str]]): Network providers that can be used in the cloud Example:
            ['provider_net_rhub'].
        owner_group_id (Union[Unset, str]):
        owner_group_name (Union[Unset, str]):
        url (Union[Unset, str]):  Example: https://rhub-cloud.rdu.example.com:13000.
    """

    credentials: Union[RhubApiOpenstackCloudListResponse200DataItemCredentialsType0, Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    domain_id: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    id: Union[Unset, RhubApiOpenstackCloudListResponse200DataItemId] = UNSET
    name: Union[Unset, str] = UNSET
    networks: Union[Unset, List[str]] = UNSET
    owner_group_id: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Dict[str, Any], Unset, str]
        if isinstance(self.credentials, Unset):
            credentials = UNSET

        elif isinstance(self.credentials, RhubApiOpenstackCloudListResponse200DataItemCredentialsType0):
            credentials = UNSET
            if not isinstance(self.credentials, Unset):
                credentials = self.credentials.to_dict()

        else:
            credentials = self.credentials

        description = self.description
        domain_id = self.domain_id
        domain_name = self.domain_name
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name
        networks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = self.networks

        owner_group_id = self.owner_group_id
        owner_group_name = self.owner_group_name
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if description is not UNSET:
            field_dict["description"] = description
        if domain_id is not UNSET:
            field_dict["domain_id"] = domain_id
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if networks is not UNSET:
            field_dict["networks"] = networks
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_credentials(
            data: object,
        ) -> Union[RhubApiOpenstackCloudListResponse200DataItemCredentialsType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _credentials_type_0 = data
                credentials_type_0: Union[Unset, RhubApiOpenstackCloudListResponse200DataItemCredentialsType0]
                if isinstance(_credentials_type_0, Unset):
                    credentials_type_0 = UNSET
                else:
                    credentials_type_0 = RhubApiOpenstackCloudListResponse200DataItemCredentialsType0.from_dict(
                        _credentials_type_0
                    )

                return credentials_type_0
            except:  # noqa: E722
                pass
            return cast(Union[RhubApiOpenstackCloudListResponse200DataItemCredentialsType0, Unset, str], data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        description = d.pop("description", UNSET)

        domain_id = d.pop("domain_id", UNSET)

        domain_name = d.pop("domain_name", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiOpenstackCloudListResponse200DataItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiOpenstackCloudListResponse200DataItemId.from_dict(_id)

        name = d.pop("name", UNSET)

        networks = cast(List[str], d.pop("networks", UNSET))

        owner_group_id = d.pop("owner_group_id", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        url = d.pop("url", UNSET)

        rhub_api_openstack_cloud_list_response_200_data_item = cls(
            credentials=credentials,
            description=description,
            domain_id=domain_id,
            domain_name=domain_name,
            id=id,
            name=name,
            networks=networks,
            owner_group_id=owner_group_id,
            owner_group_name=owner_group_name,
            url=url,
        )

        rhub_api_openstack_cloud_list_response_200_data_item.additional_properties = d
        return rhub_api_openstack_cloud_list_response_200_data_item

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
