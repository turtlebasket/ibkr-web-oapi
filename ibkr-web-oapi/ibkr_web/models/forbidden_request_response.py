from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.instruction_result import InstructionResult


T = TypeVar("T", bound="ForbiddenRequestResponse")


@_attrs_define
class ForbiddenRequestResponse:
    """
    Attributes:
        type (str):  Example: /invalid-argument.
        title (str):  Example: Bad Request.
        status (int):  Example: 400.
        detail (str):  Example: Input is not a JSON Object or doesn't contain all expected fields.
        instruction_set_id (int):  Example: 8389943.
        instruction_result (InstructionResult):
    """

    type: str
    title: str
    status: int
    detail: str
    instruction_set_id: int
    instruction_result: "InstructionResult"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        title = self.title

        status = self.status

        detail = self.detail

        instruction_set_id = self.instruction_set_id

        instruction_result = self.instruction_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "title": title,
                "status": status,
                "detail": detail,
                "instructionSetId": instruction_set_id,
                "instructionResult": instruction_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.instruction_result import InstructionResult

        d = src_dict.copy()
        type = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        detail = d.pop("detail")

        instruction_set_id = d.pop("instructionSetId")

        instruction_result = InstructionResult.from_dict(d.pop("instructionResult"))

        forbidden_request_response = cls(
            type=type,
            title=title,
            status=status,
            detail=detail,
            instruction_set_id=instruction_set_id,
            instruction_result=instruction_result,
        )

        forbidden_request_response.additional_properties = d
        return forbidden_request_response

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
