from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleOrderSubmissionRequestStrategyParameters")


@_attrs_define
class SingleOrderSubmissionRequestStrategyParameters:
    """Parameters governing the selected algorithm, if applicable.

    Attributes:
        placeholder (Union[Unset, str]): Placeholder -- these vary by algo (and not always type string, sometimes bool)
    """

    placeholder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        placeholder = self.placeholder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if placeholder is not UNSET:
            field_dict["PLACEHOLDER"] = placeholder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        placeholder = d.pop("PLACEHOLDER", UNSET)

        single_order_submission_request_strategy_parameters = cls(
            placeholder=placeholder,
        )

        single_order_submission_request_strategy_parameters.additional_properties = d
        return single_order_submission_request_strategy_parameters

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
