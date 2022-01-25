from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapiauthgroupget_group_response_200_attributes import RhubapiauthgroupgetGroupResponse200Attributes
from ..models.rhubapiauthgroupget_group_response_200_id import RhubapiauthgroupgetGroupResponse200Id
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapiauthgroupgetGroupResponse200")


@attr.s(auto_attribs=True)
class RhubapiauthgroupgetGroupResponse200:
    """See [Keycloak API: GroupRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

        Example:
            {'access': {'manage': True, 'manageMembership': True, 'view': True}, 'attributes': {'mailing-list': ['admin-
                list@example.com']}, 'clientRoles': {}, 'id': 'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path':
                '/admin', 'realmRoles': [], 'subGroups': []}

        Attributes:
            attributes (Union[Unset, RhubapiauthgroupgetGroupResponse200Attributes]): Group attributes
            id (Union[Unset, RhubapiauthgroupgetGroupResponse200Id]):
            name (Union[Unset, str]):
    """

    attributes: Union[Unset, RhubapiauthgroupgetGroupResponse200Attributes] = UNSET
    id: Union[Unset, RhubapiauthgroupgetGroupResponse200Id] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, RhubapiauthgroupgetGroupResponse200Attributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RhubapiauthgroupgetGroupResponse200Attributes.from_dict(_attributes)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthgroupgetGroupResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapiauthgroupgetGroupResponse200Id.from_dict(_id)

        name = d.pop("name", UNSET)

        rhubapiauthgroupget_group_response_200 = cls(
            attributes=attributes,
            id=id,
            name=name,
        )

        rhubapiauthgroupget_group_response_200.additional_properties = d
        return rhubapiauthgroupget_group_response_200

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
