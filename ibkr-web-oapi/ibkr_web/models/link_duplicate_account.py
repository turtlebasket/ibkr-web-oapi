from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkDuplicateAccount")


@_attrs_define
class LinkDuplicateAccount:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        external_account_id (Union[Unset, str]):
        client_active_trading (Union[Unset, bool]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    external_account_id: Union[Unset, str] = UNSET
    client_active_trading: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        external_account_id = self.external_account_id

        client_active_trading = self.client_active_trading

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if client_active_trading is not UNSET:
            field_dict["clientActiveTrading"] = client_active_trading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        external_account_id = d.pop("externalAccountId", UNSET)

        client_active_trading = d.pop("clientActiveTrading", UNSET)

        link_duplicate_account = cls(
            reference_account_id=reference_account_id,
            external_account_id=external_account_id,
            client_active_trading=client_active_trading,
        )

        link_duplicate_account.additional_properties = d
        return link_duplicate_account

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
