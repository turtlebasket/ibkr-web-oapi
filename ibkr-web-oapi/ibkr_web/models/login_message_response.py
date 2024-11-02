from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_message import LoginMessage


T = TypeVar("T", bound="LoginMessageResponse")


@_attrs_define
class LoginMessageResponse:
    """
    Attributes:
        account_id (Union[Unset, str]):
        clearing_status (Union[Unset, str]):
        clearing_status_description (Union[Unset, str]):
        login_messages (Union[Unset, List['LoginMessage']]):
        login_message_present (Union[Unset, bool]):
    """

    account_id: Union[Unset, str] = UNSET
    clearing_status: Union[Unset, str] = UNSET
    clearing_status_description: Union[Unset, str] = UNSET
    login_messages: Union[Unset, List["LoginMessage"]] = UNSET
    login_message_present: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        clearing_status = self.clearing_status

        clearing_status_description = self.clearing_status_description

        login_messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.login_messages, Unset):
            login_messages = []
            for login_messages_item_data in self.login_messages:
                login_messages_item = login_messages_item_data.to_dict()
                login_messages.append(login_messages_item)

        login_message_present = self.login_message_present

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if clearing_status is not UNSET:
            field_dict["clearingStatus"] = clearing_status
        if clearing_status_description is not UNSET:
            field_dict["clearingStatusDescription"] = clearing_status_description
        if login_messages is not UNSET:
            field_dict["loginMessages"] = login_messages
        if login_message_present is not UNSET:
            field_dict["loginMessagePresent"] = login_message_present

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.login_message import LoginMessage

        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        clearing_status = d.pop("clearingStatus", UNSET)

        clearing_status_description = d.pop("clearingStatusDescription", UNSET)

        login_messages = []
        _login_messages = d.pop("loginMessages", UNSET)
        for login_messages_item_data in _login_messages or []:
            login_messages_item = LoginMessage.from_dict(login_messages_item_data)

            login_messages.append(login_messages_item)

        login_message_present = d.pop("loginMessagePresent", UNSET)

        login_message_response = cls(
            account_id=account_id,
            clearing_status=clearing_status,
            clearing_status_description=clearing_status_description,
            login_messages=login_messages,
            login_message_present=login_message_present,
        )

        login_message_response.additional_properties = d
        return login_message_response

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
