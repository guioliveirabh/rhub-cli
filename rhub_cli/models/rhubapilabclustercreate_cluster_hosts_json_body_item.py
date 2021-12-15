from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhubapilabclustercreate_cluster_hosts_json_body_item_cluster_id import (
    RhubapilabclustercreateClusterHostsJsonBodyItemClusterId,
)
from ..models.rhubapilabclustercreate_cluster_hosts_json_body_item_id import (
    RhubapilabclustercreateClusterHostsJsonBodyItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabclustercreateClusterHostsJsonBodyItem")


@attr.s(auto_attribs=True)
class RhubapilabclustercreateClusterHostsJsonBodyItem:
    """ """

    fqdn: str
    ipaddr: List[str]
    cluster_id: Union[Unset, RhubapilabclustercreateClusterHostsJsonBodyItemClusterId] = UNSET
    id: Union[Unset, RhubapilabclustercreateClusterHostsJsonBodyItemId] = UNSET
    num_vcpus: Union[Unset, None, int] = UNSET
    num_volumes: Union[Unset, None, int] = UNSET
    ram_mb: Union[Unset, None, int] = UNSET
    volumes_gb: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fqdn = self.fqdn
        ipaddr = []
        for ipaddr_item_data in self.ipaddr:
            ipaddr_item = ipaddr_item_data

            ipaddr.append(ipaddr_item)

        cluster_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_id, Unset):
            cluster_id = self.cluster_id.to_dict()

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        num_vcpus = self.num_vcpus
        num_volumes = self.num_volumes
        ram_mb = self.ram_mb
        volumes_gb = self.volumes_gb

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fqdn": fqdn,
                "ipaddr": ipaddr,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if id is not UNSET:
            field_dict["id"] = id
        if num_vcpus is not UNSET:
            field_dict["num_vcpus"] = num_vcpus
        if num_volumes is not UNSET:
            field_dict["num_volumes"] = num_volumes
        if ram_mb is not UNSET:
            field_dict["ram_mb"] = ram_mb
        if volumes_gb is not UNSET:
            field_dict["volumes_gb"] = volumes_gb

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fqdn = d.pop("fqdn")

        ipaddr = []
        _ipaddr = d.pop("ipaddr")
        for ipaddr_item_data in _ipaddr:

            def _parse_ipaddr_item(data: object) -> str:
                return cast(str, data)

            ipaddr_item = _parse_ipaddr_item(ipaddr_item_data)

            ipaddr.append(ipaddr_item)

        _cluster_id = d.pop("cluster_id", UNSET)
        cluster_id: Union[Unset, RhubapilabclustercreateClusterHostsJsonBodyItemClusterId]
        if isinstance(_cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = RhubapilabclustercreateClusterHostsJsonBodyItemClusterId.from_dict(_cluster_id)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabclustercreateClusterHostsJsonBodyItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapilabclustercreateClusterHostsJsonBodyItemId.from_dict(_id)

        num_vcpus = d.pop("num_vcpus", UNSET)

        num_volumes = d.pop("num_volumes", UNSET)

        ram_mb = d.pop("ram_mb", UNSET)

        volumes_gb = d.pop("volumes_gb", UNSET)

        rhubapilabclustercreate_cluster_hosts_json_body_item = cls(
            fqdn=fqdn,
            ipaddr=ipaddr,
            cluster_id=cluster_id,
            id=id,
            num_vcpus=num_vcpus,
            num_volumes=num_volumes,
            ram_mb=ram_mb,
            volumes_gb=volumes_gb,
        )

        rhubapilabclustercreate_cluster_hosts_json_body_item.additional_properties = d
        return rhubapilabclustercreate_cluster_hosts_json_body_item

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
