from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrokerageSessionInitRequest")


@_attrs_define
class BrokerageSessionInitRequest:
    """
    Attributes:
        publish (Union[Unset, bool]): publish brokerage session token at the same time when brokerage session
            initialized. If set false, then session token should be published before calling init. Setting true is preferred
            way.
        compete (Union[Unset, bool]): Determines if other brokerage sessions should be disconnected to prioritize this
            connection.
    """

    publish: Union[Unset, bool] = UNSET
    compete: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        publish = self.publish

        compete = self.compete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if publish is not UNSET:
            field_dict["publish"] = publish
        if compete is not UNSET:
            field_dict["compete"] = compete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        publish = d.pop("publish", UNSET)

        compete = d.pop("compete", UNSET)

        brokerage_session_init_request = cls(
            publish=publish,
            compete=compete,
        )

        brokerage_session_init_request.additional_properties = d
        return brokerage_session_init_request

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
