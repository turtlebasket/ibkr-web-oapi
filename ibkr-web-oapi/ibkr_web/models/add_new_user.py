from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_details import UserDetails


T = TypeVar("T", bound="AddNewUser")


@_attrs_define
class AddNewUser:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        prefix (Union[Unset, str]):
        user_details (Union[Unset, UserDetails]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    user_details: Union[Unset, "UserDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        prefix = self.prefix

        user_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_details, Unset):
            user_details = self.user_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if user_details is not UNSET:
            field_dict["userDetails"] = user_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_details import UserDetails

        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        prefix = d.pop("prefix", UNSET)

        _user_details = d.pop("userDetails", UNSET)
        user_details: Union[Unset, UserDetails]
        if isinstance(_user_details, Unset):
            user_details = UNSET
        else:
            user_details = UserDetails.from_dict(_user_details)

        add_new_user = cls(
            reference_account_id=reference_account_id,
            prefix=prefix,
            user_details=user_details,
        )

        add_new_user.additional_properties = d
        return add_new_user

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
