from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pnl_partitioned_response_upnl import PnlPartitionedResponseUpnl


T = TypeVar("T", bound="PnlPartitionedResponse")


@_attrs_define
class PnlPartitionedResponse:
    """
    Attributes:
        upnl (Union[Unset, PnlPartitionedResponseUpnl]): Refers to the U accounts PnL. This does reference Realized
            Profit and Loss.
    """

    upnl: Union[Unset, "PnlPartitionedResponseUpnl"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upnl: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.upnl, Unset):
            upnl = self.upnl.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upnl is not UNSET:
            field_dict["upnl"] = upnl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pnl_partitioned_response_upnl import PnlPartitionedResponseUpnl

        d = src_dict.copy()
        _upnl = d.pop("upnl", UNSET)
        upnl: Union[Unset, PnlPartitionedResponseUpnl]
        if isinstance(_upnl, Unset):
            upnl = UNSET
        else:
            upnl = PnlPartitionedResponseUpnl.from_dict(_upnl)

        pnl_partitioned_response = cls(
            upnl=upnl,
        )

        pnl_partitioned_response.additional_properties = d
        return pnl_partitioned_response

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
