from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.rhubapiauthuserupdate_user_json_body_id import RhubapiauthuserupdateUserJsonBodyId
from typing import cast
from typing import Union
from ..types import UNSET, Unset
from typing import Dict




T = TypeVar("T", bound="RhubapiauthuserupdateUserJsonBody")

@attr.s(auto_attribs=True)
class RhubapiauthuserupdateUserJsonBody:
    """ See [Keycloak API: UserRepresentation](
  https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
 """
    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, RhubapiauthuserupdateUserJsonBodyId] = UNSET
    last_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        enabled = self.enabled
        first_name = self.first_name
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        last_name = self.last_name
        password = self.password
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        first_name = d.pop("firstName", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubapiauthuserupdateUserJsonBodyId]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = RhubapiauthuserupdateUserJsonBodyId.from_dict(_id)




        last_name = d.pop("lastName", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        rhubapiauthuserupdate_user_json_body = cls(
            email=email,
            enabled=enabled,
            first_name=first_name,
            id=id,
            last_name=last_name,
            password=password,
            username=username,
        )

        rhubapiauthuserupdate_user_json_body.additional_properties = d
        return rhubapiauthuserupdate_user_json_body

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
