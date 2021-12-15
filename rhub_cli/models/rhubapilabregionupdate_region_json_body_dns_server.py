from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhubapilabregionupdate_region_json_body_dns_server_key_type_0 import (
    RhubapilabregionupdateRegionJsonBodyDnsServerKeyType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabregionupdateRegionJsonBodyDnsServer")


@attr.s(auto_attribs=True)
class RhubapilabregionupdateRegionJsonBodyDnsServer:
    """ """

    hostname: Union[Unset, str] = UNSET
    key: Union[RhubapilabregionupdateRegionJsonBodyDnsServerKeyType0, Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname
        key: Union[Dict[str, Any], Unset, str]
        if isinstance(self.key, Unset):
            key = UNSET
        elif isinstance(self.key, RhubapilabregionupdateRegionJsonBodyDnsServerKeyType0):
            key = UNSET
            if not isinstance(self.key, Unset):
                key = self.key.to_dict()

        else:
            key = self.key

        zone = self.zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if key is not UNSET:
            field_dict["key"] = key
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hostname = d.pop("hostname", UNSET)

        def _parse_key(data: object) -> Union[RhubapilabregionupdateRegionJsonBodyDnsServerKeyType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _key_type_0 = data
                key_type_0: Union[Unset, RhubapilabregionupdateRegionJsonBodyDnsServerKeyType0]
                if isinstance(_key_type_0, Unset):
                    key_type_0 = UNSET
                else:
                    key_type_0 = RhubapilabregionupdateRegionJsonBodyDnsServerKeyType0.from_dict(_key_type_0)

                return key_type_0
            except:  # noqa: E722
                pass
            return cast(Union[RhubapilabregionupdateRegionJsonBodyDnsServerKeyType0, Unset, str], data)

        key = _parse_key(d.pop("key", UNSET))

        zone = d.pop("zone", UNSET)

        rhubapilabregionupdate_region_json_body_dns_server = cls(
            hostname=hostname,
            key=key,
            zone=zone,
        )

        rhubapilabregionupdate_region_json_body_dns_server.additional_properties = d
        return rhubapilabregionupdate_region_json_body_dns_server

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
