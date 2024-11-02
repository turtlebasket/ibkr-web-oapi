from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_email import UpdateEmail
    from ..models.update_password import UpdatePassword


T = TypeVar("T", bound="UpdateCredentials")


@_attrs_define
class UpdateCredentials:
    """
    Attributes:
        update_email (Union[Unset, UpdateEmail]):
        update_password (Union[Unset, UpdatePassword]):
        reference_account_id (Union[Unset, str]):
        reference_user_name (Union[Unset, str]):
    """

    update_email: Union[Unset, "UpdateEmail"] = UNSET
    update_password: Union[Unset, "UpdatePassword"] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    reference_user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        update_email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_email, Unset):
            update_email = self.update_email.to_dict()

        update_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_password, Unset):
            update_password = self.update_password.to_dict()

        reference_account_id = self.reference_account_id

        reference_user_name = self.reference_user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_email is not UNSET:
            field_dict["updateEmail"] = update_email
        if update_password is not UNSET:
            field_dict["updatePassword"] = update_password
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if reference_user_name is not UNSET:
            field_dict["referenceUserName"] = reference_user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_email import UpdateEmail
        from ..models.update_password import UpdatePassword

        d = src_dict.copy()
        _update_email = d.pop("updateEmail", UNSET)
        update_email: Union[Unset, UpdateEmail]
        if isinstance(_update_email, Unset):
            update_email = UNSET
        else:
            update_email = UpdateEmail.from_dict(_update_email)

        _update_password = d.pop("updatePassword", UNSET)
        update_password: Union[Unset, UpdatePassword]
        if isinstance(_update_password, Unset):
            update_password = UNSET
        else:
            update_password = UpdatePassword.from_dict(_update_password)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        reference_user_name = d.pop("referenceUserName", UNSET)

        update_credentials = cls(
            update_email=update_email,
            update_password=update_password,
            reference_account_id=reference_account_id,
            reference_user_name=reference_user_name,
        )

        update_credentials.additional_properties = d
        return update_credentials

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
