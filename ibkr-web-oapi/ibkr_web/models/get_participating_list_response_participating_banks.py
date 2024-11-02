from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetParticipatingListResponseParticipatingBanks")


@_attrs_define
class GetParticipatingListResponseParticipatingBanks:
    """
    Attributes:
        institution_name (str):  Example: WELAB BANK LIMITED.
        clearing_code (str):  Example: 390.
        bic (str):  Example: WEDIHKHHXXX.
    """

    institution_name: str
    clearing_code: str
    bic: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        institution_name = self.institution_name

        clearing_code = self.clearing_code

        bic = self.bic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "institutionName": institution_name,
                "clearingCode": clearing_code,
                "BIC": bic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        institution_name = d.pop("institutionName")

        clearing_code = d.pop("clearingCode")

        bic = d.pop("BIC")

        get_participating_list_response_participating_banks = cls(
            institution_name=institution_name,
            clearing_code=clearing_code,
            bic=bic,
        )

        get_participating_list_response_participating_banks.additional_properties = d
        return get_participating_list_response_participating_banks

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
