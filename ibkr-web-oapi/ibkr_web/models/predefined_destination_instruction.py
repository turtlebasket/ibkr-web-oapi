from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.predefined_destination_instruction_bank_instruction_method import (
    PredefinedDestinationInstructionBankInstructionMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.predefined_destination_instruction_financial_institution import (
        PredefinedDestinationInstructionFinancialInstitution,
    )


T = TypeVar("T", bound="PredefinedDestinationInstruction")


@_attrs_define
class PredefinedDestinationInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        bank_instruction_name (str):  Example: Instruction.
        bank_instruction_method (PredefinedDestinationInstructionBankInstructionMethod):  Example: ACH.
        account_id (str):  Example: U2323232.
        currency (str):  Example: USD.
        financial_institution (Union[Unset, PredefinedDestinationInstructionFinancialInstitution]):
    """

    client_instruction_id: float
    bank_instruction_name: str
    bank_instruction_method: PredefinedDestinationInstructionBankInstructionMethod
    account_id: str
    currency: str
    financial_institution: Union[Unset, "PredefinedDestinationInstructionFinancialInstitution"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        bank_instruction_name = self.bank_instruction_name

        bank_instruction_method = self.bank_instruction_method.value

        account_id = self.account_id

        currency = self.currency

        financial_institution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.financial_institution, Unset):
            financial_institution = self.financial_institution.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "bankInstructionName": bank_instruction_name,
                "bankInstructionMethod": bank_instruction_method,
                "accountId": account_id,
                "currency": currency,
            }
        )
        if financial_institution is not UNSET:
            field_dict["financialInstitution"] = financial_institution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.predefined_destination_instruction_financial_institution import (
            PredefinedDestinationInstructionFinancialInstitution,
        )

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        bank_instruction_name = d.pop("bankInstructionName")

        bank_instruction_method = PredefinedDestinationInstructionBankInstructionMethod(d.pop("bankInstructionMethod"))

        account_id = d.pop("accountId")

        currency = d.pop("currency")

        _financial_institution = d.pop("financialInstitution", UNSET)
        financial_institution: Union[Unset, PredefinedDestinationInstructionFinancialInstitution]
        if isinstance(_financial_institution, Unset):
            financial_institution = UNSET
        else:
            financial_institution = PredefinedDestinationInstructionFinancialInstitution.from_dict(
                _financial_institution
            )

        predefined_destination_instruction = cls(
            client_instruction_id=client_instruction_id,
            bank_instruction_name=bank_instruction_name,
            bank_instruction_method=bank_instruction_method,
            account_id=account_id,
            currency=currency,
            financial_institution=financial_institution,
        )

        predefined_destination_instruction.additional_properties = d
        return predefined_destination_instruction

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
