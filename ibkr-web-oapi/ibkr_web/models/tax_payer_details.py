from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_w8ben import FormW8BEN


T = TypeVar("T", bound="TaxPayerDetails")


@_attrs_define
class TaxPayerDetails:
    """
    Attributes:
        w_8_ben (Union[Unset, FormW8BEN]):
        user_name (Union[Unset, str]):
    """

    w_8_ben: Union[Unset, "FormW8BEN"] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        w_8_ben: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8_ben, Unset):
            w_8_ben = self.w_8_ben.to_dict()

        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if w_8_ben is not UNSET:
            field_dict["w8Ben"] = w_8_ben
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.form_w8ben import FormW8BEN

        d = src_dict.copy()
        _w_8_ben = d.pop("w8Ben", UNSET)
        w_8_ben: Union[Unset, FormW8BEN]
        if isinstance(_w_8_ben, Unset):
            w_8_ben = UNSET
        else:
            w_8_ben = FormW8BEN.from_dict(_w_8_ben)

        user_name = d.pop("userName", UNSET)

        tax_payer_details = cls(
            w_8_ben=w_8_ben,
            user_name=user_name,
        )

        tax_payer_details.additional_properties = d
        return tax_payer_details

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
