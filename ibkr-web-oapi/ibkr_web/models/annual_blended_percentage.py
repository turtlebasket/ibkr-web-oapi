from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnualBlendedPercentage")


@_attrs_define
class AnnualBlendedPercentage:
    """
    Attributes:
        blended_from (Union[Unset, str]):
        blended_to (Union[Unset, str]):
        percentage (Union[Unset, str]):
    """

    blended_from: Union[Unset, str] = UNSET
    blended_to: Union[Unset, str] = UNSET
    percentage: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        blended_from = self.blended_from

        blended_to = self.blended_to

        percentage = self.percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blended_from is not UNSET:
            field_dict["blendedFrom"] = blended_from
        if blended_to is not UNSET:
            field_dict["blendedTo"] = blended_to
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        blended_from = d.pop("blendedFrom", UNSET)

        blended_to = d.pop("blendedTo", UNSET)

        percentage = d.pop("percentage", UNSET)

        annual_blended_percentage = cls(
            blended_from=blended_from,
            blended_to=blended_to,
            percentage=percentage,
        )

        annual_blended_percentage.additional_properties = d
        return annual_blended_percentage

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
