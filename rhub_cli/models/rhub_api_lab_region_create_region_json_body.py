from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_lab_region_create_region_json_body_total_quota import (
    RhubApiLabRegionCreateRegionJsonBodyTotalQuota,
)
from ..models.rhub_api_lab_region_create_region_json_body_user_quota import (
    RhubApiLabRegionCreateRegionJsonBodyUserQuota,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabRegionCreateRegionJsonBody")


@attr.s(auto_attribs=True)
class RhubApiLabRegionCreateRegionJsonBody:
    """
    Attributes:
        dns_server (Any):
        download_server (str):  Example: https://download.example.com.
        name (str):  Example: rdu2-a.
        openstack (Any):
        satellite (Any):
        tower_id (int):
        vault_server (str):  Example: https://vault.example.com.
        banner (Union[Unset, str]):
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        lifespan_length (Union[Unset, None, int]):
        location (Union[Unset, None, str]): Geographical location of region. Example: RDU.
        owner_group (Union[Unset, str]):  Example: 7670ac07-cb21-448d-af8a-6e3882216be3.
        owner_group_name (Union[Unset, None, str]):
        reservation_expiration_max (Union[Unset, None, int]):
        reservations_enabled (Union[Unset, bool]):
        total_quota (Union[Unset, None, RhubApiLabRegionCreateRegionJsonBodyTotalQuota]):  Example: {'num_vcpus': 40000,
            'num_volumes': 40000, 'ram_mb': 200000000, 'volumes_gb': 540000}.
        user_quota (Union[Unset, None, RhubApiLabRegionCreateRegionJsonBodyUserQuota]):  Example: {'num_vcpus': 40,
            'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        users_group (Union[Unset, None, str]):
        users_group_name (Union[Unset, None, str]):
    """

    dns_server: Any
    download_server: str
    name: str
    openstack: Any
    satellite: Any
    tower_id: int
    vault_server: str
    banner: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    lifespan_length: Union[Unset, None, int] = UNSET
    location: Union[Unset, None, str] = UNSET
    owner_group: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, None, str] = UNSET
    reservation_expiration_max: Union[Unset, None, int] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    total_quota: Union[Unset, None, RhubApiLabRegionCreateRegionJsonBodyTotalQuota] = UNSET
    user_quota: Union[Unset, None, RhubApiLabRegionCreateRegionJsonBodyUserQuota] = UNSET
    users_group: Union[Unset, None, str] = UNSET
    users_group_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dns_server = self.dns_server
        download_server = self.download_server
        name = self.name
        openstack = self.openstack
        satellite = self.satellite
        tower_id = self.tower_id
        vault_server = self.vault_server
        banner = self.banner
        description = self.description
        enabled = self.enabled
        lifespan_length = self.lifespan_length
        location = self.location
        owner_group = self.owner_group
        owner_group_name = self.owner_group_name
        reservation_expiration_max = self.reservation_expiration_max
        reservations_enabled = self.reservations_enabled
        total_quota: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.total_quota, Unset):
            total_quota = self.total_quota.to_dict() if self.total_quota else None

        user_quota: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_quota, Unset):
            user_quota = self.user_quota.to_dict() if self.user_quota else None

        users_group = self.users_group
        users_group_name = self.users_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dns_server": dns_server,
                "download_server": download_server,
                "name": name,
                "openstack": openstack,
                "satellite": satellite,
                "tower_id": tower_id,
                "vault_server": vault_server,
            }
        )
        if banner is not UNSET:
            field_dict["banner"] = banner
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if lifespan_length is not UNSET:
            field_dict["lifespan_length"] = lifespan_length
        if location is not UNSET:
            field_dict["location"] = location
        if owner_group is not UNSET:
            field_dict["owner_group"] = owner_group
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name
        if reservation_expiration_max is not UNSET:
            field_dict["reservation_expiration_max"] = reservation_expiration_max
        if reservations_enabled is not UNSET:
            field_dict["reservations_enabled"] = reservations_enabled
        if total_quota is not UNSET:
            field_dict["total_quota"] = total_quota
        if user_quota is not UNSET:
            field_dict["user_quota"] = user_quota
        if users_group is not UNSET:
            field_dict["users_group"] = users_group
        if users_group_name is not UNSET:
            field_dict["users_group_name"] = users_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        dns_server = d.pop("dns_server")

        download_server = d.pop("download_server")

        name = d.pop("name")

        openstack = d.pop("openstack")

        satellite = d.pop("satellite")

        tower_id = d.pop("tower_id")

        vault_server = d.pop("vault_server")

        banner = d.pop("banner", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        lifespan_length = d.pop("lifespan_length", UNSET)

        location = d.pop("location", UNSET)

        owner_group = d.pop("owner_group", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        reservation_expiration_max = d.pop("reservation_expiration_max", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        _total_quota = d.pop("total_quota", UNSET)
        total_quota: Union[Unset, None, RhubApiLabRegionCreateRegionJsonBodyTotalQuota]
        if _total_quota is None:
            total_quota = None
        elif isinstance(_total_quota, Unset):
            total_quota = UNSET
        else:
            total_quota = RhubApiLabRegionCreateRegionJsonBodyTotalQuota.from_dict(_total_quota)

        _user_quota = d.pop("user_quota", UNSET)
        user_quota: Union[Unset, None, RhubApiLabRegionCreateRegionJsonBodyUserQuota]
        if _user_quota is None:
            user_quota = None
        elif isinstance(_user_quota, Unset):
            user_quota = UNSET
        else:
            user_quota = RhubApiLabRegionCreateRegionJsonBodyUserQuota.from_dict(_user_quota)

        users_group = d.pop("users_group", UNSET)

        users_group_name = d.pop("users_group_name", UNSET)

        rhub_api_lab_region_create_region_json_body = cls(
            dns_server=dns_server,
            download_server=download_server,
            name=name,
            openstack=openstack,
            satellite=satellite,
            tower_id=tower_id,
            vault_server=vault_server,
            banner=banner,
            description=description,
            enabled=enabled,
            lifespan_length=lifespan_length,
            location=location,
            owner_group=owner_group,
            owner_group_name=owner_group_name,
            reservation_expiration_max=reservation_expiration_max,
            reservations_enabled=reservations_enabled,
            total_quota=total_quota,
            user_quota=user_quota,
            users_group=users_group,
            users_group_name=users_group_name,
        )

        rhub_api_lab_region_create_region_json_body.additional_properties = d
        return rhub_api_lab_region_create_region_json_body

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
