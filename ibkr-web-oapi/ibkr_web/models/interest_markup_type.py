from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interest_markup_type_currency import InterestMarkupTypeCurrency
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterestMarkupType")


@_attrs_define
class InterestMarkupType:
    """
    Attributes:
        currency (Union[Unset, InterestMarkupTypeCurrency]):
        debit_markup (Union[Unset, float]):
        ib_debit_markup (Union[Unset, float]):
        credit_markdown (Union[Unset, float]):
        short_credit_markdown (Union[Unset, float]):
        short_cfd_credit_markdown (Union[Unset, float]):
        long_cfd_debit_markdown (Union[Unset, float]):
        short_index_cfd_credit_markdown (Union[Unset, float]):
        long_index_cfd_debit_markdown (Union[Unset, float]):
        short_fx_cfd_markup (Union[Unset, float]):
        long_fx_cfd_markdown (Union[Unset, float]):
    """

    currency: Union[Unset, InterestMarkupTypeCurrency] = UNSET
    debit_markup: Union[Unset, float] = UNSET
    ib_debit_markup: Union[Unset, float] = UNSET
    credit_markdown: Union[Unset, float] = UNSET
    short_credit_markdown: Union[Unset, float] = UNSET
    short_cfd_credit_markdown: Union[Unset, float] = UNSET
    long_cfd_debit_markdown: Union[Unset, float] = UNSET
    short_index_cfd_credit_markdown: Union[Unset, float] = UNSET
    long_index_cfd_debit_markdown: Union[Unset, float] = UNSET
    short_fx_cfd_markup: Union[Unset, float] = UNSET
    long_fx_cfd_markdown: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        debit_markup = self.debit_markup

        ib_debit_markup = self.ib_debit_markup

        credit_markdown = self.credit_markdown

        short_credit_markdown = self.short_credit_markdown

        short_cfd_credit_markdown = self.short_cfd_credit_markdown

        long_cfd_debit_markdown = self.long_cfd_debit_markdown

        short_index_cfd_credit_markdown = self.short_index_cfd_credit_markdown

        long_index_cfd_debit_markdown = self.long_index_cfd_debit_markdown

        short_fx_cfd_markup = self.short_fx_cfd_markup

        long_fx_cfd_markdown = self.long_fx_cfd_markdown

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if debit_markup is not UNSET:
            field_dict["debitMarkup"] = debit_markup
        if ib_debit_markup is not UNSET:
            field_dict["ibDebitMarkup"] = ib_debit_markup
        if credit_markdown is not UNSET:
            field_dict["creditMarkdown"] = credit_markdown
        if short_credit_markdown is not UNSET:
            field_dict["shortCreditMarkdown"] = short_credit_markdown
        if short_cfd_credit_markdown is not UNSET:
            field_dict["shortCfdCreditMarkdown"] = short_cfd_credit_markdown
        if long_cfd_debit_markdown is not UNSET:
            field_dict["longCfdDebitMarkdown"] = long_cfd_debit_markdown
        if short_index_cfd_credit_markdown is not UNSET:
            field_dict["shortIndexCfdCreditMarkdown"] = short_index_cfd_credit_markdown
        if long_index_cfd_debit_markdown is not UNSET:
            field_dict["longIndexCfdDebitMarkdown"] = long_index_cfd_debit_markdown
        if short_fx_cfd_markup is not UNSET:
            field_dict["shortFxCfdMarkup"] = short_fx_cfd_markup
        if long_fx_cfd_markdown is not UNSET:
            field_dict["longFxCfdMarkdown"] = long_fx_cfd_markdown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, InterestMarkupTypeCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = InterestMarkupTypeCurrency(_currency)

        debit_markup = d.pop("debitMarkup", UNSET)

        ib_debit_markup = d.pop("ibDebitMarkup", UNSET)

        credit_markdown = d.pop("creditMarkdown", UNSET)

        short_credit_markdown = d.pop("shortCreditMarkdown", UNSET)

        short_cfd_credit_markdown = d.pop("shortCfdCreditMarkdown", UNSET)

        long_cfd_debit_markdown = d.pop("longCfdDebitMarkdown", UNSET)

        short_index_cfd_credit_markdown = d.pop("shortIndexCfdCreditMarkdown", UNSET)

        long_index_cfd_debit_markdown = d.pop("longIndexCfdDebitMarkdown", UNSET)

        short_fx_cfd_markup = d.pop("shortFxCfdMarkup", UNSET)

        long_fx_cfd_markdown = d.pop("longFxCfdMarkdown", UNSET)

        interest_markup_type = cls(
            currency=currency,
            debit_markup=debit_markup,
            ib_debit_markup=ib_debit_markup,
            credit_markdown=credit_markdown,
            short_credit_markdown=short_credit_markdown,
            short_cfd_credit_markdown=short_cfd_credit_markdown,
            long_cfd_debit_markdown=long_cfd_debit_markdown,
            short_index_cfd_credit_markdown=short_index_cfd_credit_markdown,
            long_index_cfd_debit_markdown=long_index_cfd_debit_markdown,
            short_fx_cfd_markup=short_fx_cfd_markup,
            long_fx_cfd_markdown=long_fx_cfd_markdown,
        )

        interest_markup_type.additional_properties = d
        return interest_markup_type

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
