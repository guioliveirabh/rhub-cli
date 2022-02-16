from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerUpdateTemplateJsonBody")


@attr.s(auto_attribs=True)
class RhubApiTowerUpdateTemplateJsonBody:
    """
    Attributes:
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        server_id (Union[Unset, int]):
        tower_template_id (Union[Unset, int]):
        tower_template_is_workflow (Union[Unset, bool]): Is template workflow?
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    server_id: Union[Unset, int] = UNSET
    tower_template_id: Union[Unset, int] = UNSET
    tower_template_is_workflow: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        server_id = self.server_id
        tower_template_id = self.tower_template_id
        tower_template_is_workflow = self.tower_template_is_workflow

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if tower_template_id is not UNSET:
            field_dict["tower_template_id"] = tower_template_id
        if tower_template_is_workflow is not UNSET:
            field_dict["tower_template_is_workflow"] = tower_template_is_workflow

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        server_id = d.pop("server_id", UNSET)

        tower_template_id = d.pop("tower_template_id", UNSET)

        tower_template_is_workflow = d.pop("tower_template_is_workflow", UNSET)

        rhub_api_tower_update_template_json_body = cls(
            description=description,
            name=name,
            server_id=server_id,
            tower_template_id=tower_template_id,
            tower_template_is_workflow=tower_template_is_workflow,
        )

        rhub_api_tower_update_template_json_body.additional_properties = d
        return rhub_api_tower_update_template_json_body

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
