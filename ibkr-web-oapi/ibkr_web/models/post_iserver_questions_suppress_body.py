from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostIserverQuestionsSuppressBody")


@_attrs_define
class PostIserverQuestionsSuppressBody:
    """
    Attributes:
        message_ids (Union[Unset, List[str]]): Array of order reply messageId identifier strings to be suppressed.
    """

    message_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.message_ids, Unset):
            message_ids = self.message_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_ids is not UNSET:
            field_dict["messageIds"] = message_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message_ids = cast(List[str], d.pop("messageIds", UNSET))

        post_iserver_questions_suppress_body = cls(
            message_ids=message_ids,
        )

        post_iserver_questions_suppress_body.additional_properties = d
        return post_iserver_questions_suppress_body

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
