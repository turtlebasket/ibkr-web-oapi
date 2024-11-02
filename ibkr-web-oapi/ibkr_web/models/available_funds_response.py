from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_funds_response_securities import AvailableFundsResponseSecurities
    from ..models.available_funds_response_total import AvailableFundsResponseTotal
    from ..models.funds import Funds


T = TypeVar("T", bound="AvailableFundsResponse")


@_attrs_define
class AvailableFundsResponse:
    """Contains a combined overview of Commidity, Security and Crypto fund values.

    Attributes:
        total (Union[Unset, AvailableFundsResponseTotal]): total values
        crypto_at_paxos (Union[Unset, Funds]): Contains commodities specific fund values.
        commodities (Union[Unset, Funds]): Contains commodities specific fund values.
        securities (Union[Unset, AvailableFundsResponseSecurities]): Contains an overview of Security specific fund
            values.
    """

    total: Union[Unset, "AvailableFundsResponseTotal"] = UNSET
    crypto_at_paxos: Union[Unset, "Funds"] = UNSET
    commodities: Union[Unset, "Funds"] = UNSET
    securities: Union[Unset, "AvailableFundsResponseSecurities"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        crypto_at_paxos: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crypto_at_paxos, Unset):
            crypto_at_paxos = self.crypto_at_paxos.to_dict()

        commodities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commodities, Unset):
            commodities = self.commodities.to_dict()

        securities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.securities, Unset):
            securities = self.securities.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if crypto_at_paxos is not UNSET:
            field_dict["Crypto at Paxos"] = crypto_at_paxos
        if commodities is not UNSET:
            field_dict["commodities"] = commodities
        if securities is not UNSET:
            field_dict["securities"] = securities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.available_funds_response_securities import AvailableFundsResponseSecurities
        from ..models.available_funds_response_total import AvailableFundsResponseTotal
        from ..models.funds import Funds

        d = src_dict.copy()
        _total = d.pop("total", UNSET)
        total: Union[Unset, AvailableFundsResponseTotal]
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = AvailableFundsResponseTotal.from_dict(_total)

        _crypto_at_paxos = d.pop("Crypto at Paxos", UNSET)
        crypto_at_paxos: Union[Unset, Funds]
        if isinstance(_crypto_at_paxos, Unset):
            crypto_at_paxos = UNSET
        else:
            crypto_at_paxos = Funds.from_dict(_crypto_at_paxos)

        _commodities = d.pop("commodities", UNSET)
        commodities: Union[Unset, Funds]
        if isinstance(_commodities, Unset):
            commodities = UNSET
        else:
            commodities = Funds.from_dict(_commodities)

        _securities = d.pop("securities", UNSET)
        securities: Union[Unset, AvailableFundsResponseSecurities]
        if isinstance(_securities, Unset):
            securities = UNSET
        else:
            securities = AvailableFundsResponseSecurities.from_dict(_securities)

        available_funds_response = cls(
            total=total,
            crypto_at_paxos=crypto_at_paxos,
            commodities=commodities,
            securities=securities,
        )

        available_funds_response.additional_properties = d
        return available_funds_response

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
