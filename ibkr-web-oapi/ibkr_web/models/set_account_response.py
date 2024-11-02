from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAccountResponse")


@_attrs_define
class SetAccountResponse:
    """
    Attributes:
        set_ (Union[Unset, bool]): Confirms that the account change was set
        acct_id (Union[Unset, str]): Confirms the account switched to.
    """

    set_: Union[Unset, bool] = UNSET
    acct_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        set_ = self.set_

        acct_id = self.acct_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if set_ is not UNSET:
            field_dict["set"] = set_
        if acct_id is not UNSET:
            field_dict["acctId"] = acct_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        set_ = d.pop("set", UNSET)

        acct_id = d.pop("acctId", UNSET)

        set_account_response = cls(
            set_=set_,
            acct_id=acct_id,
        )

        set_account_response.additional_properties = d
        return set_account_response

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
