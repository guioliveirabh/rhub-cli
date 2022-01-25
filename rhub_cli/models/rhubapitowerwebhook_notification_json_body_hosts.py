from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rhubapitowerwebhook_notification_json_body_hosts_additional_property import (
    RhubapitowerwebhookNotificationJsonBodyHostsAdditionalProperty,
)

T = TypeVar("T", bound="RhubapitowerwebhookNotificationJsonBodyHosts")


@attr.s(auto_attribs=True)
class RhubapitowerwebhookNotificationJsonBodyHosts:
    """ """

    additional_properties: Dict[str, RhubapitowerwebhookNotificationJsonBodyHostsAdditionalProperty] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        rhubapitowerwebhook_notification_json_body_hosts = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RhubapitowerwebhookNotificationJsonBodyHostsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        rhubapitowerwebhook_notification_json_body_hosts.additional_properties = additional_properties
        return rhubapitowerwebhook_notification_json_body_hosts

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RhubapitowerwebhookNotificationJsonBodyHostsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RhubapitowerwebhookNotificationJsonBodyHostsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
