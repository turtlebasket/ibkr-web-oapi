from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_preview_amount import OrderPreviewAmount
    from ..models.order_preview_equity import OrderPreviewEquity
    from ..models.order_preview_initial import OrderPreviewInitial
    from ..models.order_preview_maintenance import OrderPreviewMaintenance
    from ..models.order_preview_position import OrderPreviewPosition


T = TypeVar("T", bound="OrderPreview")


@_attrs_define
class OrderPreview:
    """Projected costs and changes to margin and equity values in the account, if the order ticket were executed in full.

    Attributes:
        amount (Union[Unset, OrderPreviewAmount]): Describes the projected costs associated with the order ticket.
        equity (Union[Unset, OrderPreviewEquity]): Describes the projected change to the account's equity.
        initial (Union[Unset, OrderPreviewInitial]): Describes the projected change to initial margin.
        maintenance (Union[Unset, OrderPreviewMaintenance]): Describes the projected change to maintenance margin.
        position (Union[Unset, OrderPreviewPosition]): Describes the projected change to the account's position in the
            instrument.
        warn (Union[Unset, str]): Human-readable text of warning message, if applicable. Otherwise null.
        error (Union[Unset, str]): Human-readable text of an error message, if applicable. Otherwise null.
    """

    amount: Union[Unset, "OrderPreviewAmount"] = UNSET
    equity: Union[Unset, "OrderPreviewEquity"] = UNSET
    initial: Union[Unset, "OrderPreviewInitial"] = UNSET
    maintenance: Union[Unset, "OrderPreviewMaintenance"] = UNSET
    position: Union[Unset, "OrderPreviewPosition"] = UNSET
    warn: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        equity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equity, Unset):
            equity = self.equity.to_dict()

        initial: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initial, Unset):
            initial = self.initial.to_dict()

        maintenance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        warn = self.warn

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if equity is not UNSET:
            field_dict["equity"] = equity
        if initial is not UNSET:
            field_dict["initial"] = initial
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance
        if position is not UNSET:
            field_dict["position"] = position
        if warn is not UNSET:
            field_dict["warn"] = warn
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_preview_amount import OrderPreviewAmount
        from ..models.order_preview_equity import OrderPreviewEquity
        from ..models.order_preview_initial import OrderPreviewInitial
        from ..models.order_preview_maintenance import OrderPreviewMaintenance
        from ..models.order_preview_position import OrderPreviewPosition

        d = src_dict.copy()
        _amount = d.pop("amount", UNSET)
        amount: Union[Unset, OrderPreviewAmount]
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = OrderPreviewAmount.from_dict(_amount)

        _equity = d.pop("equity", UNSET)
        equity: Union[Unset, OrderPreviewEquity]
        if isinstance(_equity, Unset):
            equity = UNSET
        else:
            equity = OrderPreviewEquity.from_dict(_equity)

        _initial = d.pop("initial", UNSET)
        initial: Union[Unset, OrderPreviewInitial]
        if isinstance(_initial, Unset):
            initial = UNSET
        else:
            initial = OrderPreviewInitial.from_dict(_initial)

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: Union[Unset, OrderPreviewMaintenance]
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = OrderPreviewMaintenance.from_dict(_maintenance)

        _position = d.pop("position", UNSET)
        position: Union[Unset, OrderPreviewPosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = OrderPreviewPosition.from_dict(_position)

        warn = d.pop("warn", UNSET)

        error = d.pop("error", UNSET)

        order_preview = cls(
            amount=amount,
            equity=equity,
            initial=initial,
            maintenance=maintenance,
            position=position,
            warn=warn,
            error=error,
        )

        order_preview.additional_properties = d
        return order_preview

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
