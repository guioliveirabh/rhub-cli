from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_dns_server import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionDnsServer,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_openstack import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_satellite import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionSatellite,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_total_quota import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuota,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_user_quota import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuota,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductListProductRegionsResponse200ItemRegion")


@attr.s(auto_attribs=True)
class RhubApiLabProductListProductRegionsResponse200ItemRegion:
    """
    Attributes:
        banner (Union[Unset, str]):
        description (Union[Unset, str]):
        dns_server (Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionDnsServer]):  Example:
            {'hostname': 'ns.example.com', 'key': 'kv/region/rdu2-a/dns', 'zone': 'example.com.'}.
        download_server (Union[Unset, str]):  Example: https://download.example.com.
        enabled (Union[Unset, bool]):
        lifespan_length (Union[Unset, None, int]):
        location (Union[Unset, None, str]): Geographical location of region. Example: RDU.
        name (Union[Unset, str]):  Example: rdu2-a.
        openstack (Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack]):  Example:
            {'credentials': 'kv/region/rdu2-a/openstack', 'domain_id': 'default', 'domain_name': 'Default', 'keyname':
            'rhub', 'networks': ['provider_net_rhub'], 'project': 'rhub', 'url': 'https://openstack.example.com:13000'}.
        owner_group (Union[Unset, str]):  Example: 7670ac07-cb21-448d-af8a-6e3882216be3.
        owner_group_name (Union[Unset, None, str]):
        reservation_expiration_max (Union[Unset, None, int]):
        reservations_enabled (Union[Unset, bool]):
        satellite (Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionSatellite]):  Example:
            {'credentials': 'kv/region/rdu2-a/satellite', 'hostname': 'satellite.example.com'}.
        total_quota (Union[Unset, None, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuota]):  Example:
            {'num_vcpus': 40000, 'num_volumes': 40000, 'ram_mb': 200000000, 'volumes_gb': 540000}.
        tower_id (Union[Unset, int]):
        user_quota (Union[Unset, None, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuota]):  Example:
            {'num_vcpus': 40, 'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        users_group (Union[Unset, None, str]):
        users_group_name (Union[Unset, None, str]):
        vault_server (Union[Unset, str]):  Example: https://vault.example.com.
        id (Union[Unset, int]):
    """

    banner: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dns_server: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionDnsServer] = UNSET
    download_server: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    lifespan_length: Union[Unset, None, int] = UNSET
    location: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    openstack: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack] = UNSET
    owner_group: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, None, str] = UNSET
    reservation_expiration_max: Union[Unset, None, int] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    satellite: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionSatellite] = UNSET
    total_quota: Union[Unset, None, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuota] = UNSET
    tower_id: Union[Unset, int] = UNSET
    user_quota: Union[Unset, None, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuota] = UNSET
    users_group: Union[Unset, None, str] = UNSET
    users_group_name: Union[Unset, None, str] = UNSET
    vault_server: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        banner = self.banner
        description = self.description
        dns_server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dns_server, Unset):
            dns_server = self.dns_server.to_dict()

        download_server = self.download_server
        enabled = self.enabled
        lifespan_length = self.lifespan_length
        location = self.location
        name = self.name
        openstack: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.openstack, Unset):
            openstack = self.openstack.to_dict()

        owner_group = self.owner_group
        owner_group_name = self.owner_group_name
        reservation_expiration_max = self.reservation_expiration_max
        reservations_enabled = self.reservations_enabled
        satellite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.satellite, Unset):
            satellite = self.satellite.to_dict()

        total_quota: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.total_quota, Unset):
            total_quota = self.total_quota.to_dict() if self.total_quota else None

        tower_id = self.tower_id
        user_quota: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_quota, Unset):
            user_quota = self.user_quota.to_dict() if self.user_quota else None

        users_group = self.users_group
        users_group_name = self.users_group_name
        vault_server = self.vault_server
        id = self.id

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
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name
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
        if users_group_name is not UNSET:
            field_dict["users_group_name"] = users_group_name
        if vault_server is not UNSET:
            field_dict["vault_server"] = vault_server
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        banner = d.pop("banner", UNSET)

        description = d.pop("description", UNSET)

        _dns_server = d.pop("dns_server", UNSET)
        dns_server: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionDnsServer]
        if isinstance(_dns_server, Unset):
            dns_server = UNSET
        else:
            dns_server = RhubApiLabProductListProductRegionsResponse200ItemRegionDnsServer.from_dict(_dns_server)

        download_server = d.pop("download_server", UNSET)

        enabled = d.pop("enabled", UNSET)

        lifespan_length = d.pop("lifespan_length", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        _openstack = d.pop("openstack", UNSET)
        openstack: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack]
        if isinstance(_openstack, Unset):
            openstack = UNSET
        else:
            openstack = RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack.from_dict(_openstack)

        owner_group = d.pop("owner_group", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        reservation_expiration_max = d.pop("reservation_expiration_max", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        _satellite = d.pop("satellite", UNSET)
        satellite: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionSatellite]
        if isinstance(_satellite, Unset):
            satellite = UNSET
        else:
            satellite = RhubApiLabProductListProductRegionsResponse200ItemRegionSatellite.from_dict(_satellite)

        _total_quota = d.pop("total_quota", UNSET)
        total_quota: Union[Unset, None, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuota]
        if _total_quota is None:
            total_quota = None
        elif isinstance(_total_quota, Unset):
            total_quota = UNSET
        else:
            total_quota = RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuota.from_dict(_total_quota)

        tower_id = d.pop("tower_id", UNSET)

        _user_quota = d.pop("user_quota", UNSET)
        user_quota: Union[Unset, None, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuota]
        if _user_quota is None:
            user_quota = None
        elif isinstance(_user_quota, Unset):
            user_quota = UNSET
        else:
            user_quota = RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuota.from_dict(_user_quota)

        users_group = d.pop("users_group", UNSET)

        users_group_name = d.pop("users_group_name", UNSET)

        vault_server = d.pop("vault_server", UNSET)

        id = d.pop("id", UNSET)

        rhub_api_lab_product_list_product_regions_response_200_item_region = cls(
            banner=banner,
            description=description,
            dns_server=dns_server,
            download_server=download_server,
            enabled=enabled,
            lifespan_length=lifespan_length,
            location=location,
            name=name,
            openstack=openstack,
            owner_group=owner_group,
            owner_group_name=owner_group_name,
            reservation_expiration_max=reservation_expiration_max,
            reservations_enabled=reservations_enabled,
            satellite=satellite,
            total_quota=total_quota,
            tower_id=tower_id,
            user_quota=user_quota,
            users_group=users_group,
            users_group_name=users_group_name,
            vault_server=vault_server,
            id=id,
        )

        rhub_api_lab_product_list_product_regions_response_200_item_region.additional_properties = d
        return rhub_api_lab_product_list_product_regions_response_200_item_region

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
