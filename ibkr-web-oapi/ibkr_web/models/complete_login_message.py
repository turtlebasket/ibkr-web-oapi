from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompleteLoginMessage")


@_attrs_define
class CompleteLoginMessage:
    """
    Attributes:
        login_message_ids (Union[Unset, List[int]]):
        reference_account_id (Union[Unset, str]):
    """

    login_message_ids: Union[Unset, List[int]] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login_message_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.login_message_ids, Unset):
            login_message_ids = self.login_message_ids

        reference_account_id = self.reference_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login_message_ids is not UNSET:
            field_dict["loginMessageIds"] = login_message_ids
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login_message_ids = cast(List[int], d.pop("loginMessageIds", UNSET))

        reference_account_id = d.pop("referenceAccountId", UNSET)

        complete_login_message = cls(
            login_message_ids=login_message_ids,
            reference_account_id=reference_account_id,
        )

        complete_login_message.additional_properties = d
        return complete_login_message

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
