from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostIserverMarketdataUnsubscribeBody")


@_attrs_define
class PostIserverMarketdataUnsubscribeBody:
    """
    Attributes:
        conid (Union[Unset, int]): The IB contract ID of the instrument whose market data feed is to be unsubscribed.
            Example: 265598.
    """

    conid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conid = self.conid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conid is not UNSET:
            field_dict["conid"] = conid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conid = d.pop("conid", UNSET)

        post_iserver_marketdata_unsubscribe_body = cls(
            conid=conid,
        )

        post_iserver_marketdata_unsubscribe_body.additional_properties = d
        return post_iserver_marketdata_unsubscribe_body

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
