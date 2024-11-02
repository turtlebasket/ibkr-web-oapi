from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.representative_detail import RepresentativeDetail


T = TypeVar("T", bound="UpdateAccountRepresentatives")


@_attrs_define
class UpdateAccountRepresentatives:
    """
    Attributes:
        representative_details (Union[Unset, List['RepresentativeDetail']]):
        reference_account_id (Union[Unset, str]):
    """

    representative_details: Union[Unset, List["RepresentativeDetail"]] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        representative_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.representative_details, Unset):
            representative_details = []
            for representative_details_item_data in self.representative_details:
                representative_details_item = representative_details_item_data.to_dict()
                representative_details.append(representative_details_item)

        reference_account_id = self.reference_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if representative_details is not UNSET:
            field_dict["representativeDetails"] = representative_details
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.representative_detail import RepresentativeDetail

        d = src_dict.copy()
        representative_details = []
        _representative_details = d.pop("representativeDetails", UNSET)
        for representative_details_item_data in _representative_details or []:
            representative_details_item = RepresentativeDetail.from_dict(representative_details_item_data)

            representative_details.append(representative_details_item)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        update_account_representatives = cls(
            representative_details=representative_details,
            reference_account_id=reference_account_id,
        )

        update_account_representatives.additional_properties = d
        return update_account_representatives

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
