from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapiauthroleupdate_role_response_200_attributes import RhubapiauthroleupdateRoleResponse200Attributes
from ..models.rhubapiauthroleupdate_role_response_200_id import RhubapiauthroleupdateRoleResponse200Id
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapiauthroleupdateRoleResponse200")


@attr.s(auto_attribs=True)
class RhubapiauthroleupdateRoleResponse200:
    """See [Keycloak API: RoleRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
    """

    attributes: Union[Unset, RhubapiauthroleupdateRoleResponse200Attributes] = UNSET
    id: Union[Unset, RhubapiauthroleupdateRoleResponse200Id] = UNSET
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
        attributes: Union[Unset, RhubapiauthroleupdateRoleResponse200Attributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RhubapiauthroleupdateRoleResponse200Attributes.from_dict(_attributes)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthroleupdateRoleResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapiauthroleupdateRoleResponse200Id.from_dict(_id)

        name = d.pop("name", UNSET)

        rhubapiauthroleupdate_role_response_200 = cls(
            attributes=attributes,
            id=id,
            name=name,
        )

        rhubapiauthroleupdate_role_response_200.additional_properties = d
        return rhubapiauthroleupdate_role_response_200

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
