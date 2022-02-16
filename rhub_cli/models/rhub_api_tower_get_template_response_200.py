from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_tower_get_template_response_200_tower_survey import RhubApiTowerGetTemplateResponse200TowerSurvey
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerGetTemplateResponse200")


@attr.s(auto_attribs=True)
class RhubApiTowerGetTemplateResponse200:
    """
    Attributes:
        tower_survey (Union[Unset, RhubApiTowerGetTemplateResponse200TowerSurvey]): Survey spec from Tower API
    """

    tower_survey: Union[Unset, RhubApiTowerGetTemplateResponse200TowerSurvey] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tower_survey: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tower_survey, Unset):
            tower_survey = self.tower_survey.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tower_survey is not UNSET:
            field_dict["tower_survey"] = tower_survey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _tower_survey = d.pop("tower_survey", UNSET)
        tower_survey: Union[Unset, RhubApiTowerGetTemplateResponse200TowerSurvey]
        if isinstance(_tower_survey, Unset):
            tower_survey = UNSET
        else:
            tower_survey = RhubApiTowerGetTemplateResponse200TowerSurvey.from_dict(_tower_survey)

        rhub_api_tower_get_template_response_200 = cls(
            tower_survey=tower_survey,
        )

        rhub_api_tower_get_template_response_200.additional_properties = d
        return rhub_api_tower_get_template_response_200

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
