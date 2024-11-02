from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XmlResponse")


@_attrs_define
class XmlResponse:
    """
    Attributes:
        is_valid (Union[Unset, bool]):
        errors (Union[Unset, str]):
    """

    is_valid: Union[Unset, bool] = UNSET
    errors: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_valid = self.is_valid

        errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_valid = d.pop("isValid", UNSET)

        errors = d.pop("errors", UNSET)

        xml_response = cls(
            is_valid=is_valid,
            errors=errors,
        )

        xml_response.additional_properties = d
        return xml_response

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
