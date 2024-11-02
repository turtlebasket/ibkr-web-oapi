from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iserver_scanner_run_request_filter_item import IserverScannerRunRequestFilterItem


T = TypeVar("T", bound="IserverScannerRunRequest")


@_attrs_define
class IserverScannerRunRequest:
    """
    Attributes:
        instrument (Union[Unset, str]): Instrument type as the target of the market scanner request. Found in the
            “instrument_list” section of the /iserver/scanner/params response.
        type (Union[Unset, str]): Scanner value the market scanner is sorted by. Based on the “scan_type_list” section
            of the /iserver/scanner/params response.
        location (Union[Unset, str]): Location value the market scanner is searching through. Based on the
            “location_tree” section of the /iserver/scanner/params response.
        filter_ (Union[Unset, List['IserverScannerRunRequestFilterItem']]): Contains any additional filters that should
            apply to response.
    """

    instrument: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    filter_: Union[Unset, List["IserverScannerRunRequestFilterItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instrument = self.instrument

        type = self.type

        location = self.location

        filter_: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if type is not UNSET:
            field_dict["type"] = type
        if location is not UNSET:
            field_dict["location"] = location
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.iserver_scanner_run_request_filter_item import IserverScannerRunRequestFilterItem

        d = src_dict.copy()
        instrument = d.pop("instrument", UNSET)

        type = d.pop("type", UNSET)

        location = d.pop("location", UNSET)

        filter_ = []
        _filter_ = d.pop("filter", UNSET)
        for filter_item_data in _filter_ or []:
            filter_item = IserverScannerRunRequestFilterItem.from_dict(filter_item_data)

            filter_.append(filter_item)

        iserver_scanner_run_request = cls(
            instrument=instrument,
            type=type,
            location=location,
            filter_=filter_,
        )

        iserver_scanner_run_request.additional_properties = d
        return iserver_scanner_run_request

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
