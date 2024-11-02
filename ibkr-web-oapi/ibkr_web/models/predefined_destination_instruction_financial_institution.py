from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.predefined_destination_instruction_financial_institution_branch_code_type import (
    PredefinedDestinationInstructionFinancialInstitutionBranchCodeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PredefinedDestinationInstructionFinancialInstitution")


@_attrs_define
class PredefinedDestinationInstructionFinancialInstitution:
    """
    Attributes:
        name (str):  Example: SBI BANK.
        identifier (str):  Example: SBIN001000.
        identifier_type (str):  Example: IFSC.
        client_account_id (str):  Example: 132456789.
        branch_code (Union[Unset, str]):
        branch_code_type (Union[Unset, PredefinedDestinationInstructionFinancialInstitutionBranchCodeType]):
    """

    name: str
    identifier: str
    identifier_type: str
    client_account_id: str
    branch_code: Union[Unset, str] = UNSET
    branch_code_type: Union[Unset, PredefinedDestinationInstructionFinancialInstitutionBranchCodeType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        identifier = self.identifier

        identifier_type = self.identifier_type

        client_account_id = self.client_account_id

        branch_code = self.branch_code

        branch_code_type: Union[Unset, str] = UNSET
        if not isinstance(self.branch_code_type, Unset):
            branch_code_type = self.branch_code_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "identifier": identifier,
                "identifierType": identifier_type,
                "clientAccountId": client_account_id,
            }
        )
        if branch_code is not UNSET:
            field_dict["branchCode"] = branch_code
        if branch_code_type is not UNSET:
            field_dict["branchCodeType"] = branch_code_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        identifier = d.pop("identifier")

        identifier_type = d.pop("identifierType")

        client_account_id = d.pop("clientAccountId")

        branch_code = d.pop("branchCode", UNSET)

        _branch_code_type = d.pop("branchCodeType", UNSET)
        branch_code_type: Union[Unset, PredefinedDestinationInstructionFinancialInstitutionBranchCodeType]
        if isinstance(_branch_code_type, Unset):
            branch_code_type = UNSET
        else:
            branch_code_type = PredefinedDestinationInstructionFinancialInstitutionBranchCodeType(_branch_code_type)

        predefined_destination_instruction_financial_institution = cls(
            name=name,
            identifier=identifier,
            identifier_type=identifier_type,
            client_account_id=client_account_id,
            branch_code=branch_code,
            branch_code_type=branch_code_type,
        )

        predefined_destination_instruction_financial_institution.additional_properties = d
        return predefined_destination_instruction_financial_institution

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
