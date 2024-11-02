from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_crs_controlling_person_designation import FormCRSControllingPersonDesignation
from ..models.form_crs_oecd_status import FormCRSOecdStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormCRS")


@_attrs_define
class FormCRS:
    """
    Attributes:
        controlling_person_designation (Union[Unset, FormCRSControllingPersonDesignation]):
        oecd_status (Union[Unset, FormCRSOecdStatus]):
    """

    controlling_person_designation: Union[Unset, FormCRSControllingPersonDesignation] = UNSET
    oecd_status: Union[Unset, FormCRSOecdStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        controlling_person_designation: Union[Unset, str] = UNSET
        if not isinstance(self.controlling_person_designation, Unset):
            controlling_person_designation = self.controlling_person_designation.value

        oecd_status: Union[Unset, str] = UNSET
        if not isinstance(self.oecd_status, Unset):
            oecd_status = self.oecd_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if controlling_person_designation is not UNSET:
            field_dict["controllingPersonDesignation"] = controlling_person_designation
        if oecd_status is not UNSET:
            field_dict["oecdStatus"] = oecd_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _controlling_person_designation = d.pop("controllingPersonDesignation", UNSET)
        controlling_person_designation: Union[Unset, FormCRSControllingPersonDesignation]
        if isinstance(_controlling_person_designation, Unset):
            controlling_person_designation = UNSET
        else:
            controlling_person_designation = FormCRSControllingPersonDesignation(_controlling_person_designation)

        _oecd_status = d.pop("oecdStatus", UNSET)
        oecd_status: Union[Unset, FormCRSOecdStatus]
        if isinstance(_oecd_status, Unset):
            oecd_status = UNSET
        else:
            oecd_status = FormCRSOecdStatus(_oecd_status)

        form_crs = cls(
            controlling_person_designation=controlling_person_designation,
            oecd_status=oecd_status,
        )

        form_crs.additional_properties = d
        return form_crs

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
