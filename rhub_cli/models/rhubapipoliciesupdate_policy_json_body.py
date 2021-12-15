from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapipoliciesupdate_policy_json_body_constraint import RhubapipoliciesupdatePolicyJsonBodyConstraint
from ..models.rhubapipoliciesupdate_policy_json_body_id import RhubapipoliciesupdatePolicyJsonBodyId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapipoliciesupdatePolicyJsonBody")


@attr.s(auto_attribs=True)
class RhubapipoliciesupdatePolicyJsonBody:
    """ """

    constraint: Union[Unset, RhubapipoliciesupdatePolicyJsonBodyConstraint] = UNSET
    department: Union[Unset, str] = UNSET
    id: Union[Unset, RhubapipoliciesupdatePolicyJsonBodyId] = UNSET
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
        field_dict.update({})
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
        constraint: Union[Unset, RhubapipoliciesupdatePolicyJsonBodyConstraint]
        if isinstance(_constraint, Unset):
            constraint = UNSET
        else:
            constraint = RhubapipoliciesupdatePolicyJsonBodyConstraint.from_dict(_constraint)

        department = d.pop("department", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapipoliciesupdatePolicyJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapipoliciesupdatePolicyJsonBodyId.from_dict(_id)

        name = d.pop("name", UNSET)

        rhubapipoliciesupdate_policy_json_body = cls(
            constraint=constraint,
            department=department,
            id=id,
            name=name,
        )

        rhubapipoliciesupdate_policy_json_body.additional_properties = d
        return rhubapipoliciesupdate_policy_json_body

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
