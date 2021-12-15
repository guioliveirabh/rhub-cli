from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast, List
from ..models.rhubapitowerlist_jobs_response_200_data_item import RhubapitowerlistJobsResponse200DataItem
from typing import cast
from typing import Union
from ..types import UNSET, Unset
from typing import Dict




T = TypeVar("T", bound="RhubapitowerlistJobsResponse200")

@attr.s(auto_attribs=True)
class RhubapitowerlistJobsResponse200:
    """  """
    data: Union[Unset, List[RhubapitowerlistJobsResponse200DataItem]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)




        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in (_data or []):
            data_item = RhubapitowerlistJobsResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        total = d.pop("total", UNSET)

        rhubapitowerlist_jobs_response_200 = cls(
            data=data,
            total=total,
        )

        rhubapitowerlist_jobs_response_200.additional_properties = d
        return rhubapitowerlist_jobs_response_200

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
