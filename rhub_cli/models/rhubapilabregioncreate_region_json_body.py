from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabregioncreate_region_json_body_id import RhubapilabregioncreateRegionJsonBodyId
from ..models.rhubapilabregioncreate_region_json_body_quota_type_0 import RhubapilabregioncreateRegionJsonBodyQuotaType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabregioncreateRegionJsonBody")


@attr.s(auto_attribs=True)
class RhubapilabregioncreateRegionJsonBody:
    """ """

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
    id: Union[Unset, RhubapilabregioncreateRegionJsonBodyId] = UNSET
    lifespan_length: Union[Unset, None, int] = UNSET
    location: Union[Unset, None, str] = UNSET
    owner_group: Union[Unset, str] = UNSET
    quota: Union[Any, RhubapilabregioncreateRegionJsonBodyQuotaType0, Unset] = UNSET
    reservation_expiration_max: Union[Unset, None, int] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    users_group: Union[Unset, None, str] = UNSET
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
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        lifespan_length = self.lifespan_length
        location = self.location
        owner_group = self.owner_group
        quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.quota, Unset):
            quota = UNSET
        elif isinstance(self.quota, RhubapilabregioncreateRegionJsonBodyQuotaType0):
            quota = UNSET
            if not isinstance(self.quota, Unset):
                quota = self.quota.to_dict()

        else:
            quota = self.quota

        reservation_expiration_max = self.reservation_expiration_max
        reservations_enabled = self.reservations_enabled
        users_group = self.users_group

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
        if id is not UNSET:
            field_dict["id"] = id
        if lifespan_length is not UNSET:
            field_dict["lifespan_length"] = lifespan_length
        if location is not UNSET:
            field_dict["location"] = location
        if owner_group is not UNSET:
            field_dict["owner_group"] = owner_group
        if quota is not UNSET:
            field_dict["quota"] = quota
        if reservation_expiration_max is not UNSET:
            field_dict["reservation_expiration_max"] = reservation_expiration_max
        if reservations_enabled is not UNSET:
            field_dict["reservations_enabled"] = reservations_enabled
        if users_group is not UNSET:
            field_dict["users_group"] = users_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)  # TODO: find the bug
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

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabregioncreateRegionJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapilabregioncreateRegionJsonBodyId.from_dict(_id)

        lifespan_length = d.pop("lifespan_length", UNSET)

        location = d.pop("location", UNSET)

        owner_group = d.pop("owner_group", UNSET)

        def _parse_quota(data: object) -> Union[Any, RhubapilabregioncreateRegionJsonBodyQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _quota_type_0 = data
                quota_type_0: Union[Unset, RhubapilabregioncreateRegionJsonBodyQuotaType0]
                if isinstance(_quota_type_0, Unset):
                    quota_type_0 = UNSET
                else:
                    quota_type_0 = RhubapilabregioncreateRegionJsonBodyQuotaType0.from_dict(_quota_type_0)

                return quota_type_0
            except:  # noqa: E722
                pass
            quota_type_1 = data

            return quota_type_1

        quota = _parse_quota(d.pop("quota", UNSET))

        reservation_expiration_max = d.pop("reservation_expiration_max", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        users_group = d.pop("users_group", UNSET)

        rhubapilabregioncreate_region_json_body = cls(
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
            id=id,
            lifespan_length=lifespan_length,
            location=location,
            owner_group=owner_group,
            quota=quota,
            reservation_expiration_max=reservation_expiration_max,
            reservations_enabled=reservations_enabled,
            users_group=users_group,
        )

        rhubapilabregioncreate_region_json_body.additional_properties = d
        return rhubapilabregioncreate_region_json_body

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
