from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.affiliation_details_type import AffiliationDetailsType
    from ..models.aus_exposure_details_type import AUSExposureDetailsType
    from ..models.org_regulatory_info_type import ORGRegulatoryInfoType
    from ..models.political_military_diplomatic_details_type import PoliticalMilitaryDiplomaticDetailsType
    from ..models.regulatory_detail import RegulatoryDetail
    from ..models.self_regulated_membership_type import SelfRegulatedMembershipType


T = TypeVar("T", bound="RegulatoryInformation")


@_attrs_define
class RegulatoryInformation:
    """
    Attributes:
        regulatory_details (Union[Unset, List['RegulatoryDetail']]):
        regulatory_detail (Union[Unset, List['RegulatoryDetail']]):
        self_regulated_membership (Union[Unset, SelfRegulatedMembershipType]):
        affiliation_details (Union[Unset, AffiliationDetailsType]):
        financial_org_types (Union[Unset, List[str]]):
        org_regulatory_info (Union[Unset, ORGRegulatoryInfoType]):
        aus_exposure_details (Union[Unset, AUSExposureDetailsType]):
        controller_exchange_code (Union[Unset, str]):
        political_military_diplomatic_details (Union[Unset, PoliticalMilitaryDiplomaticDetailsType]):
        translated (Union[Unset, bool]):
    """

    regulatory_details: Union[Unset, List["RegulatoryDetail"]] = UNSET
    regulatory_detail: Union[Unset, List["RegulatoryDetail"]] = UNSET
    self_regulated_membership: Union[Unset, "SelfRegulatedMembershipType"] = UNSET
    affiliation_details: Union[Unset, "AffiliationDetailsType"] = UNSET
    financial_org_types: Union[Unset, List[str]] = UNSET
    org_regulatory_info: Union[Unset, "ORGRegulatoryInfoType"] = UNSET
    aus_exposure_details: Union[Unset, "AUSExposureDetailsType"] = UNSET
    controller_exchange_code: Union[Unset, str] = UNSET
    political_military_diplomatic_details: Union[Unset, "PoliticalMilitaryDiplomaticDetailsType"] = UNSET
    translated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regulatory_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regulatory_details, Unset):
            regulatory_details = []
            for regulatory_details_item_data in self.regulatory_details:
                regulatory_details_item = regulatory_details_item_data.to_dict()
                regulatory_details.append(regulatory_details_item)

        regulatory_detail: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regulatory_detail, Unset):
            regulatory_detail = []
            for regulatory_detail_item_data in self.regulatory_detail:
                regulatory_detail_item = regulatory_detail_item_data.to_dict()
                regulatory_detail.append(regulatory_detail_item)

        self_regulated_membership: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_regulated_membership, Unset):
            self_regulated_membership = self.self_regulated_membership.to_dict()

        affiliation_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.affiliation_details, Unset):
            affiliation_details = self.affiliation_details.to_dict()

        financial_org_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.financial_org_types, Unset):
            financial_org_types = self.financial_org_types

        org_regulatory_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_regulatory_info, Unset):
            org_regulatory_info = self.org_regulatory_info.to_dict()

        aus_exposure_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aus_exposure_details, Unset):
            aus_exposure_details = self.aus_exposure_details.to_dict()

        controller_exchange_code = self.controller_exchange_code

        political_military_diplomatic_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.political_military_diplomatic_details, Unset):
            political_military_diplomatic_details = self.political_military_diplomatic_details.to_dict()

        translated = self.translated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regulatory_details is not UNSET:
            field_dict["regulatoryDetails"] = regulatory_details
        if regulatory_detail is not UNSET:
            field_dict["regulatoryDetail"] = regulatory_detail
        if self_regulated_membership is not UNSET:
            field_dict["selfRegulatedMembership"] = self_regulated_membership
        if affiliation_details is not UNSET:
            field_dict["affiliationDetails"] = affiliation_details
        if financial_org_types is not UNSET:
            field_dict["financialOrgTypes"] = financial_org_types
        if org_regulatory_info is not UNSET:
            field_dict["orgRegulatoryInfo"] = org_regulatory_info
        if aus_exposure_details is not UNSET:
            field_dict["ausExposureDetails"] = aus_exposure_details
        if controller_exchange_code is not UNSET:
            field_dict["controllerExchangeCode"] = controller_exchange_code
        if political_military_diplomatic_details is not UNSET:
            field_dict["politicalMilitaryDiplomaticDetails"] = political_military_diplomatic_details
        if translated is not UNSET:
            field_dict["translated"] = translated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.affiliation_details_type import AffiliationDetailsType
        from ..models.aus_exposure_details_type import AUSExposureDetailsType
        from ..models.org_regulatory_info_type import ORGRegulatoryInfoType
        from ..models.political_military_diplomatic_details_type import PoliticalMilitaryDiplomaticDetailsType
        from ..models.regulatory_detail import RegulatoryDetail
        from ..models.self_regulated_membership_type import SelfRegulatedMembershipType

        d = src_dict.copy()
        regulatory_details = []
        _regulatory_details = d.pop("regulatoryDetails", UNSET)
        for regulatory_details_item_data in _regulatory_details or []:
            regulatory_details_item = RegulatoryDetail.from_dict(regulatory_details_item_data)

            regulatory_details.append(regulatory_details_item)

        regulatory_detail = []
        _regulatory_detail = d.pop("regulatoryDetail", UNSET)
        for regulatory_detail_item_data in _regulatory_detail or []:
            regulatory_detail_item = RegulatoryDetail.from_dict(regulatory_detail_item_data)

            regulatory_detail.append(regulatory_detail_item)

        _self_regulated_membership = d.pop("selfRegulatedMembership", UNSET)
        self_regulated_membership: Union[Unset, SelfRegulatedMembershipType]
        if isinstance(_self_regulated_membership, Unset):
            self_regulated_membership = UNSET
        else:
            self_regulated_membership = SelfRegulatedMembershipType.from_dict(_self_regulated_membership)

        _affiliation_details = d.pop("affiliationDetails", UNSET)
        affiliation_details: Union[Unset, AffiliationDetailsType]
        if isinstance(_affiliation_details, Unset):
            affiliation_details = UNSET
        else:
            affiliation_details = AffiliationDetailsType.from_dict(_affiliation_details)

        financial_org_types = cast(List[str], d.pop("financialOrgTypes", UNSET))

        _org_regulatory_info = d.pop("orgRegulatoryInfo", UNSET)
        org_regulatory_info: Union[Unset, ORGRegulatoryInfoType]
        if isinstance(_org_regulatory_info, Unset):
            org_regulatory_info = UNSET
        else:
            org_regulatory_info = ORGRegulatoryInfoType.from_dict(_org_regulatory_info)

        _aus_exposure_details = d.pop("ausExposureDetails", UNSET)
        aus_exposure_details: Union[Unset, AUSExposureDetailsType]
        if isinstance(_aus_exposure_details, Unset):
            aus_exposure_details = UNSET
        else:
            aus_exposure_details = AUSExposureDetailsType.from_dict(_aus_exposure_details)

        controller_exchange_code = d.pop("controllerExchangeCode", UNSET)

        _political_military_diplomatic_details = d.pop("politicalMilitaryDiplomaticDetails", UNSET)
        political_military_diplomatic_details: Union[Unset, PoliticalMilitaryDiplomaticDetailsType]
        if isinstance(_political_military_diplomatic_details, Unset):
            political_military_diplomatic_details = UNSET
        else:
            political_military_diplomatic_details = PoliticalMilitaryDiplomaticDetailsType.from_dict(
                _political_military_diplomatic_details
            )

        translated = d.pop("translated", UNSET)

        regulatory_information = cls(
            regulatory_details=regulatory_details,
            regulatory_detail=regulatory_detail,
            self_regulated_membership=self_regulated_membership,
            affiliation_details=affiliation_details,
            financial_org_types=financial_org_types,
            org_regulatory_info=org_regulatory_info,
            aus_exposure_details=aus_exposure_details,
            controller_exchange_code=controller_exchange_code,
            political_military_diplomatic_details=political_military_diplomatic_details,
            translated=translated,
        )

        regulatory_information.additional_properties = d
        return regulatory_information

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
