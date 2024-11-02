from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEmail")


@_attrs_define
class UpdateEmail:
    """
    Attributes:
        email (Union[Unset, str]):
        token (Union[Unset, str]):
        access (Union[Unset, bool]):
        external_id (Union[Unset, str]):
        entity_id (Union[Unset, str]):
    """

    email: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    access: Union[Unset, bool] = UNSET
    external_id: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        token = self.token

        access = self.access

        external_id = self.external_id

        entity_id = self.entity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if token is not UNSET:
            field_dict["token"] = token
        if access is not UNSET:
            field_dict["access"] = access
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        token = d.pop("token", UNSET)

        access = d.pop("access", UNSET)

        external_id = d.pop("externalId", UNSET)

        entity_id = d.pop("entityId", UNSET)

        update_email = cls(
            email=email,
            token=token,
            access=access,
            external_id=external_id,
            entity_id=entity_id,
        )

        update_email.additional_properties = d
        return update_email

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
