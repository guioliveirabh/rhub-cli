import datetime
from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.rhub_api_scheduler_cron_list_jobs_response_200_data_item_job_name import (
    RhubApiSchedulerCronListJobsResponse200DataItemJobName,
)
from ..models.rhub_api_scheduler_cron_list_jobs_response_200_data_item_job_params import (
    RhubApiSchedulerCronListJobsResponse200DataItemJobParams,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiSchedulerCronListJobsResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiSchedulerCronListJobsResponse200DataItem:
    """
    Attributes:
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        job_name (Union[Unset, RhubApiSchedulerCronListJobsResponse200DataItemJobName]):
        job_params (Union[Unset, None, RhubApiSchedulerCronListJobsResponse200DataItemJobParams]):
        last_run (Union[Unset, None, datetime.datetime]):
        name (Union[Unset, str]):
        time_expr (Union[Unset, str]): cron time expression
        id (Union[Unset, int]):
    """

    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    job_name: Union[Unset, RhubApiSchedulerCronListJobsResponse200DataItemJobName] = UNSET
    job_params: Union[Unset, None, RhubApiSchedulerCronListJobsResponse200DataItemJobParams] = UNSET
    last_run: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    time_expr: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        enabled = self.enabled
        job_name: Union[Unset, str] = UNSET
        if not isinstance(self.job_name, Unset):
            job_name = self.job_name.value

        job_params: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.job_params, Unset):
            job_params = self.job_params.to_dict() if self.job_params else None

        last_run: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat() if self.last_run else None

        name = self.name
        time_expr = self.time_expr
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if job_name is not UNSET:
            field_dict["job_name"] = job_name
        if job_params is not UNSET:
            field_dict["job_params"] = job_params
        if last_run is not UNSET:
            field_dict["last_run"] = last_run
        if name is not UNSET:
            field_dict["name"] = name
        if time_expr is not UNSET:
            field_dict["time_expr"] = time_expr
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _job_name = d.pop("job_name", UNSET)
        job_name: Union[Unset, RhubApiSchedulerCronListJobsResponse200DataItemJobName]
        if isinstance(_job_name, Unset):
            job_name = UNSET
        else:
            job_name = RhubApiSchedulerCronListJobsResponse200DataItemJobName(_job_name)

        _job_params = d.pop("job_params", UNSET)
        job_params: Union[Unset, None, RhubApiSchedulerCronListJobsResponse200DataItemJobParams]
        if _job_params is None:
            job_params = None
        elif isinstance(_job_params, Unset):
            job_params = UNSET
        else:
            job_params = RhubApiSchedulerCronListJobsResponse200DataItemJobParams.from_dict(_job_params)

        _last_run = d.pop("last_run", UNSET)
        last_run: Union[Unset, None, datetime.datetime]
        if _last_run is None:
            last_run = None
        elif isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        name = d.pop("name", UNSET)

        time_expr = d.pop("time_expr", UNSET)

        id = d.pop("id", UNSET)

        rhub_api_scheduler_cron_list_jobs_response_200_data_item = cls(
            description=description,
            enabled=enabled,
            job_name=job_name,
            job_params=job_params,
            last_run=last_run,
            name=name,
            time_expr=time_expr,
            id=id,
        )

        rhub_api_scheduler_cron_list_jobs_response_200_data_item.additional_properties = d
        return rhub_api_scheduler_cron_list_jobs_response_200_data_item

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
