from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableFundsResponseTotal")


@_attrs_define
class AvailableFundsResponseTotal:
    """total values

    Attributes:
        current_available (Union[Unset, str]): Describes currently avialable funds in your account for trading.
        current_excess (Union[Unset, str]): Describes total value of the account.
        prdctd_pst_xpry_excss (Union[Unset, str]): Displays predicted post-expiration account value.
        lk_ahd_avlbl_fnds (Union[Unset, str]): This value reflects your available funds at the next margin change.
        lk_ahd_excss_lqdty (Union[Unset, str]): * `Securities` - Equity with loan value. Look ahead maintenance margin.
             * `Commodities` - Net Liquidation value. Look ahead maintenance margin.
        overnight_available (Union[Unset, str]): Describes available funds for overnight trading.
        overnight_excess (Union[Unset, str]): Overnight refers to the window of time after the local market trading day
            is closed.
              * `Securities` - Equivalent to regular trading hours.
               * `Commodities` - Commodities Net Liquidation value. Overnight Maintenance margin.
        buying_power (Union[Unset, str]): Describes the total buying power of the account including existing balance
            with margin.
        leverage (Union[Unset, str]): Describes the total combined leverage.
        lk_ahd_nxt_chng (Union[Unset, str]): Describes when the next 'Look Ahead' calculation will take place.
        day_trades_left (Union[Unset, str]): Describes the number of trades remaining before flagging the Pattern Day
            Trader status. "Unlimited" is used for existing Pattern Day Traders.
    """

    current_available: Union[Unset, str] = UNSET
    current_excess: Union[Unset, str] = UNSET
    prdctd_pst_xpry_excss: Union[Unset, str] = UNSET
    lk_ahd_avlbl_fnds: Union[Unset, str] = UNSET
    lk_ahd_excss_lqdty: Union[Unset, str] = UNSET
    overnight_available: Union[Unset, str] = UNSET
    overnight_excess: Union[Unset, str] = UNSET
    buying_power: Union[Unset, str] = UNSET
    leverage: Union[Unset, str] = UNSET
    lk_ahd_nxt_chng: Union[Unset, str] = UNSET
    day_trades_left: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_available = self.current_available

        current_excess = self.current_excess

        prdctd_pst_xpry_excss = self.prdctd_pst_xpry_excss

        lk_ahd_avlbl_fnds = self.lk_ahd_avlbl_fnds

        lk_ahd_excss_lqdty = self.lk_ahd_excss_lqdty

        overnight_available = self.overnight_available

        overnight_excess = self.overnight_excess

        buying_power = self.buying_power

        leverage = self.leverage

        lk_ahd_nxt_chng = self.lk_ahd_nxt_chng

        day_trades_left = self.day_trades_left

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_available is not UNSET:
            field_dict["current_available"] = current_available
        if current_excess is not UNSET:
            field_dict["current_excess"] = current_excess
        if prdctd_pst_xpry_excss is not UNSET:
            field_dict["Prdctd Pst-xpry Excss"] = prdctd_pst_xpry_excss
        if lk_ahd_avlbl_fnds is not UNSET:
            field_dict["Lk Ahd Avlbl Fnds"] = lk_ahd_avlbl_fnds
        if lk_ahd_excss_lqdty is not UNSET:
            field_dict["Lk Ahd Excss Lqdty"] = lk_ahd_excss_lqdty
        if overnight_available is not UNSET:
            field_dict["overnight_available"] = overnight_available
        if overnight_excess is not UNSET:
            field_dict["overnight_excess"] = overnight_excess
        if buying_power is not UNSET:
            field_dict["buying_power"] = buying_power
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if lk_ahd_nxt_chng is not UNSET:
            field_dict["Lk Ahd Nxt Chng"] = lk_ahd_nxt_chng
        if day_trades_left is not UNSET:
            field_dict["day_trades_left"] = day_trades_left

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_available = d.pop("current_available", UNSET)

        current_excess = d.pop("current_excess", UNSET)

        prdctd_pst_xpry_excss = d.pop("Prdctd Pst-xpry Excss", UNSET)

        lk_ahd_avlbl_fnds = d.pop("Lk Ahd Avlbl Fnds", UNSET)

        lk_ahd_excss_lqdty = d.pop("Lk Ahd Excss Lqdty", UNSET)

        overnight_available = d.pop("overnight_available", UNSET)

        overnight_excess = d.pop("overnight_excess", UNSET)

        buying_power = d.pop("buying_power", UNSET)

        leverage = d.pop("leverage", UNSET)

        lk_ahd_nxt_chng = d.pop("Lk Ahd Nxt Chng", UNSET)

        day_trades_left = d.pop("day_trades_left", UNSET)

        available_funds_response_total = cls(
            current_available=current_available,
            current_excess=current_excess,
            prdctd_pst_xpry_excss=prdctd_pst_xpry_excss,
            lk_ahd_avlbl_fnds=lk_ahd_avlbl_fnds,
            lk_ahd_excss_lqdty=lk_ahd_excss_lqdty,
            overnight_available=overnight_available,
            overnight_excess=overnight_excess,
            buying_power=buying_power,
            leverage=leverage,
            lk_ahd_nxt_chng=lk_ahd_nxt_chng,
            day_trades_left=day_trades_left,
        )

        available_funds_response_total.additional_properties = d
        return available_funds_response_total

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
