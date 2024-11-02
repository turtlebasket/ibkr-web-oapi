from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polling_instruction_result_instruction_status import PollingInstructionResultInstructionStatus
from ..models.polling_instruction_result_instruction_type import PollingInstructionResultInstructionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deposit_funds_polling_result_deposit_details import DepositFundsPollingResultDepositDetails
    from ..models.polling_instruction_result_error import PollingInstructionResultError


T = TypeVar("T", bound="DepositFundsPollingResult")


@_attrs_define
class DepositFundsPollingResult:
    """
    Attributes:
        client_instruction_id (str):  Example: 1012983.
        instruction_type (PollingInstructionResultInstructionType):  Example: INTERNAL_CASH_TRANSFER.
        instruction_status (PollingInstructionResultInstructionStatus):  Example: PENDING.
        instruction_id (float):  Example: 45123654.
        ib_reference_id (Union[Unset, float]):  Example: 23456745.
        description (Union[Unset, str]):  Example: Please poll for status after 10 minutes.
        error (Union[Unset, PollingInstructionResultError]):
        deposit_details (Union[Unset, DepositFundsPollingResultDepositDetails]):
    """

    client_instruction_id: str
    instruction_type: PollingInstructionResultInstructionType
    instruction_status: PollingInstructionResultInstructionStatus
    instruction_id: float
    ib_reference_id: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, "PollingInstructionResultError"] = UNSET
    deposit_details: Union[Unset, "DepositFundsPollingResultDepositDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        instruction_type = self.instruction_type.value

        instruction_status = self.instruction_status.value

        instruction_id = self.instruction_id

        ib_reference_id = self.ib_reference_id

        description = self.description

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        deposit_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deposit_details, Unset):
            deposit_details = self.deposit_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "instructionType": instruction_type,
                "instructionStatus": instruction_status,
                "instructionId": instruction_id,
            }
        )
        if ib_reference_id is not UNSET:
            field_dict["ibReferenceId"] = ib_reference_id
        if description is not UNSET:
            field_dict["description"] = description
        if error is not UNSET:
            field_dict["error"] = error
        if deposit_details is not UNSET:
            field_dict["depositDetails"] = deposit_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deposit_funds_polling_result_deposit_details import DepositFundsPollingResultDepositDetails
        from ..models.polling_instruction_result_error import PollingInstructionResultError

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        instruction_type = PollingInstructionResultInstructionType(d.pop("instructionType"))

        instruction_status = PollingInstructionResultInstructionStatus(d.pop("instructionStatus"))

        instruction_id = d.pop("instructionId")

        ib_reference_id = d.pop("ibReferenceId", UNSET)

        description = d.pop("description", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, PollingInstructionResultError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PollingInstructionResultError.from_dict(_error)

        _deposit_details = d.pop("depositDetails", UNSET)
        deposit_details: Union[Unset, DepositFundsPollingResultDepositDetails]
        if isinstance(_deposit_details, Unset):
            deposit_details = UNSET
        else:
            deposit_details = DepositFundsPollingResultDepositDetails.from_dict(_deposit_details)

        deposit_funds_polling_result = cls(
            client_instruction_id=client_instruction_id,
            instruction_type=instruction_type,
            instruction_status=instruction_status,
            instruction_id=instruction_id,
            ib_reference_id=ib_reference_id,
            description=description,
            error=error,
            deposit_details=deposit_details,
        )

        deposit_funds_polling_result.additional_properties = d
        return deposit_funds_polling_result

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
