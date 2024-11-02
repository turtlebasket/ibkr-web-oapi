from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.single_historical_bar import SingleHistoricalBar


T = TypeVar("T", bound="HmdsHistoryResponse")


@_attrs_define
class HmdsHistoryResponse:
    """Object containing the requested historical data and related metadata.

    Attributes:
        start_time (Union[Unset, str]): UTC date and time of the start (chronologically earlier) of the complete period
            in format YYYYMMDD-hh:mm:ss.
        start_time_val (Union[Unset, int]): Unix timestamp of the start (chronologically earlier) of the complete
            period.
        end_time (Union[Unset, str]): UTC date and time of the end (chronologically later) of the complete period in
            format YYYYMMDD-hh:mm:ss.
        end_time_val (Union[Unset, int]): Unix timestamp of the end (chronologically later) of the complete period.
        data (Union[Unset, List['SingleHistoricalBar']]): Array containing OHLC bars for the requested period.
        points (Union[Unset, int]): Count of the number of bars returned in the data array.
        mkt_data_delay (Union[Unset, int]): Number of milliseconds taken to satisfy this historical data request.
    """

    start_time: Union[Unset, str] = UNSET
    start_time_val: Union[Unset, int] = UNSET
    end_time: Union[Unset, str] = UNSET
    end_time_val: Union[Unset, int] = UNSET
    data: Union[Unset, List["SingleHistoricalBar"]] = UNSET
    points: Union[Unset, int] = UNSET
    mkt_data_delay: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_time = self.start_time

        start_time_val = self.start_time_val

        end_time = self.end_time

        end_time_val = self.end_time_val

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        points = self.points

        mkt_data_delay = self.mkt_data_delay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if start_time_val is not UNSET:
            field_dict["startTimeVal"] = start_time_val
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if end_time_val is not UNSET:
            field_dict["endTimeVal"] = end_time_val
        if data is not UNSET:
            field_dict["data"] = data
        if points is not UNSET:
            field_dict["points"] = points
        if mkt_data_delay is not UNSET:
            field_dict["mktDataDelay"] = mkt_data_delay

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_historical_bar import SingleHistoricalBar

        d = src_dict.copy()
        start_time = d.pop("startTime", UNSET)

        start_time_val = d.pop("startTimeVal", UNSET)

        end_time = d.pop("endTime", UNSET)

        end_time_val = d.pop("endTimeVal", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = SingleHistoricalBar.from_dict(data_item_data)

            data.append(data_item)

        points = d.pop("points", UNSET)

        mkt_data_delay = d.pop("mktDataDelay", UNSET)

        hmds_history_response = cls(
            start_time=start_time,
            start_time_val=start_time_val,
            end_time=end_time,
            end_time_val=end_time_val,
            data=data,
            points=points,
            mkt_data_delay=mkt_data_delay,
        )

        hmds_history_response.additional_properties = d
        return hmds_history_response

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
