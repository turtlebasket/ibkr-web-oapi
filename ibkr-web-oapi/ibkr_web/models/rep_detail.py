from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepDetail")


@_attrs_define
class RepDetail:
    """
    Attributes:
        rep_id (Union[Unset, str]):
        percentage (Union[Unset, int]):
    """

    rep_id: Union[Unset, str] = UNSET
    percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rep_id = self.rep_id

        percentage = self.percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rep_id is not UNSET:
            field_dict["repId"] = rep_id
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rep_id = d.pop("repId", UNSET)

        percentage = d.pop("percentage", UNSET)

        rep_detail = cls(
            rep_id=rep_id,
            percentage=percentage,
        )

        rep_detail.additional_properties = d
        return rep_detail

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
