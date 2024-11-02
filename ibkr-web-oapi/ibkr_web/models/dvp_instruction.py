import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dvp_instruction_asset_class import DVPInstructionAssetClass
from ..models.dvp_instruction_exchange import DVPInstructionExchange
from ..models.dvp_instruction_role import DVPInstructionRole
from ..models.dvp_instruction_tx_group_code import DVPInstructionTxGroupCode
from ..models.dvp_instruction_type import DVPInstructionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DVPInstruction")


@_attrs_define
class DVPInstruction:
    """
    Attributes:
        id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        external_account_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[Unset, DVPInstructionType]):
        role (Union[Unset, DVPInstructionRole]):
        agent_id (Union[Unset, str]):
        firm_id (Union[Unset, str]):
        agent_name (Union[Unset, str]):
        account_name (Union[Unset, str]):
        day_do_id (Union[Unset, str]):
        tx_group_code (Union[Unset, DVPInstructionTxGroupCode]):
        broker_code (Union[Unset, str]):
        asset_class (Union[Unset, DVPInstructionAssetClass]):
        exchange (Union[Unset, DVPInstructionExchange]):
        prepay_tax (Union[Unset, bool]):
        prepay_commission (Union[Unset, bool]):
        expiry (Union[Unset, datetime.date]):
        default (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    external_account_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, DVPInstructionType] = UNSET
    role: Union[Unset, DVPInstructionRole] = UNSET
    agent_id: Union[Unset, str] = UNSET
    firm_id: Union[Unset, str] = UNSET
    agent_name: Union[Unset, str] = UNSET
    account_name: Union[Unset, str] = UNSET
    day_do_id: Union[Unset, str] = UNSET
    tx_group_code: Union[Unset, DVPInstructionTxGroupCode] = UNSET
    broker_code: Union[Unset, str] = UNSET
    asset_class: Union[Unset, DVPInstructionAssetClass] = UNSET
    exchange: Union[Unset, DVPInstructionExchange] = UNSET
    prepay_tax: Union[Unset, bool] = UNSET
    prepay_commission: Union[Unset, bool] = UNSET
    expiry: Union[Unset, datetime.date] = UNSET
    default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        external_id = self.external_id

        external_account_id = self.external_account_id

        account_id = self.account_id

        name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        agent_id = self.agent_id

        firm_id = self.firm_id

        agent_name = self.agent_name

        account_name = self.account_name

        day_do_id = self.day_do_id

        tx_group_code: Union[Unset, str] = UNSET
        if not isinstance(self.tx_group_code, Unset):
            tx_group_code = self.tx_group_code.value

        broker_code = self.broker_code

        asset_class: Union[Unset, str] = UNSET
        if not isinstance(self.asset_class, Unset):
            asset_class = self.asset_class.value

        exchange: Union[Unset, str] = UNSET
        if not isinstance(self.exchange, Unset):
            exchange = self.exchange.value

        prepay_tax = self.prepay_tax

        prepay_commission = self.prepay_commission

        expiry: Union[Unset, str] = UNSET
        if not isinstance(self.expiry, Unset):
            expiry = self.expiry.isoformat()

        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if external_account_id is not UNSET:
            field_dict["externalAccountID"] = external_account_id
        if account_id is not UNSET:
            field_dict["accountID"] = account_id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if role is not UNSET:
            field_dict["role"] = role
        if agent_id is not UNSET:
            field_dict["agentID"] = agent_id
        if firm_id is not UNSET:
            field_dict["firmID"] = firm_id
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if day_do_id is not UNSET:
            field_dict["dayDoID"] = day_do_id
        if tx_group_code is not UNSET:
            field_dict["txGroupCode"] = tx_group_code
        if broker_code is not UNSET:
            field_dict["brokerCode"] = broker_code
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if prepay_tax is not UNSET:
            field_dict["prepayTax"] = prepay_tax
        if prepay_commission is not UNSET:
            field_dict["prepayCommission"] = prepay_commission
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        external_account_id = d.pop("externalAccountID", UNSET)

        account_id = d.pop("accountID", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DVPInstructionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DVPInstructionType(_type)

        _role = d.pop("role", UNSET)
        role: Union[Unset, DVPInstructionRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = DVPInstructionRole(_role)

        agent_id = d.pop("agentID", UNSET)

        firm_id = d.pop("firmID", UNSET)

        agent_name = d.pop("agentName", UNSET)

        account_name = d.pop("accountName", UNSET)

        day_do_id = d.pop("dayDoID", UNSET)

        _tx_group_code = d.pop("txGroupCode", UNSET)
        tx_group_code: Union[Unset, DVPInstructionTxGroupCode]
        if isinstance(_tx_group_code, Unset):
            tx_group_code = UNSET
        else:
            tx_group_code = DVPInstructionTxGroupCode(_tx_group_code)

        broker_code = d.pop("brokerCode", UNSET)

        _asset_class = d.pop("assetClass", UNSET)
        asset_class: Union[Unset, DVPInstructionAssetClass]
        if isinstance(_asset_class, Unset):
            asset_class = UNSET
        else:
            asset_class = DVPInstructionAssetClass(_asset_class)

        _exchange = d.pop("exchange", UNSET)
        exchange: Union[Unset, DVPInstructionExchange]
        if isinstance(_exchange, Unset):
            exchange = UNSET
        else:
            exchange = DVPInstructionExchange(_exchange)

        prepay_tax = d.pop("prepayTax", UNSET)

        prepay_commission = d.pop("prepayCommission", UNSET)

        _expiry = d.pop("expiry", UNSET)
        expiry: Union[Unset, datetime.date]
        if isinstance(_expiry, Unset):
            expiry = UNSET
        else:
            expiry = isoparse(_expiry).date()

        default = d.pop("default", UNSET)

        dvp_instruction = cls(
            id=id,
            external_id=external_id,
            external_account_id=external_account_id,
            account_id=account_id,
            name=name,
            type=type,
            role=role,
            agent_id=agent_id,
            firm_id=firm_id,
            agent_name=agent_name,
            account_name=account_name,
            day_do_id=day_do_id,
            tx_group_code=tx_group_code,
            broker_code=broker_code,
            asset_class=asset_class,
            exchange=exchange,
            prepay_tax=prepay_tax,
            prepay_commission=prepay_commission,
            expiry=expiry,
            default=default,
        )

        dvp_instruction.additional_properties = d
        return dvp_instruction

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
