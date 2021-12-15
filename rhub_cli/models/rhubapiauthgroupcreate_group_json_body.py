from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapiauthgroupcreate_group_json_body_attributes import RhubapiauthgroupcreateGroupJsonBodyAttributes
from ..models.rhubapiauthgroupcreate_group_json_body_id import RhubapiauthgroupcreateGroupJsonBodyId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapiauthgroupcreateGroupJsonBody")


@attr.s(auto_attribs=True)
class RhubapiauthgroupcreateGroupJsonBody:
    """ """

    name: str
    attributes: Union[Unset, RhubapiauthgroupcreateGroupJsonBodyAttributes] = UNSET
    id: Union[Unset, RhubapiauthgroupcreateGroupJsonBodyId] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, RhubapiauthgroupcreateGroupJsonBodyAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RhubapiauthgroupcreateGroupJsonBodyAttributes.from_dict(_attributes)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthgroupcreateGroupJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapiauthgroupcreateGroupJsonBodyId.from_dict(_id)

        rhubapiauthgroupcreate_group_json_body = cls(
            name=name,
            attributes=attributes,
            id=id,
        )

        rhubapiauthgroupcreate_group_json_body.additional_properties = d
        return rhubapiauthgroupcreate_group_json_body

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
