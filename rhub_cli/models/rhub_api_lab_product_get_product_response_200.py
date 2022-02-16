from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_product_get_product_response_200_flavors import RhubApiLabProductGetProductResponse200Flavors
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductGetProductResponse200")


@attr.s(auto_attribs=True)
class RhubApiLabProductGetProductResponse200:
    """
    Attributes:
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        flavors (Union[Unset, None, RhubApiLabProductGetProductResponse200Flavors]):
        name (Union[Unset, str]):  Example: OpenShift.
        parameters (Union[Unset, List[Any]]):
        tower_template_name_create (Union[Unset, str]):  Example: rhub-openshift-create.
        tower_template_name_delete (Union[Unset, str]):  Example: rhub-openshift-delete.
        id (Union[Unset, int]):
    """

    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    flavors: Union[Unset, None, RhubApiLabProductGetProductResponse200Flavors] = UNSET
    name: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[Any]] = UNSET
    tower_template_name_create: Union[Unset, str] = UNSET
    tower_template_name_delete: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        enabled = self.enabled
        flavors: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.flavors, Unset):
            flavors = self.flavors.to_dict() if self.flavors else None

        name = self.name
        parameters: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:

                parameters_item = parameters_item_data

                parameters.append(parameters_item)

        tower_template_name_create = self.tower_template_name_create
        tower_template_name_delete = self.tower_template_name_delete
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if flavors is not UNSET:
            field_dict["flavors"] = flavors
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if tower_template_name_create is not UNSET:
            field_dict["tower_template_name_create"] = tower_template_name_create
        if tower_template_name_delete is not UNSET:
            field_dict["tower_template_name_delete"] = tower_template_name_delete
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _flavors = d.pop("flavors", UNSET)
        flavors: Union[Unset, None, RhubApiLabProductGetProductResponse200Flavors]
        if _flavors is None:
            flavors = None
        elif isinstance(_flavors, Unset):
            flavors = UNSET
        else:
            flavors = RhubApiLabProductGetProductResponse200Flavors.from_dict(_flavors)

        name = d.pop("name", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:

            def _parse_parameters_item(data: object) -> Any:
                return cast(Any, data)

            parameters_item = _parse_parameters_item(parameters_item_data)

            parameters.append(parameters_item)

        tower_template_name_create = d.pop("tower_template_name_create", UNSET)

        tower_template_name_delete = d.pop("tower_template_name_delete", UNSET)

        id = d.pop("id", UNSET)

        rhub_api_lab_product_get_product_response_200 = cls(
            description=description,
            enabled=enabled,
            flavors=flavors,
            name=name,
            parameters=parameters,
            tower_template_name_create=tower_template_name_create,
            tower_template_name_delete=tower_template_name_delete,
            id=id,
        )

        rhub_api_lab_product_get_product_response_200.additional_properties = d
        return rhub_api_lab_product_get_product_response_200

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
