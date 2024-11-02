from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fop_instruction_direction import FopInstructionDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trading_instrument_description import TradingInstrumentDescription


T = TypeVar("T", bound="FopInstruction")


@_attrs_define
class FopInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        direction (FopInstructionDirection):  Example: IN.
        account_id (str):  Example: U46377.
        contra_broker_account_id (str):  Example: 12345678A.
        contra_broker_dtc_code (str):  Example: 348.
        quantity (float):  Example: 1000.
        trading_instrument (Union['TradingInstrumentDescription', Unset, float]):
    """

    client_instruction_id: float
    direction: FopInstructionDirection
    account_id: str
    contra_broker_account_id: str
    contra_broker_dtc_code: str
    quantity: float
    trading_instrument: Union["TradingInstrumentDescription", Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trading_instrument_description import TradingInstrumentDescription

        client_instruction_id = self.client_instruction_id

        direction = self.direction.value

        account_id = self.account_id

        contra_broker_account_id = self.contra_broker_account_id

        contra_broker_dtc_code = self.contra_broker_dtc_code

        quantity = self.quantity

        trading_instrument: Union[Dict[str, Any], Unset, float]
        if isinstance(self.trading_instrument, Unset):
            trading_instrument = UNSET
        elif isinstance(self.trading_instrument, TradingInstrumentDescription):
            trading_instrument = self.trading_instrument.to_dict()
        else:
            trading_instrument = self.trading_instrument

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "direction": direction,
                "accountId": account_id,
                "contraBrokerAccountId": contra_broker_account_id,
                "contraBrokerDtcCode": contra_broker_dtc_code,
                "quantity": quantity,
            }
        )
        if trading_instrument is not UNSET:
            field_dict["tradingInstrument"] = trading_instrument

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trading_instrument_description import TradingInstrumentDescription

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        direction = FopInstructionDirection(d.pop("direction"))

        account_id = d.pop("accountId")

        contra_broker_account_id = d.pop("contraBrokerAccountId")

        contra_broker_dtc_code = d.pop("contraBrokerDtcCode")

        quantity = d.pop("quantity")

        def _parse_trading_instrument(data: object) -> Union["TradingInstrumentDescription", Unset, float]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_trading_instrument_type_1 = TradingInstrumentDescription.from_dict(data)

                return componentsschemas_trading_instrument_type_1
            except:  # noqa: E722
                pass
            return cast(Union["TradingInstrumentDescription", Unset, float], data)

        trading_instrument = _parse_trading_instrument(d.pop("tradingInstrument", UNSET))

        fop_instruction = cls(
            client_instruction_id=client_instruction_id,
            direction=direction,
            account_id=account_id,
            contra_broker_account_id=contra_broker_account_id,
            contra_broker_dtc_code=contra_broker_dtc_code,
            quantity=quantity,
            trading_instrument=trading_instrument,
        )

        fop_instruction.additional_properties = d
        return fop_instruction

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
