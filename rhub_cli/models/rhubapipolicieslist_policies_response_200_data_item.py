from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.rhubapipolicieslist_policies_response_200_data_item_id import RhubapipolicieslistPoliciesResponse200DataItemId
from typing import cast
from typing import Union
from ..types import UNSET, Unset
from typing import Dict




T = TypeVar("T", bound="RhubapipolicieslistPoliciesResponse200DataItem")

@attr.s(auto_attribs=True)
class RhubapipolicieslistPoliciesResponse200DataItem:
    """  """
    department: Union[Unset, str] = UNSET
    id: Union[Unset, RhubapipolicieslistPoliciesResponse200DataItemId] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        department = self.department
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if department is not UNSET:
            field_dict["department"] = department
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        department = d.pop("department", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapipolicieslistPoliciesResponse200DataItemId]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = RhubapipolicieslistPoliciesResponse200DataItemId.from_dict(_id)




        name = d.pop("name", UNSET)

        rhubapipolicieslist_policies_response_200_data_item = cls(
            department=department,
            id=id,
            name=name,
        )

        rhubapipolicieslist_policies_response_200_data_item.additional_properties = d
        return rhubapipolicieslist_policies_response_200_data_item

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
