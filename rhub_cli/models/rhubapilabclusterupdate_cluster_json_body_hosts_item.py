from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast, List
from typing import Optional
from ..models.rhubapilabclusterupdate_cluster_json_body_hosts_item_id import RhubapilabclusterupdateClusterJsonBodyHostsItemId
from ..models.rhubapilabclusterupdate_cluster_json_body_hosts_item_cluster_id import RhubapilabclusterupdateClusterJsonBodyHostsItemClusterId
from typing import Dict
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union




T = TypeVar("T", bound="RhubapilabclusterupdateClusterJsonBodyHostsItem")

@attr.s(auto_attribs=True)
class RhubapilabclusterupdateClusterJsonBodyHostsItem:
    """  """
    cluster_id: Union[Unset, RhubapilabclusterupdateClusterJsonBodyHostsItemClusterId] = UNSET
    fqdn: Union[Unset, str] = UNSET
    id: Union[Unset, RhubapilabclusterupdateClusterJsonBodyHostsItemId] = UNSET
    ipaddr: Union[Unset, List[str]] = UNSET
    num_vcpus: Union[Unset, None, int] = UNSET
    num_volumes: Union[Unset, None, int] = UNSET
    ram_mb: Union[Unset, None, int] = UNSET
    volumes_gb: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        cluster_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_id, Unset):
            cluster_id = self.cluster_id.to_dict()

        fqdn = self.fqdn
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        ipaddr: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ipaddr, Unset):
            ipaddr = []
            for ipaddr_item_data in self.ipaddr:
                ipaddr_item = ipaddr_item_data


                ipaddr.append(ipaddr_item)




        num_vcpus = self.num_vcpus
        num_volumes = self.num_volumes
        ram_mb = self.ram_mb
        volumes_gb = self.volumes_gb

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if id is not UNSET:
            field_dict["id"] = id
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
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
        _cluster_id = d.pop("cluster_id", UNSET)
        cluster_id: Union[Unset, RhubapilabclusterupdateClusterJsonBodyHostsItemClusterId]
        if isinstance(_cluster_id,  Unset):
            cluster_id = UNSET
        else:
            cluster_id = RhubapilabclusterupdateClusterJsonBodyHostsItemClusterId.from_dict(_cluster_id)




        fqdn = d.pop("fqdn", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabclusterupdateClusterJsonBodyHostsItemId]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = RhubapilabclusterupdateClusterJsonBodyHostsItemId.from_dict(_id)




        ipaddr = []
        _ipaddr = d.pop("ipaddr", UNSET)
        for ipaddr_item_data in (_ipaddr or []):
            def _parse_ipaddr_item(data: object) -> str:
                return cast(str, data)

            ipaddr_item = _parse_ipaddr_item(ipaddr_item_data)

            ipaddr.append(ipaddr_item)


        num_vcpus = d.pop("num_vcpus", UNSET)

        num_volumes = d.pop("num_volumes", UNSET)

        ram_mb = d.pop("ram_mb", UNSET)

        volumes_gb = d.pop("volumes_gb", UNSET)

        rhubapilabclusterupdate_cluster_json_body_hosts_item = cls(
            cluster_id=cluster_id,
            fqdn=fqdn,
            id=id,
            ipaddr=ipaddr,
            num_vcpus=num_vcpus,
            num_volumes=num_volumes,
            ram_mb=ram_mb,
            volumes_gb=volumes_gb,
        )

        rhubapilabclusterupdate_cluster_json_body_hosts_item.additional_properties = d
        return rhubapilabclusterupdate_cluster_json_body_hosts_item

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
