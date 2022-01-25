from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RhubapilabclusterupdateClusterResponse200HostsItemClusterId")


@attr.s(auto_attribs=True)
class RhubapilabclusterupdateClusterResponse200HostsItemClusterId:
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        rhubapilabclusterupdate_cluster_response_200_hosts_item_cluster_id = cls()

        rhubapilabclusterupdate_cluster_response_200_hosts_item_cluster_id.additional_properties = d
        return rhubapilabclusterupdate_cluster_response_200_hosts_item_cluster_id

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
