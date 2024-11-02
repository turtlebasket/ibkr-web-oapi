from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialFundPosition")


@_attrs_define
class PartialFundPosition:
    """
    Attributes:
        symbol (Union[Unset, str]):
        number_of_shares (Union[Unset, int]):
        all_ (Union[Unset, bool]):
    """

    symbol: Union[Unset, str] = UNSET
    number_of_shares: Union[Unset, int] = UNSET
    all_: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol

        number_of_shares = self.number_of_shares

        all_ = self.all_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if number_of_shares is not UNSET:
            field_dict["numberOfShares"] = number_of_shares
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol", UNSET)

        number_of_shares = d.pop("numberOfShares", UNSET)

        all_ = d.pop("all", UNSET)

        partial_fund_position = cls(
            symbol=symbol,
            number_of_shares=number_of_shares,
            all_=all_,
        )

        partial_fund_position.additional_properties = d
        return partial_fund_position

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
