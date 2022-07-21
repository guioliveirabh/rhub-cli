from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_openstack_project_create_json_body_id import RhubApiOpenstackProjectCreateJsonBodyId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackProjectCreateJsonBody")


@attr.s(auto_attribs=True)
class RhubApiOpenstackProjectCreateJsonBody:
    """
    Attributes:
        cloud_id (int):
        name (str):  Example: myproject.
        cloud_name (Union[Unset, str]):
        description (Union[Unset, None, str]):
        group_id (Union[Unset, None, str]):
        group_name (Union[Unset, None, str]):
        id (Union[Unset, RhubApiOpenstackProjectCreateJsonBodyId]):
        owner_id (Union[Unset, str]): Defaults to user who created a project.
        owner_name (Union[Unset, str]):
    """

    cloud_id: int
    name: str
    cloud_name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    group_id: Union[Unset, None, str] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    id: Union[Unset, RhubApiOpenstackProjectCreateJsonBodyId] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_id = self.cloud_id
        name = self.name
        cloud_name = self.cloud_name
        description = self.description
        group_id = self.group_id
        group_name = self.group_name
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        owner_id = self.owner_id
        owner_name = self.owner_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_id": cloud_id,
                "name": name,
            }
        )
        if cloud_name is not UNSET:
            field_dict["cloud_name"] = cloud_name
        if description is not UNSET:
            field_dict["description"] = description
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if id is not UNSET:
            field_dict["id"] = id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        cloud_id = d.pop("cloud_id")

        name = d.pop("name")

        cloud_name = d.pop("cloud_name", UNSET)

        description = d.pop("description", UNSET)

        group_id = d.pop("group_id", UNSET)

        group_name = d.pop("group_name", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiOpenstackProjectCreateJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiOpenstackProjectCreateJsonBodyId.from_dict(_id)

        owner_id = d.pop("owner_id", UNSET)

        owner_name = d.pop("owner_name", UNSET)

        rhub_api_openstack_project_create_json_body = cls(
            cloud_id=cloud_id,
            name=name,
            cloud_name=cloud_name,
            description=description,
            group_id=group_id,
            group_name=group_name,
            id=id,
            owner_id=owner_id,
            owner_name=owner_name,
        )

        rhub_api_openstack_project_create_json_body.additional_properties = d
        return rhub_api_openstack_project_create_json_body

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
