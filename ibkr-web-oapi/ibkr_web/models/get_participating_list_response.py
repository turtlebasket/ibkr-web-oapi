from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_participating_list_response_participating_banks import (
        GetParticipatingListResponseParticipatingBanks,
    )


T = TypeVar("T", bound="GetParticipatingListResponse")


@_attrs_define
class GetParticipatingListResponse:
    """
    Attributes:
        type (str):  Example: eDDA.
        participating_banks (GetParticipatingListResponseParticipatingBanks):
    """

    type: str
    participating_banks: "GetParticipatingListResponseParticipatingBanks"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        participating_banks = self.participating_banks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "participatingBanks": participating_banks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_participating_list_response_participating_banks import (
            GetParticipatingListResponseParticipatingBanks,
        )

        d = src_dict.copy()
        type = d.pop("type")

        participating_banks = GetParticipatingListResponseParticipatingBanks.from_dict(d.pop("participatingBanks"))

        get_participating_list_response = cls(
            type=type,
            participating_banks=participating_banks,
        )

        get_participating_list_response.additional_properties = d
        return get_participating_list_response

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
