from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detailed_contract_information_additional_property_additional_property_start_nav import (
        DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav,
    )


T = TypeVar("T", bound="DetailedContractInformationAdditionalPropertyAdditionalProperty")


@_attrs_define
class DetailedContractInformationAdditionalPropertyAdditionalProperty:
    """Returns the performance data for the given period value.

    Attributes:
        nav (Union[Unset, List[float]]): Net asset value data for the account or consolidated accounts. NAV data is not
            applicable to benchmarks.
        cps (Union[Unset, List[float]]): Returns the object containing the Cumulative performance data. Correlates to
            the same index position of data reutnred by the "nav" field.
        freq (Union[Unset, str]): Returns the determining frequency of the data range.
        dates (Union[Unset, List[str]]): Returns the dates corresponding to the frequency of data.
        start_nav (Union[Unset, DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav]): Returns the
            starting data for the current NAV details.
    """

    nav: Union[Unset, List[float]] = UNSET
    cps: Union[Unset, List[float]] = UNSET
    freq: Union[Unset, str] = UNSET
    dates: Union[Unset, List[str]] = UNSET
    start_nav: Union[Unset, "DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nav: Union[Unset, List[float]] = UNSET
        if not isinstance(self.nav, Unset):
            nav = self.nav

        cps: Union[Unset, List[float]] = UNSET
        if not isinstance(self.cps, Unset):
            cps = self.cps

        freq = self.freq

        dates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates

        start_nav: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_nav, Unset):
            start_nav = self.start_nav.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nav is not UNSET:
            field_dict["nav"] = nav
        if cps is not UNSET:
            field_dict["cps"] = cps
        if freq is not UNSET:
            field_dict["freq"] = freq
        if dates is not UNSET:
            field_dict["dates"] = dates
        if start_nav is not UNSET:
            field_dict["startNav"] = start_nav

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.detailed_contract_information_additional_property_additional_property_start_nav import (
            DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav,
        )

        d = src_dict.copy()
        nav = cast(List[float], d.pop("nav", UNSET))

        cps = cast(List[float], d.pop("cps", UNSET))

        freq = d.pop("freq", UNSET)

        dates = cast(List[str], d.pop("dates", UNSET))

        _start_nav = d.pop("startNav", UNSET)
        start_nav: Union[Unset, DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav]
        if isinstance(_start_nav, Unset):
            start_nav = UNSET
        else:
            start_nav = DetailedContractInformationAdditionalPropertyAdditionalPropertyStartNav.from_dict(_start_nav)

        detailed_contract_information_additional_property_additional_property = cls(
            nav=nav,
            cps=cps,
            freq=freq,
            dates=dates,
            start_nav=start_nav,
        )

        detailed_contract_information_additional_property_additional_property.additional_properties = d
        return detailed_contract_information_additional_property_additional_property

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
