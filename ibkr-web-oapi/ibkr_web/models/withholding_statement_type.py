import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.withholding_statement_type_fatca_compliant_type import WithholdingStatementTypeFatcaCompliantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WithholdingStatementType")


@_attrs_define
class WithholdingStatementType:
    """
    Attributes:
        account_id (Union[Unset, str]):
        fatca_compliant_type (Union[Unset, WithholdingStatementTypeFatcaCompliantType]):
        us_backup_withholding (Union[Unset, bool]):
        treaty_country (Union[Unset, str]):
        corporation (Union[Unset, bool]):
        flow_through (Union[Unset, bool]):
        effective_date (Union[Unset, datetime.date]):
        dividend_rate (Union[Unset, float]):
        interest_rate (Union[Unset, float]):
        us_other_rate (Union[Unset, float]):
        eci_rate (Union[Unset, float]):
    """

    account_id: Union[Unset, str] = UNSET
    fatca_compliant_type: Union[Unset, WithholdingStatementTypeFatcaCompliantType] = UNSET
    us_backup_withholding: Union[Unset, bool] = UNSET
    treaty_country: Union[Unset, str] = UNSET
    corporation: Union[Unset, bool] = UNSET
    flow_through: Union[Unset, bool] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    dividend_rate: Union[Unset, float] = UNSET
    interest_rate: Union[Unset, float] = UNSET
    us_other_rate: Union[Unset, float] = UNSET
    eci_rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        fatca_compliant_type: Union[Unset, str] = UNSET
        if not isinstance(self.fatca_compliant_type, Unset):
            fatca_compliant_type = self.fatca_compliant_type.value

        us_backup_withholding = self.us_backup_withholding

        treaty_country = self.treaty_country

        corporation = self.corporation

        flow_through = self.flow_through

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        dividend_rate = self.dividend_rate

        interest_rate = self.interest_rate

        us_other_rate = self.us_other_rate

        eci_rate = self.eci_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if fatca_compliant_type is not UNSET:
            field_dict["fatcaCompliantType"] = fatca_compliant_type
        if us_backup_withholding is not UNSET:
            field_dict["usBackupWithholding"] = us_backup_withholding
        if treaty_country is not UNSET:
            field_dict["treatyCountry"] = treaty_country
        if corporation is not UNSET:
            field_dict["corporation"] = corporation
        if flow_through is not UNSET:
            field_dict["flowThrough"] = flow_through
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if dividend_rate is not UNSET:
            field_dict["dividendRate"] = dividend_rate
        if interest_rate is not UNSET:
            field_dict["interestRate"] = interest_rate
        if us_other_rate is not UNSET:
            field_dict["usOtherRate"] = us_other_rate
        if eci_rate is not UNSET:
            field_dict["eciRate"] = eci_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        _fatca_compliant_type = d.pop("fatcaCompliantType", UNSET)
        fatca_compliant_type: Union[Unset, WithholdingStatementTypeFatcaCompliantType]
        if isinstance(_fatca_compliant_type, Unset):
            fatca_compliant_type = UNSET
        else:
            fatca_compliant_type = WithholdingStatementTypeFatcaCompliantType(_fatca_compliant_type)

        us_backup_withholding = d.pop("usBackupWithholding", UNSET)

        treaty_country = d.pop("treatyCountry", UNSET)

        corporation = d.pop("corporation", UNSET)

        flow_through = d.pop("flowThrough", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        dividend_rate = d.pop("dividendRate", UNSET)

        interest_rate = d.pop("interestRate", UNSET)

        us_other_rate = d.pop("usOtherRate", UNSET)

        eci_rate = d.pop("eciRate", UNSET)

        withholding_statement_type = cls(
            account_id=account_id,
            fatca_compliant_type=fatca_compliant_type,
            us_backup_withholding=us_backup_withholding,
            treaty_country=treaty_country,
            corporation=corporation,
            flow_through=flow_through,
            effective_date=effective_date,
            dividend_rate=dividend_rate,
            interest_rate=interest_rate,
            us_other_rate=us_other_rate,
            eci_rate=eci_rate,
        )

        withholding_statement_type.additional_properties = d
        return withholding_statement_type

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
