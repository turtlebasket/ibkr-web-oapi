from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ext_positions_transfer_type_src_ira_type import ExtPositionsTransferTypeSrcIRAType
from ..models.ext_positions_transfer_type_sub_type import ExtPositionsTransferTypeSubType
from ..models.ext_positions_transfer_type_type import ExtPositionsTransferTypeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_bond_position import PartialBondPosition
    from ..models.partial_cash_position import PartialCashPosition
    from ..models.partial_fund_position import PartialFundPosition
    from ..models.partial_option_position import PartialOptionPosition
    from ..models.partial_stock_position import PartialStockPosition
    from ..models.partial_warrant_position import PartialWarrantPosition


T = TypeVar("T", bound="ExtPositionsTransferType")


@_attrs_define
class ExtPositionsTransferType:
    """
    Attributes:
        partial_stock_positions (Union[Unset, List['PartialStockPosition']]):
        partial_bond_positions (Union[Unset, List['PartialBondPosition']]):
        partial_option_positions (Union[Unset, List['PartialOptionPosition']]):
        partial_warrant_positions (Union[Unset, List['PartialWarrantPosition']]):
        partial_fund_positions (Union[Unset, List['PartialFundPosition']]):
        partial_cash_positions (Union[Unset, List['PartialCashPosition']]):
        type (Union[Unset, ExtPositionsTransferTypeType]):
        sub_type (Union[Unset, ExtPositionsTransferTypeSubType]):
        broker_id (Union[Unset, str]):
        broker_name (Union[Unset, str]):
        account_at_broker (Union[Unset, str]):
        src_ira_type (Union[Unset, ExtPositionsTransferTypeSrcIRAType]):
        margin_loan (Union[Unset, bool]):
        short_pos (Union[Unset, bool]):
        option_pos (Union[Unset, bool]):
        ib_account (Union[Unset, str]):
        third_party_type (Union[Unset, str]):
        approximate_account_value (Union[Unset, int]):
        ssn (Union[Unset, str]):
        ein (Union[Unset, str]):
        signature (Union[Unset, str]):
        authorize_to_remove_fund (Union[Unset, bool]):
    """

    partial_stock_positions: Union[Unset, List["PartialStockPosition"]] = UNSET
    partial_bond_positions: Union[Unset, List["PartialBondPosition"]] = UNSET
    partial_option_positions: Union[Unset, List["PartialOptionPosition"]] = UNSET
    partial_warrant_positions: Union[Unset, List["PartialWarrantPosition"]] = UNSET
    partial_fund_positions: Union[Unset, List["PartialFundPosition"]] = UNSET
    partial_cash_positions: Union[Unset, List["PartialCashPosition"]] = UNSET
    type: Union[Unset, ExtPositionsTransferTypeType] = UNSET
    sub_type: Union[Unset, ExtPositionsTransferTypeSubType] = UNSET
    broker_id: Union[Unset, str] = UNSET
    broker_name: Union[Unset, str] = UNSET
    account_at_broker: Union[Unset, str] = UNSET
    src_ira_type: Union[Unset, ExtPositionsTransferTypeSrcIRAType] = UNSET
    margin_loan: Union[Unset, bool] = UNSET
    short_pos: Union[Unset, bool] = UNSET
    option_pos: Union[Unset, bool] = UNSET
    ib_account: Union[Unset, str] = UNSET
    third_party_type: Union[Unset, str] = UNSET
    approximate_account_value: Union[Unset, int] = UNSET
    ssn: Union[Unset, str] = UNSET
    ein: Union[Unset, str] = UNSET
    signature: Union[Unset, str] = UNSET
    authorize_to_remove_fund: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        partial_stock_positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partial_stock_positions, Unset):
            partial_stock_positions = []
            for partial_stock_positions_item_data in self.partial_stock_positions:
                partial_stock_positions_item = partial_stock_positions_item_data.to_dict()
                partial_stock_positions.append(partial_stock_positions_item)

        partial_bond_positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partial_bond_positions, Unset):
            partial_bond_positions = []
            for partial_bond_positions_item_data in self.partial_bond_positions:
                partial_bond_positions_item = partial_bond_positions_item_data.to_dict()
                partial_bond_positions.append(partial_bond_positions_item)

        partial_option_positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partial_option_positions, Unset):
            partial_option_positions = []
            for partial_option_positions_item_data in self.partial_option_positions:
                partial_option_positions_item = partial_option_positions_item_data.to_dict()
                partial_option_positions.append(partial_option_positions_item)

        partial_warrant_positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partial_warrant_positions, Unset):
            partial_warrant_positions = []
            for partial_warrant_positions_item_data in self.partial_warrant_positions:
                partial_warrant_positions_item = partial_warrant_positions_item_data.to_dict()
                partial_warrant_positions.append(partial_warrant_positions_item)

        partial_fund_positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partial_fund_positions, Unset):
            partial_fund_positions = []
            for partial_fund_positions_item_data in self.partial_fund_positions:
                partial_fund_positions_item = partial_fund_positions_item_data.to_dict()
                partial_fund_positions.append(partial_fund_positions_item)

        partial_cash_positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partial_cash_positions, Unset):
            partial_cash_positions = []
            for partial_cash_positions_item_data in self.partial_cash_positions:
                partial_cash_positions_item = partial_cash_positions_item_data.to_dict()
                partial_cash_positions.append(partial_cash_positions_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        sub_type: Union[Unset, str] = UNSET
        if not isinstance(self.sub_type, Unset):
            sub_type = self.sub_type.value

        broker_id = self.broker_id

        broker_name = self.broker_name

        account_at_broker = self.account_at_broker

        src_ira_type: Union[Unset, str] = UNSET
        if not isinstance(self.src_ira_type, Unset):
            src_ira_type = self.src_ira_type.value

        margin_loan = self.margin_loan

        short_pos = self.short_pos

        option_pos = self.option_pos

        ib_account = self.ib_account

        third_party_type = self.third_party_type

        approximate_account_value = self.approximate_account_value

        ssn = self.ssn

        ein = self.ein

        signature = self.signature

        authorize_to_remove_fund = self.authorize_to_remove_fund

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partial_stock_positions is not UNSET:
            field_dict["partialStockPositions"] = partial_stock_positions
        if partial_bond_positions is not UNSET:
            field_dict["partialBondPositions"] = partial_bond_positions
        if partial_option_positions is not UNSET:
            field_dict["partialOptionPositions"] = partial_option_positions
        if partial_warrant_positions is not UNSET:
            field_dict["partialWarrantPositions"] = partial_warrant_positions
        if partial_fund_positions is not UNSET:
            field_dict["partialFundPositions"] = partial_fund_positions
        if partial_cash_positions is not UNSET:
            field_dict["partialCashPositions"] = partial_cash_positions
        if type is not UNSET:
            field_dict["type"] = type
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if broker_id is not UNSET:
            field_dict["brokerId"] = broker_id
        if broker_name is not UNSET:
            field_dict["brokerName"] = broker_name
        if account_at_broker is not UNSET:
            field_dict["accountAtBroker"] = account_at_broker
        if src_ira_type is not UNSET:
            field_dict["srcIRAType"] = src_ira_type
        if margin_loan is not UNSET:
            field_dict["marginLoan"] = margin_loan
        if short_pos is not UNSET:
            field_dict["shortPos"] = short_pos
        if option_pos is not UNSET:
            field_dict["optionPos"] = option_pos
        if ib_account is not UNSET:
            field_dict["ibAccount"] = ib_account
        if third_party_type is not UNSET:
            field_dict["thirdPartyType"] = third_party_type
        if approximate_account_value is not UNSET:
            field_dict["approximateAccountValue"] = approximate_account_value
        if ssn is not UNSET:
            field_dict["ssn"] = ssn
        if ein is not UNSET:
            field_dict["ein"] = ein
        if signature is not UNSET:
            field_dict["signature"] = signature
        if authorize_to_remove_fund is not UNSET:
            field_dict["authorizeToRemoveFund"] = authorize_to_remove_fund

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.partial_bond_position import PartialBondPosition
        from ..models.partial_cash_position import PartialCashPosition
        from ..models.partial_fund_position import PartialFundPosition
        from ..models.partial_option_position import PartialOptionPosition
        from ..models.partial_stock_position import PartialStockPosition
        from ..models.partial_warrant_position import PartialWarrantPosition

        d = src_dict.copy()
        partial_stock_positions = []
        _partial_stock_positions = d.pop("partialStockPositions", UNSET)
        for partial_stock_positions_item_data in _partial_stock_positions or []:
            partial_stock_positions_item = PartialStockPosition.from_dict(partial_stock_positions_item_data)

            partial_stock_positions.append(partial_stock_positions_item)

        partial_bond_positions = []
        _partial_bond_positions = d.pop("partialBondPositions", UNSET)
        for partial_bond_positions_item_data in _partial_bond_positions or []:
            partial_bond_positions_item = PartialBondPosition.from_dict(partial_bond_positions_item_data)

            partial_bond_positions.append(partial_bond_positions_item)

        partial_option_positions = []
        _partial_option_positions = d.pop("partialOptionPositions", UNSET)
        for partial_option_positions_item_data in _partial_option_positions or []:
            partial_option_positions_item = PartialOptionPosition.from_dict(partial_option_positions_item_data)

            partial_option_positions.append(partial_option_positions_item)

        partial_warrant_positions = []
        _partial_warrant_positions = d.pop("partialWarrantPositions", UNSET)
        for partial_warrant_positions_item_data in _partial_warrant_positions or []:
            partial_warrant_positions_item = PartialWarrantPosition.from_dict(partial_warrant_positions_item_data)

            partial_warrant_positions.append(partial_warrant_positions_item)

        partial_fund_positions = []
        _partial_fund_positions = d.pop("partialFundPositions", UNSET)
        for partial_fund_positions_item_data in _partial_fund_positions or []:
            partial_fund_positions_item = PartialFundPosition.from_dict(partial_fund_positions_item_data)

            partial_fund_positions.append(partial_fund_positions_item)

        partial_cash_positions = []
        _partial_cash_positions = d.pop("partialCashPositions", UNSET)
        for partial_cash_positions_item_data in _partial_cash_positions or []:
            partial_cash_positions_item = PartialCashPosition.from_dict(partial_cash_positions_item_data)

            partial_cash_positions.append(partial_cash_positions_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ExtPositionsTransferTypeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ExtPositionsTransferTypeType(_type)

        _sub_type = d.pop("subType", UNSET)
        sub_type: Union[Unset, ExtPositionsTransferTypeSubType]
        if isinstance(_sub_type, Unset):
            sub_type = UNSET
        else:
            sub_type = ExtPositionsTransferTypeSubType(_sub_type)

        broker_id = d.pop("brokerId", UNSET)

        broker_name = d.pop("brokerName", UNSET)

        account_at_broker = d.pop("accountAtBroker", UNSET)

        _src_ira_type = d.pop("srcIRAType", UNSET)
        src_ira_type: Union[Unset, ExtPositionsTransferTypeSrcIRAType]
        if isinstance(_src_ira_type, Unset):
            src_ira_type = UNSET
        else:
            src_ira_type = ExtPositionsTransferTypeSrcIRAType(_src_ira_type)

        margin_loan = d.pop("marginLoan", UNSET)

        short_pos = d.pop("shortPos", UNSET)

        option_pos = d.pop("optionPos", UNSET)

        ib_account = d.pop("ibAccount", UNSET)

        third_party_type = d.pop("thirdPartyType", UNSET)

        approximate_account_value = d.pop("approximateAccountValue", UNSET)

        ssn = d.pop("ssn", UNSET)

        ein = d.pop("ein", UNSET)

        signature = d.pop("signature", UNSET)

        authorize_to_remove_fund = d.pop("authorizeToRemoveFund", UNSET)

        ext_positions_transfer_type = cls(
            partial_stock_positions=partial_stock_positions,
            partial_bond_positions=partial_bond_positions,
            partial_option_positions=partial_option_positions,
            partial_warrant_positions=partial_warrant_positions,
            partial_fund_positions=partial_fund_positions,
            partial_cash_positions=partial_cash_positions,
            type=type,
            sub_type=sub_type,
            broker_id=broker_id,
            broker_name=broker_name,
            account_at_broker=account_at_broker,
            src_ira_type=src_ira_type,
            margin_loan=margin_loan,
            short_pos=short_pos,
            option_pos=option_pos,
            ib_account=ib_account,
            third_party_type=third_party_type,
            approximate_account_value=approximate_account_value,
            ssn=ssn,
            ein=ein,
            signature=signature,
            authorize_to_remove_fund=authorize_to_remove_fund,
        )

        ext_positions_transfer_type.additional_properties = d
        return ext_positions_transfer_type

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
