from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rhubapilabproductget_product_response_200_flavors_additional_property import (
    RhubapilabproductgetProductResponse200FlavorsAdditionalProperty,
)

T = TypeVar("T", bound="RhubapilabproductgetProductResponse200Flavors")


@attr.s(auto_attribs=True)
class RhubapilabproductgetProductResponse200Flavors:
    """ """

    additional_properties: Dict[str, RhubapilabproductgetProductResponse200FlavorsAdditionalProperty] = attr.ib(
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
        rhubapilabproductget_product_response_200_flavors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RhubapilabproductgetProductResponse200FlavorsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        rhubapilabproductget_product_response_200_flavors.additional_properties = additional_properties
        return rhubapilabproductget_product_response_200_flavors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RhubapilabproductgetProductResponse200FlavorsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RhubapilabproductgetProductResponse200FlavorsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
