from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapipoliciescreate_policy_json_body_constraint import RhubapipoliciescreatePolicyJsonBodyConstraint
from ..models.rhubapipoliciescreate_policy_json_body_id import RhubapipoliciescreatePolicyJsonBodyId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapipoliciescreatePolicyJsonBody")


@attr.s(auto_attribs=True)
class RhubapipoliciescreatePolicyJsonBody:
    """ """

    department: str
    name: str
    constraint: Union[Unset, RhubapipoliciescreatePolicyJsonBodyConstraint] = UNSET
    id: Union[Unset, RhubapipoliciescreatePolicyJsonBodyId] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        department = self.department
        name = self.name
        constraint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "department": department,
                "name": name,
            }
        )
        if constraint is not UNSET:
            field_dict["constraint"] = constraint
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        department = d.pop("department")

        name = d.pop("name")

        _constraint = d.pop("constraint", UNSET)
        constraint: Union[Unset, RhubapipoliciescreatePolicyJsonBodyConstraint]
        if isinstance(_constraint, Unset):
            constraint = UNSET
        else:
            constraint = RhubapipoliciescreatePolicyJsonBodyConstraint.from_dict(_constraint)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapipoliciescreatePolicyJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapipoliciescreatePolicyJsonBodyId.from_dict(_id)

        rhubapipoliciescreate_policy_json_body = cls(
            department=department,
            name=name,
            constraint=constraint,
            id=id,
        )

        rhubapipoliciescreate_policy_json_body.additional_properties = d
        return rhubapipoliciescreate_policy_json_body

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
