from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_data import AccountData
    from ..models.account_details_response_decedents_item import AccountDetailsResponseDecedentsItem
    from ..models.account_details_response_financial_information import AccountDetailsResponseFinancialInformation
    from ..models.account_details_response_market_data_item import AccountDetailsResponseMarketDataItem
    from ..models.account_details_response_sources_of_wealth_item import AccountDetailsResponseSourcesOfWealthItem
    from ..models.account_details_response_with_holding_statement import AccountDetailsResponseWithHoldingStatement
    from ..models.associated_entity import AssociatedEntity
    from ..models.associated_person import AssociatedPerson
    from ..models.entity_ira_bene import EntityIRABene
    from ..models.error_response import ErrorResponse
    from ..models.individual_ira_bene import IndividualIRABene
    from ..models.restriction_info import RestrictionInfo


T = TypeVar("T", bound="AccountDetailsResponse")


@_attrs_define
class AccountDetailsResponse:
    """
    Attributes:
        error (Union[Unset, ErrorResponse]):
        has_error (Union[Unset, bool]):
        error_description (Union[Unset, str]):
        account (Union[Unset, AccountData]):
        associated_persons (Union[Unset, List['AssociatedPerson']]):
        associated_entities (Union[Unset, List['AssociatedEntity']]):
        with_holding_statement (Union[Unset, AccountDetailsResponseWithHoldingStatement]):
        market_data (Union[Unset, List['AccountDetailsResponseMarketDataItem']]):
        financial_information (Union[Unset, AccountDetailsResponseFinancialInformation]):
        sources_of_wealth (Union[Unset, List['AccountDetailsResponseSourcesOfWealthItem']]):
        trade_bundles (Union[Unset, List[str]]):
        individual_ira_beneficiaries (Union[Unset, List['IndividualIRABene']]):
        entity_ira_beneficiaries (Union[Unset, List['EntityIRABene']]):
        decedents (Union[Unset, List['AccountDetailsResponseDecedentsItem']]):
        restrictions (Union[Unset, List['RestrictionInfo']]):
    """

    error: Union[Unset, "ErrorResponse"] = UNSET
    has_error: Union[Unset, bool] = UNSET
    error_description: Union[Unset, str] = UNSET
    account: Union[Unset, "AccountData"] = UNSET
    associated_persons: Union[Unset, List["AssociatedPerson"]] = UNSET
    associated_entities: Union[Unset, List["AssociatedEntity"]] = UNSET
    with_holding_statement: Union[Unset, "AccountDetailsResponseWithHoldingStatement"] = UNSET
    market_data: Union[Unset, List["AccountDetailsResponseMarketDataItem"]] = UNSET
    financial_information: Union[Unset, "AccountDetailsResponseFinancialInformation"] = UNSET
    sources_of_wealth: Union[Unset, List["AccountDetailsResponseSourcesOfWealthItem"]] = UNSET
    trade_bundles: Union[Unset, List[str]] = UNSET
    individual_ira_beneficiaries: Union[Unset, List["IndividualIRABene"]] = UNSET
    entity_ira_beneficiaries: Union[Unset, List["EntityIRABene"]] = UNSET
    decedents: Union[Unset, List["AccountDetailsResponseDecedentsItem"]] = UNSET
    restrictions: Union[Unset, List["RestrictionInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        has_error = self.has_error

        error_description = self.error_description

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        associated_persons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.associated_persons, Unset):
            associated_persons = []
            for associated_persons_item_data in self.associated_persons:
                associated_persons_item = associated_persons_item_data.to_dict()
                associated_persons.append(associated_persons_item)

        associated_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.associated_entities, Unset):
            associated_entities = []
            for associated_entities_item_data in self.associated_entities:
                associated_entities_item = associated_entities_item_data.to_dict()
                associated_entities.append(associated_entities_item)

        with_holding_statement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.with_holding_statement, Unset):
            with_holding_statement = self.with_holding_statement.to_dict()

        market_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.market_data, Unset):
            market_data = []
            for market_data_item_data in self.market_data:
                market_data_item = market_data_item_data.to_dict()
                market_data.append(market_data_item)

        financial_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.financial_information, Unset):
            financial_information = self.financial_information.to_dict()

        sources_of_wealth: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources_of_wealth, Unset):
            sources_of_wealth = []
            for sources_of_wealth_item_data in self.sources_of_wealth:
                sources_of_wealth_item = sources_of_wealth_item_data.to_dict()
                sources_of_wealth.append(sources_of_wealth_item)

        trade_bundles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.trade_bundles, Unset):
            trade_bundles = self.trade_bundles

        individual_ira_beneficiaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.individual_ira_beneficiaries, Unset):
            individual_ira_beneficiaries = []
            for individual_ira_beneficiaries_item_data in self.individual_ira_beneficiaries:
                individual_ira_beneficiaries_item = individual_ira_beneficiaries_item_data.to_dict()
                individual_ira_beneficiaries.append(individual_ira_beneficiaries_item)

        entity_ira_beneficiaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entity_ira_beneficiaries, Unset):
            entity_ira_beneficiaries = []
            for entity_ira_beneficiaries_item_data in self.entity_ira_beneficiaries:
                entity_ira_beneficiaries_item = entity_ira_beneficiaries_item_data.to_dict()
                entity_ira_beneficiaries.append(entity_ira_beneficiaries_item)

        decedents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.decedents, Unset):
            decedents = []
            for decedents_item_data in self.decedents:
                decedents_item = decedents_item_data.to_dict()
                decedents.append(decedents_item)

        restrictions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = []
            for restrictions_item_data in self.restrictions:
                restrictions_item = restrictions_item_data.to_dict()
                restrictions.append(restrictions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if has_error is not UNSET:
            field_dict["hasError"] = has_error
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if account is not UNSET:
            field_dict["account"] = account
        if associated_persons is not UNSET:
            field_dict["associatedPersons"] = associated_persons
        if associated_entities is not UNSET:
            field_dict["associatedEntities"] = associated_entities
        if with_holding_statement is not UNSET:
            field_dict["withHoldingStatement"] = with_holding_statement
        if market_data is not UNSET:
            field_dict["marketData"] = market_data
        if financial_information is not UNSET:
            field_dict["financialInformation"] = financial_information
        if sources_of_wealth is not UNSET:
            field_dict["sourcesOfWealth"] = sources_of_wealth
        if trade_bundles is not UNSET:
            field_dict["tradeBundles"] = trade_bundles
        if individual_ira_beneficiaries is not UNSET:
            field_dict["individualIRABeneficiaries"] = individual_ira_beneficiaries
        if entity_ira_beneficiaries is not UNSET:
            field_dict["entityIRABeneficiaries"] = entity_ira_beneficiaries
        if decedents is not UNSET:
            field_dict["decedents"] = decedents
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_data import AccountData
        from ..models.account_details_response_decedents_item import AccountDetailsResponseDecedentsItem
        from ..models.account_details_response_financial_information import AccountDetailsResponseFinancialInformation
        from ..models.account_details_response_market_data_item import AccountDetailsResponseMarketDataItem
        from ..models.account_details_response_sources_of_wealth_item import AccountDetailsResponseSourcesOfWealthItem
        from ..models.account_details_response_with_holding_statement import AccountDetailsResponseWithHoldingStatement
        from ..models.associated_entity import AssociatedEntity
        from ..models.associated_person import AssociatedPerson
        from ..models.entity_ira_bene import EntityIRABene
        from ..models.error_response import ErrorResponse
        from ..models.individual_ira_bene import IndividualIRABene
        from ..models.restriction_info import RestrictionInfo

        d = src_dict.copy()
        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorResponse]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorResponse.from_dict(_error)

        has_error = d.pop("hasError", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _account = d.pop("account", UNSET)
        account: Union[Unset, AccountData]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = AccountData.from_dict(_account)

        associated_persons = []
        _associated_persons = d.pop("associatedPersons", UNSET)
        for associated_persons_item_data in _associated_persons or []:
            associated_persons_item = AssociatedPerson.from_dict(associated_persons_item_data)

            associated_persons.append(associated_persons_item)

        associated_entities = []
        _associated_entities = d.pop("associatedEntities", UNSET)
        for associated_entities_item_data in _associated_entities or []:
            associated_entities_item = AssociatedEntity.from_dict(associated_entities_item_data)

            associated_entities.append(associated_entities_item)

        _with_holding_statement = d.pop("withHoldingStatement", UNSET)
        with_holding_statement: Union[Unset, AccountDetailsResponseWithHoldingStatement]
        if isinstance(_with_holding_statement, Unset):
            with_holding_statement = UNSET
        else:
            with_holding_statement = AccountDetailsResponseWithHoldingStatement.from_dict(_with_holding_statement)

        market_data = []
        _market_data = d.pop("marketData", UNSET)
        for market_data_item_data in _market_data or []:
            market_data_item = AccountDetailsResponseMarketDataItem.from_dict(market_data_item_data)

            market_data.append(market_data_item)

        _financial_information = d.pop("financialInformation", UNSET)
        financial_information: Union[Unset, AccountDetailsResponseFinancialInformation]
        if isinstance(_financial_information, Unset):
            financial_information = UNSET
        else:
            financial_information = AccountDetailsResponseFinancialInformation.from_dict(_financial_information)

        sources_of_wealth = []
        _sources_of_wealth = d.pop("sourcesOfWealth", UNSET)
        for sources_of_wealth_item_data in _sources_of_wealth or []:
            sources_of_wealth_item = AccountDetailsResponseSourcesOfWealthItem.from_dict(sources_of_wealth_item_data)

            sources_of_wealth.append(sources_of_wealth_item)

        trade_bundles = cast(List[str], d.pop("tradeBundles", UNSET))

        individual_ira_beneficiaries = []
        _individual_ira_beneficiaries = d.pop("individualIRABeneficiaries", UNSET)
        for individual_ira_beneficiaries_item_data in _individual_ira_beneficiaries or []:
            individual_ira_beneficiaries_item = IndividualIRABene.from_dict(individual_ira_beneficiaries_item_data)

            individual_ira_beneficiaries.append(individual_ira_beneficiaries_item)

        entity_ira_beneficiaries = []
        _entity_ira_beneficiaries = d.pop("entityIRABeneficiaries", UNSET)
        for entity_ira_beneficiaries_item_data in _entity_ira_beneficiaries or []:
            entity_ira_beneficiaries_item = EntityIRABene.from_dict(entity_ira_beneficiaries_item_data)

            entity_ira_beneficiaries.append(entity_ira_beneficiaries_item)

        decedents = []
        _decedents = d.pop("decedents", UNSET)
        for decedents_item_data in _decedents or []:
            decedents_item = AccountDetailsResponseDecedentsItem.from_dict(decedents_item_data)

            decedents.append(decedents_item)

        restrictions = []
        _restrictions = d.pop("restrictions", UNSET)
        for restrictions_item_data in _restrictions or []:
            restrictions_item = RestrictionInfo.from_dict(restrictions_item_data)

            restrictions.append(restrictions_item)

        account_details_response = cls(
            error=error,
            has_error=has_error,
            error_description=error_description,
            account=account,
            associated_persons=associated_persons,
            associated_entities=associated_entities,
            with_holding_statement=with_holding_statement,
            market_data=market_data,
            financial_information=financial_information,
            sources_of_wealth=sources_of_wealth,
            trade_bundles=trade_bundles,
            individual_ira_beneficiaries=individual_ira_beneficiaries,
            entity_ira_beneficiaries=entity_ira_beneficiaries,
            decedents=decedents,
            restrictions=restrictions,
        )

        account_details_response.additional_properties = d
        return account_details_response

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
