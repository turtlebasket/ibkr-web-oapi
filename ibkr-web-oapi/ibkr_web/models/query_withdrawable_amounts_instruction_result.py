from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polling_instruction_result_instruction_status import PollingInstructionResultInstructionStatus
from ..models.polling_instruction_result_instruction_type import PollingInstructionResultInstructionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polling_instruction_result_error import PollingInstructionResultError


T = TypeVar("T", bound="QueryWithdrawableAmountsInstructionResult")


@_attrs_define
class QueryWithdrawableAmountsInstructionResult:
    """
    Attributes:
        client_instruction_id (str):  Example: 1012983.
        instruction_type (PollingInstructionResultInstructionType):  Example: INTERNAL_CASH_TRANSFER.
        instruction_status (PollingInstructionResultInstructionStatus):  Example: PENDING.
        instruction_id (float):  Example: 45123654.
        account_id (str):
        currency (str):
        withdrawable_amount (float):
        withdrawable_amount_no_borrow (float):
        allowed_transfer_amount_to_master (float):
        withdrawable_amount_without_origination_hold_no_borrow (float):
        ib_reference_id (Union[Unset, float]):  Example: 23456745.
        description (Union[Unset, str]):  Example: Please poll for status after 10 minutes.
        error (Union[Unset, PollingInstructionResultError]):
    """

    client_instruction_id: str
    instruction_type: PollingInstructionResultInstructionType
    instruction_status: PollingInstructionResultInstructionStatus
    instruction_id: float
    account_id: str
    currency: str
    withdrawable_amount: float
    withdrawable_amount_no_borrow: float
    allowed_transfer_amount_to_master: float
    withdrawable_amount_without_origination_hold_no_borrow: float
    ib_reference_id: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    error: Union[Unset, "PollingInstructionResultError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        instruction_type = self.instruction_type.value

        instruction_status = self.instruction_status.value

        instruction_id = self.instruction_id

        account_id = self.account_id

        currency = self.currency

        withdrawable_amount = self.withdrawable_amount

        withdrawable_amount_no_borrow = self.withdrawable_amount_no_borrow

        allowed_transfer_amount_to_master = self.allowed_transfer_amount_to_master

        withdrawable_amount_without_origination_hold_no_borrow = (
            self.withdrawable_amount_without_origination_hold_no_borrow
        )

        ib_reference_id = self.ib_reference_id

        description = self.description

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "instructionType": instruction_type,
                "instructionStatus": instruction_status,
                "instructionId": instruction_id,
                "accountId": account_id,
                "currency": currency,
                "withdrawableAmount": withdrawable_amount,
                "withdrawableAmountNoBorrow": withdrawable_amount_no_borrow,
                "allowedTransferAmountToMaster": allowed_transfer_amount_to_master,
                "withdrawableAmountWithoutOriginationHoldNoBorrow": withdrawable_amount_without_origination_hold_no_borrow,
            }
        )
        if ib_reference_id is not UNSET:
            field_dict["ibReferenceId"] = ib_reference_id
        if description is not UNSET:
            field_dict["description"] = description
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.polling_instruction_result_error import PollingInstructionResultError

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        instruction_type = PollingInstructionResultInstructionType(d.pop("instructionType"))

        instruction_status = PollingInstructionResultInstructionStatus(d.pop("instructionStatus"))

        instruction_id = d.pop("instructionId")

        account_id = d.pop("accountId")

        currency = d.pop("currency")

        withdrawable_amount = d.pop("withdrawableAmount")

        withdrawable_amount_no_borrow = d.pop("withdrawableAmountNoBorrow")

        allowed_transfer_amount_to_master = d.pop("allowedTransferAmountToMaster")

        withdrawable_amount_without_origination_hold_no_borrow = d.pop(
            "withdrawableAmountWithoutOriginationHoldNoBorrow"
        )

        ib_reference_id = d.pop("ibReferenceId", UNSET)

        description = d.pop("description", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, PollingInstructionResultError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PollingInstructionResultError.from_dict(_error)

        query_withdrawable_amounts_instruction_result = cls(
            client_instruction_id=client_instruction_id,
            instruction_type=instruction_type,
            instruction_status=instruction_status,
            instruction_id=instruction_id,
            account_id=account_id,
            currency=currency,
            withdrawable_amount=withdrawable_amount,
            withdrawable_amount_no_borrow=withdrawable_amount_no_borrow,
            allowed_transfer_amount_to_master=allowed_transfer_amount_to_master,
            withdrawable_amount_without_origination_hold_no_borrow=withdrawable_amount_without_origination_hold_no_borrow,
            ib_reference_id=ib_reference_id,
            description=description,
            error=error,
        )

        query_withdrawable_amounts_instruction_result.additional_properties = d
        return query_withdrawable_amounts_instruction_result

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
