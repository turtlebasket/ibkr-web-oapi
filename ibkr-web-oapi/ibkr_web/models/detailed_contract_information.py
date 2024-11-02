from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detailed_contract_information_additional_property import DetailedContractInformationAdditionalProperty


T = TypeVar("T", bound="DetailedContractInformation")


@_attrs_define
class DetailedContractInformation:
    """
    Attributes:
        currency_type (Union[Unset, str]): Confirms if the currency type. If trading exclusively in your base currency,
            “base” will be returned.
        rc (Union[Unset, int]): Returns the data identifier (Internal Use Only).
        view (Union[Unset, List[str]]): Returns the accountIds being viewed and returned.
        nd (Union[Unset, int]): Returns the total data points.
        id (Union[Unset, str]): Returns the request identifier, getPerformanceAllPeriods.
        included (Union[Unset, List[str]]): Returns an array containing accounts reviewed.
        pm (Union[Unset, str]): Portfolio Measure. Used to indicate TWR or MWR values returned.
    """

    currency_type: Union[Unset, str] = UNSET
    rc: Union[Unset, int] = UNSET
    view: Union[Unset, List[str]] = UNSET
    nd: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    included: Union[Unset, List[str]] = UNSET
    pm: Union[Unset, str] = UNSET
    additional_properties: Dict[str, "DetailedContractInformationAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        currency_type = self.currency_type

        rc = self.rc

        view: Union[Unset, List[str]] = UNSET
        if not isinstance(self.view, Unset):
            view = self.view

        nd = self.nd

        id = self.id

        included: Union[Unset, List[str]] = UNSET
        if not isinstance(self.included, Unset):
            included = self.included

        pm = self.pm

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()
        field_dict.update({})
        if currency_type is not UNSET:
            field_dict["currencyType"] = currency_type
        if rc is not UNSET:
            field_dict["rc"] = rc
        if view is not UNSET:
            field_dict["view"] = view
        if nd is not UNSET:
            field_dict["nd"] = nd
        if id is not UNSET:
            field_dict["id"] = id
        if included is not UNSET:
            field_dict["included"] = included
        if pm is not UNSET:
            field_dict["pm"] = pm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.detailed_contract_information_additional_property import (
            DetailedContractInformationAdditionalProperty,
        )

        d = src_dict.copy()
        currency_type = d.pop("currencyType", UNSET)

        rc = d.pop("rc", UNSET)

        view = cast(List[str], d.pop("view", UNSET))

        nd = d.pop("nd", UNSET)

        id = d.pop("id", UNSET)

        included = cast(List[str], d.pop("included", UNSET))

        pm = d.pop("pm", UNSET)

        detailed_contract_information = cls(
            currency_type=currency_type,
            rc=rc,
            view=view,
            nd=nd,
            id=id,
            included=included,
            pm=pm,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DetailedContractInformationAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        detailed_contract_information.additional_properties = additional_properties
        return detailed_contract_information

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DetailedContractInformationAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DetailedContractInformationAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
