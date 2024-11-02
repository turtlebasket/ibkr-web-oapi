from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StmtRequest")


@_attrs_define
class StmtRequest:
    """
    Attributes:
        account_id (str): account id
        start_date (str): from date
        end_date (str): to date
        account_ids (Union[Unset, List[str]]): array of account id's Example: ['U123', 'U456'].
        multi_account_format (Union[Unset, str]): possible values are consolidate, concatenate, or customConsolidate
        crypto_consol_if_available (Union[Unset, bool]): crypto consolidate flag, If request contains any accounts with
            crypto segment, will turn request into Crypto Consolidated Default: False.
        mime_type (Union[Unset, str]): output format Example: application/pdf, text/html, or text/csv.
        language (Union[Unset, str]): two character ISO language code Default: 'en'. Example: en, fr defaults to en
            (english).
        gzip (Union[Unset, bool]): to gzip the whole response pass true Default: False.
    """

    account_id: str
    start_date: str
    end_date: str
    account_ids: Union[Unset, List[str]] = UNSET
    multi_account_format: Union[Unset, str] = UNSET
    crypto_consol_if_available: Union[Unset, bool] = False
    mime_type: Union[Unset, str] = UNSET
    language: Union[Unset, str] = "en"
    gzip: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        start_date = self.start_date

        end_date = self.end_date

        account_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.account_ids, Unset):
            account_ids = self.account_ids

        multi_account_format = self.multi_account_format

        crypto_consol_if_available = self.crypto_consol_if_available

        mime_type = self.mime_type

        language = self.language

        gzip = self.gzip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids
        if multi_account_format is not UNSET:
            field_dict["multiAccountFormat"] = multi_account_format
        if crypto_consol_if_available is not UNSET:
            field_dict["cryptoConsolIfAvailable"] = crypto_consol_if_available
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if language is not UNSET:
            field_dict["language"] = language
        if gzip is not UNSET:
            field_dict["gzip"] = gzip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        start_date = d.pop("startDate")

        end_date = d.pop("endDate")

        account_ids = cast(List[str], d.pop("accountIds", UNSET))

        multi_account_format = d.pop("multiAccountFormat", UNSET)

        crypto_consol_if_available = d.pop("cryptoConsolIfAvailable", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        language = d.pop("language", UNSET)

        gzip = d.pop("gzip", UNSET)

        stmt_request = cls(
            account_id=account_id,
            start_date=start_date,
            end_date=end_date,
            account_ids=account_ids,
            multi_account_format=multi_account_format,
            crypto_consol_if_available=crypto_consol_if_available,
            mime_type=mime_type,
            language=language,
            gzip=gzip,
        )

        stmt_request.additional_properties = d
        return stmt_request

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
