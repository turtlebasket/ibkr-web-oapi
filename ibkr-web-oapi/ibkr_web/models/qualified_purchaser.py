from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qualified_purchaser_details import QualifiedPurchaserDetails


T = TypeVar("T", bound="QualifiedPurchaser")


@_attrs_define
class QualifiedPurchaser:
    """
    Attributes:
        qualified_purchaser_details (Union[Unset, List['QualifiedPurchaserDetails']]):
        status (Union[Unset, bool]):
    """

    qualified_purchaser_details: Union[Unset, List["QualifiedPurchaserDetails"]] = UNSET
    status: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        qualified_purchaser_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.qualified_purchaser_details, Unset):
            qualified_purchaser_details = []
            for qualified_purchaser_details_item_data in self.qualified_purchaser_details:
                qualified_purchaser_details_item = qualified_purchaser_details_item_data.to_dict()
                qualified_purchaser_details.append(qualified_purchaser_details_item)

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qualified_purchaser_details is not UNSET:
            field_dict["qualifiedPurchaserDetails"] = qualified_purchaser_details
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.qualified_purchaser_details import QualifiedPurchaserDetails

        d = src_dict.copy()
        qualified_purchaser_details = []
        _qualified_purchaser_details = d.pop("qualifiedPurchaserDetails", UNSET)
        for qualified_purchaser_details_item_data in _qualified_purchaser_details or []:
            qualified_purchaser_details_item = QualifiedPurchaserDetails.from_dict(
                qualified_purchaser_details_item_data
            )

            qualified_purchaser_details.append(qualified_purchaser_details_item)

        status = d.pop("status", UNSET)

        qualified_purchaser = cls(
            qualified_purchaser_details=qualified_purchaser_details,
            status=status,
        )

        qualified_purchaser.additional_properties = d
        return qualified_purchaser

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
