from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabregionget_usage_response_200_openstack_limits import (
    RhubapilabregiongetUsageResponse200OpenstackLimits,
)
from ..models.rhubapilabregionget_usage_response_200_total_quota_type_0 import (
    RhubapilabregiongetUsageResponse200TotalQuotaType0,
)
from ..models.rhubapilabregionget_usage_response_200_total_quota_usage import (
    RhubapilabregiongetUsageResponse200TotalQuotaUsage,
)
from ..models.rhubapilabregionget_usage_response_200_user_quota_type_0 import (
    RhubapilabregiongetUsageResponse200UserQuotaType0,
)
from ..models.rhubapilabregionget_usage_response_200_user_quota_usage import (
    RhubapilabregiongetUsageResponse200UserQuotaUsage,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabregiongetUsageResponse200")


@attr.s(auto_attribs=True)
class RhubapilabregiongetUsageResponse200:
    """
    Attributes:
        openstack_limits (Union[Unset, RhubapilabregiongetUsageResponse200OpenstackLimits]): OpenStack limits RAW value
            from the API.
        total_quota (Union[Any, RhubapilabregiongetUsageResponse200TotalQuotaType0, Unset]):
        total_quota_usage (Union[Unset, RhubapilabregiongetUsageResponse200TotalQuotaUsage]):
        user_quota (Union[Any, RhubapilabregiongetUsageResponse200UserQuotaType0, Unset]):
        user_quota_usage (Union[Unset, RhubapilabregiongetUsageResponse200UserQuotaUsage]):
    """

    openstack_limits: Union[Unset, RhubapilabregiongetUsageResponse200OpenstackLimits] = UNSET
    total_quota: Union[Any, RhubapilabregiongetUsageResponse200TotalQuotaType0, Unset] = UNSET
    total_quota_usage: Union[Unset, RhubapilabregiongetUsageResponse200TotalQuotaUsage] = UNSET
    user_quota: Union[Any, RhubapilabregiongetUsageResponse200UserQuotaType0, Unset] = UNSET
    user_quota_usage: Union[Unset, RhubapilabregiongetUsageResponse200UserQuotaUsage] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        openstack_limits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.openstack_limits, Unset):
            openstack_limits = self.openstack_limits.to_dict()

        total_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.total_quota, Unset):
            total_quota = UNSET
        elif isinstance(self.total_quota, RhubapilabregiongetUsageResponse200TotalQuotaType0):
            total_quota = UNSET
            if not isinstance(self.total_quota, Unset):
                total_quota = self.total_quota.to_dict()

        else:
            total_quota = self.total_quota

        total_quota_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_quota_usage, Unset):
            total_quota_usage = self.total_quota_usage.to_dict()

        user_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.user_quota, Unset):
            user_quota = UNSET
        elif isinstance(self.user_quota, RhubapilabregiongetUsageResponse200UserQuotaType0):
            user_quota = UNSET
            if not isinstance(self.user_quota, Unset):
                user_quota = self.user_quota.to_dict()

        else:
            user_quota = self.user_quota

        user_quota_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_quota_usage, Unset):
            user_quota_usage = self.user_quota_usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if openstack_limits is not UNSET:
            field_dict["openstack_limits"] = openstack_limits
        if total_quota is not UNSET:
            field_dict["total_quota"] = total_quota
        if total_quota_usage is not UNSET:
            field_dict["total_quota_usage"] = total_quota_usage
        if user_quota is not UNSET:
            field_dict["user_quota"] = user_quota
        if user_quota_usage is not UNSET:
            field_dict["user_quota_usage"] = user_quota_usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _openstack_limits = d.pop("openstack_limits", UNSET)
        openstack_limits: Union[Unset, RhubapilabregiongetUsageResponse200OpenstackLimits]
        if isinstance(_openstack_limits, Unset):
            openstack_limits = UNSET
        else:
            openstack_limits = RhubapilabregiongetUsageResponse200OpenstackLimits.from_dict(_openstack_limits)

        def _parse_total_quota(data: object) -> Union[Any, RhubapilabregiongetUsageResponse200TotalQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _total_quota_type_0 = data
                total_quota_type_0: Union[Unset, RhubapilabregiongetUsageResponse200TotalQuotaType0]
                if isinstance(_total_quota_type_0, Unset):
                    total_quota_type_0 = UNSET
                else:
                    total_quota_type_0 = RhubapilabregiongetUsageResponse200TotalQuotaType0.from_dict(
                        _total_quota_type_0
                    )

                return total_quota_type_0
            except:  # noqa: E722
                pass
            total_quota_type_1 = data

            return total_quota_type_1

        total_quota = _parse_total_quota(d.pop("total_quota", UNSET))

        _total_quota_usage = d.pop("total_quota_usage", UNSET)
        total_quota_usage: Union[Unset, RhubapilabregiongetUsageResponse200TotalQuotaUsage]
        if isinstance(_total_quota_usage, Unset):
            total_quota_usage = UNSET
        else:
            total_quota_usage = RhubapilabregiongetUsageResponse200TotalQuotaUsage.from_dict(_total_quota_usage)

        def _parse_user_quota(data: object) -> Union[Any, RhubapilabregiongetUsageResponse200UserQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _user_quota_type_0 = data
                user_quota_type_0: Union[Unset, RhubapilabregiongetUsageResponse200UserQuotaType0]
                if isinstance(_user_quota_type_0, Unset):
                    user_quota_type_0 = UNSET
                else:
                    user_quota_type_0 = RhubapilabregiongetUsageResponse200UserQuotaType0.from_dict(_user_quota_type_0)

                return user_quota_type_0
            except:  # noqa: E722
                pass
            user_quota_type_1 = data

            return user_quota_type_1

        user_quota = _parse_user_quota(d.pop("user_quota", UNSET))

        _user_quota_usage = d.pop("user_quota_usage", UNSET)
        user_quota_usage: Union[Unset, RhubapilabregiongetUsageResponse200UserQuotaUsage]
        if isinstance(_user_quota_usage, Unset):
            user_quota_usage = UNSET
        else:
            user_quota_usage = RhubapilabregiongetUsageResponse200UserQuotaUsage.from_dict(_user_quota_usage)

        rhubapilabregionget_usage_response_200 = cls(
            openstack_limits=openstack_limits,
            total_quota=total_quota,
            total_quota_usage=total_quota_usage,
            user_quota=user_quota,
            user_quota_usage=user_quota_usage,
        )

        rhubapilabregionget_usage_response_200.additional_properties = d
        return rhubapilabregionget_usage_response_200

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
