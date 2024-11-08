from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application import Application


T = TypeVar("T", bound="ApplicationPayload")


@_attrs_define
class ApplicationPayload:
    """
    Attributes:
        application (Union[Unset, Application]):
    """

    application: Union[Unset, "Application"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        application: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application is not UNSET:
            field_dict["application"] = application

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.application import Application

        d = src_dict.copy()
        _application = d.pop("application", UNSET)
        application: Union[Unset, Application]
        if isinstance(_application, Unset):
            application = UNSET
        else:
            application = Application.from_dict(_application)

        application_payload = cls(
            application=application,
        )

        application_payload.additional_properties = d
        return application_payload

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
