from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUser")


@_attrs_define
class CreateUser:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        prefix (Union[Unset, str]):
        user_name (Union[Unset, str]):
        id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        authorized_trader (Union[Unset, bool]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    authorized_trader: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        prefix = self.prefix

        user_name = self.user_name

        id = self.id

        external_id = self.external_id

        authorized_trader = self.authorized_trader

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if authorized_trader is not UNSET:
            field_dict["authorizedTrader"] = authorized_trader

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        prefix = d.pop("prefix", UNSET)

        user_name = d.pop("userName", UNSET)

        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        authorized_trader = d.pop("authorizedTrader", UNSET)

        create_user = cls(
            reference_account_id=reference_account_id,
            prefix=prefix,
            user_name=user_name,
            id=id,
            external_id=external_id,
            authorized_trader=authorized_trader,
        )

        create_user.additional_properties = d
        return create_user

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
