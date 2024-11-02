from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partial_warrant_position_option_type import PartialWarrantPositionOptionType
from ..models.partial_warrant_position_position import PartialWarrantPositionPosition
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialWarrantPosition")


@_attrs_define
class PartialWarrantPosition:
    """
    Attributes:
        symbol (Union[Unset, str]):
        number_of_shares (Union[Unset, int]):
        all_ (Union[Unset, bool]):
        position (Union[Unset, PartialWarrantPositionPosition]):
        option_type (Union[Unset, PartialWarrantPositionOptionType]):
        strike_price (Union[Unset, int]):
        expiration_date (Union[Unset, str]):
    """

    symbol: Union[Unset, str] = UNSET
    number_of_shares: Union[Unset, int] = UNSET
    all_: Union[Unset, bool] = UNSET
    position: Union[Unset, PartialWarrantPositionPosition] = UNSET
    option_type: Union[Unset, PartialWarrantPositionOptionType] = UNSET
    strike_price: Union[Unset, int] = UNSET
    expiration_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol

        number_of_shares = self.number_of_shares

        all_ = self.all_

        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value

        option_type: Union[Unset, str] = UNSET
        if not isinstance(self.option_type, Unset):
            option_type = self.option_type.value

        strike_price = self.strike_price

        expiration_date = self.expiration_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if number_of_shares is not UNSET:
            field_dict["numberOfShares"] = number_of_shares
        if all_ is not UNSET:
            field_dict["all"] = all_
        if position is not UNSET:
            field_dict["position"] = position
        if option_type is not UNSET:
            field_dict["optionType"] = option_type
        if strike_price is not UNSET:
            field_dict["strikePrice"] = strike_price
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol", UNSET)

        number_of_shares = d.pop("numberOfShares", UNSET)

        all_ = d.pop("all", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, PartialWarrantPositionPosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = PartialWarrantPositionPosition(_position)

        _option_type = d.pop("optionType", UNSET)
        option_type: Union[Unset, PartialWarrantPositionOptionType]
        if isinstance(_option_type, Unset):
            option_type = UNSET
        else:
            option_type = PartialWarrantPositionOptionType(_option_type)

        strike_price = d.pop("strikePrice", UNSET)

        expiration_date = d.pop("expirationDate", UNSET)

        partial_warrant_position = cls(
            symbol=symbol,
            number_of_shares=number_of_shares,
            all_=all_,
            position=position,
            option_type=option_type,
            strike_price=strike_price,
            expiration_date=expiration_date,
        )

        partial_warrant_position.additional_properties = d
        return partial_warrant_position

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
