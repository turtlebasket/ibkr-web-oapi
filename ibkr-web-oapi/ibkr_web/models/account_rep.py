from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rep_detail import RepDetail


T = TypeVar("T", bound="AccountRep")


@_attrs_define
class AccountRep:
    """
    Attributes:
        rep_details (Union[Unset, List['RepDetail']]):
        included (Union[Unset, bool]):
    """

    rep_details: Union[Unset, List["RepDetail"]] = UNSET
    included: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rep_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rep_details, Unset):
            rep_details = []
            for rep_details_item_data in self.rep_details:
                rep_details_item = rep_details_item_data.to_dict()
                rep_details.append(rep_details_item)

        included = self.included

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rep_details is not UNSET:
            field_dict["repDetails"] = rep_details
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rep_detail import RepDetail

        d = src_dict.copy()
        rep_details = []
        _rep_details = d.pop("repDetails", UNSET)
        for rep_details_item_data in _rep_details or []:
            rep_details_item = RepDetail.from_dict(rep_details_item_data)

            rep_details.append(rep_details_item)

        included = d.pop("included", UNSET)

        account_rep = cls(
            rep_details=rep_details,
            included=included,
        )

        account_rep.additional_properties = d
        return account_rep

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
