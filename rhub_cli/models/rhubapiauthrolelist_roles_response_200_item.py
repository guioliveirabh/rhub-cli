from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapiauthrolelist_roles_response_200_item_attributes import (
    RhubapiauthrolelistRolesResponse200ItemAttributes,
)
from ..models.rhubapiauthrolelist_roles_response_200_item_id import RhubapiauthrolelistRolesResponse200ItemId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapiauthrolelistRolesResponse200Item")


@attr.s(auto_attribs=True)
class RhubapiauthrolelistRolesResponse200Item:
    """See [Keycloak API: RoleRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
    """

    attributes: Union[Unset, RhubapiauthrolelistRolesResponse200ItemAttributes] = UNSET
    id: Union[Unset, RhubapiauthrolelistRolesResponse200ItemId] = UNSET
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
        d = src_dict.copy()
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, RhubapiauthrolelistRolesResponse200ItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RhubapiauthrolelistRolesResponse200ItemAttributes.from_dict(_attributes)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthrolelistRolesResponse200ItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapiauthrolelistRolesResponse200ItemId.from_dict(_id)

        name = d.pop("name", UNSET)

        rhubapiauthrolelist_roles_response_200_item = cls(
            attributes=attributes,
            id=id,
            name=name,
        )

        rhubapiauthrolelist_roles_response_200_item.additional_properties = d
        return rhubapiauthrolelist_roles_response_200_item

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
