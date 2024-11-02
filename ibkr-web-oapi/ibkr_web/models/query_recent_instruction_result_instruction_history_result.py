from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueryRecentInstructionResultInstructionHistoryResult")


@_attrs_define
class QueryRecentInstructionResultInstructionHistoryResult:
    """
    Attributes:
        client_instruction_id (float):
        ib_instruction_id (float):
        instruction_type (str):
        request_date (str):
        status (str):
        instruction_set_id (float):
    """

    client_instruction_id: float
    ib_instruction_id: float
    instruction_type: str
    request_date: str
    status: str
    instruction_set_id: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        ib_instruction_id = self.ib_instruction_id

        instruction_type = self.instruction_type

        request_date = self.request_date

        status = self.status

        instruction_set_id = self.instruction_set_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "ibInstructionId": ib_instruction_id,
                "instructionType": instruction_type,
                "requestDate": request_date,
                "status": status,
                "instructionSetId": instruction_set_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        ib_instruction_id = d.pop("ibInstructionId")

        instruction_type = d.pop("instructionType")

        request_date = d.pop("requestDate")

        status = d.pop("status")

        instruction_set_id = d.pop("instructionSetId")

        query_recent_instruction_result_instruction_history_result = cls(
            client_instruction_id=client_instruction_id,
            ib_instruction_id=ib_instruction_id,
            instruction_type=instruction_type,
            request_date=request_date,
            status=status,
            instruction_set_id=instruction_set_id,
        )

        query_recent_instruction_result_instruction_history_result.additional_properties = d
        return query_recent_instruction_result_instruction_history_result

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
