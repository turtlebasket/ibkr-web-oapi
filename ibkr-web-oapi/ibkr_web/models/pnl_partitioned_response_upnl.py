from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pnl_partitioned_response_upnl_u1234567_core import PnlPartitionedResponseUpnlU1234567Core


T = TypeVar("T", bound="PnlPartitionedResponseUpnl")


@_attrs_define
class PnlPartitionedResponseUpnl:
    """Refers to the U accounts PnL. This does reference Realized Profit and Loss.

    Attributes:
        u1234567_core (Union[Unset, PnlPartitionedResponseUpnlU1234567Core]): The account or model's Profit and Loss.
    """

    u1234567_core: Union[Unset, "PnlPartitionedResponseUpnlU1234567Core"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        u1234567_core: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.u1234567_core, Unset):
            u1234567_core = self.u1234567_core.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if u1234567_core is not UNSET:
            field_dict["U1234567.Core"] = u1234567_core

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pnl_partitioned_response_upnl_u1234567_core import PnlPartitionedResponseUpnlU1234567Core

        d = src_dict.copy()
        _u1234567_core = d.pop("U1234567.Core", UNSET)
        u1234567_core: Union[Unset, PnlPartitionedResponseUpnlU1234567Core]
        if isinstance(_u1234567_core, Unset):
            u1234567_core = UNSET
        else:
            u1234567_core = PnlPartitionedResponseUpnlU1234567Core.from_dict(_u1234567_core)

        pnl_partitioned_response_upnl = cls(
            u1234567_core=u1234567_core,
        )

        pnl_partitioned_response_upnl.additional_properties = d
        return pnl_partitioned_response_upnl

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
