from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_crs import FormCRS
    from ..models.form_w8ben import FormW8BEN
    from ..models.form_w8bene import FormW8BENE
    from ..models.form_w9 import FormW9


T = TypeVar("T", bound="IndividualTaxInformation")


@_attrs_define
class IndividualTaxInformation:
    """
    Attributes:
        w9 (Union[Unset, FormW9]):
        w_8_ben (Union[Unset, FormW8BEN]):
        crs (Union[Unset, FormCRS]):
        w_8_ben_e (Union[Unset, FormW8BENE]):
    """

    w9: Union[Unset, "FormW9"] = UNSET
    w_8_ben: Union[Unset, "FormW8BEN"] = UNSET
    crs: Union[Unset, "FormCRS"] = UNSET
    w_8_ben_e: Union[Unset, "FormW8BENE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        w9: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w9, Unset):
            w9 = self.w9.to_dict()

        w_8_ben: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8_ben, Unset):
            w_8_ben = self.w_8_ben.to_dict()

        crs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crs, Unset):
            crs = self.crs.to_dict()

        w_8_ben_e: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8_ben_e, Unset):
            w_8_ben_e = self.w_8_ben_e.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if w9 is not UNSET:
            field_dict["w9"] = w9
        if w_8_ben is not UNSET:
            field_dict["w8Ben"] = w_8_ben
        if crs is not UNSET:
            field_dict["crs"] = crs
        if w_8_ben_e is not UNSET:
            field_dict["w8BenE"] = w_8_ben_e

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.form_crs import FormCRS
        from ..models.form_w8ben import FormW8BEN
        from ..models.form_w8bene import FormW8BENE
        from ..models.form_w9 import FormW9

        d = src_dict.copy()
        _w9 = d.pop("w9", UNSET)
        w9: Union[Unset, FormW9]
        if isinstance(_w9, Unset):
            w9 = UNSET
        else:
            w9 = FormW9.from_dict(_w9)

        _w_8_ben = d.pop("w8Ben", UNSET)
        w_8_ben: Union[Unset, FormW8BEN]
        if isinstance(_w_8_ben, Unset):
            w_8_ben = UNSET
        else:
            w_8_ben = FormW8BEN.from_dict(_w_8_ben)

        _crs = d.pop("crs", UNSET)
        crs: Union[Unset, FormCRS]
        if isinstance(_crs, Unset):
            crs = UNSET
        else:
            crs = FormCRS.from_dict(_crs)

        _w_8_ben_e = d.pop("w8BenE", UNSET)
        w_8_ben_e: Union[Unset, FormW8BENE]
        if isinstance(_w_8_ben_e, Unset):
            w_8_ben_e = UNSET
        else:
            w_8_ben_e = FormW8BENE.from_dict(_w_8_ben_e)

        individual_tax_information = cls(
            w9=w9,
            w_8_ben=w_8_ben,
            crs=crs,
            w_8_ben_e=w_8_ben_e,
        )

        individual_tax_information.additional_properties = d
        return individual_tax_information

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
