from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_position_transfer_source_ira_type import ExternalPositionTransferSourceIRAType
from ..models.external_position_transfer_subtype import ExternalPositionTransferSubtype
from ..models.external_position_transfer_type import ExternalPositionTransferType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalPositionTransfer")


@_attrs_define
class ExternalPositionTransfer:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        type (ExternalPositionTransferType):  Example: FULL.
        subtype (ExternalPositionTransferSubtype):  Example: ACATS.
        broker_id (str):  Example: 0226.
        broker_name (str):  Example: Wall Street Financial Group.
        account_at_broker (str):  Example: SOL12345.
        account_id (str):  Example: U2323232.
        signature (str):  Example: sample signature.
        source_ira_type (Union[Unset, ExternalPositionTransferSourceIRAType]):  Example: RO.
    """

    client_instruction_id: float
    type: ExternalPositionTransferType
    subtype: ExternalPositionTransferSubtype
    broker_id: str
    broker_name: str
    account_at_broker: str
    account_id: str
    signature: str
    source_ira_type: Union[Unset, ExternalPositionTransferSourceIRAType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        type = self.type.value

        subtype = self.subtype.value

        broker_id = self.broker_id

        broker_name = self.broker_name

        account_at_broker = self.account_at_broker

        account_id = self.account_id

        signature = self.signature

        source_ira_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_ira_type, Unset):
            source_ira_type = self.source_ira_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "type": type,
                "subtype": subtype,
                "brokerId": broker_id,
                "brokerName": broker_name,
                "accountAtBroker": account_at_broker,
                "accountId": account_id,
                "signature": signature,
            }
        )
        if source_ira_type is not UNSET:
            field_dict["sourceIRAType"] = source_ira_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        type = ExternalPositionTransferType(d.pop("type"))

        subtype = ExternalPositionTransferSubtype(d.pop("subtype"))

        broker_id = d.pop("brokerId")

        broker_name = d.pop("brokerName")

        account_at_broker = d.pop("accountAtBroker")

        account_id = d.pop("accountId")

        signature = d.pop("signature")

        _source_ira_type = d.pop("sourceIRAType", UNSET)
        source_ira_type: Union[Unset, ExternalPositionTransferSourceIRAType]
        if isinstance(_source_ira_type, Unset):
            source_ira_type = UNSET
        else:
            source_ira_type = ExternalPositionTransferSourceIRAType(_source_ira_type)

        external_position_transfer = cls(
            client_instruction_id=client_instruction_id,
            type=type,
            subtype=subtype,
            broker_id=broker_id,
            broker_name=broker_name,
            account_at_broker=account_at_broker,
            account_id=account_id,
            signature=signature,
            source_ira_type=source_ira_type,
        )

        external_position_transfer.additional_properties = d
        return external_position_transfer

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
