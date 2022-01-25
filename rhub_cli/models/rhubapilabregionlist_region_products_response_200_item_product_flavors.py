from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rhubapilabregionlist_region_products_response_200_item_product_flavors_additional_property import (
    RhubapilabregionlistRegionProductsResponse200ItemProductFlavorsAdditionalProperty,
)

T = TypeVar("T", bound="RhubapilabregionlistRegionProductsResponse200ItemProductFlavors")


@attr.s(auto_attribs=True)
class RhubapilabregionlistRegionProductsResponse200ItemProductFlavors:
    """ """

    additional_properties: Dict[
        str, RhubapilabregionlistRegionProductsResponse200ItemProductFlavorsAdditionalProperty
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        rhubapilabregionlist_region_products_response_200_item_product_flavors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                RhubapilabregionlistRegionProductsResponse200ItemProductFlavorsAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        rhubapilabregionlist_region_products_response_200_item_product_flavors.additional_properties = (
            additional_properties
        )
        return rhubapilabregionlist_region_products_response_200_item_product_flavors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> RhubapilabregionlistRegionProductsResponse200ItemProductFlavorsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: RhubapilabregionlistRegionProductsResponse200ItemProductFlavorsAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
