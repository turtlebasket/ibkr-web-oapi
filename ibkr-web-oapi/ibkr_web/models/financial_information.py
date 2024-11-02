from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_information_investment_objectives_item import FinancialInformationInvestmentObjectivesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_experience import AssetExperience
    from ..models.questionnaire_type import QuestionnaireType
    from ..models.soi_questionnaire import SOIQuestionnaire
    from ..models.source_of_income_type import SourceOfIncomeType
    from ..models.source_of_wealth_type import SourceOfWealthType


T = TypeVar("T", bound="FinancialInformation")


@_attrs_define
class FinancialInformation:
    """
    Attributes:
        investment_experience (Union[Unset, List['AssetExperience']]):
        investment_objectives (Union[Unset, List[FinancialInformationInvestmentObjectivesItem]]):
        additional_sources_of_income (Union[Unset, List['SourceOfIncomeType']]):
        sources_of_wealth (Union[Unset, List['SourceOfWealthType']]):
        soi_questionnaire (Union[Unset, SOIQuestionnaire]):
        questionnaires (Union[Unset, List['QuestionnaireType']]):
        net_worth (Union[Unset, float]):
        liquid_net_worth (Union[Unset, float]):
        annual_net_income (Union[Unset, float]):
        total_assets (Union[Unset, float]):
        source_of_funds (Union[Unset, str]):
        translated (Union[Unset, bool]):
    """

    investment_experience: Union[Unset, List["AssetExperience"]] = UNSET
    investment_objectives: Union[Unset, List[FinancialInformationInvestmentObjectivesItem]] = UNSET
    additional_sources_of_income: Union[Unset, List["SourceOfIncomeType"]] = UNSET
    sources_of_wealth: Union[Unset, List["SourceOfWealthType"]] = UNSET
    soi_questionnaire: Union[Unset, "SOIQuestionnaire"] = UNSET
    questionnaires: Union[Unset, List["QuestionnaireType"]] = UNSET
    net_worth: Union[Unset, float] = UNSET
    liquid_net_worth: Union[Unset, float] = UNSET
    annual_net_income: Union[Unset, float] = UNSET
    total_assets: Union[Unset, float] = UNSET
    source_of_funds: Union[Unset, str] = UNSET
    translated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        investment_experience: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.investment_experience, Unset):
            investment_experience = []
            for investment_experience_item_data in self.investment_experience:
                investment_experience_item = investment_experience_item_data.to_dict()
                investment_experience.append(investment_experience_item)

        investment_objectives: Union[Unset, List[str]] = UNSET
        if not isinstance(self.investment_objectives, Unset):
            investment_objectives = []
            for investment_objectives_item_data in self.investment_objectives:
                investment_objectives_item = investment_objectives_item_data.value
                investment_objectives.append(investment_objectives_item)

        additional_sources_of_income: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_sources_of_income, Unset):
            additional_sources_of_income = []
            for additional_sources_of_income_item_data in self.additional_sources_of_income:
                additional_sources_of_income_item = additional_sources_of_income_item_data.to_dict()
                additional_sources_of_income.append(additional_sources_of_income_item)

        sources_of_wealth: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources_of_wealth, Unset):
            sources_of_wealth = []
            for sources_of_wealth_item_data in self.sources_of_wealth:
                sources_of_wealth_item = sources_of_wealth_item_data.to_dict()
                sources_of_wealth.append(sources_of_wealth_item)

        soi_questionnaire: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.soi_questionnaire, Unset):
            soi_questionnaire = self.soi_questionnaire.to_dict()

        questionnaires: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.questionnaires, Unset):
            questionnaires = []
            for questionnaires_item_data in self.questionnaires:
                questionnaires_item = questionnaires_item_data.to_dict()
                questionnaires.append(questionnaires_item)

        net_worth = self.net_worth

        liquid_net_worth = self.liquid_net_worth

        annual_net_income = self.annual_net_income

        total_assets = self.total_assets

        source_of_funds = self.source_of_funds

        translated = self.translated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if investment_experience is not UNSET:
            field_dict["investmentExperience"] = investment_experience
        if investment_objectives is not UNSET:
            field_dict["investmentObjectives"] = investment_objectives
        if additional_sources_of_income is not UNSET:
            field_dict["additionalSourcesOfIncome"] = additional_sources_of_income
        if sources_of_wealth is not UNSET:
            field_dict["sourcesOfWealth"] = sources_of_wealth
        if soi_questionnaire is not UNSET:
            field_dict["soiQuestionnaire"] = soi_questionnaire
        if questionnaires is not UNSET:
            field_dict["questionnaires"] = questionnaires
        if net_worth is not UNSET:
            field_dict["netWorth"] = net_worth
        if liquid_net_worth is not UNSET:
            field_dict["liquidNetWorth"] = liquid_net_worth
        if annual_net_income is not UNSET:
            field_dict["annualNetIncome"] = annual_net_income
        if total_assets is not UNSET:
            field_dict["totalAssets"] = total_assets
        if source_of_funds is not UNSET:
            field_dict["sourceOfFunds"] = source_of_funds
        if translated is not UNSET:
            field_dict["translated"] = translated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_experience import AssetExperience
        from ..models.questionnaire_type import QuestionnaireType
        from ..models.soi_questionnaire import SOIQuestionnaire
        from ..models.source_of_income_type import SourceOfIncomeType
        from ..models.source_of_wealth_type import SourceOfWealthType

        d = src_dict.copy()
        investment_experience = []
        _investment_experience = d.pop("investmentExperience", UNSET)
        for investment_experience_item_data in _investment_experience or []:
            investment_experience_item = AssetExperience.from_dict(investment_experience_item_data)

            investment_experience.append(investment_experience_item)

        investment_objectives = []
        _investment_objectives = d.pop("investmentObjectives", UNSET)
        for investment_objectives_item_data in _investment_objectives or []:
            investment_objectives_item = FinancialInformationInvestmentObjectivesItem(investment_objectives_item_data)

            investment_objectives.append(investment_objectives_item)

        additional_sources_of_income = []
        _additional_sources_of_income = d.pop("additionalSourcesOfIncome", UNSET)
        for additional_sources_of_income_item_data in _additional_sources_of_income or []:
            additional_sources_of_income_item = SourceOfIncomeType.from_dict(additional_sources_of_income_item_data)

            additional_sources_of_income.append(additional_sources_of_income_item)

        sources_of_wealth = []
        _sources_of_wealth = d.pop("sourcesOfWealth", UNSET)
        for sources_of_wealth_item_data in _sources_of_wealth or []:
            sources_of_wealth_item = SourceOfWealthType.from_dict(sources_of_wealth_item_data)

            sources_of_wealth.append(sources_of_wealth_item)

        _soi_questionnaire = d.pop("soiQuestionnaire", UNSET)
        soi_questionnaire: Union[Unset, SOIQuestionnaire]
        if isinstance(_soi_questionnaire, Unset):
            soi_questionnaire = UNSET
        else:
            soi_questionnaire = SOIQuestionnaire.from_dict(_soi_questionnaire)

        questionnaires = []
        _questionnaires = d.pop("questionnaires", UNSET)
        for questionnaires_item_data in _questionnaires or []:
            questionnaires_item = QuestionnaireType.from_dict(questionnaires_item_data)

            questionnaires.append(questionnaires_item)

        net_worth = d.pop("netWorth", UNSET)

        liquid_net_worth = d.pop("liquidNetWorth", UNSET)

        annual_net_income = d.pop("annualNetIncome", UNSET)

        total_assets = d.pop("totalAssets", UNSET)

        source_of_funds = d.pop("sourceOfFunds", UNSET)

        translated = d.pop("translated", UNSET)

        financial_information = cls(
            investment_experience=investment_experience,
            investment_objectives=investment_objectives,
            additional_sources_of_income=additional_sources_of_income,
            sources_of_wealth=sources_of_wealth,
            soi_questionnaire=soi_questionnaire,
            questionnaires=questionnaires,
            net_worth=net_worth,
            liquid_net_worth=liquid_net_worth,
            annual_net_income=annual_net_income,
            total_assets=total_assets,
            source_of_funds=source_of_funds,
            translated=translated,
        )

        financial_information.additional_properties = d
        return financial_information

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
