from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.commission_schedule_type_pricing_structure import CommissionScheduleTypePricingStructure
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commission_markup_type import CommissionMarkupType


T = TypeVar("T", bound="CommissionScheduleType")


@_attrs_define
class CommissionScheduleType:
    """
    Attributes:
        markups (Union[Unset, List['CommissionMarkupType']]):
        pricing_structure (Union[Unset, CommissionScheduleTypePricingStructure]):
    """

    markups: Union[Unset, List["CommissionMarkupType"]] = UNSET
    pricing_structure: Union[Unset, CommissionScheduleTypePricingStructure] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        markups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.markups, Unset):
            markups = []
            for markups_item_data in self.markups:
                markups_item = markups_item_data.to_dict()
                markups.append(markups_item)

        pricing_structure: Union[Unset, str] = UNSET
        if not isinstance(self.pricing_structure, Unset):
            pricing_structure = self.pricing_structure.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markups is not UNSET:
            field_dict["markups"] = markups
        if pricing_structure is not UNSET:
            field_dict["pricingStructure"] = pricing_structure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commission_markup_type import CommissionMarkupType

        d = src_dict.copy()
        markups = []
        _markups = d.pop("markups", UNSET)
        for markups_item_data in _markups or []:
            markups_item = CommissionMarkupType.from_dict(markups_item_data)

            markups.append(markups_item)

        _pricing_structure = d.pop("pricingStructure", UNSET)
        pricing_structure: Union[Unset, CommissionScheduleTypePricingStructure]
        if isinstance(_pricing_structure, Unset):
            pricing_structure = UNSET
        else:
            pricing_structure = CommissionScheduleTypePricingStructure(_pricing_structure)

        commission_schedule_type = cls(
            markups=markups,
            pricing_structure=pricing_structure,
        )

        commission_schedule_type.additional_properties = d
        return commission_schedule_type

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
