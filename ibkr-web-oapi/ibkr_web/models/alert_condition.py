from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertCondition")


@_attrs_define
class AlertCondition:
    """
    Attributes:
        condition_type (Union[Unset, int]): The type of condition set.
        conidex (Union[Unset, str]): Returns conid and exchange in the format “conid@exchange”
        contract_description_1 (Union[Unset, str]): Includes relevant descriptions (if applicable).
        condition_operator (Union[Unset, str]): Condition operator set for alert.
        condition_trigger_method (Union[Unset, int]): TriggerMethod value set.
        condition_value (Union[Unset, str]): Condition value set.
        condition_logic_bind (Union[Unset, bool]): Condition logic_bind value set.
        condition_time_zone (Union[Unset, str]): Condition timeZone value set.
    """

    condition_type: Union[Unset, int] = UNSET
    conidex: Union[Unset, str] = UNSET
    contract_description_1: Union[Unset, str] = UNSET
    condition_operator: Union[Unset, str] = UNSET
    condition_trigger_method: Union[Unset, int] = UNSET
    condition_value: Union[Unset, str] = UNSET
    condition_logic_bind: Union[Unset, bool] = UNSET
    condition_time_zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_type = self.condition_type

        conidex = self.conidex

        contract_description_1 = self.contract_description_1

        condition_operator = self.condition_operator

        condition_trigger_method = self.condition_trigger_method

        condition_value = self.condition_value

        condition_logic_bind = self.condition_logic_bind

        condition_time_zone = self.condition_time_zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if conidex is not UNSET:
            field_dict["conidex"] = conidex
        if contract_description_1 is not UNSET:
            field_dict["contract_description_1"] = contract_description_1
        if condition_operator is not UNSET:
            field_dict["condition_operator"] = condition_operator
        if condition_trigger_method is not UNSET:
            field_dict["condition_trigger_method"] = condition_trigger_method
        if condition_value is not UNSET:
            field_dict["condition_value"] = condition_value
        if condition_logic_bind is not UNSET:
            field_dict["condition_logic_bind"] = condition_logic_bind
        if condition_time_zone is not UNSET:
            field_dict["condition_time_zone"] = condition_time_zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        condition_type = d.pop("condition_type", UNSET)

        conidex = d.pop("conidex", UNSET)

        contract_description_1 = d.pop("contract_description_1", UNSET)

        condition_operator = d.pop("condition_operator", UNSET)

        condition_trigger_method = d.pop("condition_trigger_method", UNSET)

        condition_value = d.pop("condition_value", UNSET)

        condition_logic_bind = d.pop("condition_logic_bind", UNSET)

        condition_time_zone = d.pop("condition_time_zone", UNSET)

        alert_condition = cls(
            condition_type=condition_type,
            conidex=conidex,
            contract_description_1=contract_description_1,
            condition_operator=condition_operator,
            condition_trigger_method=condition_trigger_method,
            condition_value=condition_value,
            condition_logic_bind=condition_logic_bind,
            condition_time_zone=condition_time_zone,
        )

        alert_condition.additional_properties = d
        return alert_condition

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
