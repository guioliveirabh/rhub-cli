from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhubapilabproductget_product_response_200_id import RhubapilabproductgetProductResponse200Id
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubapilabproductgetProductResponse200")


@attr.s(auto_attribs=True)
class RhubapilabproductgetProductResponse200:
    """ """

    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, RhubapilabproductgetProductResponse200Id] = UNSET
    name: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[Any]] = UNSET
    tower_template_name_create: Union[Unset, str] = UNSET
    tower_template_name_delete: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        enabled = self.enabled
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name
        parameters: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.parameters, Unset):
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if tower_template_name_create is not UNSET:
            field_dict["tower_template_name_create"] = tower_template_name_create
        if tower_template_name_delete is not UNSET:
            field_dict["tower_template_name_delete"] = tower_template_name_delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapilabproductgetProductResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubapilabproductgetProductResponse200Id.from_dict(_id)

        name = d.pop("name", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:

            def _parse_parameters_item(data: object) -> Any:
                parameters_item_type_0 = data

                return parameters_item_type_0
                parameters_item_type_1 = data

                return parameters_item_type_1
                parameters_item_type_2 = data

                return parameters_item_type_2

            parameters_item = _parse_parameters_item(parameters_item_data)

            parameters.append(parameters_item)

        tower_template_name_create = d.pop("tower_template_name_create", UNSET)

        tower_template_name_delete = d.pop("tower_template_name_delete", UNSET)

        rhubapilabproductget_product_response_200 = cls(
            description=description,
            enabled=enabled,
            id=id,
            name=name,
            parameters=parameters,
            tower_template_name_create=tower_template_name_create,
            tower_template_name_delete=tower_template_name_delete,
        )

        rhubapilabproductget_product_response_200.additional_properties = d
        return rhubapilabproductget_product_response_200

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
