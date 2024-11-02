from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.advisor_wrap_fees_type_strategy import AdvisorWrapFeesTypeStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automated_wrap_fee_details_type import AutomatedWrapFeeDetailsType
    from ..models.high_water_mark_type import HighWaterMarkType


T = TypeVar("T", bound="AdvisorWrapFeesType")


@_attrs_define
class AdvisorWrapFeesType:
    """
    Attributes:
        automated_fees_details (Union[Unset, List['AutomatedWrapFeeDetailsType']]):
        high_water_mark_config_hwma (Union[Unset, HighWaterMarkType]):
        high_water_mark_config_hwmq (Union[Unset, HighWaterMarkType]):
        strategy (Union[Unset, AdvisorWrapFeesTypeStrategy]):
        charge_advisor (Union[Unset, bool]):
        charge_other_fees_to_advisor (Union[Unset, bool]):
    """

    automated_fees_details: Union[Unset, List["AutomatedWrapFeeDetailsType"]] = UNSET
    high_water_mark_config_hwma: Union[Unset, "HighWaterMarkType"] = UNSET
    high_water_mark_config_hwmq: Union[Unset, "HighWaterMarkType"] = UNSET
    strategy: Union[Unset, AdvisorWrapFeesTypeStrategy] = UNSET
    charge_advisor: Union[Unset, bool] = UNSET
    charge_other_fees_to_advisor: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        automated_fees_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.automated_fees_details, Unset):
            automated_fees_details = []
            for automated_fees_details_item_data in self.automated_fees_details:
                automated_fees_details_item = automated_fees_details_item_data.to_dict()
                automated_fees_details.append(automated_fees_details_item)

        high_water_mark_config_hwma: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.high_water_mark_config_hwma, Unset):
            high_water_mark_config_hwma = self.high_water_mark_config_hwma.to_dict()

        high_water_mark_config_hwmq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.high_water_mark_config_hwmq, Unset):
            high_water_mark_config_hwmq = self.high_water_mark_config_hwmq.to_dict()

        strategy: Union[Unset, str] = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.value

        charge_advisor = self.charge_advisor

        charge_other_fees_to_advisor = self.charge_other_fees_to_advisor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automated_fees_details is not UNSET:
            field_dict["automatedFeesDetails"] = automated_fees_details
        if high_water_mark_config_hwma is not UNSET:
            field_dict["highWaterMarkConfigHwma"] = high_water_mark_config_hwma
        if high_water_mark_config_hwmq is not UNSET:
            field_dict["highWaterMarkConfigHwmq"] = high_water_mark_config_hwmq
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if charge_advisor is not UNSET:
            field_dict["chargeAdvisor"] = charge_advisor
        if charge_other_fees_to_advisor is not UNSET:
            field_dict["chargeOtherFeesToAdvisor"] = charge_other_fees_to_advisor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.automated_wrap_fee_details_type import AutomatedWrapFeeDetailsType
        from ..models.high_water_mark_type import HighWaterMarkType

        d = src_dict.copy()
        automated_fees_details = []
        _automated_fees_details = d.pop("automatedFeesDetails", UNSET)
        for automated_fees_details_item_data in _automated_fees_details or []:
            automated_fees_details_item = AutomatedWrapFeeDetailsType.from_dict(automated_fees_details_item_data)

            automated_fees_details.append(automated_fees_details_item)

        _high_water_mark_config_hwma = d.pop("highWaterMarkConfigHwma", UNSET)
        high_water_mark_config_hwma: Union[Unset, HighWaterMarkType]
        if isinstance(_high_water_mark_config_hwma, Unset):
            high_water_mark_config_hwma = UNSET
        else:
            high_water_mark_config_hwma = HighWaterMarkType.from_dict(_high_water_mark_config_hwma)

        _high_water_mark_config_hwmq = d.pop("highWaterMarkConfigHwmq", UNSET)
        high_water_mark_config_hwmq: Union[Unset, HighWaterMarkType]
        if isinstance(_high_water_mark_config_hwmq, Unset):
            high_water_mark_config_hwmq = UNSET
        else:
            high_water_mark_config_hwmq = HighWaterMarkType.from_dict(_high_water_mark_config_hwmq)

        _strategy = d.pop("strategy", UNSET)
        strategy: Union[Unset, AdvisorWrapFeesTypeStrategy]
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = AdvisorWrapFeesTypeStrategy(_strategy)

        charge_advisor = d.pop("chargeAdvisor", UNSET)

        charge_other_fees_to_advisor = d.pop("chargeOtherFeesToAdvisor", UNSET)

        advisor_wrap_fees_type = cls(
            automated_fees_details=automated_fees_details,
            high_water_mark_config_hwma=high_water_mark_config_hwma,
            high_water_mark_config_hwmq=high_water_mark_config_hwmq,
            strategy=strategy,
            charge_advisor=charge_advisor,
            charge_other_fees_to_advisor=charge_other_fees_to_advisor,
        )

        advisor_wrap_fees_type.additional_properties = d
        return advisor_wrap_fees_type

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
