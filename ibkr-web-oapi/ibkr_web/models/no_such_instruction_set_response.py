from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoSuchInstructionSetResponse")


@_attrs_define
class NoSuchInstructionSetResponse:
    """
    Attributes:
        type (str):  Example: /simple.
        title (str):  Example: Not found.
        status (int):  Example: 404.
        instruction_set_id (int):  Example: 8389943.
        detail (Union[Unset, str]):  Example: No such instruction set found.
    """

    type: str
    title: str
    status: int
    instruction_set_id: int
    detail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        title = self.title

        status = self.status

        instruction_set_id = self.instruction_set_id

        detail = self.detail

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
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        instruction_set_id = d.pop("instructionSetId")

        detail = d.pop("detail", UNSET)

        no_such_instruction_set_response = cls(
            type=type,
            title=title,
            status=status,
            instruction_set_id=instruction_set_id,
            detail=detail,
        )

        no_such_instruction_set_response.additional_properties = d
        return no_such_instruction_set_response

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
