from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.title_code import TitleCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="Title")


@_attrs_define
class Title:
    """
    Attributes:
        value (Union[Unset, str]):
        code (Union[Unset, TitleCode]):
    """

    value: Union[Unset, str] = UNSET
    code: Union[Unset, TitleCode] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        _code = d.pop("code", UNSET)
        code: Union[Unset, TitleCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = TitleCode(_code)

        title = cls(
            value=value,
            code=code,
        )

        title.additional_properties = d
        return title

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
