from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_policies_get_policy_response_200_constraint import RhubApiPoliciesGetPolicyResponse200Constraint
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiPoliciesGetPolicyResponse200")


@attr.s(auto_attribs=True)
class RhubApiPoliciesGetPolicyResponse200:
    """
    Attributes:
        constraint (Union[Unset, RhubApiPoliciesGetPolicyResponse200Constraint]):
        department (Union[Unset, str]): Department Name
        name (Union[Unset, str]): Name
        id (Union[Unset, int]):
    """

    constraint: Union[Unset, RhubApiPoliciesGetPolicyResponse200Constraint] = UNSET
    department: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        constraint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        department = self.department
        name = self.name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constraint is not UNSET:
            field_dict["constraint"] = constraint
        if department is not UNSET:
            field_dict["department"] = department
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _constraint = d.pop("constraint", UNSET)
        constraint: Union[Unset, RhubApiPoliciesGetPolicyResponse200Constraint]
        if isinstance(_constraint, Unset):
            constraint = UNSET
        else:
            constraint = RhubApiPoliciesGetPolicyResponse200Constraint.from_dict(_constraint)

        department = d.pop("department", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        rhub_api_policies_get_policy_response_200 = cls(
            constraint=constraint,
            department=department,
            name=name,
            id=id,
        )

        rhub_api_policies_get_policy_response_200.additional_properties = d
        return rhub_api_policies_get_policy_response_200

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
