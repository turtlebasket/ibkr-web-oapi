from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ira_withdrawal_details_distribution_type import IRAWithdrawalDetailsDistributionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IRAWithdrawalDetails")


@_attrs_define
class IRAWithdrawalDetails:
    """
    Attributes:
        distribution_type (Union[Unset, IRAWithdrawalDetailsDistributionType]):
        excess_contrib_yr (Union[Unset, int]):
        fed_tax_rate (Union[Unset, float]):
        legal_residence_state (Union[Unset, str]):
        state_tax_rate (Union[Unset, float]):
    """

    distribution_type: Union[Unset, IRAWithdrawalDetailsDistributionType] = UNSET
    excess_contrib_yr: Union[Unset, int] = UNSET
    fed_tax_rate: Union[Unset, float] = UNSET
    legal_residence_state: Union[Unset, str] = UNSET
    state_tax_rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distribution_type: Union[Unset, str] = UNSET
        if not isinstance(self.distribution_type, Unset):
            distribution_type = self.distribution_type.value

        excess_contrib_yr = self.excess_contrib_yr

        fed_tax_rate = self.fed_tax_rate

        legal_residence_state = self.legal_residence_state

        state_tax_rate = self.state_tax_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distribution_type is not UNSET:
            field_dict["distributionType"] = distribution_type
        if excess_contrib_yr is not UNSET:
            field_dict["excessContribYr"] = excess_contrib_yr
        if fed_tax_rate is not UNSET:
            field_dict["fedTaxRate"] = fed_tax_rate
        if legal_residence_state is not UNSET:
            field_dict["legalResidenceState"] = legal_residence_state
        if state_tax_rate is not UNSET:
            field_dict["stateTaxRate"] = state_tax_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _distribution_type = d.pop("distributionType", UNSET)
        distribution_type: Union[Unset, IRAWithdrawalDetailsDistributionType]
        if isinstance(_distribution_type, Unset):
            distribution_type = UNSET
        else:
            distribution_type = IRAWithdrawalDetailsDistributionType(_distribution_type)

        excess_contrib_yr = d.pop("excessContribYr", UNSET)

        fed_tax_rate = d.pop("fedTaxRate", UNSET)

        legal_residence_state = d.pop("legalResidenceState", UNSET)

        state_tax_rate = d.pop("stateTaxRate", UNSET)

        ira_withdrawal_details = cls(
            distribution_type=distribution_type,
            excess_contrib_yr=excess_contrib_yr,
            fed_tax_rate=fed_tax_rate,
            legal_residence_state=legal_residence_state,
            state_tax_rate=state_tax_rate,
        )

        ira_withdrawal_details.additional_properties = d
        return ira_withdrawal_details

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
