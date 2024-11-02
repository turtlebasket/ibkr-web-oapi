from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueryIRAContributionsResultContributionsItem")


@_attrs_define
class QueryIRAContributionsResultContributionsItem:
    """
    Attributes:
        maximum_contribution_limit (float):
        year_to_date_contribution (float):
        allowed_contribution_limit (float):
    """

    maximum_contribution_limit: float
    year_to_date_contribution: float
    allowed_contribution_limit: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        maximum_contribution_limit = self.maximum_contribution_limit

        year_to_date_contribution = self.year_to_date_contribution

        allowed_contribution_limit = self.allowed_contribution_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maximumContributionLimit": maximum_contribution_limit,
                "yearToDateContribution": year_to_date_contribution,
                "allowedContributionLimit": allowed_contribution_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        maximum_contribution_limit = d.pop("maximumContributionLimit")

        year_to_date_contribution = d.pop("yearToDateContribution")

        allowed_contribution_limit = d.pop("allowedContributionLimit")

        query_ira_contributions_result_contributions_item = cls(
            maximum_contribution_limit=maximum_contribution_limit,
            year_to_date_contribution=year_to_date_contribution,
            allowed_contribution_limit=allowed_contribution_limit,
        )

        query_ira_contributions_result_contributions_item.additional_properties = d
        return query_ira_contributions_result_contributions_item

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
