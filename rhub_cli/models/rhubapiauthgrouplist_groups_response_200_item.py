from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapiauthgrouplist_groups_response_200_item_attributes import (
    RhubapiauthgrouplistGroupsResponse200ItemAttributes,
)
from ..models.rhubapiauthgrouplist_groups_response_200_item_id import RhubapiauthgrouplistGroupsResponse200ItemId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapiauthgrouplistGroupsResponse200Item")


@attr.s(auto_attribs=True)
class RhubapiauthgrouplistGroupsResponse200Item:
    """See [Keycloak API: GroupRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
    """

    attributes: Union[Unset, RhubapiauthgrouplistGroupsResponse200ItemAttributes] = UNSET
    id: Union[Unset, RhubapiauthgrouplistGroupsResponse200ItemId] = UNSET
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
        d = copy(src_dict)  # TODO: find the bug
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, RhubapiauthgrouplistGroupsResponse200ItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RhubapiauthgrouplistGroupsResponse200ItemAttributes.from_dict(_attributes)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthgrouplistGroupsResponse200ItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapiauthgrouplistGroupsResponse200ItemId.from_dict(_id)

        name = d.pop("name", UNSET)

        rhubapiauthgrouplist_groups_response_200_item = cls(
            attributes=attributes,
            id=id,
            name=name,
        )

        rhubapiauthgrouplist_groups_response_200_item.additional_properties = d
        return rhubapiauthgrouplist_groups_response_200_item

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
