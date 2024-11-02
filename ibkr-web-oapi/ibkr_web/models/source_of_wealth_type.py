from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_of_wealth_type_source_type import SourceOfWealthTypeSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceOfWealthType")


@_attrs_define
class SourceOfWealthType:
    """
    Attributes:
        source_type (Union[Unset, SourceOfWealthTypeSourceType]):
        percentage (Union[Unset, int]):
        used_for_funds (Union[Unset, bool]):
        description (Union[Unset, str]):
    """

    source_type: Union[Unset, SourceOfWealthTypeSourceType] = UNSET
    percentage: Union[Unset, int] = UNSET
    used_for_funds: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        percentage = self.percentage

        used_for_funds = self.used_for_funds

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if used_for_funds is not UNSET:
            field_dict["usedForFunds"] = used_for_funds
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, SourceOfWealthTypeSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = SourceOfWealthTypeSourceType(_source_type)

        percentage = d.pop("percentage", UNSET)

        used_for_funds = d.pop("usedForFunds", UNSET)

        description = d.pop("description", UNSET)

        source_of_wealth_type = cls(
            source_type=source_type,
            percentage=percentage,
            used_for_funds=used_for_funds,
            description=description,
        )

        source_of_wealth_type.additional_properties = d
        return source_of_wealth_type

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
