from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset




T = TypeVar("T", bound="RhubapitowerlistJobsFilter")

@attr.s(auto_attribs=True)
class RhubapitowerlistJobsFilter:
    """  """
    launched_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        launched_by = self.launched_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if launched_by is not UNSET:
            field_dict["launched_by"] = launched_by

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        launched_by = d.pop("launched_by", UNSET)

        rhubapitowerlist_jobs_filter = cls(
            launched_by=launched_by,
        )

        rhubapitowerlist_jobs_filter.additional_properties = d
        return rhubapitowerlist_jobs_filter

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
