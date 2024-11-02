from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.withdraw_funds_instruction_ira_withdrawal_detail_ira_withhold_type import (
    WithdrawFundsInstructionIraWithdrawalDetailIraWithholdType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WithdrawFundsInstructionIraWithdrawalDetail")


@_attrs_define
class WithdrawFundsInstructionIraWithdrawalDetail:
    """
    Attributes:
        fed_income_tax_percentage (Union[Unset, float]):  Example: 12.
        state_income_tax_percentage (Union[Unset, float]):  Example: 10.
        state_cd (Union[Unset, str]):  Example: TE.
        ira_withhold_type (Union[Unset, WithdrawFundsInstructionIraWithdrawalDetailIraWithholdType]):  Example: NORMAL.
    """

    fed_income_tax_percentage: Union[Unset, float] = UNSET
    state_income_tax_percentage: Union[Unset, float] = UNSET
    state_cd: Union[Unset, str] = UNSET
    ira_withhold_type: Union[Unset, WithdrawFundsInstructionIraWithdrawalDetailIraWithholdType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fed_income_tax_percentage = self.fed_income_tax_percentage

        state_income_tax_percentage = self.state_income_tax_percentage

        state_cd = self.state_cd

        ira_withhold_type: Union[Unset, str] = UNSET
        if not isinstance(self.ira_withhold_type, Unset):
            ira_withhold_type = self.ira_withhold_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fed_income_tax_percentage is not UNSET:
            field_dict["fedIncomeTaxPercentage"] = fed_income_tax_percentage
        if state_income_tax_percentage is not UNSET:
            field_dict["stateIncomeTaxPercentage"] = state_income_tax_percentage
        if state_cd is not UNSET:
            field_dict["stateCd"] = state_cd
        if ira_withhold_type is not UNSET:
            field_dict["iraWithholdType"] = ira_withhold_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fed_income_tax_percentage = d.pop("fedIncomeTaxPercentage", UNSET)

        state_income_tax_percentage = d.pop("stateIncomeTaxPercentage", UNSET)

        state_cd = d.pop("stateCd", UNSET)

        _ira_withhold_type = d.pop("iraWithholdType", UNSET)
        ira_withhold_type: Union[Unset, WithdrawFundsInstructionIraWithdrawalDetailIraWithholdType]
        if isinstance(_ira_withhold_type, Unset):
            ira_withhold_type = UNSET
        else:
            ira_withhold_type = WithdrawFundsInstructionIraWithdrawalDetailIraWithholdType(_ira_withhold_type)

        withdraw_funds_instruction_ira_withdrawal_detail = cls(
            fed_income_tax_percentage=fed_income_tax_percentage,
            state_income_tax_percentage=state_income_tax_percentage,
            state_cd=state_cd,
            ira_withhold_type=ira_withhold_type,
        )

        withdraw_funds_instruction_ira_withdrawal_detail.additional_properties = d
        return withdraw_funds_instruction_ira_withdrawal_detail

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
