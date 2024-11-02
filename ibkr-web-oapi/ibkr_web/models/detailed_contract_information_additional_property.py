from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detailed_contract_information_additional_property_additional_property import (
        DetailedContractInformationAdditionalPropertyAdditionalProperty,
    )


T = TypeVar("T", bound="DetailedContractInformationAdditionalProperty")


@_attrs_define
class DetailedContractInformationAdditionalProperty:
    """Contains the relevant performance data for the specified accountId.

    Attributes:
        last_successful_update (Union[Unset, str]): Returns the datetime in EST of the last successful call to the /pa
            endpoint.
        start (Union[Unset, str]): Returns the start date of the request range.
        periods (Union[Unset, List[str]]): Returns the valid period values returned by the /pa/allperiods endpoint.
        end (Union[Unset, str]): Returns the end date of the request range.
        base_currency (Union[Unset, str]): Clarifies the base currency of the primary accountId.
    """

    last_successful_update: Union[Unset, str] = UNSET
    start: Union[Unset, str] = UNSET
    periods: Union[Unset, List[str]] = UNSET
    end: Union[Unset, str] = UNSET
    base_currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, "DetailedContractInformationAdditionalPropertyAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        last_successful_update = self.last_successful_update

        start = self.start

        periods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = self.periods

        end = self.end

        base_currency = self.base_currency

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()
        field_dict.update({})
        if last_successful_update is not UNSET:
            field_dict["lastSuccessfulUpdate"] = last_successful_update
        if start is not UNSET:
            field_dict["start"] = start
        if periods is not UNSET:
            field_dict["periods"] = periods
        if end is not UNSET:
            field_dict["end"] = end
        if base_currency is not UNSET:
            field_dict["baseCurrency"] = base_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.detailed_contract_information_additional_property_additional_property import (
            DetailedContractInformationAdditionalPropertyAdditionalProperty,
        )

        d = src_dict.copy()
        last_successful_update = d.pop("lastSuccessfulUpdate", UNSET)

        start = d.pop("start", UNSET)

        periods = cast(List[str], d.pop("periods", UNSET))

        end = d.pop("end", UNSET)

        base_currency = d.pop("baseCurrency", UNSET)

        detailed_contract_information_additional_property = cls(
            last_successful_update=last_successful_update,
            start=start,
            periods=periods,
            end=end,
            base_currency=base_currency,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DetailedContractInformationAdditionalPropertyAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        detailed_contract_information_additional_property.additional_properties = additional_properties
        return detailed_contract_information_additional_property

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DetailedContractInformationAdditionalPropertyAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DetailedContractInformationAdditionalPropertyAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
