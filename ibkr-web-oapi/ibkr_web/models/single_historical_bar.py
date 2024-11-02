from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleHistoricalBar")


@_attrs_define
class SingleHistoricalBar:
    """Object containing data for a single OHLC bar.

    Attributes:
        t (Union[Unset, int]): Unix timestamp of the start (chronologically earlier) of the bar.
        o (Union[Unset, float]): Opening value of the bar.
        c (Union[Unset, float]): Closing value of the bar.
        h (Union[Unset, float]): High value of the bar.
        l (Union[Unset, float]): Low value of the bar.
        v (Union[Unset, float]): Volume value of the bar, returned only for "Last" barType.
    """

    t: Union[Unset, int] = UNSET
    o: Union[Unset, float] = UNSET
    c: Union[Unset, float] = UNSET
    h: Union[Unset, float] = UNSET
    l: Union[Unset, float] = UNSET
    v: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t = self.t

        o = self.o

        c = self.c

        h = self.h

        l = self.l

        v = self.v

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t is not UNSET:
            field_dict["t"] = t
        if o is not UNSET:
            field_dict["o"] = o
        if c is not UNSET:
            field_dict["c"] = c
        if h is not UNSET:
            field_dict["h"] = h
        if l is not UNSET:
            field_dict["l"] = l
        if v is not UNSET:
            field_dict["v"] = v

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        t = d.pop("t", UNSET)

        o = d.pop("o", UNSET)

        c = d.pop("c", UNSET)

        h = d.pop("h", UNSET)

        l = d.pop("l", UNSET)

        v = d.pop("v", UNSET)

        single_historical_bar = cls(
            t=t,
            o=o,
            c=c,
            h=h,
            l=l,
            v=v,
        )

        single_historical_bar.additional_properties = d
        return single_historical_bar

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
