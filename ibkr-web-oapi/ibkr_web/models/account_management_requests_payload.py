from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_management_requests import AccountManagementRequests


T = TypeVar("T", bound="AccountManagementRequestsPayload")


@_attrs_define
class AccountManagementRequestsPayload:
    """
    Attributes:
        account_management_requests (Union[Unset, AccountManagementRequests]):
    """

    account_management_requests: Union[Unset, "AccountManagementRequests"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_management_requests: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_management_requests, Unset):
            account_management_requests = self.account_management_requests.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_management_requests is not UNSET:
            field_dict["accountManagementRequests"] = account_management_requests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_management_requests import AccountManagementRequests

        d = src_dict.copy()
        _account_management_requests = d.pop("accountManagementRequests", UNSET)
        account_management_requests: Union[Unset, AccountManagementRequests]
        if isinstance(_account_management_requests, Unset):
            account_management_requests = UNSET
        else:
            account_management_requests = AccountManagementRequests.from_dict(_account_management_requests)

        account_management_requests_payload = cls(
            account_management_requests=account_management_requests,
        )

        account_management_requests_payload.additional_properties = d
        return account_management_requests_payload

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
