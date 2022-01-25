import datetime
from copy import copy
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.rhub_api_lab_cluster_create_cluster_response_200_hosts_item import (
    RhubApiLabClusterCreateClusterResponse200HostsItem,
)
from ..models.rhub_api_lab_cluster_create_cluster_response_200_id import RhubApiLabClusterCreateClusterResponse200Id
from ..models.rhub_api_lab_cluster_create_cluster_response_200_product_params import (
    RhubApiLabClusterCreateClusterResponse200ProductParams,
)
from ..models.rhub_api_lab_cluster_create_cluster_response_200_quota_type_0 import (
    RhubApiLabClusterCreateClusterResponse200QuotaType0,
)
from ..models.rhub_api_lab_cluster_create_cluster_response_200_quota_usage_type_0 import (
    RhubApiLabClusterCreateClusterResponse200QuotaUsageType0,
)
from ..models.rhub_api_lab_cluster_create_cluster_response_200_status import (
    RhubApiLabClusterCreateClusterResponse200Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabClusterCreateClusterResponse200")


@attr.s(auto_attribs=True)
class RhubApiLabClusterCreateClusterResponse200:
    """
    Attributes:
        name (str):
        product_id (int):
        product_params (RhubApiLabClusterCreateClusterResponse200ProductParams):
        region_id (int):
        created (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        group_id (Union[Unset, None, str]):
        group_name (Union[Unset, None, str]):
        hosts (Union[Unset, List[RhubApiLabClusterCreateClusterResponse200HostsItem]]):
        id (Union[Unset, RhubApiLabClusterCreateClusterResponse200Id]):
        lifespan_expiration (Union[Unset, None, datetime.datetime]): Hard-limit expiration.
        product_name (Union[Unset, str]):
        quota (Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaType0, Unset]):  Example: {'num_vcpus': 40,
            'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        quota_usage (Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaUsageType0, Unset]):  Example:
            {'num_vcpus': 16, 'num_volumes': 2, 'ram_mb': 64000, 'volumes_gb': 256}.
        region_name (Union[Unset, str]):
        reservation_expiration (Optional[datetime.datetime]): Soft-limit expiration.
        shared (Union[Unset, bool]):
        status (Union[Unset, None, RhubApiLabClusterCreateClusterResponse200Status]):
        user_id (Union[Unset, str]):
        user_name (Union[Unset, str]):
    """

    name: str
    product_id: int
    product_params: RhubApiLabClusterCreateClusterResponse200ProductParams
    region_id: int
    reservation_expiration: Optional[datetime.datetime]
    created: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    group_id: Union[Unset, None, str] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    hosts: Union[Unset, List[RhubApiLabClusterCreateClusterResponse200HostsItem]] = UNSET
    id: Union[Unset, RhubApiLabClusterCreateClusterResponse200Id] = UNSET
    lifespan_expiration: Union[Unset, None, datetime.datetime] = UNSET
    product_name: Union[Unset, str] = UNSET
    quota: Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaType0, Unset] = UNSET
    quota_usage: Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaUsageType0, Unset] = UNSET
    region_name: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    status: Union[Unset, None, RhubApiLabClusterCreateClusterResponse200Status] = UNSET
    user_id: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        product_id = self.product_id
        product_params = self.product_params.to_dict()

        region_id = self.region_id
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

        product_name = self.product_name
        quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.quota, Unset):
            quota = UNSET

        elif isinstance(self.quota, RhubApiLabClusterCreateClusterResponse200QuotaType0):
            quota = UNSET
            if not isinstance(self.quota, Unset):
                quota = self.quota.to_dict()

        else:
            quota = self.quota

        quota_usage: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.quota_usage, Unset):
            quota_usage = UNSET

        elif isinstance(self.quota_usage, RhubApiLabClusterCreateClusterResponse200QuotaUsageType0):
            quota_usage = UNSET
            if not isinstance(self.quota_usage, Unset):
                quota_usage = self.quota_usage.to_dict()

        else:
            quota_usage = self.quota_usage

        region_name = self.region_name
        reservation_expiration = self.reservation_expiration.isoformat() if self.reservation_expiration else None

        shared = self.shared
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        user_id = self.user_id
        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "product_id": product_id,
                "product_params": product_params,
                "region_id": region_id,
                "reservation_expiration": reservation_expiration,
            }
        )
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
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if quota is not UNSET:
            field_dict["quota"] = quota
        if quota_usage is not UNSET:
            field_dict["quota_usage"] = quota_usage
        if region_name is not UNSET:
            field_dict["region_name"] = region_name
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
        name = d.pop("name")

        product_id = d.pop("product_id")

        product_params = RhubApiLabClusterCreateClusterResponse200ProductParams.from_dict(d.pop("product_params"))

        region_id = d.pop("region_id")

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
            hosts_item = RhubApiLabClusterCreateClusterResponse200HostsItem.from_dict(hosts_item_data)

            hosts.append(hosts_item)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiLabClusterCreateClusterResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiLabClusterCreateClusterResponse200Id.from_dict(_id)

        _lifespan_expiration = d.pop("lifespan_expiration", UNSET)
        lifespan_expiration: Union[Unset, None, datetime.datetime]
        if _lifespan_expiration is None:
            lifespan_expiration = None
        elif isinstance(_lifespan_expiration, Unset):
            lifespan_expiration = UNSET
        else:
            lifespan_expiration = isoparse(_lifespan_expiration)

        product_name = d.pop("product_name", UNSET)

        def _parse_quota(data: object) -> Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _quota_type_0 = data
                quota_type_0: Union[Unset, RhubApiLabClusterCreateClusterResponse200QuotaType0]
                if isinstance(_quota_type_0, Unset):
                    quota_type_0 = UNSET
                else:
                    quota_type_0 = RhubApiLabClusterCreateClusterResponse200QuotaType0.from_dict(_quota_type_0)

                return quota_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaType0, Unset], data)

        quota = _parse_quota(d.pop("quota", UNSET))

        def _parse_quota_usage(
            data: object,
        ) -> Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaUsageType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _quota_usage_type_0 = data
                quota_usage_type_0: Union[Unset, RhubApiLabClusterCreateClusterResponse200QuotaUsageType0]
                if isinstance(_quota_usage_type_0, Unset):
                    quota_usage_type_0 = UNSET
                else:
                    quota_usage_type_0 = RhubApiLabClusterCreateClusterResponse200QuotaUsageType0.from_dict(
                        _quota_usage_type_0
                    )

                return quota_usage_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabClusterCreateClusterResponse200QuotaUsageType0, Unset], data)

        quota_usage = _parse_quota_usage(d.pop("quota_usage", UNSET))

        region_name = d.pop("region_name", UNSET)

        _reservation_expiration = d.pop("reservation_expiration")
        reservation_expiration: Optional[datetime.datetime]
        if _reservation_expiration is None:
            reservation_expiration = None
        else:
            reservation_expiration = isoparse(_reservation_expiration)

        shared = d.pop("shared", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, RhubApiLabClusterCreateClusterResponse200Status]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = RhubApiLabClusterCreateClusterResponse200Status(_status)

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        rhub_api_lab_cluster_create_cluster_response_200 = cls(
            name=name,
            product_id=product_id,
            product_params=product_params,
            region_id=region_id,
            created=created,
            description=description,
            group_id=group_id,
            group_name=group_name,
            hosts=hosts,
            id=id,
            lifespan_expiration=lifespan_expiration,
            product_name=product_name,
            quota=quota,
            quota_usage=quota_usage,
            region_name=region_name,
            reservation_expiration=reservation_expiration,
            shared=shared,
            status=status,
            user_id=user_id,
            user_name=user_name,
        )

        rhub_api_lab_cluster_create_cluster_response_200.additional_properties = d
        return rhub_api_lab_cluster_create_cluster_response_200

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
