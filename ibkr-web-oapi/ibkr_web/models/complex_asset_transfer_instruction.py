from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.complex_asset_transfer_instruction_direction import ComplexAssetTransferInstructionDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contra_broker_info import ContraBrokerInfo
    from ..models.non_disclosed_detail import NonDisclosedDetail
    from ..models.trading_instrument_description import TradingInstrumentDescription


T = TypeVar("T", bound="ComplexAssetTransferInstruction")


@_attrs_define
class ComplexAssetTransferInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        direction (ComplexAssetTransferInstructionDirection):  Example: IN.
        account_id (str):  Example: U46377.
        quantity (float):  Example: 1000.
        trading_instrument (Union['TradingInstrumentDescription', float]):
        contra_broker_info (ContraBrokerInfo):
        non_disclosed_detail (Union[Unset, NonDisclosedDetail]):
    """

    client_instruction_id: float
    direction: ComplexAssetTransferInstructionDirection
    account_id: str
    quantity: float
    trading_instrument: Union["TradingInstrumentDescription", float]
    contra_broker_info: "ContraBrokerInfo"
    non_disclosed_detail: Union[Unset, "NonDisclosedDetail"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trading_instrument_description import TradingInstrumentDescription

        client_instruction_id = self.client_instruction_id

        direction = self.direction.value

        account_id = self.account_id

        quantity = self.quantity

        trading_instrument: Union[Dict[str, Any], float]
        if isinstance(self.trading_instrument, TradingInstrumentDescription):
            trading_instrument = self.trading_instrument.to_dict()
        else:
            trading_instrument = self.trading_instrument

        contra_broker_info = self.contra_broker_info.to_dict()

        non_disclosed_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.non_disclosed_detail, Unset):
            non_disclosed_detail = self.non_disclosed_detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "direction": direction,
                "accountId": account_id,
                "quantity": quantity,
                "tradingInstrument": trading_instrument,
                "contraBrokerInfo": contra_broker_info,
            }
        )
        if non_disclosed_detail is not UNSET:
            field_dict["nonDisclosedDetail"] = non_disclosed_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contra_broker_info import ContraBrokerInfo
        from ..models.non_disclosed_detail import NonDisclosedDetail
        from ..models.trading_instrument_description import TradingInstrumentDescription

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        direction = ComplexAssetTransferInstructionDirection(d.pop("direction"))

        account_id = d.pop("accountId")

        quantity = d.pop("quantity")

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

        contra_broker_info = ContraBrokerInfo.from_dict(d.pop("contraBrokerInfo"))

        _non_disclosed_detail = d.pop("nonDisclosedDetail", UNSET)
        non_disclosed_detail: Union[Unset, NonDisclosedDetail]
        if isinstance(_non_disclosed_detail, Unset):
            non_disclosed_detail = UNSET
        else:
            non_disclosed_detail = NonDisclosedDetail.from_dict(_non_disclosed_detail)

        complex_asset_transfer_instruction = cls(
            client_instruction_id=client_instruction_id,
            direction=direction,
            account_id=account_id,
            quantity=quantity,
            trading_instrument=trading_instrument,
            contra_broker_info=contra_broker_info,
            non_disclosed_detail=non_disclosed_detail,
        )

        complex_asset_transfer_instruction.additional_properties = d
        return complex_asset_transfer_instruction

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
