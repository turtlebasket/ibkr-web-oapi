from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_of_income_type_source_type import SourceOfIncomeTypeSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceOfIncomeType")


@_attrs_define
class SourceOfIncomeType:
    """
    Attributes:
        source_type (Union[Unset, SourceOfIncomeTypeSourceType]):
        percentage (Union[Unset, int]):
        description (Union[Unset, str]):
    """

    source_type: Union[Unset, SourceOfIncomeTypeSourceType] = UNSET
    percentage: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        percentage = self.percentage

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, SourceOfIncomeTypeSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = SourceOfIncomeTypeSourceType(_source_type)

        percentage = d.pop("percentage", UNSET)

        description = d.pop("description", UNSET)

        source_of_income_type = cls(
            source_type=source_type,
            percentage=percentage,
            description=description,
        )

        source_of_income_type.additional_properties = d
        return source_of_income_type

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
