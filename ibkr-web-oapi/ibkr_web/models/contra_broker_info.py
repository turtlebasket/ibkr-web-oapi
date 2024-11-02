from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContraBrokerInfo")


@_attrs_define
class ContraBrokerInfo:
    """
    Attributes:
        account_type (str):  Example: ORG.
        broker_name (str):  Example: JP MORGAN.
        depository_id (str):  Example: 1234.
        broker_account_id (str):  Example: as3456567678578N.
        country (str):  Example: United States.
        contact_email (str):  Example: a@gmail.com.
        contact_phone (float):  Example: 2039126155.
        contact_name (Union[Unset, str]):  Example: as.
    """

    account_type: str
    broker_name: str
    depository_id: str
    broker_account_id: str
    country: str
    contact_email: str
    contact_phone: float
    contact_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_type = self.account_type

        broker_name = self.broker_name

        depository_id = self.depository_id

        broker_account_id = self.broker_account_id

        country = self.country

        contact_email = self.contact_email

        contact_phone = self.contact_phone

        contact_name = self.contact_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountType": account_type,
                "brokerName": broker_name,
                "depositoryId": depository_id,
                "brokerAccountId": broker_account_id,
                "country": country,
                "contactEmail": contact_email,
                "contactPhone": contact_phone,
            }
        )
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_type = d.pop("accountType")

        broker_name = d.pop("brokerName")

        depository_id = d.pop("depositoryId")

        broker_account_id = d.pop("brokerAccountId")

        country = d.pop("country")

        contact_email = d.pop("contactEmail")

        contact_phone = d.pop("contactPhone")

        contact_name = d.pop("contactName", UNSET)

        contra_broker_info = cls(
            account_type=account_type,
            broker_name=broker_name,
            depository_id=depository_id,
            broker_account_id=broker_account_id,
            country=country,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_name=contact_name,
        )

        contra_broker_info.additional_properties = d
        return contra_broker_info

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
