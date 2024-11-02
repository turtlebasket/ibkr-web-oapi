from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identification import Identification


T = TypeVar("T", bound="AddMiFIRData")


@_attrs_define
class AddMiFIRData:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        title (Union[Unset, str]):
        identifications (Union[Unset, List['Identification']]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    identifications: Union[Unset, List["Identification"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        title = self.title

        identifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identifications, Unset):
            identifications = []
            for identifications_item_data in self.identifications:
                identifications_item = identifications_item_data.to_dict()
                identifications.append(identifications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if title is not UNSET:
            field_dict["title"] = title
        if identifications is not UNSET:
            field_dict["identifications"] = identifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identification import Identification

        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        title = d.pop("title", UNSET)

        identifications = []
        _identifications = d.pop("identifications", UNSET)
        for identifications_item_data in _identifications or []:
            identifications_item = Identification.from_dict(identifications_item_data)

            identifications.append(identifications_item)

        add_mi_fir_data = cls(
            reference_account_id=reference_account_id,
            title=title,
            identifications=identifications,
        )

        add_mi_fir_data.additional_properties = d
        return add_mi_fir_data

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
