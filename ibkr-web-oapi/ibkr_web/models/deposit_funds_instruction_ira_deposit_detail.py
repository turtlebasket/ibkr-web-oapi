from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deposit_funds_instruction_ira_deposit_detail_from_ira_type import (
    DepositFundsInstructionIraDepositDetailFromIraType,
)
from ..models.deposit_funds_instruction_ira_deposit_detail_ira_contribution_type import (
    DepositFundsInstructionIraDepositDetailIraContributionType,
)
from ..models.deposit_funds_instruction_ira_deposit_detail_ira_tax_year_type import (
    DepositFundsInstructionIraDepositDetailIraTaxYearType,
)

T = TypeVar("T", bound="DepositFundsInstructionIraDepositDetail")


@_attrs_define
class DepositFundsInstructionIraDepositDetail:
    """
    Attributes:
        ira_contribution_type (DepositFundsInstructionIraDepositDetailIraContributionType):  Example: ROLLOVER.
        ira_tax_year_type (DepositFundsInstructionIraDepositDetailIraTaxYearType):  Example: CURRENT.
        from_ira_type (DepositFundsInstructionIraDepositDetailFromIraType):  Example: TRADITIONAL.
    """

    ira_contribution_type: DepositFundsInstructionIraDepositDetailIraContributionType
    ira_tax_year_type: DepositFundsInstructionIraDepositDetailIraTaxYearType
    from_ira_type: DepositFundsInstructionIraDepositDetailFromIraType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ira_contribution_type = self.ira_contribution_type.value

        ira_tax_year_type = self.ira_tax_year_type.value

        from_ira_type = self.from_ira_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iraContributionType": ira_contribution_type,
                "iraTaxYearType": ira_tax_year_type,
                "fromIraType": from_ira_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ira_contribution_type = DepositFundsInstructionIraDepositDetailIraContributionType(d.pop("iraContributionType"))

        ira_tax_year_type = DepositFundsInstructionIraDepositDetailIraTaxYearType(d.pop("iraTaxYearType"))

        from_ira_type = DepositFundsInstructionIraDepositDetailFromIraType(d.pop("fromIraType"))

        deposit_funds_instruction_ira_deposit_detail = cls(
            ira_contribution_type=ira_contribution_type,
            ira_tax_year_type=ira_tax_year_type,
            from_ira_type=from_ira_type,
        )

        deposit_funds_instruction_ira_deposit_detail.additional_properties = d
        return deposit_funds_instruction_ira_deposit_detail

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
