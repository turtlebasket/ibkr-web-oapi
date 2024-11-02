from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trading_instrument_description import TradingInstrumentDescription


T = TypeVar("T", bound="InternalPositionTransferInstruction")


@_attrs_define
class InternalPositionTransferInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        source_account_id (str):  Example: U46377.
        target_account_id (str):  Example: U463756.
        transfer_quantity (float):  Example: 100.
        trading_instrument (Union['TradingInstrumentDescription', float]):
    """

    client_instruction_id: float
    source_account_id: str
    target_account_id: str
    transfer_quantity: float
    trading_instrument: Union["TradingInstrumentDescription", float]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trading_instrument_description import TradingInstrumentDescription

        client_instruction_id = self.client_instruction_id

        source_account_id = self.source_account_id

        target_account_id = self.target_account_id

        transfer_quantity = self.transfer_quantity

        trading_instrument: Union[Dict[str, Any], float]
        if isinstance(self.trading_instrument, TradingInstrumentDescription):
            trading_instrument = self.trading_instrument.to_dict()
        else:
            trading_instrument = self.trading_instrument

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "sourceAccountId": source_account_id,
                "targetAccountId": target_account_id,
                "transferQuantity": transfer_quantity,
                "tradingInstrument": trading_instrument,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trading_instrument_description import TradingInstrumentDescription

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        source_account_id = d.pop("sourceAccountId")

        target_account_id = d.pop("targetAccountId")

        transfer_quantity = d.pop("transferQuantity")

        def _parse_trading_instrument(data: object) -> Union["TradingInstrumentDescription", float]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_trading_instrument_type_1 = TradingInstrumentDescription.from_dict(data)

                return componentsschemas_trading_instrument_type_1
            except:  # noqa: E722
                pass
            return cast(Union["TradingInstrumentDescription", float], data)

        trading_instrument = _parse_trading_instrument(d.pop("tradingInstrument"))

        internal_position_transfer_instruction = cls(
            client_instruction_id=client_instruction_id,
            source_account_id=source_account_id,
            target_account_id=target_account_id,
            transfer_quantity=transfer_quantity,
            trading_instrument=trading_instrument,
        )

        internal_position_transfer_instruction.additional_properties = d
        return internal_position_transfer_instruction

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
