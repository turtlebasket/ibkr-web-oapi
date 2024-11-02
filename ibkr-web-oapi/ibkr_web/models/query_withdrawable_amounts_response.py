from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polling_instruction_result import PollingInstructionResult


T = TypeVar("T", bound="QueryWithdrawableAmountsResponse")


@_attrs_define
class QueryWithdrawableAmountsResponse:
    """
    Attributes:
        status (float):  Example: 202.
        instruction_set_id (float):  Example: -1988905739.
        instruction_result (Union[Unset, PollingInstructionResult]):
    """

    status: float
    instruction_set_id: float
    instruction_result: Union[Unset, "PollingInstructionResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        instruction_set_id = self.instruction_set_id

        instruction_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instruction_result, Unset):
            instruction_result = self.instruction_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "instructionSetId": instruction_set_id,
            }
        )
        if instruction_result is not UNSET:
            field_dict["instructionResult"] = instruction_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.polling_instruction_result import PollingInstructionResult

        d = src_dict.copy()
        status = d.pop("status")

        instruction_set_id = d.pop("instructionSetId")

        _instruction_result = d.pop("instructionResult", UNSET)
        instruction_result: Union[Unset, PollingInstructionResult]
        if isinstance(_instruction_result, Unset):
            instruction_result = UNSET
        else:
            instruction_result = PollingInstructionResult.from_dict(_instruction_result)

        query_withdrawable_amounts_response = cls(
            status=status,
            instruction_set_id=instruction_set_id,
            instruction_result=instruction_result,
        )

        query_withdrawable_amounts_response.additional_properties = d
        return query_withdrawable_amounts_response

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
