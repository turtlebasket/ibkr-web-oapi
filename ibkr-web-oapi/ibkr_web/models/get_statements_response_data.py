from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStatementsResponseData")


@_attrs_define
class GetStatementsResponseData:
    """
    Attributes:
        data_type (Union[Unset, str]): the data type of the value after decoding
        encoding (Union[Unset, str]): encoding used for the value
        value (Union[Unset, str]): Base 64 encoded String of report data
        mime_type (Union[Unset, str]): mimeType of document after decoding and serializing the value
    """

    data_type: Union[Unset, str] = UNSET
    encoding: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type

        encoding = self.encoding

        value = self.value

        mime_type = self.mime_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if value is not UNSET:
            field_dict["value"] = value
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_type = d.pop("dataType", UNSET)

        encoding = d.pop("encoding", UNSET)

        value = d.pop("value", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        get_statements_response_data = cls(
            data_type=data_type,
            encoding=encoding,
            value=value,
            mime_type=mime_type,
        )

        get_statements_response_data.additional_properties = d
        return get_statements_response_data

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
