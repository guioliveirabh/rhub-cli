from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Optional
from typing import Union
from ..types import UNSET, Unset




T = TypeVar("T", bound="RhubapilabclusterlistClustersFilter")

@attr.s(auto_attribs=True)
class RhubapilabclusterlistClustersFilter:
    """  """
    group_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    region_id: Union[Unset, int] = UNSET
    shared: Union[Unset, bool] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        name = self.name
        region_id = self.region_id
        shared = self.shared
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if region_id is not UNSET:
            field_dict["region_id"] = region_id
        if shared is not UNSET:
            field_dict["shared"] = shared
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("group_id", UNSET)

        name = d.pop("name", UNSET)

        region_id = d.pop("region_id", UNSET)

        shared = d.pop("shared", UNSET)

        user_id = d.pop("user_id", UNSET)

        rhubapilabclusterlist_clusters_filter = cls(
            group_id=group_id,
            name=name,
            region_id=region_id,
            shared=shared,
            user_id=user_id,
        )

        rhubapilabclusterlist_clusters_filter.additional_properties = d
        return rhubapilabclusterlist_clusters_filter

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
