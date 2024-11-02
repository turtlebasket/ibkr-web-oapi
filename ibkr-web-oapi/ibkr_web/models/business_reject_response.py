from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instruction_result import InstructionResult


T = TypeVar("T", bound="BusinessRejectResponse")


@_attrs_define
class BusinessRejectResponse:
    """
    Attributes:
        type (str):  Example: /simple.
        title (str):  Example: Business Error.
        status (int):  Example: 422.
        instruction_set_id (int):  Example: 8389943.
        instruction_result (Union[Unset, InstructionResult]):
    """

    type: str
    title: str
    status: int
    instruction_set_id: int
    instruction_result: Union[Unset, "InstructionResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        title = self.title

        status = self.status

        instruction_set_id = self.instruction_set_id

        instruction_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instruction_result, Unset):
            instruction_result = self.instruction_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "title": title,
                "status": status,
                "instructionSetId": instruction_set_id,
            }
        )
        if instruction_result is not UNSET:
            field_dict["instructionResult"] = instruction_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.instruction_result import InstructionResult

        d = src_dict.copy()
        type = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        instruction_set_id = d.pop("instructionSetId")

        _instruction_result = d.pop("instructionResult", UNSET)
        instruction_result: Union[Unset, InstructionResult]
        if isinstance(_instruction_result, Unset):
            instruction_result = UNSET
        else:
            instruction_result = InstructionResult.from_dict(_instruction_result)

        business_reject_response = cls(
            type=type,
            title=title,
            status=status,
            instruction_set_id=instruction_set_id,
            instruction_result=instruction_result,
        )

        business_reject_response.additional_properties = d
        return business_reject_response

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
