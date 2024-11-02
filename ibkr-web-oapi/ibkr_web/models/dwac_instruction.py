from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dwac_instruction_direction import DwacInstructionDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trading_instrument_description import TradingInstrumentDescription


T = TypeVar("T", bound="DwacInstruction")


@_attrs_define
class DwacInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        direction (DwacInstructionDirection):  Example: IN.
        account_id (str):  Example: U46377.
        contra_broker_account_id (str):  Example: 12345678A.
        contra_broker_tax_id (str):  Example: 123456789.
        quantity (float):  Example: 1000.
        trading_instrument (Union['TradingInstrumentDescription', Unset, float]):
        account_title (Union[Unset, str]):  Example: Title.
        refrence_id (Union[Unset, str]):  Example: refId.
    """

    client_instruction_id: float
    direction: DwacInstructionDirection
    account_id: str
    contra_broker_account_id: str
    contra_broker_tax_id: str
    quantity: float
    trading_instrument: Union["TradingInstrumentDescription", Unset, float] = UNSET
    account_title: Union[Unset, str] = UNSET
    refrence_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trading_instrument_description import TradingInstrumentDescription

        client_instruction_id = self.client_instruction_id

        direction = self.direction.value

        account_id = self.account_id

        contra_broker_account_id = self.contra_broker_account_id

        contra_broker_tax_id = self.contra_broker_tax_id

        quantity = self.quantity

        trading_instrument: Union[Dict[str, Any], Unset, float]
        if isinstance(self.trading_instrument, Unset):
            trading_instrument = UNSET
        elif isinstance(self.trading_instrument, TradingInstrumentDescription):
            trading_instrument = self.trading_instrument.to_dict()
        else:
            trading_instrument = self.trading_instrument

        account_title = self.account_title

        refrence_id = self.refrence_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "direction": direction,
                "accountId": account_id,
                "contraBrokerAccountId": contra_broker_account_id,
                "contraBrokerTaxId": contra_broker_tax_id,
                "quantity": quantity,
            }
        )
        if trading_instrument is not UNSET:
            field_dict["tradingInstrument"] = trading_instrument
        if account_title is not UNSET:
            field_dict["accountTitle"] = account_title
        if refrence_id is not UNSET:
            field_dict["refrenceId"] = refrence_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trading_instrument_description import TradingInstrumentDescription

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        direction = DwacInstructionDirection(d.pop("direction"))

        account_id = d.pop("accountId")

        contra_broker_account_id = d.pop("contraBrokerAccountId")

        contra_broker_tax_id = d.pop("contraBrokerTaxId")

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

        account_title = d.pop("accountTitle", UNSET)

        refrence_id = d.pop("refrenceId", UNSET)

        dwac_instruction = cls(
            client_instruction_id=client_instruction_id,
            direction=direction,
            account_id=account_id,
            contra_broker_account_id=contra_broker_account_id,
            contra_broker_tax_id=contra_broker_tax_id,
            quantity=quantity,
            trading_instrument=trading_instrument,
            account_title=account_title,
            refrence_id=refrence_id,
        )

        dwac_instruction.additional_properties = d
        return dwac_instruction

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
