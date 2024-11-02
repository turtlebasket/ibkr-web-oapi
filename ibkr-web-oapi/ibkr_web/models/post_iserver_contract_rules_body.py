from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostIserverContractRulesBody")


@_attrs_define
class PostIserverContractRulesBody:
    """
    Attributes:
        conid (Union[Unset, int]): Contract identifier for the interested contract.
        is_buy (Union[Unset, bool]): Side of the market rules apply too. Set to true for Buy Orders, set to false for
            Sell orders. Default: True.
        modify_order (Union[Unset, bool]): Used to find trading rules related to an existing order. Default: False.
        order_id (Union[Unset, int]): Specify the order identifier used for tracking a given order.
    """

    conid: Union[Unset, int] = UNSET
    is_buy: Union[Unset, bool] = True
    modify_order: Union[Unset, bool] = False
    order_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conid = self.conid

        is_buy = self.is_buy

        modify_order = self.modify_order

        order_id = self.order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conid is not UNSET:
            field_dict["conid"] = conid
        if is_buy is not UNSET:
            field_dict["isBuy"] = is_buy
        if modify_order is not UNSET:
            field_dict["modifyOrder"] = modify_order
        if order_id is not UNSET:
            field_dict["orderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conid = d.pop("conid", UNSET)

        is_buy = d.pop("isBuy", UNSET)

        modify_order = d.pop("modifyOrder", UNSET)

        order_id = d.pop("orderId", UNSET)

        post_iserver_contract_rules_body = cls(
            conid=conid,
            is_buy=is_buy,
            modify_order=modify_order,
            order_id=order_id,
        )

        post_iserver_contract_rules_body.additional_properties = d
        return post_iserver_contract_rules_body

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
