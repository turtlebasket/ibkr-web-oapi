from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccountsResponseAliases")


@_attrs_define
class UserAccountsResponseAliases:
    """
    Attributes:
        u1234567 (Union[Unset, str]):
    """

    u1234567: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        u1234567 = self.u1234567

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if u1234567 is not UNSET:
            field_dict["U1234567"] = u1234567

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        u1234567 = d.pop("U1234567", UNSET)

        user_accounts_response_aliases = cls(
            u1234567=u1234567,
        )

        user_accounts_response_aliases.additional_properties = d
        return user_accounts_response_aliases

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
