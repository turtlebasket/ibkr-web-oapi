from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="EmploymentDetails")


@_attrs_define
class EmploymentDetails:
    """
    Attributes:
        employer (Union[Unset, str]):
        occupation (Union[Unset, str]):
        description (Union[Unset, str]):
        employer_business (Union[Unset, str]):
        employer_address (Union[Unset, Address]):
        employer_phone (Union[Unset, str]):
        empl_country_res_country_details (Union[Unset, str]):
    """

    employer: Union[Unset, str] = UNSET
    occupation: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    employer_business: Union[Unset, str] = UNSET
    employer_address: Union[Unset, "Address"] = UNSET
    employer_phone: Union[Unset, str] = UNSET
    empl_country_res_country_details: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employer = self.employer

        occupation = self.occupation

        description = self.description

        employer_business = self.employer_business

        employer_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employer_address, Unset):
            employer_address = self.employer_address.to_dict()

        employer_phone = self.employer_phone

        empl_country_res_country_details = self.empl_country_res_country_details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employer is not UNSET:
            field_dict["employer"] = employer
        if occupation is not UNSET:
            field_dict["occupation"] = occupation
        if description is not UNSET:
            field_dict["description"] = description
        if employer_business is not UNSET:
            field_dict["employerBusiness"] = employer_business
        if employer_address is not UNSET:
            field_dict["employerAddress"] = employer_address
        if employer_phone is not UNSET:
            field_dict["employerPhone"] = employer_phone
        if empl_country_res_country_details is not UNSET:
            field_dict["emplCountryResCountryDetails"] = empl_country_res_country_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        employer = d.pop("employer", UNSET)

        occupation = d.pop("occupation", UNSET)

        description = d.pop("description", UNSET)

        employer_business = d.pop("employerBusiness", UNSET)

        _employer_address = d.pop("employerAddress", UNSET)
        employer_address: Union[Unset, Address]
        if isinstance(_employer_address, Unset):
            employer_address = UNSET
        else:
            employer_address = Address.from_dict(_employer_address)

        employer_phone = d.pop("employerPhone", UNSET)

        empl_country_res_country_details = d.pop("emplCountryResCountryDetails", UNSET)

        employment_details = cls(
            employer=employer,
            occupation=occupation,
            description=description,
            employer_business=employer_business,
            employer_address=employer_address,
            employer_phone=employer_phone,
            empl_country_res_country_details=empl_country_res_country_details,
        )

        employment_details.additional_properties = d
        return employment_details

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
