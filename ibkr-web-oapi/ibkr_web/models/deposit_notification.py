from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deposit_notification_currency import DepositNotificationCurrency
from ..models.deposit_notification_type import DepositNotificationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ach_details import ACHDetails
    from ..models.check_details import CheckDetails
    from ..models.ira_deposit_details import IRADepositDetails
    from ..models.wire_details import WireDetails


T = TypeVar("T", bound="DepositNotification")


@_attrs_define
class DepositNotification:
    """
    Attributes:
        check_details (Union[Unset, CheckDetails]):
        wire_details (Union[Unset, WireDetails]):
        ach_details (Union[Unset, ACHDetails]):
        ira_deposit_details (Union[Unset, IRADepositDetails]):
        type (Union[Unset, DepositNotificationType]):
        amount (Union[Unset, float]):
        currency (Union[Unset, DepositNotificationCurrency]):
        ib_account (Union[Unset, str]):
    """

    check_details: Union[Unset, "CheckDetails"] = UNSET
    wire_details: Union[Unset, "WireDetails"] = UNSET
    ach_details: Union[Unset, "ACHDetails"] = UNSET
    ira_deposit_details: Union[Unset, "IRADepositDetails"] = UNSET
    type: Union[Unset, DepositNotificationType] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, DepositNotificationCurrency] = UNSET
    ib_account: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        check_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.check_details, Unset):
            check_details = self.check_details.to_dict()

        wire_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wire_details, Unset):
            wire_details = self.wire_details.to_dict()

        ach_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ach_details, Unset):
            ach_details = self.ach_details.to_dict()

        ira_deposit_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ira_deposit_details, Unset):
            ira_deposit_details = self.ira_deposit_details.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        amount = self.amount

        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        ib_account = self.ib_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_details is not UNSET:
            field_dict["checkDetails"] = check_details
        if wire_details is not UNSET:
            field_dict["wireDetails"] = wire_details
        if ach_details is not UNSET:
            field_dict["achDetails"] = ach_details
        if ira_deposit_details is not UNSET:
            field_dict["iraDepositDetails"] = ira_deposit_details
        if type is not UNSET:
            field_dict["type"] = type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ib_account is not UNSET:
            field_dict["ibAccount"] = ib_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ach_details import ACHDetails
        from ..models.check_details import CheckDetails
        from ..models.ira_deposit_details import IRADepositDetails
        from ..models.wire_details import WireDetails

        d = src_dict.copy()
        _check_details = d.pop("checkDetails", UNSET)
        check_details: Union[Unset, CheckDetails]
        if isinstance(_check_details, Unset):
            check_details = UNSET
        else:
            check_details = CheckDetails.from_dict(_check_details)

        _wire_details = d.pop("wireDetails", UNSET)
        wire_details: Union[Unset, WireDetails]
        if isinstance(_wire_details, Unset):
            wire_details = UNSET
        else:
            wire_details = WireDetails.from_dict(_wire_details)

        _ach_details = d.pop("achDetails", UNSET)
        ach_details: Union[Unset, ACHDetails]
        if isinstance(_ach_details, Unset):
            ach_details = UNSET
        else:
            ach_details = ACHDetails.from_dict(_ach_details)

        _ira_deposit_details = d.pop("iraDepositDetails", UNSET)
        ira_deposit_details: Union[Unset, IRADepositDetails]
        if isinstance(_ira_deposit_details, Unset):
            ira_deposit_details = UNSET
        else:
            ira_deposit_details = IRADepositDetails.from_dict(_ira_deposit_details)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DepositNotificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DepositNotificationType(_type)

        amount = d.pop("amount", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, DepositNotificationCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = DepositNotificationCurrency(_currency)

        ib_account = d.pop("ibAccount", UNSET)

        deposit_notification = cls(
            check_details=check_details,
            wire_details=wire_details,
            ach_details=ach_details,
            ira_deposit_details=ira_deposit_details,
            type=type,
            amount=amount,
            currency=currency,
            ib_account=ib_account,
        )

        deposit_notification.additional_properties = d
        return deposit_notification

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
