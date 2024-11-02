from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegulatedMembership")


@_attrs_define
class RegulatedMembership:
    """
    Attributes:
        organization_code (Union[Unset, str]):
        membership_id (Union[Unset, str]):
    """

    organization_code: Union[Unset, str] = UNSET
    membership_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_code = self.organization_code

        membership_id = self.membership_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_code is not UNSET:
            field_dict["organizationCode"] = organization_code
        if membership_id is not UNSET:
            field_dict["membershipId"] = membership_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_code = d.pop("organizationCode", UNSET)

        membership_id = d.pop("membershipId", UNSET)

        regulated_membership = cls(
            organization_code=organization_code,
            membership_id=membership_id,
        )

        regulated_membership.additional_properties = d
        return regulated_membership

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
