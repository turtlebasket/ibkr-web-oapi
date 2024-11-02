from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSessionRequest")


@_attrs_define
class CreateSessionRequest:
    """
    Attributes:
        iss (str): The underlying client ID Example: c23341f4-b51e-49a7-a655-7db2f07b1a26.
        jti (str): A unique JWT ID used to prevent replay attacks Example: 8366182a-c92e-4e9c-bd4f-7a0a074dd230.
        service (str):  Example: AM_LOGIN.
        credential (str):  Example: ddowney2.
        user_ip (Union[Unset, str]):  Example: 10.10.10.10.
    """

    iss: str
    jti: str
    service: str
    credential: str
    user_ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iss = self.iss

        jti = self.jti

        service = self.service

        credential = self.credential

        user_ip = self.user_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iss": iss,
                "jti": jti,
                "service": service,
                "credential": credential,
            }
        )
        if user_ip is not UNSET:
            field_dict["userIp"] = user_ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iss = d.pop("iss")

        jti = d.pop("jti")

        service = d.pop("service")

        credential = d.pop("credential")

        user_ip = d.pop("userIp", UNSET)

        create_session_request = cls(
            iss=iss,
            jti=jti,
            service=service,
            credential=credential,
            user_ip=user_ip,
        )

        create_session_request.additional_properties = d
        return create_session_request

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
