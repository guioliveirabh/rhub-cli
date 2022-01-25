from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabclusterreboot_hosts_json_body_hosts_type_0 import RhubapilabclusterrebootHostsJsonBodyHostsType0
from ..models.rhubapilabclusterreboot_hosts_json_body_hosts_type_1_item import (
    RhubapilabclusterrebootHostsJsonBodyHostsType1Item,
)
from ..models.rhubapilabclusterreboot_hosts_json_body_type import RhubapilabclusterrebootHostsJsonBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabclusterrebootHostsJsonBody")


@attr.s(auto_attribs=True)
class RhubapilabclusterrebootHostsJsonBody:
    """
    Attributes:
        hosts (Union[List[RhubapilabclusterrebootHostsJsonBodyHostsType1Item],
            RhubapilabclusterrebootHostsJsonBodyHostsType0, Unset]):
        type (Union[Unset, RhubapilabclusterrebootHostsJsonBodyType]):  Default:
            RhubapilabclusterrebootHostsJsonBodyType.SOFT.
    """

    hosts: Union[
        List[RhubapilabclusterrebootHostsJsonBodyHostsType1Item], RhubapilabclusterrebootHostsJsonBodyHostsType0, Unset
    ] = UNSET
    type: Union[Unset, RhubapilabclusterrebootHostsJsonBodyType] = RhubapilabclusterrebootHostsJsonBodyType.SOFT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hosts: Union[List[Dict[str, Any]], Unset, str]
        if isinstance(self.hosts, Unset):
            hosts = UNSET
        elif isinstance(self.hosts, RhubapilabclusterrebootHostsJsonBodyHostsType0):
            hosts = UNSET
            if not isinstance(self.hosts, Unset):
                hosts = self.hosts.value

        else:
            hosts = UNSET
            if not isinstance(self.hosts, Unset):
                hosts = []
                for hosts_type_1_item_data in self.hosts:
                    hosts_type_1_item = hosts_type_1_item_data.to_dict()

                    hosts.append(hosts_type_1_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_hosts(
            data: object,
        ) -> Union[
            List[RhubapilabclusterrebootHostsJsonBodyHostsType1Item],
            RhubapilabclusterrebootHostsJsonBodyHostsType0,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _hosts_type_0 = data
                hosts_type_0: Union[Unset, RhubapilabclusterrebootHostsJsonBodyHostsType0]
                if isinstance(_hosts_type_0, Unset):
                    hosts_type_0 = UNSET
                else:
                    hosts_type_0 = RhubapilabclusterrebootHostsJsonBodyHostsType0(_hosts_type_0)

                return hosts_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            hosts_type_1 = UNSET
            _hosts_type_1 = data
            for hosts_type_1_item_data in _hosts_type_1 or []:
                hosts_type_1_item = RhubapilabclusterrebootHostsJsonBodyHostsType1Item.from_dict(hosts_type_1_item_data)

                hosts_type_1.append(hosts_type_1_item)

            return hosts_type_1

        hosts = _parse_hosts(d.pop("hosts", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, RhubapilabclusterrebootHostsJsonBodyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RhubapilabclusterrebootHostsJsonBodyType(_type)

        rhubapilabclusterreboot_hosts_json_body = cls(
            hosts=hosts,
            type=type,
        )

        rhubapilabclusterreboot_hosts_json_body.additional_properties = d
        return rhubapilabclusterreboot_hosts_json_body

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
