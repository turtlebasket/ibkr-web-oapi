from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAvailableDatesResponse")


@_attrs_define
class GetAvailableDatesResponse:
    """
    Attributes:
        rc (Union[Unset, int]): response code
        msg (Union[Unset, str]): status message
        data (Union[Unset, str]): Base 64 encoded String of report data
        data_type (Union[Unset, str]): Type of data in property data
    """

    rc: Union[Unset, int] = UNSET
    msg: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rc = self.rc

        msg = self.msg

        data = self.data

        data_type = self.data_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rc is not UNSET:
            field_dict["rc"] = rc
        if msg is not UNSET:
            field_dict["msg"] = msg
        if data is not UNSET:
            field_dict["data"] = data
        if data_type is not UNSET:
            field_dict["dataType"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rc = d.pop("rc", UNSET)

        msg = d.pop("msg", UNSET)

        data = d.pop("data", UNSET)

        data_type = d.pop("dataType", UNSET)

        get_available_dates_response = cls(
            rc=rc,
            msg=msg,
            data=data,
            data_type=data_type,
        )

        get_available_dates_response.additional_properties = d
        return get_available_dates_response

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
