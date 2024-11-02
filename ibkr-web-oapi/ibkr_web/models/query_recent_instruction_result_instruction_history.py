from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.query_recent_instruction_result_instruction_history_result import (
        QueryRecentInstructionResultInstructionHistoryResult,
    )


T = TypeVar("T", bound="QueryRecentInstructionResultInstructionHistory")


@_attrs_define
class QueryRecentInstructionResultInstructionHistory:
    """
    Attributes:
        history_max_depth_number_of_days (int):
        history_max_depth_number_of_instruction (int):
        result (QueryRecentInstructionResultInstructionHistoryResult):
    """

    history_max_depth_number_of_days: int
    history_max_depth_number_of_instruction: int
    result: "QueryRecentInstructionResultInstructionHistoryResult"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        history_max_depth_number_of_days = self.history_max_depth_number_of_days

        history_max_depth_number_of_instruction = self.history_max_depth_number_of_instruction

        result = self.result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "historyMaxDepthNumberOfDays": history_max_depth_number_of_days,
                "historyMaxDepthNumberOfInstruction": history_max_depth_number_of_instruction,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_recent_instruction_result_instruction_history_result import (
            QueryRecentInstructionResultInstructionHistoryResult,
        )

        d = src_dict.copy()
        history_max_depth_number_of_days = d.pop("historyMaxDepthNumberOfDays")

        history_max_depth_number_of_instruction = d.pop("historyMaxDepthNumberOfInstruction")

        result = QueryRecentInstructionResultInstructionHistoryResult.from_dict(d.pop("result"))

        query_recent_instruction_result_instruction_history = cls(
            history_max_depth_number_of_days=history_max_depth_number_of_days,
            history_max_depth_number_of_instruction=history_max_depth_number_of_instruction,
            result=result,
        )

        query_recent_instruction_result_instruction_history.additional_properties = d
        return query_recent_instruction_result_instruction_history

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
