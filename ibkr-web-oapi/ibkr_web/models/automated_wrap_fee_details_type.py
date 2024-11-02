from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automated_wrap_fee_details_type_type import AutomatedWrapFeeDetailsTypeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annual_blended_percentage import AnnualBlendedPercentage
    from ..models.commission_schedule_type import CommissionScheduleType
    from ..models.nav_range_type import NAVRangeType


T = TypeVar("T", bound="AutomatedWrapFeeDetailsType")


@_attrs_define
class AutomatedWrapFeeDetailsType:
    """
    Attributes:
        per_trade_markups (Union[Unset, CommissionScheduleType]):
        annual_blended_percentages (Union[Unset, List['AnnualBlendedPercentage']]):
        nav_ranges (Union[Unset, List['NAVRangeType']]):
        type (Union[Unset, AutomatedWrapFeeDetailsTypeType]):
        max_fee (Union[Unset, float]):
        num_contracts (Union[Unset, int]):
        post_frequency (Union[Unset, str]):
        percent_of_nlv_cap (Union[Unset, str]):
        percent_of_nlv_cap_q (Union[Unset, str]):
    """

    per_trade_markups: Union[Unset, "CommissionScheduleType"] = UNSET
    annual_blended_percentages: Union[Unset, List["AnnualBlendedPercentage"]] = UNSET
    nav_ranges: Union[Unset, List["NAVRangeType"]] = UNSET
    type: Union[Unset, AutomatedWrapFeeDetailsTypeType] = UNSET
    max_fee: Union[Unset, float] = UNSET
    num_contracts: Union[Unset, int] = UNSET
    post_frequency: Union[Unset, str] = UNSET
    percent_of_nlv_cap: Union[Unset, str] = UNSET
    percent_of_nlv_cap_q: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        per_trade_markups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_trade_markups, Unset):
            per_trade_markups = self.per_trade_markups.to_dict()

        annual_blended_percentages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.annual_blended_percentages, Unset):
            annual_blended_percentages = []
            for annual_blended_percentages_item_data in self.annual_blended_percentages:
                annual_blended_percentages_item = annual_blended_percentages_item_data.to_dict()
                annual_blended_percentages.append(annual_blended_percentages_item)

        nav_ranges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nav_ranges, Unset):
            nav_ranges = []
            for nav_ranges_item_data in self.nav_ranges:
                nav_ranges_item = nav_ranges_item_data.to_dict()
                nav_ranges.append(nav_ranges_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        max_fee = self.max_fee

        num_contracts = self.num_contracts

        post_frequency = self.post_frequency

        percent_of_nlv_cap = self.percent_of_nlv_cap

        percent_of_nlv_cap_q = self.percent_of_nlv_cap_q

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if per_trade_markups is not UNSET:
            field_dict["perTradeMarkups"] = per_trade_markups
        if annual_blended_percentages is not UNSET:
            field_dict["annualBlendedPercentages"] = annual_blended_percentages
        if nav_ranges is not UNSET:
            field_dict["navRanges"] = nav_ranges
        if type is not UNSET:
            field_dict["type"] = type
        if max_fee is not UNSET:
            field_dict["maxFee"] = max_fee
        if num_contracts is not UNSET:
            field_dict["numContracts"] = num_contracts
        if post_frequency is not UNSET:
            field_dict["postFrequency"] = post_frequency
        if percent_of_nlv_cap is not UNSET:
            field_dict["percentOfNLVCap"] = percent_of_nlv_cap
        if percent_of_nlv_cap_q is not UNSET:
            field_dict["percentOfNLVCapQ"] = percent_of_nlv_cap_q

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annual_blended_percentage import AnnualBlendedPercentage
        from ..models.commission_schedule_type import CommissionScheduleType
        from ..models.nav_range_type import NAVRangeType

        d = src_dict.copy()
        _per_trade_markups = d.pop("perTradeMarkups", UNSET)
        per_trade_markups: Union[Unset, CommissionScheduleType]
        if isinstance(_per_trade_markups, Unset):
            per_trade_markups = UNSET
        else:
            per_trade_markups = CommissionScheduleType.from_dict(_per_trade_markups)

        annual_blended_percentages = []
        _annual_blended_percentages = d.pop("annualBlendedPercentages", UNSET)
        for annual_blended_percentages_item_data in _annual_blended_percentages or []:
            annual_blended_percentages_item = AnnualBlendedPercentage.from_dict(annual_blended_percentages_item_data)

            annual_blended_percentages.append(annual_blended_percentages_item)

        nav_ranges = []
        _nav_ranges = d.pop("navRanges", UNSET)
        for nav_ranges_item_data in _nav_ranges or []:
            nav_ranges_item = NAVRangeType.from_dict(nav_ranges_item_data)

            nav_ranges.append(nav_ranges_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AutomatedWrapFeeDetailsTypeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AutomatedWrapFeeDetailsTypeType(_type)

        max_fee = d.pop("maxFee", UNSET)

        num_contracts = d.pop("numContracts", UNSET)

        post_frequency = d.pop("postFrequency", UNSET)

        percent_of_nlv_cap = d.pop("percentOfNLVCap", UNSET)

        percent_of_nlv_cap_q = d.pop("percentOfNLVCapQ", UNSET)

        automated_wrap_fee_details_type = cls(
            per_trade_markups=per_trade_markups,
            annual_blended_percentages=annual_blended_percentages,
            nav_ranges=nav_ranges,
            type=type,
            max_fee=max_fee,
            num_contracts=num_contracts,
            post_frequency=post_frequency,
            percent_of_nlv_cap=percent_of_nlv_cap,
            percent_of_nlv_cap_q=percent_of_nlv_cap_q,
        )

        automated_wrap_fee_details_type.additional_properties = d
        return automated_wrap_fee_details_type

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
