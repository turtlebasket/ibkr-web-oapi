from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trading_instrument_description_asset_type import TradingInstrumentDescriptionAssetType
from ..models.trading_instrument_description_security_id_type import TradingInstrumentDescriptionSecurityIdType

T = TypeVar("T", bound="TradingInstrumentDescription")


@_attrs_define
class TradingInstrumentDescription:
    """
    Attributes:
        security_id_type (TradingInstrumentDescriptionSecurityIdType):  Example: ISIN.
        security_id (str):  Example: 459200101.
        asset_type (TradingInstrumentDescriptionAssetType):  Example: STK.
    """

    security_id_type: TradingInstrumentDescriptionSecurityIdType
    security_id: str
    asset_type: TradingInstrumentDescriptionAssetType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        security_id_type = self.security_id_type.value

        security_id = self.security_id

        asset_type = self.asset_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "securityIdType": security_id_type,
                "securityId": security_id,
                "assetType": asset_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        security_id_type = TradingInstrumentDescriptionSecurityIdType(d.pop("securityIdType"))

        security_id = d.pop("securityId")

        asset_type = TradingInstrumentDescriptionAssetType(d.pop("assetType"))

        trading_instrument_description = cls(
            security_id_type=security_id_type,
            security_id=security_id,
            asset_type=asset_type,
        )

        trading_instrument_description.additional_properties = d
        return trading_instrument_description

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
