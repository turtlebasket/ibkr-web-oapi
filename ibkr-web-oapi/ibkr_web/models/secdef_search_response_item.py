from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secdef_search_response_item_issuers_item import SecdefSearchResponseItemIssuersItem
    from ..models.secdef_search_response_item_sections_item import SecdefSearchResponseItemSectionsItem


T = TypeVar("T", bound="SecdefSearchResponseItem")


@_attrs_define
class SecdefSearchResponseItem:
    """
    Attributes:
        bondid (Union[Unset, int]): applicable for bonds
        conid (Union[Unset, str]): Contract identifier for the unique contract.
        company_header (Union[Unset, str]): Company Name - Exchange
        company_name (Union[Unset, str]): Formal name of the company.
        symbol (Union[Unset, str]): Underlying ticker symbol.
        description (Union[Unset, str]): Primary exchange of the contract
        restricted (Union[None, Unset, bool]): Returns if the contract is available for trading.
        fop (Union[None, Unset, str]): Returns a string of dates, separated by semicolons.
        opt (Union[None, Unset, str]): Returns a string of dates, separated by semicolons.
        war (Union[None, Unset, str]): Returns a string of dates, separated by semicolons.
        sections (Union[Unset, List['SecdefSearchResponseItemSectionsItem']]):
        issuers (Union[Unset, List['SecdefSearchResponseItemIssuersItem']]):
    """

    bondid: Union[Unset, int] = UNSET
    conid: Union[Unset, str] = UNSET
    company_header: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    restricted: Union[None, Unset, bool] = UNSET
    fop: Union[None, Unset, str] = UNSET
    opt: Union[None, Unset, str] = UNSET
    war: Union[None, Unset, str] = UNSET
    sections: Union[Unset, List["SecdefSearchResponseItemSectionsItem"]] = UNSET
    issuers: Union[Unset, List["SecdefSearchResponseItemIssuersItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bondid = self.bondid

        conid = self.conid

        company_header = self.company_header

        company_name = self.company_name

        symbol = self.symbol

        description = self.description

        restricted: Union[None, Unset, bool]
        if isinstance(self.restricted, Unset):
            restricted = UNSET
        else:
            restricted = self.restricted

        fop: Union[None, Unset, str]
        if isinstance(self.fop, Unset):
            fop = UNSET
        else:
            fop = self.fop

        opt: Union[None, Unset, str]
        if isinstance(self.opt, Unset):
            opt = UNSET
        else:
            opt = self.opt

        war: Union[None, Unset, str]
        if isinstance(self.war, Unset):
            war = UNSET
        else:
            war = self.war

        sections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)

        issuers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.issuers, Unset):
            issuers = []
            for issuers_item_data in self.issuers:
                issuers_item = issuers_item_data.to_dict()
                issuers.append(issuers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bondid is not UNSET:
            field_dict["bondid"] = bondid
        if conid is not UNSET:
            field_dict["conid"] = conid
        if company_header is not UNSET:
            field_dict["companyHeader"] = company_header
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if description is not UNSET:
            field_dict["description"] = description
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if fop is not UNSET:
            field_dict["fop"] = fop
        if opt is not UNSET:
            field_dict["opt"] = opt
        if war is not UNSET:
            field_dict["war"] = war
        if sections is not UNSET:
            field_dict["sections"] = sections
        if issuers is not UNSET:
            field_dict["issuers"] = issuers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.secdef_search_response_item_issuers_item import SecdefSearchResponseItemIssuersItem
        from ..models.secdef_search_response_item_sections_item import SecdefSearchResponseItemSectionsItem

        d = src_dict.copy()
        bondid = d.pop("bondid", UNSET)

        conid = d.pop("conid", UNSET)

        company_header = d.pop("companyHeader", UNSET)

        company_name = d.pop("companyName", UNSET)

        symbol = d.pop("symbol", UNSET)

        description = d.pop("description", UNSET)

        def _parse_restricted(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        restricted = _parse_restricted(d.pop("restricted", UNSET))

        def _parse_fop(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fop = _parse_fop(d.pop("fop", UNSET))

        def _parse_opt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        opt = _parse_opt(d.pop("opt", UNSET))

        def _parse_war(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        war = _parse_war(d.pop("war", UNSET))

        sections = []
        _sections = d.pop("sections", UNSET)
        for sections_item_data in _sections or []:
            sections_item = SecdefSearchResponseItemSectionsItem.from_dict(sections_item_data)

            sections.append(sections_item)

        issuers = []
        _issuers = d.pop("issuers", UNSET)
        for issuers_item_data in _issuers or []:
            issuers_item = SecdefSearchResponseItemIssuersItem.from_dict(issuers_item_data)

            issuers.append(issuers_item)

        secdef_search_response_item = cls(
            bondid=bondid,
            conid=conid,
            company_header=company_header,
            company_name=company_name,
            symbol=symbol,
            description=description,
            restricted=restricted,
            fop=fop,
            opt=opt,
            war=war,
            sections=sections,
            issuers=issuers,
        )

        secdef_search_response_item.additional_properties = d
        return secdef_search_response_item

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
