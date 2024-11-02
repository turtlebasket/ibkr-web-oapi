from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IserverScannerRunRequestFilterItem")


@_attrs_define
class IserverScannerRunRequestFilterItem:
    """
    Attributes:
        code (Union[Unset, str]): Code value of the filter. Based on the “code” value within the “filter_list” section
            of the /iserver/scanner/params response.
        value (Union[Unset, bool, float, int, str]): Value corresponding to the input for “code”.
    """

    code: Union[Unset, str] = UNSET
    value: Union[Unset, bool, float, int, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        value: Union[Unset, bool, float, int, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        def _parse_value(data: object) -> Union[Unset, bool, float, int, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, bool, float, int, str], data)

        value = _parse_value(d.pop("value", UNSET))

        iserver_scanner_run_request_filter_item = cls(
            code=code,
            value=value,
        )

        iserver_scanner_run_request_filter_item.additional_properties = d
        return iserver_scanner_run_request_filter_item

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
