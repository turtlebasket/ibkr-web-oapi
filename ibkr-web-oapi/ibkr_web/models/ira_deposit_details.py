from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ira_deposit_details_deposit_type import IRADepositDetailsDepositType
from ..models.ira_deposit_details_from_ira_type import IRADepositDetailsFromIraType
from ..models.ira_deposit_details_tax_year import IRADepositDetailsTaxYear
from ..types import UNSET, Unset

T = TypeVar("T", bound="IRADepositDetails")


@_attrs_define
class IRADepositDetails:
    """
    Attributes:
        deposit_type (Union[Unset, IRADepositDetailsDepositType]):
        tax_year (Union[Unset, IRADepositDetailsTaxYear]):
        from_ira_type (Union[Unset, IRADepositDetailsFromIraType]):
    """

    deposit_type: Union[Unset, IRADepositDetailsDepositType] = UNSET
    tax_year: Union[Unset, IRADepositDetailsTaxYear] = UNSET
    from_ira_type: Union[Unset, IRADepositDetailsFromIraType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deposit_type: Union[Unset, str] = UNSET
        if not isinstance(self.deposit_type, Unset):
            deposit_type = self.deposit_type.value

        tax_year: Union[Unset, str] = UNSET
        if not isinstance(self.tax_year, Unset):
            tax_year = self.tax_year.value

        from_ira_type: Union[Unset, str] = UNSET
        if not isinstance(self.from_ira_type, Unset):
            from_ira_type = self.from_ira_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deposit_type is not UNSET:
            field_dict["depositType"] = deposit_type
        if tax_year is not UNSET:
            field_dict["taxYear"] = tax_year
        if from_ira_type is not UNSET:
            field_dict["fromIraType"] = from_ira_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _deposit_type = d.pop("depositType", UNSET)
        deposit_type: Union[Unset, IRADepositDetailsDepositType]
        if isinstance(_deposit_type, Unset):
            deposit_type = UNSET
        else:
            deposit_type = IRADepositDetailsDepositType(_deposit_type)

        _tax_year = d.pop("taxYear", UNSET)
        tax_year: Union[Unset, IRADepositDetailsTaxYear]
        if isinstance(_tax_year, Unset):
            tax_year = UNSET
        else:
            tax_year = IRADepositDetailsTaxYear(_tax_year)

        _from_ira_type = d.pop("fromIraType", UNSET)
        from_ira_type: Union[Unset, IRADepositDetailsFromIraType]
        if isinstance(_from_ira_type, Unset):
            from_ira_type = UNSET
        else:
            from_ira_type = IRADepositDetailsFromIraType(_from_ira_type)

        ira_deposit_details = cls(
            deposit_type=deposit_type,
            tax_year=tax_year,
            from_ira_type=from_ira_type,
        )

        ira_deposit_details.additional_properties = d
        return ira_deposit_details

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
