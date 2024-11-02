from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YodleeSession")


@_attrs_define
class YodleeSession:
    """
    Attributes:
        request (Union[Unset, str]):
        username (Union[Unset, str]):
        item_account_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
    """

    request: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    item_account_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request = self.request

        username = self.username

        item_account_id = self.item_account_id

        account_id = self.account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request is not UNSET:
            field_dict["request"] = request
        if username is not UNSET:
            field_dict["username"] = username
        if item_account_id is not UNSET:
            field_dict["itemAccountId"] = item_account_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request = d.pop("request", UNSET)

        username = d.pop("username", UNSET)

        item_account_id = d.pop("itemAccountId", UNSET)

        account_id = d.pop("accountId", UNSET)

        yodlee_session = cls(
            request=request,
            username=username,
            item_account_id=item_account_id,
            account_id=account_id,
        )

        yodlee_session.additional_properties = d
        return yodlee_session

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
