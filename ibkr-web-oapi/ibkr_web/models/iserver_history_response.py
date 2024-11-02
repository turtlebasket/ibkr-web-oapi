from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.single_historical_bar import SingleHistoricalBar


T = TypeVar("T", bound="IserverHistoryResponse")


@_attrs_define
class IserverHistoryResponse:
    """Object containing the requested historical data and related metadata.

    Attributes:
        server_id (Union[Unset, str]): Internal use. Identifier of the request.
        symbol (Union[Unset, str]): Symbol of the request instrument.
        text (Union[Unset, str]): Description or company name of the instrument.
        price_factor (Union[Unset, int]): Internal use. Used to scale Client Portal chart Y-axis.
        start_time (Union[Unset, str]): UTC date and time of the start (chronologically earlier) of the complete period
            in format YYYYMMDD-hh:mm:ss.
        high (Union[Unset, str]): Internal use. Delivers highest price value in total interval. Used for chart scaling.
            A string constructed as 'highestPrice*priceFactor/totalVolume*volumeFactor/minutesFromStartTime'.
        low (Union[Unset, str]): Internal use. Delivers lowest price value in total interval. Used for chart scaling. A
            string constructed as 'lowestPrice*priceFactor/totalVolume*volumeFactor/minutesFromStartTime'.
        time_period (Union[Unset, str]): The client-specified period value.
        bar_length (Union[Unset, int]): The client-specified bar width, represented in seconds.
        md_availability (Union[Unset, str]): A three-character string reflecting the nature of available data. R =
            Realtime, D = Delayed, Z = Frozen, Y = Frozen Delayed, N = Not Subscribed. P = Snapshot, p = Consolidated. B =
            Top of book.
        outside_rth (Union[Unset, bool]): Indicates whether data from outside regular trading hours is included in the
            response.
        trading_day_duration (Union[Unset, int]): Length of instrument's trading day in seconds.
        volume_factor (Union[Unset, int]): Internal use. Used to scale volume histograms.
        price_display_rule (Union[Unset, int]): Internal use. Governs application of pricing display rule.
        price_display_value (Union[Unset, str]): Internal use. Governs rendering of displayed pricing.
        chart_pan_start_time (Union[Unset, str]): Internal use. UTC datetime string used to center Client Portal charts.
            Format YYYYMMDD-hh:mm:ss.
        direction (Union[Unset, int]): Indicates how the period is applied in relation to the startTime. Value will
            always be -1, indicating that the period extends from the startTime forward into the future.
        negative_capable (Union[Unset, bool]): Indicates whether instrument is capable of negative pricing.
        message_version (Union[Unset, int]): Internal use. Reflects the version of the response schema used.
        travel_time (Union[Unset, int]): Internal time in flight to serve the request.
        data (Union[Unset, List['SingleHistoricalBar']]): Array containing OHLC bars for the requested period.
        points (Union[Unset, int]): Count of the number of bars returned in the data array.
        mkt_data_delay (Union[Unset, int]): Number of milliseconds taken to satisfy this historical data request.
    """

    server_id: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    price_factor: Union[Unset, int] = UNSET
    start_time: Union[Unset, str] = UNSET
    high: Union[Unset, str] = UNSET
    low: Union[Unset, str] = UNSET
    time_period: Union[Unset, str] = UNSET
    bar_length: Union[Unset, int] = UNSET
    md_availability: Union[Unset, str] = UNSET
    outside_rth: Union[Unset, bool] = UNSET
    trading_day_duration: Union[Unset, int] = UNSET
    volume_factor: Union[Unset, int] = UNSET
    price_display_rule: Union[Unset, int] = UNSET
    price_display_value: Union[Unset, str] = UNSET
    chart_pan_start_time: Union[Unset, str] = UNSET
    direction: Union[Unset, int] = UNSET
    negative_capable: Union[Unset, bool] = UNSET
    message_version: Union[Unset, int] = UNSET
    travel_time: Union[Unset, int] = UNSET
    data: Union[Unset, List["SingleHistoricalBar"]] = UNSET
    points: Union[Unset, int] = UNSET
    mkt_data_delay: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_id = self.server_id

        symbol = self.symbol

        text = self.text

        price_factor = self.price_factor

        start_time = self.start_time

        high = self.high

        low = self.low

        time_period = self.time_period

        bar_length = self.bar_length

        md_availability = self.md_availability

        outside_rth = self.outside_rth

        trading_day_duration = self.trading_day_duration

        volume_factor = self.volume_factor

        price_display_rule = self.price_display_rule

        price_display_value = self.price_display_value

        chart_pan_start_time = self.chart_pan_start_time

        direction = self.direction

        negative_capable = self.negative_capable

        message_version = self.message_version

        travel_time = self.travel_time

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
        if server_id is not UNSET:
            field_dict["serverId"] = server_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if text is not UNSET:
            field_dict["text"] = text
        if price_factor is not UNSET:
            field_dict["priceFactor"] = price_factor
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if time_period is not UNSET:
            field_dict["timePeriod"] = time_period
        if bar_length is not UNSET:
            field_dict["barLength"] = bar_length
        if md_availability is not UNSET:
            field_dict["mdAvailability"] = md_availability
        if outside_rth is not UNSET:
            field_dict["outsideRth"] = outside_rth
        if trading_day_duration is not UNSET:
            field_dict["tradingDayDuration"] = trading_day_duration
        if volume_factor is not UNSET:
            field_dict["volumeFactor"] = volume_factor
        if price_display_rule is not UNSET:
            field_dict["priceDisplayRule"] = price_display_rule
        if price_display_value is not UNSET:
            field_dict["priceDisplayValue"] = price_display_value
        if chart_pan_start_time is not UNSET:
            field_dict["chartPanStartTime"] = chart_pan_start_time
        if direction is not UNSET:
            field_dict["direction"] = direction
        if negative_capable is not UNSET:
            field_dict["negativeCapable"] = negative_capable
        if message_version is not UNSET:
            field_dict["messageVersion"] = message_version
        if travel_time is not UNSET:
            field_dict["travelTime"] = travel_time
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
        server_id = d.pop("serverId", UNSET)

        symbol = d.pop("symbol", UNSET)

        text = d.pop("text", UNSET)

        price_factor = d.pop("priceFactor", UNSET)

        start_time = d.pop("startTime", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        time_period = d.pop("timePeriod", UNSET)

        bar_length = d.pop("barLength", UNSET)

        md_availability = d.pop("mdAvailability", UNSET)

        outside_rth = d.pop("outsideRth", UNSET)

        trading_day_duration = d.pop("tradingDayDuration", UNSET)

        volume_factor = d.pop("volumeFactor", UNSET)

        price_display_rule = d.pop("priceDisplayRule", UNSET)

        price_display_value = d.pop("priceDisplayValue", UNSET)

        chart_pan_start_time = d.pop("chartPanStartTime", UNSET)

        direction = d.pop("direction", UNSET)

        negative_capable = d.pop("negativeCapable", UNSET)

        message_version = d.pop("messageVersion", UNSET)

        travel_time = d.pop("travelTime", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = SingleHistoricalBar.from_dict(data_item_data)

            data.append(data_item)

        points = d.pop("points", UNSET)

        mkt_data_delay = d.pop("mktDataDelay", UNSET)

        iserver_history_response = cls(
            server_id=server_id,
            symbol=symbol,
            text=text,
            price_factor=price_factor,
            start_time=start_time,
            high=high,
            low=low,
            time_period=time_period,
            bar_length=bar_length,
            md_availability=md_availability,
            outside_rth=outside_rth,
            trading_day_duration=trading_day_duration,
            volume_factor=volume_factor,
            price_display_rule=price_display_rule,
            price_display_value=price_display_value,
            chart_pan_start_time=chart_pan_start_time,
            direction=direction,
            negative_capable=negative_capable,
            message_version=message_version,
            travel_time=travel_time,
            data=data,
            points=points,
            mkt_data_delay=mkt_data_delay,
        )

        iserver_history_response.additional_properties = d
        return iserver_history_response

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
