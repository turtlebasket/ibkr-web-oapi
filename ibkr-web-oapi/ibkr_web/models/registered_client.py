import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.registered_client_client_status import RegisteredClientClientStatus
from ..models.registered_client_client_type import RegisteredClientClientType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_public_key_set import ClientPublicKeySet


T = TypeVar("T", bound="RegisteredClient")


@_attrs_define
class RegisteredClient:
    """
    Attributes:
        id (Union[Unset, int]):
        client_id (Union[Unset, str]):
        client_name (Union[Unset, str]):
        client_type (Union[Unset, RegisteredClientClientType]):
        client_status (Union[Unset, RegisteredClientClientStatus]):
        redirect_uris (Union[Unset, List[str]]):
        jwks (Union[Unset, ClientPublicKeySet]):
        description (Union[Unset, str]):
        client_uri (Union[Unset, str]):
        logo_uri (Union[Unset, str]):
        policy_uri (Union[Unset, str]):
        account_id (Union[Unset, str]):
        csid (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    client_id: Union[Unset, str] = UNSET
    client_name: Union[Unset, str] = UNSET
    client_type: Union[Unset, RegisteredClientClientType] = UNSET
    client_status: Union[Unset, RegisteredClientClientStatus] = UNSET
    redirect_uris: Union[Unset, List[str]] = UNSET
    jwks: Union[Unset, "ClientPublicKeySet"] = UNSET
    description: Union[Unset, str] = UNSET
    client_uri: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, str] = UNSET
    policy_uri: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    csid: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        client_id = self.client_id

        client_name = self.client_name

        client_type: Union[Unset, str] = UNSET
        if not isinstance(self.client_type, Unset):
            client_type = self.client_type.value

        client_status: Union[Unset, str] = UNSET
        if not isinstance(self.client_status, Unset):
            client_status = self.client_status.value

        redirect_uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        jwks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jwks, Unset):
            jwks = self.jwks.to_dict()

        description = self.description

        client_uri = self.client_uri

        logo_uri = self.logo_uri

        policy_uri = self.policy_uri

        account_id = self.account_id

        csid = self.csid

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_name is not UNSET:
            field_dict["client_name"] = client_name
        if client_type is not UNSET:
            field_dict["client_type"] = client_type
        if client_status is not UNSET:
            field_dict["client_status"] = client_status
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris
        if jwks is not UNSET:
            field_dict["jwks"] = jwks
        if description is not UNSET:
            field_dict["description"] = description
        if client_uri is not UNSET:
            field_dict["client_uri"] = client_uri
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if policy_uri is not UNSET:
            field_dict["policy_uri"] = policy_uri
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if csid is not UNSET:
            field_dict["csid"] = csid
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_public_key_set import ClientPublicKeySet

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        client_id = d.pop("client_id", UNSET)

        client_name = d.pop("client_name", UNSET)

        _client_type = d.pop("client_type", UNSET)
        client_type: Union[Unset, RegisteredClientClientType]
        if isinstance(_client_type, Unset):
            client_type = UNSET
        else:
            client_type = RegisteredClientClientType(_client_type)

        _client_status = d.pop("client_status", UNSET)
        client_status: Union[Unset, RegisteredClientClientStatus]
        if isinstance(_client_status, Unset):
            client_status = UNSET
        else:
            client_status = RegisteredClientClientStatus(_client_status)

        redirect_uris = cast(List[str], d.pop("redirect_uris", UNSET))

        _jwks = d.pop("jwks", UNSET)
        jwks: Union[Unset, ClientPublicKeySet]
        if isinstance(_jwks, Unset):
            jwks = UNSET
        else:
            jwks = ClientPublicKeySet.from_dict(_jwks)

        description = d.pop("description", UNSET)

        client_uri = d.pop("client_uri", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        policy_uri = d.pop("policy_uri", UNSET)

        account_id = d.pop("account_id", UNSET)

        csid = d.pop("csid", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        registered_client = cls(
            id=id,
            client_id=client_id,
            client_name=client_name,
            client_type=client_type,
            client_status=client_status,
            redirect_uris=redirect_uris,
            jwks=jwks,
            description=description,
            client_uri=client_uri,
            logo_uri=logo_uri,
            policy_uri=policy_uri,
            account_id=account_id,
            csid=csid,
            created_at=created_at,
        )

        registered_client.additional_properties = d
        return registered_client

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
