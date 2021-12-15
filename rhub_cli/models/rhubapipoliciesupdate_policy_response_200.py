from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from ..types import UNSET, Unset
from ..models.rhubapipoliciesupdate_policy_response_200_id import RhubapipoliciesupdatePolicyResponse200Id
from ..models.rhubapipoliciesupdate_policy_response_200_constraint import RhubapipoliciesupdatePolicyResponse200Constraint
from typing import cast
from typing import Union




T = TypeVar("T", bound="RhubapipoliciesupdatePolicyResponse200")

@attr.s(auto_attribs=True)
class RhubapipoliciesupdatePolicyResponse200:
    """  """
    constraint: Union[Unset, RhubapipoliciesupdatePolicyResponse200Constraint] = UNSET
    department: Union[Unset, str] = UNSET
    id: Union[Unset, RhubapipoliciesupdatePolicyResponse200Id] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        constraint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        department = self.department
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if constraint is not UNSET:
            field_dict["constraint"] = constraint
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
        _constraint = d.pop("constraint", UNSET)
        constraint: Union[Unset, RhubapipoliciesupdatePolicyResponse200Constraint]
        if isinstance(_constraint,  Unset):
            constraint = UNSET
        else:
            constraint = RhubapipoliciesupdatePolicyResponse200Constraint.from_dict(_constraint)




        department = d.pop("department", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapipoliciesupdatePolicyResponse200Id]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = RhubapipoliciesupdatePolicyResponse200Id.from_dict(_id)




        name = d.pop("name", UNSET)

        rhubapipoliciesupdate_policy_response_200 = cls(
            constraint=constraint,
            department=department,
            id=id,
            name=name,
        )

        rhubapipoliciesupdate_policy_response_200.additional_properties = d
        return rhubapipoliciesupdate_policy_response_200

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
