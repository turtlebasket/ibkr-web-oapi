from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ORGRegulatorType")


@_attrs_define
class ORGRegulatorType:
    """
    Attributes:
        regulator_name (Union[Unset, str]):
        regulator_country (Union[Unset, str]):
        regulated_in_capacity (Union[Unset, str]):
        regulator_id (Union[Unset, str]):
    """

    regulator_name: Union[Unset, str] = UNSET
    regulator_country: Union[Unset, str] = UNSET
    regulated_in_capacity: Union[Unset, str] = UNSET
    regulator_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regulator_name = self.regulator_name

        regulator_country = self.regulator_country

        regulated_in_capacity = self.regulated_in_capacity

        regulator_id = self.regulator_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regulator_name is not UNSET:
            field_dict["regulatorName"] = regulator_name
        if regulator_country is not UNSET:
            field_dict["regulatorCountry"] = regulator_country
        if regulated_in_capacity is not UNSET:
            field_dict["regulatedInCapacity"] = regulated_in_capacity
        if regulator_id is not UNSET:
            field_dict["regulatorId"] = regulator_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        regulator_name = d.pop("regulatorName", UNSET)

        regulator_country = d.pop("regulatorCountry", UNSET)

        regulated_in_capacity = d.pop("regulatedInCapacity", UNSET)

        regulator_id = d.pop("regulatorId", UNSET)

        org_regulator_type = cls(
            regulator_name=regulator_name,
            regulator_country=regulator_country,
            regulated_in_capacity=regulated_in_capacity,
            regulator_id=regulator_id,
        )

        org_regulator_type.additional_properties = d
        return org_regulator_type

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
