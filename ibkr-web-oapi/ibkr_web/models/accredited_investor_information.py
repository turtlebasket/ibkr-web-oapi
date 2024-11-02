from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccreditedInvestorInformation")


@_attrs_define
class AccreditedInvestorInformation:
    """
    Attributes:
        q1 (Union[Unset, bool]):
        q2 (Union[Unset, bool]):
        q3 (Union[Unset, bool]):
        q4 (Union[Unset, bool]):
        q5 (Union[Unset, bool]):
    """

    q1: Union[Unset, bool] = UNSET
    q2: Union[Unset, bool] = UNSET
    q3: Union[Unset, bool] = UNSET
    q4: Union[Unset, bool] = UNSET
    q5: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        q1 = self.q1

        q2 = self.q2

        q3 = self.q3

        q4 = self.q4

        q5 = self.q5

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if q1 is not UNSET:
            field_dict["q1"] = q1
        if q2 is not UNSET:
            field_dict["q2"] = q2
        if q3 is not UNSET:
            field_dict["q3"] = q3
        if q4 is not UNSET:
            field_dict["q4"] = q4
        if q5 is not UNSET:
            field_dict["q5"] = q5

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        q1 = d.pop("q1", UNSET)

        q2 = d.pop("q2", UNSET)

        q3 = d.pop("q3", UNSET)

        q4 = d.pop("q4", UNSET)

        q5 = d.pop("q5", UNSET)

        accredited_investor_information = cls(
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
        )

        accredited_investor_information.additional_properties = d
        return accredited_investor_information

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
