from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabregionupdate_region_json_body_dns_server import RhubapilabregionupdateRegionJsonBodyDnsServer
from ..models.rhubapilabregionupdate_region_json_body_id import RhubapilabregionupdateRegionJsonBodyId
from ..models.rhubapilabregionupdate_region_json_body_openstack import RhubapilabregionupdateRegionJsonBodyOpenstack
from ..models.rhubapilabregionupdate_region_json_body_quota_type_0 import RhubapilabregionupdateRegionJsonBodyQuotaType0
from ..models.rhubapilabregionupdate_region_json_body_satellite import RhubapilabregionupdateRegionJsonBodySatellite
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabregionupdateRegionJsonBody")


@attr.s(auto_attribs=True)
class RhubapilabregionupdateRegionJsonBody:
    """
    Attributes:
        banner (Union[Unset, str]):
        description (Union[Unset, str]):
        dns_server (Union[Unset, RhubapilabregionupdateRegionJsonBodyDnsServer]):  Example: {'hostname':
            'ns.example.com', 'key': 'kv/region/rdu2-a/dns', 'zone': 'example.com.'}.
        download_server (Union[Unset, str]):  Example: https://download.example.com.
        enabled (Union[Unset, bool]):
        id (Union[Unset, RhubapilabregionupdateRegionJsonBodyId]):
        lifespan_length (Union[Unset, None, int]):
        location (Union[Unset, None, str]): Geographical location of region. Example: RDU.
        name (Union[Unset, str]):  Example: rdu2-a.
        openstack (Union[Unset, RhubapilabregionupdateRegionJsonBodyOpenstack]):  Example: {'credentials':
            'kv/region/rdu2-a/openstack', 'domain_id': 'default', 'domain_name': 'Default', 'keyname': 'rhub', 'networks':
            ['provider_net_rhub'], 'project': 'rhub', 'url': 'https://openstack.example.com:13000'}.
        owner_group (Union[Unset, str]):  Example: 7670ac07-cb21-448d-af8a-6e3882216be3.
        quota (Union[Any, RhubapilabregionupdateRegionJsonBodyQuotaType0, Unset]):  Example: {'num_vcpus': 40,
            'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        reservation_expiration_max (Union[Unset, None, int]):
        reservations_enabled (Union[Unset, bool]):
        satellite (Union[Unset, RhubapilabregionupdateRegionJsonBodySatellite]):  Example: {'credentials':
            'kv/region/rdu2-a/satellite', 'hostname': 'satellite.example.com'}.
        tower_id (Union[Unset, int]):
        users_group (Union[Unset, None, str]):
        vault_server (Union[Unset, str]):  Example: https://vault.example.com.
    """

    banner: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dns_server: Union[Unset, RhubapilabregionupdateRegionJsonBodyDnsServer] = UNSET
    download_server: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, RhubapilabregionupdateRegionJsonBodyId] = UNSET
    lifespan_length: Union[Unset, None, int] = UNSET
    location: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    openstack: Union[Unset, RhubapilabregionupdateRegionJsonBodyOpenstack] = UNSET
    owner_group: Union[Unset, str] = UNSET
    quota: Union[Any, RhubapilabregionupdateRegionJsonBodyQuotaType0, Unset] = UNSET
    reservation_expiration_max: Union[Unset, None, int] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    satellite: Union[Unset, RhubapilabregionupdateRegionJsonBodySatellite] = UNSET
    tower_id: Union[Unset, int] = UNSET
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
        quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.quota, Unset):
            quota = UNSET
        elif isinstance(self.quota, RhubapilabregionupdateRegionJsonBodyQuotaType0):
            quota = UNSET
            if not isinstance(self.quota, Unset):
                quota = self.quota.to_dict()

        else:
            quota = self.quota

        reservation_expiration_max = self.reservation_expiration_max
        reservations_enabled = self.reservations_enabled
        satellite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.satellite, Unset):
            satellite = self.satellite.to_dict()

        tower_id = self.tower_id
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
        if quota is not UNSET:
            field_dict["quota"] = quota
        if reservation_expiration_max is not UNSET:
            field_dict["reservation_expiration_max"] = reservation_expiration_max
        if reservations_enabled is not UNSET:
            field_dict["reservations_enabled"] = reservations_enabled
        if satellite is not UNSET:
            field_dict["satellite"] = satellite
        if tower_id is not UNSET:
            field_dict["tower_id"] = tower_id
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
        dns_server: Union[Unset, RhubapilabregionupdateRegionJsonBodyDnsServer]
        if isinstance(_dns_server, Unset):
            dns_server = UNSET
        else:
            dns_server = RhubapilabregionupdateRegionJsonBodyDnsServer.from_dict(_dns_server)

        download_server = d.pop("download_server", UNSET)

        enabled = d.pop("enabled", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabregionupdateRegionJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapilabregionupdateRegionJsonBodyId.from_dict(_id)

        lifespan_length = d.pop("lifespan_length", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        _openstack = d.pop("openstack", UNSET)
        openstack: Union[Unset, RhubapilabregionupdateRegionJsonBodyOpenstack]
        if isinstance(_openstack, Unset):
            openstack = UNSET
        else:
            openstack = RhubapilabregionupdateRegionJsonBodyOpenstack.from_dict(_openstack)

        owner_group = d.pop("owner_group", UNSET)

        def _parse_quota(data: object) -> Union[Any, RhubapilabregionupdateRegionJsonBodyQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _quota_type_0 = data
                quota_type_0: Union[Unset, RhubapilabregionupdateRegionJsonBodyQuotaType0]
                if isinstance(_quota_type_0, Unset):
                    quota_type_0 = UNSET
                else:
                    quota_type_0 = RhubapilabregionupdateRegionJsonBodyQuotaType0.from_dict(_quota_type_0)

                return quota_type_0
            except:  # noqa: E722
                pass
            quota_type_1 = data

            return quota_type_1

        quota = _parse_quota(d.pop("quota", UNSET))

        reservation_expiration_max = d.pop("reservation_expiration_max", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        _satellite = d.pop("satellite", UNSET)
        satellite: Union[Unset, RhubapilabregionupdateRegionJsonBodySatellite]
        if isinstance(_satellite, Unset):
            satellite = UNSET
        else:
            satellite = RhubapilabregionupdateRegionJsonBodySatellite.from_dict(_satellite)

        tower_id = d.pop("tower_id", UNSET)

        users_group = d.pop("users_group", UNSET)

        vault_server = d.pop("vault_server", UNSET)

        rhubapilabregionupdate_region_json_body = cls(
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
            quota=quota,
            reservation_expiration_max=reservation_expiration_max,
            reservations_enabled=reservations_enabled,
            satellite=satellite,
            tower_id=tower_id,
            users_group=users_group,
            vault_server=vault_server,
        )

        rhubapilabregionupdate_region_json_body.additional_properties = d
        return rhubapilabregionupdate_region_json_body

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
