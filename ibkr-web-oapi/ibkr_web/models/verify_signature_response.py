from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_64_url_string import Base64UrlString
    from ..models.jose_header import JoseHeader
    from ..models.jws_payload import JwsPayload


T = TypeVar("T", bound="VerifySignatureResponse")


@_attrs_define
class VerifySignatureResponse:
    """
    Attributes:
        active (Union[Unset, bool]):
        client_id (Union[Unset, str]):
        header (Union[Unset, JoseHeader]):
        payload (Union[Unset, JwsPayload]):
        signature (Union[Unset, Base64UrlString]):
        csid (Union[Unset, str]):
        account_id (Union[Unset, str]):
        jwt (Union[Unset, str]):
    """

    active: Union[Unset, bool] = UNSET
    client_id: Union[Unset, str] = UNSET
    header: Union[Unset, "JoseHeader"] = UNSET
    payload: Union[Unset, "JwsPayload"] = UNSET
    signature: Union[Unset, "Base64UrlString"] = UNSET
    csid: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    jwt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active

        client_id = self.client_id

        header: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        signature: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        csid = self.csid

        account_id = self.account_id

        jwt = self.jwt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if header is not UNSET:
            field_dict["header"] = header
        if payload is not UNSET:
            field_dict["payload"] = payload
        if signature is not UNSET:
            field_dict["signature"] = signature
        if csid is not UNSET:
            field_dict["csid"] = csid
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if jwt is not UNSET:
            field_dict["jwt"] = jwt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_64_url_string import Base64UrlString
        from ..models.jose_header import JoseHeader
        from ..models.jws_payload import JwsPayload

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        client_id = d.pop("client_id", UNSET)

        _header = d.pop("header", UNSET)
        header: Union[Unset, JoseHeader]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = JoseHeader.from_dict(_header)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, JwsPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = JwsPayload.from_dict(_payload)

        _signature = d.pop("signature", UNSET)
        signature: Union[Unset, Base64UrlString]
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = Base64UrlString.from_dict(_signature)

        csid = d.pop("csid", UNSET)

        account_id = d.pop("account_id", UNSET)

        jwt = d.pop("jwt", UNSET)

        verify_signature_response = cls(
            active=active,
            client_id=client_id,
            header=header,
            payload=payload,
            signature=signature,
            csid=csid,
            account_id=account_id,
            jwt=jwt,
        )

        verify_signature_response.additional_properties = d
        return verify_signature_response

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
