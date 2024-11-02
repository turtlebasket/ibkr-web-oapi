from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetIserverSecdefStrikesResponse200")


@_attrs_define
class GetIserverSecdefStrikesResponse200:
    """
    Attributes:
        call (Union[Unset, List[float]]): Array containing a series of comma separated values representing potential
            call strikes for the instrument.
        put (Union[Unset, List[float]]): Array containing a series of comma separated values representing potential put
            strikes for the instrument.
    """

    call: Union[Unset, List[float]] = UNSET
    put: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call: Union[Unset, List[float]] = UNSET
        if not isinstance(self.call, Unset):
            call = self.call

        put: Union[Unset, List[float]] = UNSET
        if not isinstance(self.put, Unset):
            put = self.put

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call is not UNSET:
            field_dict["call"] = call
        if put is not UNSET:
            field_dict["put"] = put

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        call = cast(List[float], d.pop("call", UNSET))

        put = cast(List[float], d.pop("put", UNSET))

        get_iserver_secdef_strikes_response_200 = cls(
            call=call,
            put=put,
        )

        get_iserver_secdef_strikes_response_200.additional_properties = d
        return get_iserver_secdef_strikes_response_200

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
