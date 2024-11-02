from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelfRegulatedMembershipType")


@_attrs_define
class SelfRegulatedMembershipType:
    """
    Attributes:
        exchanges (Union[Unset, str]):
        organizations (Union[Unset, str]):
    """

    exchanges: Union[Unset, str] = UNSET
    organizations: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exchanges = self.exchanges

        organizations = self.organizations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchanges is not UNSET:
            field_dict["exchanges"] = exchanges
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exchanges = d.pop("exchanges", UNSET)

        organizations = d.pop("organizations", UNSET)

        self_regulated_membership_type = cls(
            exchanges=exchanges,
            organizations=organizations,
        )

        self_regulated_membership_type.additional_properties = d
        return self_regulated_membership_type

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
