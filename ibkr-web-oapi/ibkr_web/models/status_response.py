import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData
    from ..models.xml_response import XmlResponse


T = TypeVar("T", bound="StatusResponse")


@_attrs_define
class StatusResponse:
    """
    Attributes:
        request_id (Union[Unset, str]):
        date_submitted (Union[Unset, datetime.datetime]):
        file_data (Union[Unset, FileData]):
        xml (Union[Unset, XmlResponse]):
    """

    request_id: Union[Unset, str] = UNSET
    date_submitted: Union[Unset, datetime.datetime] = UNSET
    file_data: Union[Unset, "FileData"] = UNSET
    xml: Union[Unset, "XmlResponse"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        date_submitted: Union[Unset, str] = UNSET
        if not isinstance(self.date_submitted, Unset):
            date_submitted = self.date_submitted.isoformat()

        file_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_data, Unset):
            file_data = self.file_data.to_dict()

        xml: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xml, Unset):
            xml = self.xml.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if date_submitted is not UNSET:
            field_dict["dateSubmitted"] = date_submitted
        if file_data is not UNSET:
            field_dict["fileData"] = file_data
        if xml is not UNSET:
            field_dict["xml"] = xml

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData
        from ..models.xml_response import XmlResponse

        d = src_dict.copy()
        request_id = d.pop("requestId", UNSET)

        _date_submitted = d.pop("dateSubmitted", UNSET)
        date_submitted: Union[Unset, datetime.datetime]
        if isinstance(_date_submitted, Unset):
            date_submitted = UNSET
        else:
            date_submitted = isoparse(_date_submitted)

        _file_data = d.pop("fileData", UNSET)
        file_data: Union[Unset, FileData]
        if isinstance(_file_data, Unset):
            file_data = UNSET
        else:
            file_data = FileData.from_dict(_file_data)

        _xml = d.pop("xml", UNSET)
        xml: Union[Unset, XmlResponse]
        if isinstance(_xml, Unset):
            xml = UNSET
        else:
            xml = XmlResponse.from_dict(_xml)

        status_response = cls(
            request_id=request_id,
            date_submitted=date_submitted,
            file_data=file_data,
            xml=xml,
        )

        status_response.additional_properties = d
        return status_response

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
