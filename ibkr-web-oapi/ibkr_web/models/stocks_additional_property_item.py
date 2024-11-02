from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stocks_additional_property_item_contracts_item import StocksAdditionalPropertyItemContractsItem


T = TypeVar("T", bound="StocksAdditionalPropertyItem")


@_attrs_define
class StocksAdditionalPropertyItem:
    """Contains a series of objects for each symbol that matches the requested

    Attributes:
        name (Union[Unset, str]): Full company name for the given contract.
        chinese_name (Union[Unset, str]): Chinese name for the given company as unicode.
        asset_class (Union[Unset, str]): Asset class for the given company.
        contracts (Union[Unset, List['StocksAdditionalPropertyItemContractsItem']]): A series of arrays pertaining to
            the same company listed by “name”. Typically differentiated based on currency of the primary exchange.
    """

    name: Union[Unset, str] = UNSET
    chinese_name: Union[Unset, str] = UNSET
    asset_class: Union[Unset, str] = UNSET
    contracts: Union[Unset, List["StocksAdditionalPropertyItemContractsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        chinese_name = self.chinese_name

        asset_class = self.asset_class

        contracts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contracts, Unset):
            contracts = []
            for contracts_item_data in self.contracts:
                contracts_item = contracts_item_data.to_dict()
                contracts.append(contracts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if chinese_name is not UNSET:
            field_dict["chineseName"] = chinese_name
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if contracts is not UNSET:
            field_dict["contracts"] = contracts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stocks_additional_property_item_contracts_item import StocksAdditionalPropertyItemContractsItem

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        chinese_name = d.pop("chineseName", UNSET)

        asset_class = d.pop("assetClass", UNSET)

        contracts = []
        _contracts = d.pop("contracts", UNSET)
        for contracts_item_data in _contracts or []:
            contracts_item = StocksAdditionalPropertyItemContractsItem.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        stocks_additional_property_item = cls(
            name=name,
            chinese_name=chinese_name,
            asset_class=asset_class,
            contracts=contracts,
        )

        stocks_additional_property_item.additional_properties = d
        return stocks_additional_property_item

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
