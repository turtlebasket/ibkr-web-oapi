from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.high_water_mark_configuration_type import HighWaterMarkConfigurationType
    from ..models.previous_losses_type import PreviousLossesType


T = TypeVar("T", bound="HighWaterMarkType")


@_attrs_define
class HighWaterMarkType:
    """
    Attributes:
        hwm (Union[Unset, HighWaterMarkConfigurationType]):
        previous_losses (Union[Unset, List['PreviousLossesType']]):
    """

    hwm: Union[Unset, "HighWaterMarkConfigurationType"] = UNSET
    previous_losses: Union[Unset, List["PreviousLossesType"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hwm: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hwm, Unset):
            hwm = self.hwm.to_dict()

        previous_losses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.previous_losses, Unset):
            previous_losses = []
            for previous_losses_item_data in self.previous_losses:
                previous_losses_item = previous_losses_item_data.to_dict()
                previous_losses.append(previous_losses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hwm is not UNSET:
            field_dict["hwm"] = hwm
        if previous_losses is not UNSET:
            field_dict["previousLosses"] = previous_losses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.high_water_mark_configuration_type import HighWaterMarkConfigurationType
        from ..models.previous_losses_type import PreviousLossesType

        d = src_dict.copy()
        _hwm = d.pop("hwm", UNSET)
        hwm: Union[Unset, HighWaterMarkConfigurationType]
        if isinstance(_hwm, Unset):
            hwm = UNSET
        else:
            hwm = HighWaterMarkConfigurationType.from_dict(_hwm)

        previous_losses = []
        _previous_losses = d.pop("previousLosses", UNSET)
        for previous_losses_item_data in _previous_losses or []:
            previous_losses_item = PreviousLossesType.from_dict(previous_losses_item_data)

            previous_losses.append(previous_losses_item)

        high_water_mark_type = cls(
            hwm=hwm,
            previous_losses=previous_losses,
        )

        high_water_mark_type.additional_properties = d
        return high_water_mark_type

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
