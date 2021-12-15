from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabproductlist_product_regions_response_200_item_region import (
    RhubapilabproductlistProductRegionsResponse200ItemRegion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabproductlistProductRegionsResponse200Item")


@attr.s(auto_attribs=True)
class RhubapilabproductlistProductRegionsResponse200Item:
    """ """

    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    region: Union[Unset, RhubapilabproductlistProductRegionsResponse200ItemRegion] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        id = self.id
        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, RhubapilabproductlistProductRegionsResponse200ItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = RhubapilabproductlistProductRegionsResponse200ItemRegion.from_dict(_region)

        rhubapilabproductlist_product_regions_response_200_item = cls(
            enabled=enabled,
            id=id,
            region=region,
        )

        rhubapilabproductlist_product_regions_response_200_item.additional_properties = d
        return rhubapilabproductlist_product_regions_response_200_item

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
