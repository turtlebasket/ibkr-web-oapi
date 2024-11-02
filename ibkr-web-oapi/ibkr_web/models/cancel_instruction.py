from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CancelInstruction")


@_attrs_define
class CancelInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        instruction_id (float):  Example: 43085477.
        reason (str):  Example: Testing.
    """

    client_instruction_id: float
    instruction_id: float
    reason: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        instruction_id = self.instruction_id

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "instructionId": instruction_id,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        instruction_id = d.pop("instructionId")

        reason = d.pop("reason")

        cancel_instruction = cls(
            client_instruction_id=client_instruction_id,
            instruction_id=instruction_id,
            reason=reason,
        )

        cancel_instruction.additional_properties = d
        return cancel_instruction

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
