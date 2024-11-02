from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_close_instruction_withdrawal_info import AccountCloseInstructionWithdrawalInfo


T = TypeVar("T", bound="AccountCloseInstruction")


@_attrs_define
class AccountCloseInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        account_id (str):  Example: U46377.
        close_reason (Union[Unset, str]):  Example: Input your reason of closure here.
        withdrawal_info (Union[Unset, AccountCloseInstructionWithdrawalInfo]):
    """

    client_instruction_id: float
    account_id: str
    close_reason: Union[Unset, str] = UNSET
    withdrawal_info: Union[Unset, "AccountCloseInstructionWithdrawalInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        account_id = self.account_id

        close_reason = self.close_reason

        withdrawal_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.withdrawal_info, Unset):
            withdrawal_info = self.withdrawal_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "accountId": account_id,
            }
        )
        if close_reason is not UNSET:
            field_dict["closeReason"] = close_reason
        if withdrawal_info is not UNSET:
            field_dict["withdrawalInfo"] = withdrawal_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_close_instruction_withdrawal_info import AccountCloseInstructionWithdrawalInfo

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        account_id = d.pop("accountId")

        close_reason = d.pop("closeReason", UNSET)

        _withdrawal_info = d.pop("withdrawalInfo", UNSET)
        withdrawal_info: Union[Unset, AccountCloseInstructionWithdrawalInfo]
        if isinstance(_withdrawal_info, Unset):
            withdrawal_info = UNSET
        else:
            withdrawal_info = AccountCloseInstructionWithdrawalInfo.from_dict(_withdrawal_info)

        account_close_instruction = cls(
            client_instruction_id=client_instruction_id,
            account_id=account_id,
            close_reason=close_reason,
            withdrawal_info=withdrawal_info,
        )

        account_close_instruction.additional_properties = d
        return account_close_instruction

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
