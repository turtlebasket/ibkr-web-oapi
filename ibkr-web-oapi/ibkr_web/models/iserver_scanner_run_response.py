from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iserver_scanner_run_response_contracts_item import IserverScannerRunResponseContractsItem


T = TypeVar("T", bound="IserverScannerRunResponse")


@_attrs_define
class IserverScannerRunResponse:
    """
    Attributes:
        contracts (Union[Unset, List['IserverScannerRunResponseContractsItem']]): Contains contracts related to the
            market scanner request.
        scan_data_column_name (Union[Unset, str]): Internal Use Only
    """

    contracts: Union[Unset, List["IserverScannerRunResponseContractsItem"]] = UNSET
    scan_data_column_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contracts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contracts, Unset):
            contracts = []
            for contracts_item_data in self.contracts:
                contracts_item = contracts_item_data.to_dict()
                contracts.append(contracts_item)

        scan_data_column_name = self.scan_data_column_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if scan_data_column_name is not UNSET:
            field_dict["scan_data_column_name"] = scan_data_column_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.iserver_scanner_run_response_contracts_item import IserverScannerRunResponseContractsItem

        d = src_dict.copy()
        contracts = []
        _contracts = d.pop("contracts", UNSET)
        for contracts_item_data in _contracts or []:
            contracts_item = IserverScannerRunResponseContractsItem.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        scan_data_column_name = d.pop("scan_data_column_name", UNSET)

        iserver_scanner_run_response = cls(
            contracts=contracts,
            scan_data_column_name=scan_data_column_name,
        )

        iserver_scanner_run_response.additional_properties = d
        return iserver_scanner_run_response

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
