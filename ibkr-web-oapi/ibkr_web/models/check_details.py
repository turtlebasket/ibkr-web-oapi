from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckDetails")


@_attrs_define
class CheckDetails:
    """
    Attributes:
        check_number (Union[Unset, str]):
        routing_number (Union[Unset, str]):
        account_number (Union[Unset, str]):
    """

    check_number: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        check_number = self.check_number

        routing_number = self.routing_number

        account_number = self.account_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_number is not UNSET:
            field_dict["checkNumber"] = check_number
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        check_number = d.pop("checkNumber", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        check_details = cls(
            check_number=check_number,
            routing_number=routing_number,
            account_number=account_number,
        )

        check_details.additional_properties = d
        return check_details

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
