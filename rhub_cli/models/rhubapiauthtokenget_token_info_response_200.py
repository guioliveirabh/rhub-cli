from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset





T = TypeVar("T", bound="RhubapiauthtokengetTokenInfoResponse200")

@attr.s(auto_attribs=True)
class RhubapiauthtokengetTokenInfoResponse200:
    """ See [RFC 7662, Section 2.2](https://tools.ietf.org/html/rfc7662#section-2.2)
and [Keycloak API: AccessToken](https://www.keycloak.org/docs-api/11.0/rest-api/#_accesstoken)
 """
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rhubapiauthtokenget_token_info_response_200 = cls(
        )

        rhubapiauthtokenget_token_info_response_200.additional_properties = d
        return rhubapiauthtokenget_token_info_response_200

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
