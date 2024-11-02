from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.commission_markup_type_type import CommissionMarkupTypeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.markup_staircase_type import MarkupStaircaseType


T = TypeVar("T", bound="CommissionMarkupType")


@_attrs_define
class CommissionMarkupType:
    """
    Attributes:
        stairs (Union[Unset, List['MarkupStaircaseType']]):
        code (Union[Unset, str]):
        minimum (Union[Unset, float]):
        maximum (Union[Unset, float]):
        type (Union[Unset, CommissionMarkupTypeType]):
        amount (Union[Unset, float]):
        plus_cost (Union[Unset, bool]):
        ticket_charge (Union[Unset, float]):
    """

    stairs: Union[Unset, List["MarkupStaircaseType"]] = UNSET
    code: Union[Unset, str] = UNSET
    minimum: Union[Unset, float] = UNSET
    maximum: Union[Unset, float] = UNSET
    type: Union[Unset, CommissionMarkupTypeType] = UNSET
    amount: Union[Unset, float] = UNSET
    plus_cost: Union[Unset, bool] = UNSET
    ticket_charge: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stairs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stairs, Unset):
            stairs = []
            for stairs_item_data in self.stairs:
                stairs_item = stairs_item_data.to_dict()
                stairs.append(stairs_item)

        code = self.code

        minimum = self.minimum

        maximum = self.maximum

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        amount = self.amount

        plus_cost = self.plus_cost

        ticket_charge = self.ticket_charge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stairs is not UNSET:
            field_dict["stairs"] = stairs
        if code is not UNSET:
            field_dict["code"] = code
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if type is not UNSET:
            field_dict["type"] = type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if plus_cost is not UNSET:
            field_dict["plusCost"] = plus_cost
        if ticket_charge is not UNSET:
            field_dict["ticketCharge"] = ticket_charge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.markup_staircase_type import MarkupStaircaseType

        d = src_dict.copy()
        stairs = []
        _stairs = d.pop("stairs", UNSET)
        for stairs_item_data in _stairs or []:
            stairs_item = MarkupStaircaseType.from_dict(stairs_item_data)

            stairs.append(stairs_item)

        code = d.pop("code", UNSET)

        minimum = d.pop("minimum", UNSET)

        maximum = d.pop("maximum", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CommissionMarkupTypeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CommissionMarkupTypeType(_type)

        amount = d.pop("amount", UNSET)

        plus_cost = d.pop("plusCost", UNSET)

        ticket_charge = d.pop("ticketCharge", UNSET)

        commission_markup_type = cls(
            stairs=stairs,
            code=code,
            minimum=minimum,
            maximum=maximum,
            type=type,
            amount=amount,
            plus_cost=plus_cost,
            ticket_charge=ticket_charge,
        )

        commission_markup_type.additional_properties = d
        return commission_markup_type

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
