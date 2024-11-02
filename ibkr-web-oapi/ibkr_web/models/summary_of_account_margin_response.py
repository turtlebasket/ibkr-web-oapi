from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_of_account_margin_response_commodities import SummaryOfAccountMarginResponseCommodities
    from ..models.summary_of_account_margin_response_securities import SummaryOfAccountMarginResponseSecurities
    from ..models.summary_of_account_margin_response_total import SummaryOfAccountMarginResponseTotal


T = TypeVar("T", bound="SummaryOfAccountMarginResponse")


@_attrs_define
class SummaryOfAccountMarginResponse:
    """
    Attributes:
        total (Union[Unset, SummaryOfAccountMarginResponseTotal]):
        commodities (Union[Unset, SummaryOfAccountMarginResponseCommodities]):
        securities (Union[Unset, SummaryOfAccountMarginResponseSecurities]):
    """

    total: Union[Unset, "SummaryOfAccountMarginResponseTotal"] = UNSET
    commodities: Union[Unset, "SummaryOfAccountMarginResponseCommodities"] = UNSET
    securities: Union[Unset, "SummaryOfAccountMarginResponseSecurities"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        commodities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commodities, Unset):
            commodities = self.commodities.to_dict()

        securities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.securities, Unset):
            securities = self.securities.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if commodities is not UNSET:
            field_dict["commodities"] = commodities
        if securities is not UNSET:
            field_dict["securities"] = securities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.summary_of_account_margin_response_commodities import SummaryOfAccountMarginResponseCommodities
        from ..models.summary_of_account_margin_response_securities import SummaryOfAccountMarginResponseSecurities
        from ..models.summary_of_account_margin_response_total import SummaryOfAccountMarginResponseTotal

        d = src_dict.copy()
        _total = d.pop("total", UNSET)
        total: Union[Unset, SummaryOfAccountMarginResponseTotal]
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = SummaryOfAccountMarginResponseTotal.from_dict(_total)

        _commodities = d.pop("commodities", UNSET)
        commodities: Union[Unset, SummaryOfAccountMarginResponseCommodities]
        if isinstance(_commodities, Unset):
            commodities = UNSET
        else:
            commodities = SummaryOfAccountMarginResponseCommodities.from_dict(_commodities)

        _securities = d.pop("securities", UNSET)
        securities: Union[Unset, SummaryOfAccountMarginResponseSecurities]
        if isinstance(_securities, Unset):
            securities = UNSET
        else:
            securities = SummaryOfAccountMarginResponseSecurities.from_dict(_securities)

        summary_of_account_margin_response = cls(
            total=total,
            commodities=commodities,
            securities=securities,
        )

        summary_of_account_margin_response.additional_properties = d
        return summary_of_account_margin_response

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
