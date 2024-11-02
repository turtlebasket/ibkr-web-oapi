from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.affiliation_details_type_affiliation_relationship import AffiliationDetailsTypeAffiliationRelationship
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="AffiliationDetailsType")


@_attrs_define
class AffiliationDetailsType:
    """
    Attributes:
        affiliation_relationship (Union[Unset, AffiliationDetailsTypeAffiliationRelationship]):
        person_name (Union[Unset, str]):
        company_id (Union[Unset, int]):
        company (Union[Unset, str]):
        company_mailing_address (Union[Unset, Address]):
        company_phone (Union[Unset, str]):
        company_email_address (Union[Unset, str]):
        duplicate_stmt_required (Union[Unset, bool]):
    """

    affiliation_relationship: Union[Unset, AffiliationDetailsTypeAffiliationRelationship] = UNSET
    person_name: Union[Unset, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    company: Union[Unset, str] = UNSET
    company_mailing_address: Union[Unset, "Address"] = UNSET
    company_phone: Union[Unset, str] = UNSET
    company_email_address: Union[Unset, str] = UNSET
    duplicate_stmt_required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        affiliation_relationship: Union[Unset, str] = UNSET
        if not isinstance(self.affiliation_relationship, Unset):
            affiliation_relationship = self.affiliation_relationship.value

        person_name = self.person_name

        company_id = self.company_id

        company = self.company

        company_mailing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.company_mailing_address, Unset):
            company_mailing_address = self.company_mailing_address.to_dict()

        company_phone = self.company_phone

        company_email_address = self.company_email_address

        duplicate_stmt_required = self.duplicate_stmt_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affiliation_relationship is not UNSET:
            field_dict["affiliationRelationship"] = affiliation_relationship
        if person_name is not UNSET:
            field_dict["personName"] = person_name
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company is not UNSET:
            field_dict["company"] = company
        if company_mailing_address is not UNSET:
            field_dict["companyMailingAddress"] = company_mailing_address
        if company_phone is not UNSET:
            field_dict["companyPhone"] = company_phone
        if company_email_address is not UNSET:
            field_dict["companyEmailAddress"] = company_email_address
        if duplicate_stmt_required is not UNSET:
            field_dict["duplicateStmtRequired"] = duplicate_stmt_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        _affiliation_relationship = d.pop("affiliationRelationship", UNSET)
        affiliation_relationship: Union[Unset, AffiliationDetailsTypeAffiliationRelationship]
        if isinstance(_affiliation_relationship, Unset):
            affiliation_relationship = UNSET
        else:
            affiliation_relationship = AffiliationDetailsTypeAffiliationRelationship(_affiliation_relationship)

        person_name = d.pop("personName", UNSET)

        company_id = d.pop("companyId", UNSET)

        company = d.pop("company", UNSET)

        _company_mailing_address = d.pop("companyMailingAddress", UNSET)
        company_mailing_address: Union[Unset, Address]
        if isinstance(_company_mailing_address, Unset):
            company_mailing_address = UNSET
        else:
            company_mailing_address = Address.from_dict(_company_mailing_address)

        company_phone = d.pop("companyPhone", UNSET)

        company_email_address = d.pop("companyEmailAddress", UNSET)

        duplicate_stmt_required = d.pop("duplicateStmtRequired", UNSET)

        affiliation_details_type = cls(
            affiliation_relationship=affiliation_relationship,
            person_name=person_name,
            company_id=company_id,
            company=company,
            company_mailing_address=company_mailing_address,
            company_phone=company_phone,
            company_email_address=company_email_address,
            duplicate_stmt_required=duplicate_stmt_required,
        )

        affiliation_details_type.additional_properties = d
        return affiliation_details_type

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
