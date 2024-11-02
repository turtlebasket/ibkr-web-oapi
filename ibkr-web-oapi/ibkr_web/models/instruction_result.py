from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.instruction_result_instruction_status import InstructionResultInstructionStatus
from ..models.instruction_result_instruction_type import InstructionResultInstructionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstructionResult")


@_attrs_define
class InstructionResult:
    """
    Attributes:
        client_instruction_id (str):  Example: 1012983.
        instruction_type (InstructionResultInstructionType):  Example: INTERNAL_CASH_TRANSFER.
        instruction_status (InstructionResultInstructionStatus):  Example: PENDING.
        instruction_id (float):  Example: 45123654.
        ib_reference_id (Union[Unset, float]):  Example: 23456745.
        description (Union[Unset, str]):  Example: Please poll for status after 10 minutes.
    """

    client_instruction_id: str
    instruction_type: InstructionResultInstructionType
    instruction_status: InstructionResultInstructionStatus
    instruction_id: float
    ib_reference_id: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        instruction_type = self.instruction_type.value

        instruction_status = self.instruction_status.value

        instruction_id = self.instruction_id

        ib_reference_id = self.ib_reference_id

        description = self.description

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        instruction_type = InstructionResultInstructionType(d.pop("instructionType"))

        instruction_status = InstructionResultInstructionStatus(d.pop("instructionStatus"))

        instruction_id = d.pop("instructionId")

        ib_reference_id = d.pop("ibReferenceId", UNSET)

        description = d.pop("description", UNSET)

        instruction_result = cls(
            client_instruction_id=client_instruction_id,
            instruction_type=instruction_type,
            instruction_status=instruction_status,
            instruction_id=instruction_id,
            ib_reference_id=ib_reference_id,
            description=description,
        )

        instruction_result.additional_properties = d
        return instruction_result

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
