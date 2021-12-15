from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rhubapitowerlaunch_template_json_body_extra_vars import RhubapitowerlaunchTemplateJsonBodyExtraVars

T = TypeVar("T", bound="RhubapitowerlaunchTemplateJsonBody")


@attr.s(auto_attribs=True)
class RhubapitowerlaunchTemplateJsonBody:
    """ """

    extra_vars: RhubapitowerlaunchTemplateJsonBodyExtraVars
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extra_vars = self.extra_vars.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extra_vars": extra_vars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        extra_vars = RhubapitowerlaunchTemplateJsonBodyExtraVars.from_dict(d.pop("extra_vars"))

        rhubapitowerlaunch_template_json_body = cls(
            extra_vars=extra_vars,
        )

        rhubapitowerlaunch_template_json_body.additional_properties = d
        return rhubapitowerlaunch_template_json_body

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
