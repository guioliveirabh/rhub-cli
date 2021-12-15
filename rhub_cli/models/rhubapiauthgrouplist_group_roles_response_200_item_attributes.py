from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="RhubapiauthgrouplistGroupRolesResponse200ItemAttributes")


@attr.s(auto_attribs=True)
class RhubapiauthgrouplistGroupRolesResponse200ItemAttributes:
    """Role attributes"""

    additional_properties: Dict[str, List[str]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rhubapiauthgrouplist_group_roles_response_200_item_attributes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(List[str], prop_dict)

            additional_properties[prop_name] = additional_property

        rhubapiauthgrouplist_group_roles_response_200_item_attributes.additional_properties = additional_properties
        return rhubapiauthgrouplist_group_roles_response_200_item_attributes

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
