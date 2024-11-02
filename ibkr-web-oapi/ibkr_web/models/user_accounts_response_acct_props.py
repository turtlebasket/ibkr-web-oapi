from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_accounts_response_acct_props_u1234567 import UserAccountsResponseAcctPropsU1234567


T = TypeVar("T", bound="UserAccountsResponseAcctProps")


@_attrs_define
class UserAccountsResponseAcctProps:
    """Returns an json object for each accessible account’s properties.

    Attributes:
        u1234567 (Union[Unset, UserAccountsResponseAcctPropsU1234567]):
    """

    u1234567: Union[Unset, "UserAccountsResponseAcctPropsU1234567"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        u1234567: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.u1234567, Unset):
            u1234567 = self.u1234567.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if u1234567 is not UNSET:
            field_dict["U1234567"] = u1234567

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_accounts_response_acct_props_u1234567 import UserAccountsResponseAcctPropsU1234567

        d = src_dict.copy()
        _u1234567 = d.pop("U1234567", UNSET)
        u1234567: Union[Unset, UserAccountsResponseAcctPropsU1234567]
        if isinstance(_u1234567, Unset):
            u1234567 = UNSET
        else:
            u1234567 = UserAccountsResponseAcctPropsU1234567.from_dict(_u1234567)

        user_accounts_response_acct_props = cls(
            u1234567=u1234567,
        )

        user_accounts_response_acct_props.additional_properties = d
        return user_accounts_response_acct_props

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
