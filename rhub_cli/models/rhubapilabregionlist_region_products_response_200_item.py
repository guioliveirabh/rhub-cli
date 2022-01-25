from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabregionlist_region_products_response_200_item_product import (
    RhubapilabregionlistRegionProductsResponse200ItemProduct,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabregionlistRegionProductsResponse200Item")


@attr.s(auto_attribs=True)
class RhubapilabregionlistRegionProductsResponse200Item:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        id (Union[Unset, int]):
        product (Union[Unset, RhubapilabregionlistRegionProductsResponse200ItemProduct]):
    """

    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    product: Union[Unset, RhubapilabregionlistRegionProductsResponse200ItemProduct] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        id = self.id
        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, RhubapilabregionlistRegionProductsResponse200ItemProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = RhubapilabregionlistRegionProductsResponse200ItemProduct.from_dict(_product)

        rhubapilabregionlist_region_products_response_200_item = cls(
            enabled=enabled,
            id=id,
            product=product,
        )

        rhubapilabregionlist_region_products_response_200_item.additional_properties = d
        return rhubapilabregionlist_region_products_response_200_item

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
