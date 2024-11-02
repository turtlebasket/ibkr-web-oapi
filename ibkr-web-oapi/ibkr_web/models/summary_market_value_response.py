from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_market_value_response_currency import SummaryMarketValueResponseCurrency


T = TypeVar("T", bound="SummaryMarketValueResponse")


@_attrs_define
class SummaryMarketValueResponse:
    """
    Attributes:
        currency (Union[Unset, SummaryMarketValueResponseCurrency]): Returns an object containing market value details
            of the currency and positions held using that currency.
    """

    currency: Union[Unset, "SummaryMarketValueResponseCurrency"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.summary_market_value_response_currency import SummaryMarketValueResponseCurrency

        d = src_dict.copy()
        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, SummaryMarketValueResponseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = SummaryMarketValueResponseCurrency.from_dict(_currency)

        summary_market_value_response = cls(
            currency=currency,
        )

        summary_market_value_response.additional_properties = d
        return summary_market_value_response

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
