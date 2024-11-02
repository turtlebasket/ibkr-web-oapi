from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Funds")


@_attrs_define
class Funds:
    """Contains commodities specific fund values.

    Attributes:
        current_available (Union[Unset, str]): Describes currently avialable funds in your account for trading.
        current_excess (Union[Unset, str]): Describes total value of the account.
        prdctd_pst_xpry_excss (Union[Unset, str]): Displays predicted post-expiration account value.
        lk_ahd_avlbl_fnds (Union[Unset, str]): This value reflects your available funds at the next margin change.
        overnight_available (Union[Unset, str]): Describes available funds for overnight trading.
        overnight_excess (Union[Unset, str]): Overnight refers to the window of time after the local market trading day
            is closed.
              * `Securities` - Equivalent to regular trading hours.
               * `Commodities` - Commodities Net Liquidation value. Overnight Maintenance margin.
    """

    current_available: Union[Unset, str] = UNSET
    current_excess: Union[Unset, str] = UNSET
    prdctd_pst_xpry_excss: Union[Unset, str] = UNSET
    lk_ahd_avlbl_fnds: Union[Unset, str] = UNSET
    overnight_available: Union[Unset, str] = UNSET
    overnight_excess: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_available = self.current_available

        current_excess = self.current_excess

        prdctd_pst_xpry_excss = self.prdctd_pst_xpry_excss

        lk_ahd_avlbl_fnds = self.lk_ahd_avlbl_fnds

        overnight_available = self.overnight_available

        overnight_excess = self.overnight_excess

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
        if overnight_available is not UNSET:
            field_dict["overnight_available"] = overnight_available
        if overnight_excess is not UNSET:
            field_dict["overnight_excess"] = overnight_excess

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_available = d.pop("current_available", UNSET)

        current_excess = d.pop("current_excess", UNSET)

        prdctd_pst_xpry_excss = d.pop("Prdctd Pst-xpry Excss", UNSET)

        lk_ahd_avlbl_fnds = d.pop("Lk Ahd Avlbl Fnds", UNSET)

        overnight_available = d.pop("overnight_available", UNSET)

        overnight_excess = d.pop("overnight_excess", UNSET)

        funds = cls(
            current_available=current_available,
            current_excess=current_excess,
            prdctd_pst_xpry_excss=prdctd_pst_xpry_excss,
            lk_ahd_avlbl_fnds=lk_ahd_avlbl_fnds,
            overnight_available=overnight_available,
            overnight_excess=overnight_excess,
        )

        funds.additional_properties = d
        return funds

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
