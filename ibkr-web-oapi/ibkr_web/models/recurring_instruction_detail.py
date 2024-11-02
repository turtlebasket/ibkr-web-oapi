from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recurring_instruction_detail_frequency import RecurringInstructionDetailFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecurringInstructionDetail")


@_attrs_define
class RecurringInstructionDetail:
    """
    Attributes:
        instruction_name (str):  Example: Arkansas-Test.
        frequency (RecurringInstructionDetailFrequency):  Example: MONTHLY.
        start_date (str):  Example: 2023-10-16.
        end_date (Union[Unset, str]):  Example: 2023-10-16.
    """

    instruction_name: str
    frequency: RecurringInstructionDetailFrequency
    start_date: str
    end_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instruction_name = self.instruction_name

        frequency = self.frequency.value

        start_date = self.start_date

        end_date = self.end_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instructionName": instruction_name,
                "frequency": frequency,
                "startDate": start_date,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instruction_name = d.pop("instructionName")

        frequency = RecurringInstructionDetailFrequency(d.pop("frequency"))

        start_date = d.pop("startDate")

        end_date = d.pop("endDate", UNSET)

        recurring_instruction_detail = cls(
            instruction_name=instruction_name,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date,
        )

        recurring_instruction_detail.additional_properties = d
        return recurring_instruction_detail

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
