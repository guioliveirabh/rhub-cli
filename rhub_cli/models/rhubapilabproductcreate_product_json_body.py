from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabproductcreate_product_json_body_flavors import RhubapilabproductcreateProductJsonBodyFlavors
from ..models.rhubapilabproductcreate_product_json_body_id import RhubapilabproductcreateProductJsonBodyId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabproductcreateProductJsonBody")


@attr.s(auto_attribs=True)
class RhubapilabproductcreateProductJsonBody:
    """
    Attributes:
        name (str):  Example: OpenShift.
        parameters (List[Any]):
        tower_template_name_create (str):  Example: rhub-openshift-create.
        tower_template_name_delete (str):  Example: rhub-openshift-delete.
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        flavors (Union[Unset, None, RhubapilabproductcreateProductJsonBodyFlavors]):
        id (Union[Unset, RhubapilabproductcreateProductJsonBodyId]):
    """

    name: str
    parameters: List[Any]
    tower_template_name_create: str
    tower_template_name_delete: str
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    flavors: Union[Unset, None, RhubapilabproductcreateProductJsonBodyFlavors] = UNSET
    id: Union[Unset, RhubapilabproductcreateProductJsonBodyId] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        parameters = []
        for parameters_item_data in self.parameters:
            if isinstance(parameters_item_data, Any):
                parameters_item = parameters_item_data

            elif isinstance(parameters_item_data, Any):
                parameters_item = parameters_item_data

            else:
                parameters_item = parameters_item_data

            parameters.append(parameters_item)

        tower_template_name_create = self.tower_template_name_create
        tower_template_name_delete = self.tower_template_name_delete
        description = self.description
        enabled = self.enabled
        flavors: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.flavors, Unset):
            flavors = self.flavors.to_dict() if self.flavors else None

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parameters": parameters,
                "tower_template_name_create": tower_template_name_create,
                "tower_template_name_delete": tower_template_name_delete,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if flavors is not UNSET:
            field_dict["flavors"] = flavors
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:

            def _parse_parameters_item(data: object) -> Any:
                parameters_item_type_0 = data

                return parameters_item_type_0
                parameters_item_type_1 = data

                return parameters_item_type_1
                parameters_item_type_2 = data

                return parameters_item_type_2

            parameters_item = _parse_parameters_item(parameters_item_data)

            parameters.append(parameters_item)

        tower_template_name_create = d.pop("tower_template_name_create")

        tower_template_name_delete = d.pop("tower_template_name_delete")

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _flavors = d.pop("flavors", UNSET)
        flavors: Union[Unset, None, RhubapilabproductcreateProductJsonBodyFlavors]
        if _flavors is None:
            flavors = None
        elif isinstance(_flavors, Unset):
            flavors = UNSET
        else:
            flavors = RhubapilabproductcreateProductJsonBodyFlavors.from_dict(_flavors)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabproductcreateProductJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapilabproductcreateProductJsonBodyId.from_dict(_id)

        rhubapilabproductcreate_product_json_body = cls(
            name=name,
            parameters=parameters,
            tower_template_name_create=tower_template_name_create,
            tower_template_name_delete=tower_template_name_delete,
            description=description,
            enabled=enabled,
            flavors=flavors,
            id=id,
        )

        rhubapilabproductcreate_product_json_body.additional_properties = d
        return rhubapilabproductcreate_product_json_body

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
