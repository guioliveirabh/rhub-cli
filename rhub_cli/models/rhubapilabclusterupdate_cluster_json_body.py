import datetime
from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.rhubapilabclusterupdate_cluster_json_body_hosts_item import (
    RhubapilabclusterupdateClusterJsonBodyHostsItem,
)
from ..models.rhubapilabclusterupdate_cluster_json_body_id import RhubapilabclusterupdateClusterJsonBodyId
from ..models.rhubapilabclusterupdate_cluster_json_body_product_params import (
    RhubapilabclusterupdateClusterJsonBodyProductParams,
)
from ..models.rhubapilabclusterupdate_cluster_json_body_quota_type_0 import (
    RhubapilabclusterupdateClusterJsonBodyQuotaType0,
)
from ..models.rhubapilabclusterupdate_cluster_json_body_quota_usage_type_0 import (
    RhubapilabclusterupdateClusterJsonBodyQuotaUsageType0,
)
from ..models.rhubapilabclusterupdate_cluster_json_body_status import RhubapilabclusterupdateClusterJsonBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabclusterupdateClusterJsonBody")


@attr.s(auto_attribs=True)
class RhubapilabclusterupdateClusterJsonBody:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        group_id (Union[Unset, None, str]):
        group_name (Union[Unset, None, str]):
        hosts (Union[Unset, List[RhubapilabclusterupdateClusterJsonBodyHostsItem]]):
        id (Union[Unset, RhubapilabclusterupdateClusterJsonBodyId]):
        lifespan_expiration (Union[Unset, None, datetime.datetime]): Hard-limit expiration.
        name (Union[Unset, str]):
        product_id (Union[Unset, int]):
        product_name (Union[Unset, str]):
        product_params (Union[Unset, RhubapilabclusterupdateClusterJsonBodyProductParams]):
        quota (Union[Any, RhubapilabclusterupdateClusterJsonBodyQuotaType0, Unset]):  Example: {'num_vcpus': 40,
            'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        quota_usage (Union[Any, RhubapilabclusterupdateClusterJsonBodyQuotaUsageType0, Unset]):  Example: {'num_vcpus':
            16, 'num_volumes': 2, 'ram_mb': 64000, 'volumes_gb': 256}.
        region_id (Union[Unset, int]):
        region_name (Union[Unset, str]):
        reservation_expiration (Union[Unset, None, datetime.datetime]): Soft-limit expiration.
        shared (Union[Unset, bool]):
        status (Union[Unset, None, RhubapilabclusterupdateClusterJsonBodyStatus]):
        user_id (Union[Unset, str]):
        user_name (Union[Unset, str]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    group_id: Union[Unset, None, str] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    hosts: Union[Unset, List[RhubapilabclusterupdateClusterJsonBodyHostsItem]] = UNSET
    id: Union[Unset, RhubapilabclusterupdateClusterJsonBodyId] = UNSET
    lifespan_expiration: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    product_id: Union[Unset, int] = UNSET
    product_name: Union[Unset, str] = UNSET
    product_params: Union[Unset, RhubapilabclusterupdateClusterJsonBodyProductParams] = UNSET
    quota: Union[Any, RhubapilabclusterupdateClusterJsonBodyQuotaType0, Unset] = UNSET
    quota_usage: Union[Any, RhubapilabclusterupdateClusterJsonBodyQuotaUsageType0, Unset] = UNSET
    region_id: Union[Unset, int] = UNSET
    region_name: Union[Unset, str] = UNSET
    reservation_expiration: Union[Unset, None, datetime.datetime] = UNSET
    shared: Union[Unset, bool] = UNSET
    status: Union[Unset, None, RhubapilabclusterupdateClusterJsonBodyStatus] = UNSET
    user_id: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        description = self.description
        group_id = self.group_id
        group_name = self.group_name
        hosts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()

                hosts.append(hosts_item)

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        lifespan_expiration: Union[Unset, None, str] = UNSET
        if not isinstance(self.lifespan_expiration, Unset):
            lifespan_expiration = self.lifespan_expiration.isoformat() if self.lifespan_expiration else None

        name = self.name
        product_id = self.product_id
        product_name = self.product_name
        product_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_params, Unset):
            product_params = self.product_params.to_dict()

        quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.quota, Unset):
            quota = UNSET
        elif isinstance(self.quota, RhubapilabclusterupdateClusterJsonBodyQuotaType0):
            quota = UNSET
            if not isinstance(self.quota, Unset):
                quota = self.quota.to_dict()

        else:
            quota = self.quota

        quota_usage: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.quota_usage, Unset):
            quota_usage = UNSET
        elif isinstance(self.quota_usage, RhubapilabclusterupdateClusterJsonBodyQuotaUsageType0):
            quota_usage = UNSET
            if not isinstance(self.quota_usage, Unset):
                quota_usage = self.quota_usage.to_dict()

        else:
            quota_usage = self.quota_usage

        region_id = self.region_id
        region_name = self.region_name
        reservation_expiration: Union[Unset, None, str] = UNSET
        if not isinstance(self.reservation_expiration, Unset):
            reservation_expiration = self.reservation_expiration.isoformat() if self.reservation_expiration else None

        shared = self.shared
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        user_id = self.user_id
        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if id is not UNSET:
            field_dict["id"] = id
        if lifespan_expiration is not UNSET:
            field_dict["lifespan_expiration"] = lifespan_expiration
        if name is not UNSET:
            field_dict["name"] = name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_params is not UNSET:
            field_dict["product_params"] = product_params
        if quota is not UNSET:
            field_dict["quota"] = quota
        if quota_usage is not UNSET:
            field_dict["quota_usage"] = quota_usage
        if region_id is not UNSET:
            field_dict["region_id"] = region_id
        if region_name is not UNSET:
            field_dict["region_name"] = region_name
        if reservation_expiration is not UNSET:
            field_dict["reservation_expiration"] = reservation_expiration
        if shared is not UNSET:
            field_dict["shared"] = shared
        if status is not UNSET:
            field_dict["status"] = status
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        description = d.pop("description", UNSET)

        group_id = d.pop("group_id", UNSET)

        group_name = d.pop("group_name", UNSET)

        hosts = []
        _hosts = d.pop("hosts", UNSET)
        for hosts_item_data in _hosts or []:
            hosts_item = RhubapilabclusterupdateClusterJsonBodyHostsItem.from_dict(hosts_item_data)

            hosts.append(hosts_item)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabclusterupdateClusterJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapilabclusterupdateClusterJsonBodyId.from_dict(_id)

        _lifespan_expiration = d.pop("lifespan_expiration", UNSET)
        lifespan_expiration: Union[Unset, None, datetime.datetime]
        if _lifespan_expiration is None:
            lifespan_expiration = None
        elif isinstance(_lifespan_expiration, Unset):
            lifespan_expiration = UNSET
        else:
            lifespan_expiration = isoparse(_lifespan_expiration)

        name = d.pop("name", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        _product_params = d.pop("product_params", UNSET)
        product_params: Union[Unset, RhubapilabclusterupdateClusterJsonBodyProductParams]
        if isinstance(_product_params, Unset):
            product_params = UNSET
        else:
            product_params = RhubapilabclusterupdateClusterJsonBodyProductParams.from_dict(_product_params)

        def _parse_quota(data: object) -> Union[Any, RhubapilabclusterupdateClusterJsonBodyQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _quota_type_0 = data
                quota_type_0: Union[Unset, RhubapilabclusterupdateClusterJsonBodyQuotaType0]
                if isinstance(_quota_type_0, Unset):
                    quota_type_0 = UNSET
                else:
                    quota_type_0 = RhubapilabclusterupdateClusterJsonBodyQuotaType0.from_dict(_quota_type_0)

                return quota_type_0
            except:  # noqa: E722
                pass
            quota_type_1 = data

            return quota_type_1

        quota = _parse_quota(d.pop("quota", UNSET))

        def _parse_quota_usage(
            data: object,
        ) -> Union[Any, RhubapilabclusterupdateClusterJsonBodyQuotaUsageType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _quota_usage_type_0 = data
                quota_usage_type_0: Union[Unset, RhubapilabclusterupdateClusterJsonBodyQuotaUsageType0]
                if isinstance(_quota_usage_type_0, Unset):
                    quota_usage_type_0 = UNSET
                else:
                    quota_usage_type_0 = RhubapilabclusterupdateClusterJsonBodyQuotaUsageType0.from_dict(
                        _quota_usage_type_0
                    )

                return quota_usage_type_0
            except:  # noqa: E722
                pass
            quota_usage_type_1 = data

            return quota_usage_type_1

        quota_usage = _parse_quota_usage(d.pop("quota_usage", UNSET))

        region_id = d.pop("region_id", UNSET)

        region_name = d.pop("region_name", UNSET)

        _reservation_expiration = d.pop("reservation_expiration", UNSET)
        reservation_expiration: Union[Unset, None, datetime.datetime]
        if _reservation_expiration is None:
            reservation_expiration = None
        elif isinstance(_reservation_expiration, Unset):
            reservation_expiration = UNSET
        else:
            reservation_expiration = isoparse(_reservation_expiration)

        shared = d.pop("shared", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, RhubapilabclusterupdateClusterJsonBodyStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = RhubapilabclusterupdateClusterJsonBodyStatus(_status)

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        rhubapilabclusterupdate_cluster_json_body = cls(
            created=created,
            description=description,
            group_id=group_id,
            group_name=group_name,
            hosts=hosts,
            id=id,
            lifespan_expiration=lifespan_expiration,
            name=name,
            product_id=product_id,
            product_name=product_name,
            product_params=product_params,
            quota=quota,
            quota_usage=quota_usage,
            region_id=region_id,
            region_name=region_name,
            reservation_expiration=reservation_expiration,
            shared=shared,
            status=status,
            user_id=user_id,
            user_name=user_name,
        )

        rhubapilabclusterupdate_cluster_json_body.additional_properties = d
        return rhubapilabclusterupdate_cluster_json_body

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
