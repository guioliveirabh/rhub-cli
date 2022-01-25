from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rhubapilabproductupdate_product_json_body_flavors_additional_property import (
    RhubapilabproductupdateProductJsonBodyFlavorsAdditionalProperty,
)

T = TypeVar("T", bound="RhubapilabproductupdateProductJsonBodyFlavors")


@attr.s(auto_attribs=True)
class RhubapilabproductupdateProductJsonBodyFlavors:
    """ """

    additional_properties: Dict[str, RhubapilabproductupdateProductJsonBodyFlavorsAdditionalProperty] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        rhubapilabproductupdate_product_json_body_flavors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RhubapilabproductupdateProductJsonBodyFlavorsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        rhubapilabproductupdate_product_json_body_flavors.additional_properties = additional_properties
        return rhubapilabproductupdate_product_json_body_flavors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RhubapilabproductupdateProductJsonBodyFlavorsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RhubapilabproductupdateProductJsonBodyFlavorsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
