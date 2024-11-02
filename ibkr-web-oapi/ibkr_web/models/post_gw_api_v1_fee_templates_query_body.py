from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_gw_api_v1_fee_templates_query_body_instruction_type import (
    PostGwApiV1FeeTemplatesQueryBodyInstructionType,
)

if TYPE_CHECKING:
    from ..models.query_fee_template import QueryFeeTemplate


T = TypeVar("T", bound="PostGwApiV1FeeTemplatesQueryBody")


@_attrs_define
class PostGwApiV1FeeTemplatesQueryBody:
    """
    Attributes:
        instruction_type (PostGwApiV1FeeTemplatesQueryBodyInstructionType):
        instruction (QueryFeeTemplate):
    """

    instruction_type: PostGwApiV1FeeTemplatesQueryBodyInstructionType
    instruction: "QueryFeeTemplate"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instruction_type = self.instruction_type.value

        instruction = self.instruction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instructionType": instruction_type,
                "instruction": instruction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_fee_template import QueryFeeTemplate

        d = src_dict.copy()
        instruction_type = PostGwApiV1FeeTemplatesQueryBodyInstructionType(d.pop("instructionType"))

        instruction = QueryFeeTemplate.from_dict(d.pop("instruction"))

        post_gw_api_v1_fee_templates_query_body = cls(
            instruction_type=instruction_type,
            instruction=instruction,
        )

        post_gw_api_v1_fee_templates_query_body.additional_properties = d
        return post_gw_api_v1_fee_templates_query_body

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
