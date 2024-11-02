from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachedFileType")


@_attrs_define
class AttachedFileType:
    """
    Attributes:
        file_name (Union[Unset, str]):
        file_length (Union[Unset, int]):
        sha_1_checksum (Union[Unset, str]):
    """

    file_name: Union[Unset, str] = UNSET
    file_length: Union[Unset, int] = UNSET
    sha_1_checksum: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name

        file_length = self.file_length

        sha_1_checksum = self.sha_1_checksum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_length is not UNSET:
            field_dict["fileLength"] = file_length
        if sha_1_checksum is not UNSET:
            field_dict["sha1Checksum"] = sha_1_checksum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop("fileName", UNSET)

        file_length = d.pop("fileLength", UNSET)

        sha_1_checksum = d.pop("sha1Checksum", UNSET)

        attached_file_type = cls(
            file_name=file_name,
            file_length=file_length,
            sha_1_checksum=sha_1_checksum,
        )

        attached_file_type.additional_properties = d
        return attached_file_type

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
