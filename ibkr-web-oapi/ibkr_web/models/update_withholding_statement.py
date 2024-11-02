import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_withholding_statement_fatca_compliant_type import UpdateWithholdingStatementFatcaCompliantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWithholdingStatement")


@_attrs_define
class UpdateWithholdingStatement:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        fatca_compliant_type (Union[Unset, UpdateWithholdingStatementFatcaCompliantType]):
        us_income_tax (Union[Unset, bool]):
        treaty_country (Union[Unset, str]):
        cert_w8_imy (Union[Unset, bool]):
        effective_date (Union[Unset, datetime.date]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    fatca_compliant_type: Union[Unset, UpdateWithholdingStatementFatcaCompliantType] = UNSET
    us_income_tax: Union[Unset, bool] = UNSET
    treaty_country: Union[Unset, str] = UNSET
    cert_w8_imy: Union[Unset, bool] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        fatca_compliant_type: Union[Unset, str] = UNSET
        if not isinstance(self.fatca_compliant_type, Unset):
            fatca_compliant_type = self.fatca_compliant_type.value

        us_income_tax = self.us_income_tax

        treaty_country = self.treaty_country

        cert_w8_imy = self.cert_w8_imy

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if fatca_compliant_type is not UNSET:
            field_dict["fatcaCompliantType"] = fatca_compliant_type
        if us_income_tax is not UNSET:
            field_dict["usIncomeTax"] = us_income_tax
        if treaty_country is not UNSET:
            field_dict["treatyCountry"] = treaty_country
        if cert_w8_imy is not UNSET:
            field_dict["certW8Imy"] = cert_w8_imy
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        _fatca_compliant_type = d.pop("fatcaCompliantType", UNSET)
        fatca_compliant_type: Union[Unset, UpdateWithholdingStatementFatcaCompliantType]
        if isinstance(_fatca_compliant_type, Unset):
            fatca_compliant_type = UNSET
        else:
            fatca_compliant_type = UpdateWithholdingStatementFatcaCompliantType(_fatca_compliant_type)

        us_income_tax = d.pop("usIncomeTax", UNSET)

        treaty_country = d.pop("treatyCountry", UNSET)

        cert_w8_imy = d.pop("certW8Imy", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        update_withholding_statement = cls(
            reference_account_id=reference_account_id,
            fatca_compliant_type=fatca_compliant_type,
            us_income_tax=us_income_tax,
            treaty_country=treaty_country,
            cert_w8_imy=cert_w8_imy,
            effective_date=effective_date,
        )

        update_withholding_statement.additional_properties = d
        return update_withholding_statement

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
