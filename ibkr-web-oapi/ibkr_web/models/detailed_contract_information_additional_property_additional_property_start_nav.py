from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav")


@_attrs_define
class DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav:
    """Returns the starting data for the current NAV details.

    Attributes:
        date (Union[Unset, str]): Returns the starting date for the current period's NAV range.
        val (Union[Unset, int]): Returns the inital NAV value of {Period Range} from the current date.
    """

    date: Union[Unset, str] = UNSET
    val: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date

        val = self.val

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if val is not UNSET:
            field_dict["val"] = val

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        val = d.pop("val", UNSET)

        detailed_contract_information_additional_property_additional_property_start_nav = cls(
            date=date,
            val=val,
        )

        detailed_contract_information_additional_property_additional_property_start_nav.additional_properties = d
        return detailed_contract_information_additional_property_additional_property_start_nav

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
