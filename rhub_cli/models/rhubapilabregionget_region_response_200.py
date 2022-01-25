from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabregionget_region_response_200_dns_server import RhubapilabregiongetRegionResponse200DnsServer
from ..models.rhubapilabregionget_region_response_200_id import RhubapilabregiongetRegionResponse200Id
from ..models.rhubapilabregionget_region_response_200_openstack import RhubapilabregiongetRegionResponse200Openstack
from ..models.rhubapilabregionget_region_response_200_satellite import RhubapilabregiongetRegionResponse200Satellite
from ..models.rhubapilabregionget_region_response_200_total_quota_type_0 import (
    RhubapilabregiongetRegionResponse200TotalQuotaType0,
)
from ..models.rhubapilabregionget_region_response_200_user_quota_type_0 import (
    RhubapilabregiongetRegionResponse200UserQuotaType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabregiongetRegionResponse200")


@attr.s(auto_attribs=True)
class RhubapilabregiongetRegionResponse200:
    """
    Attributes:
        banner (Union[Unset, str]):
        description (Union[Unset, str]):
        dns_server (Union[Unset, RhubapilabregiongetRegionResponse200DnsServer]):  Example: {'hostname':
            'ns.example.com', 'key': 'kv/region/rdu2-a/dns', 'zone': 'example.com.'}.
        download_server (Union[Unset, str]):  Example: https://download.example.com.
        enabled (Union[Unset, bool]):
        id (Union[Unset, RhubapilabregiongetRegionResponse200Id]):
        lifespan_length (Union[Unset, None, int]):
        location (Union[Unset, None, str]): Geographical location of region. Example: RDU.
        name (Union[Unset, str]):  Example: rdu2-a.
        openstack (Union[Unset, RhubapilabregiongetRegionResponse200Openstack]):  Example: {'credentials':
            'kv/region/rdu2-a/openstack', 'domain_id': 'default', 'domain_name': 'Default', 'keyname': 'rhub', 'networks':
            ['provider_net_rhub'], 'project': 'rhub', 'url': 'https://openstack.example.com:13000'}.
        owner_group (Union[Unset, str]):  Example: 7670ac07-cb21-448d-af8a-6e3882216be3.
        reservation_expiration_max (Union[Unset, None, int]):
        reservations_enabled (Union[Unset, bool]):
        satellite (Union[Unset, RhubapilabregiongetRegionResponse200Satellite]):  Example: {'credentials':
            'kv/region/rdu2-a/satellite', 'hostname': 'satellite.example.com'}.
        total_quota (Union[Any, RhubapilabregiongetRegionResponse200TotalQuotaType0, Unset]):  Example: {'num_vcpus':
            40000, 'num_volumes': 40000, 'ram_mb': 200000000, 'volumes_gb': 540000}.
        tower_id (Union[Unset, int]):
        user_quota (Union[Any, RhubapilabregiongetRegionResponse200UserQuotaType0, Unset]):  Example: {'num_vcpus': 40,
            'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        users_group (Union[Unset, None, str]):
        vault_server (Union[Unset, str]):  Example: https://vault.example.com.
    """

    banner: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dns_server: Union[Unset, RhubapilabregiongetRegionResponse200DnsServer] = UNSET
    download_server: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, RhubapilabregiongetRegionResponse200Id] = UNSET
    lifespan_length: Union[Unset, None, int] = UNSET
    location: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    openstack: Union[Unset, RhubapilabregiongetRegionResponse200Openstack] = UNSET
    owner_group: Union[Unset, str] = UNSET
    reservation_expiration_max: Union[Unset, None, int] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    satellite: Union[Unset, RhubapilabregiongetRegionResponse200Satellite] = UNSET
    total_quota: Union[Any, RhubapilabregiongetRegionResponse200TotalQuotaType0, Unset] = UNSET
    tower_id: Union[Unset, int] = UNSET
    user_quota: Union[Any, RhubapilabregiongetRegionResponse200UserQuotaType0, Unset] = UNSET
    users_group: Union[Unset, None, str] = UNSET
    vault_server: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        banner = self.banner
        description = self.description
        dns_server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dns_server, Unset):
            dns_server = self.dns_server.to_dict()

        download_server = self.download_server
        enabled = self.enabled
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        lifespan_length = self.lifespan_length
        location = self.location
        name = self.name
        openstack: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.openstack, Unset):
            openstack = self.openstack.to_dict()

        owner_group = self.owner_group
        reservation_expiration_max = self.reservation_expiration_max
        reservations_enabled = self.reservations_enabled
        satellite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.satellite, Unset):
            satellite = self.satellite.to_dict()

        total_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.total_quota, Unset):
            total_quota = UNSET
        elif isinstance(self.total_quota, RhubapilabregiongetRegionResponse200TotalQuotaType0):
            total_quota = UNSET
            if not isinstance(self.total_quota, Unset):
                total_quota = self.total_quota.to_dict()

        else:
            total_quota = self.total_quota

        tower_id = self.tower_id
        user_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.user_quota, Unset):
            user_quota = UNSET
        elif isinstance(self.user_quota, RhubapilabregiongetRegionResponse200UserQuotaType0):
            user_quota = UNSET
            if not isinstance(self.user_quota, Unset):
                user_quota = self.user_quota.to_dict()

        else:
            user_quota = self.user_quota

        users_group = self.users_group
        vault_server = self.vault_server

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if banner is not UNSET:
            field_dict["banner"] = banner
        if description is not UNSET:
            field_dict["description"] = description
        if dns_server is not UNSET:
            field_dict["dns_server"] = dns_server
        if download_server is not UNSET:
            field_dict["download_server"] = download_server
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if lifespan_length is not UNSET:
            field_dict["lifespan_length"] = lifespan_length
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if openstack is not UNSET:
            field_dict["openstack"] = openstack
        if owner_group is not UNSET:
            field_dict["owner_group"] = owner_group
        if reservation_expiration_max is not UNSET:
            field_dict["reservation_expiration_max"] = reservation_expiration_max
        if reservations_enabled is not UNSET:
            field_dict["reservations_enabled"] = reservations_enabled
        if satellite is not UNSET:
            field_dict["satellite"] = satellite
        if total_quota is not UNSET:
            field_dict["total_quota"] = total_quota
        if tower_id is not UNSET:
            field_dict["tower_id"] = tower_id
        if user_quota is not UNSET:
            field_dict["user_quota"] = user_quota
        if users_group is not UNSET:
            field_dict["users_group"] = users_group
        if vault_server is not UNSET:
            field_dict["vault_server"] = vault_server

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        banner = d.pop("banner", UNSET)

        description = d.pop("description", UNSET)

        _dns_server = d.pop("dns_server", UNSET)
        dns_server: Union[Unset, RhubapilabregiongetRegionResponse200DnsServer]
        if isinstance(_dns_server, Unset):
            dns_server = UNSET
        else:
            dns_server = RhubapilabregiongetRegionResponse200DnsServer.from_dict(_dns_server)

        download_server = d.pop("download_server", UNSET)

        enabled = d.pop("enabled", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabregiongetRegionResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapilabregiongetRegionResponse200Id.from_dict(_id)

        lifespan_length = d.pop("lifespan_length", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        _openstack = d.pop("openstack", UNSET)
        openstack: Union[Unset, RhubapilabregiongetRegionResponse200Openstack]
        if isinstance(_openstack, Unset):
            openstack = UNSET
        else:
            openstack = RhubapilabregiongetRegionResponse200Openstack.from_dict(_openstack)

        owner_group = d.pop("owner_group", UNSET)

        reservation_expiration_max = d.pop("reservation_expiration_max", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        _satellite = d.pop("satellite", UNSET)
        satellite: Union[Unset, RhubapilabregiongetRegionResponse200Satellite]
        if isinstance(_satellite, Unset):
            satellite = UNSET
        else:
            satellite = RhubapilabregiongetRegionResponse200Satellite.from_dict(_satellite)

        def _parse_total_quota(data: object) -> Union[Any, RhubapilabregiongetRegionResponse200TotalQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _total_quota_type_0 = data
                total_quota_type_0: Union[Unset, RhubapilabregiongetRegionResponse200TotalQuotaType0]
                if isinstance(_total_quota_type_0, Unset):
                    total_quota_type_0 = UNSET
                else:
                    total_quota_type_0 = RhubapilabregiongetRegionResponse200TotalQuotaType0.from_dict(
                        _total_quota_type_0
                    )

                return total_quota_type_0
            except:  # noqa: E722
                pass
            total_quota_type_1 = data

            return total_quota_type_1

        total_quota = _parse_total_quota(d.pop("total_quota", UNSET))

        tower_id = d.pop("tower_id", UNSET)

        def _parse_user_quota(data: object) -> Union[Any, RhubapilabregiongetRegionResponse200UserQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _user_quota_type_0 = data
                user_quota_type_0: Union[Unset, RhubapilabregiongetRegionResponse200UserQuotaType0]
                if isinstance(_user_quota_type_0, Unset):
                    user_quota_type_0 = UNSET
                else:
                    user_quota_type_0 = RhubapilabregiongetRegionResponse200UserQuotaType0.from_dict(_user_quota_type_0)

                return user_quota_type_0
            except:  # noqa: E722
                pass
            user_quota_type_1 = data

            return user_quota_type_1

        user_quota = _parse_user_quota(d.pop("user_quota", UNSET))

        users_group = d.pop("users_group", UNSET)

        vault_server = d.pop("vault_server", UNSET)

        rhubapilabregionget_region_response_200 = cls(
            banner=banner,
            description=description,
            dns_server=dns_server,
            download_server=download_server,
            enabled=enabled,
            id=id,
            lifespan_length=lifespan_length,
            location=location,
            name=name,
            openstack=openstack,
            owner_group=owner_group,
            reservation_expiration_max=reservation_expiration_max,
            reservations_enabled=reservations_enabled,
            satellite=satellite,
            total_quota=total_quota,
            tower_id=tower_id,
            user_quota=user_quota,
            users_group=users_group,
            vault_server=vault_server,
        )

        rhubapilabregionget_region_response_200.additional_properties = d
        return rhubapilabregionget_region_response_200

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
