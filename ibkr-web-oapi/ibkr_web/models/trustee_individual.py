from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trustee_individual_gender import TrusteeIndividualGender
from ..models.trustee_individual_marital_status import TrusteeIndividualMaritalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.employment_details import EmploymentDetails
    from ..models.form_crs import FormCRS
    from ..models.form_w8ben import FormW8BEN
    from ..models.form_w9 import FormW9
    from ..models.identification import Identification
    from ..models.individual_name import IndividualName
    from ..models.phone_info import PhoneInfo
    from ..models.prohibited_country_questionnaire_list import ProhibitedCountryQuestionnaireList
    from ..models.residence_address import ResidenceAddress
    from ..models.tax_residency import TaxResidency


T = TypeVar("T", bound="TrusteeIndividual")


@_attrs_define
class TrusteeIndividual:
    r"""
    Attributes:
        name (Union[Unset, IndividualName]):
        native_name (Union[Unset, IndividualName]):
        birth_name (Union[Unset, IndividualName]):
        mother_maiden_name (Union[Unset, IndividualName]):
        date_of_birth (Union[Unset, str]): Date of birth of the applicant. The applicant must be 18 years or older to
            open an account. <br><ul><li>If the YYY-MM-DD < 18 years error will be triggered and the account will not be
            created.</li><li>If YYYY-MM-DD < 21 the applicant is restricted to opening a CASH account only.</li><li>UGMA and
            UTMA accounts are available for minors 18 years of age or younger. An individual or entity who manages an
            account for a minor until that minor reaches a specific age. Available to US residents only.</li><li>This
            application must be opened using the front-end application which is available within the IBKR
            Portal.</li><li>Assets held in a single account managed by a single Custodian user.</li><li>Error will be thrown
            if dateOfBirth is any value other than YYYY-MM-DD.</li></ul> Example: 1990-08-14.
        country_of_birth (Union[Unset, str]):
        city_of_birth (Union[Unset, str]):
        gender (Union[Unset, TrusteeIndividualGender]):
        marital_status (Union[Unset, TrusteeIndividualMaritalStatus]):
        num_dependents (Union[Unset, int]):
        residence_address (Union[Unset, ResidenceAddress]): Provide the residential address where the applicant
            physically resides. <br><ul><li>If the mailing address is different from the address provided in Residence
            element, THEN you will also include MailingAddress element.</li><li>Post Office Box is not accepted for
            Residential Address.</li><li>Our system validates street_1 and street_2 included within Residence attribute to
            ensure Post Office Box address is not provided.</li><li>An error will be thrown if the below combinations are
            included within street_1 OR street_2:</li><ul><li>PB</li><li>PO Box</li><li>Post Office Box</li><li>P.O.
            Box</li><li>In care of</li><li>General Delivery</li><li>Regular Expression to validate street_1 and
            street_2:</li></ul></ul>English: (?:P(?:ost(?:al)?)?[\.\-
            \s]*(?:(?:O(?:ffice)?[\.\s]*)?B(?:ox|in|\b|\d)|o(?:ffice|\b)(?:[-\s]*\d)|code)|box[-\s]*\d)<br>Chinese
            Simplified: PO Box    (?i)\b((邮政信箱) [0-9]*)\bChinese Traditional: PO Box   (?i)\b((郵政信箱) [0-9]*)\b Example:
            {"street1": "1 Tester Street", "city": "London", "state": "GB-ENG" ,"country":"GBR","postalCode": "SW10 9QL"},.
        mailing_address (Union[Unset, Address]):
        phones (Union[Unset, List['PhoneInfo']]):
        email (Union[Unset, str]):
        identification (Union[Unset, Identification]): Identification information of the associated person. Example:
            {'citizenship': 'AUS', 'driversLicense': '989444798', 'issuingCountry': 'AUS', 'hasExpirationDate': True,
            'expirationDate': '2029-03-22', 'rta': '9999999', 'issuingState': 'AU-QLD'}.
        employment_type (Union[Unset, str]):
        employment_details (Union[Unset, EmploymentDetails]):
        employee_title (Union[Unset, str]):
        tax_residencies (Union[Unset, List['TaxResidency']]):
        w9 (Union[Unset, FormW9]):
        w_8_ben (Union[Unset, FormW8BEN]):
        crs (Union[Unset, FormCRS]):
        prohibited_country_questionnaire (Union[Unset, ProhibitedCountryQuestionnaireList]):
        id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        same_mail_address (Union[Unset, bool]):
        authorized_to_sign_on_behalf_of_owner (Union[Unset, bool]):
        authorized_trader (Union[Unset, bool]):
        us_tax_resident (Union[Unset, bool]):
        translated (Union[Unset, bool]):
        primary_trustee (Union[Unset, bool]):
        nfa_registered (Union[Unset, bool]):
        nfa_registration_number (Union[Unset, str]):
    """

    name: Union[Unset, "IndividualName"] = UNSET
    native_name: Union[Unset, "IndividualName"] = UNSET
    birth_name: Union[Unset, "IndividualName"] = UNSET
    mother_maiden_name: Union[Unset, "IndividualName"] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    country_of_birth: Union[Unset, str] = UNSET
    city_of_birth: Union[Unset, str] = UNSET
    gender: Union[Unset, TrusteeIndividualGender] = UNSET
    marital_status: Union[Unset, TrusteeIndividualMaritalStatus] = UNSET
    num_dependents: Union[Unset, int] = UNSET
    residence_address: Union[Unset, "ResidenceAddress"] = UNSET
    mailing_address: Union[Unset, "Address"] = UNSET
    phones: Union[Unset, List["PhoneInfo"]] = UNSET
    email: Union[Unset, str] = UNSET
    identification: Union[Unset, "Identification"] = UNSET
    employment_type: Union[Unset, str] = UNSET
    employment_details: Union[Unset, "EmploymentDetails"] = UNSET
    employee_title: Union[Unset, str] = UNSET
    tax_residencies: Union[Unset, List["TaxResidency"]] = UNSET
    w9: Union[Unset, "FormW9"] = UNSET
    w_8_ben: Union[Unset, "FormW8BEN"] = UNSET
    crs: Union[Unset, "FormCRS"] = UNSET
    prohibited_country_questionnaire: Union[Unset, "ProhibitedCountryQuestionnaireList"] = UNSET
    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    same_mail_address: Union[Unset, bool] = UNSET
    authorized_to_sign_on_behalf_of_owner: Union[Unset, bool] = UNSET
    authorized_trader: Union[Unset, bool] = UNSET
    us_tax_resident: Union[Unset, bool] = UNSET
    translated: Union[Unset, bool] = UNSET
    primary_trustee: Union[Unset, bool] = UNSET
    nfa_registered: Union[Unset, bool] = UNSET
    nfa_registration_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        native_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.native_name, Unset):
            native_name = self.native_name.to_dict()

        birth_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_name, Unset):
            birth_name = self.birth_name.to_dict()

        mother_maiden_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mother_maiden_name, Unset):
            mother_maiden_name = self.mother_maiden_name.to_dict()

        date_of_birth = self.date_of_birth

        country_of_birth = self.country_of_birth

        city_of_birth = self.city_of_birth

        gender: Union[Unset, str] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        marital_status: Union[Unset, str] = UNSET
        if not isinstance(self.marital_status, Unset):
            marital_status = self.marital_status.value

        num_dependents = self.num_dependents

        residence_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.residence_address, Unset):
            residence_address = self.residence_address.to_dict()

        mailing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mailing_address, Unset):
            mailing_address = self.mailing_address.to_dict()

        phones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()
                phones.append(phones_item)

        email = self.email

        identification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identification, Unset):
            identification = self.identification.to_dict()

        employment_type = self.employment_type

        employment_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employment_details, Unset):
            employment_details = self.employment_details.to_dict()

        employee_title = self.employee_title

        tax_residencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_residencies, Unset):
            tax_residencies = []
            for tax_residencies_item_data in self.tax_residencies:
                tax_residencies_item = tax_residencies_item_data.to_dict()
                tax_residencies.append(tax_residencies_item)

        w9: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w9, Unset):
            w9 = self.w9.to_dict()

        w_8_ben: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8_ben, Unset):
            w_8_ben = self.w_8_ben.to_dict()

        crs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crs, Unset):
            crs = self.crs.to_dict()

        prohibited_country_questionnaire: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prohibited_country_questionnaire, Unset):
            prohibited_country_questionnaire = self.prohibited_country_questionnaire.to_dict()

        id = self.id

        external_id = self.external_id

        user_id = self.user_id

        same_mail_address = self.same_mail_address

        authorized_to_sign_on_behalf_of_owner = self.authorized_to_sign_on_behalf_of_owner

        authorized_trader = self.authorized_trader

        us_tax_resident = self.us_tax_resident

        translated = self.translated

        primary_trustee = self.primary_trustee

        nfa_registered = self.nfa_registered

        nfa_registration_number = self.nfa_registration_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if native_name is not UNSET:
            field_dict["nativeName"] = native_name
        if birth_name is not UNSET:
            field_dict["birthName"] = birth_name
        if mother_maiden_name is not UNSET:
            field_dict["motherMaidenName"] = mother_maiden_name
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if country_of_birth is not UNSET:
            field_dict["countryOfBirth"] = country_of_birth
        if city_of_birth is not UNSET:
            field_dict["cityOfBirth"] = city_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if marital_status is not UNSET:
            field_dict["maritalStatus"] = marital_status
        if num_dependents is not UNSET:
            field_dict["numDependents"] = num_dependents
        if residence_address is not UNSET:
            field_dict["residenceAddress"] = residence_address
        if mailing_address is not UNSET:
            field_dict["mailingAddress"] = mailing_address
        if phones is not UNSET:
            field_dict["phones"] = phones
        if email is not UNSET:
            field_dict["email"] = email
        if identification is not UNSET:
            field_dict["identification"] = identification
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if employment_details is not UNSET:
            field_dict["employmentDetails"] = employment_details
        if employee_title is not UNSET:
            field_dict["employeeTitle"] = employee_title
        if tax_residencies is not UNSET:
            field_dict["taxResidencies"] = tax_residencies
        if w9 is not UNSET:
            field_dict["w9"] = w9
        if w_8_ben is not UNSET:
            field_dict["w8Ben"] = w_8_ben
        if crs is not UNSET:
            field_dict["crs"] = crs
        if prohibited_country_questionnaire is not UNSET:
            field_dict["prohibitedCountryQuestionnaire"] = prohibited_country_questionnaire
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if same_mail_address is not UNSET:
            field_dict["sameMailAddress"] = same_mail_address
        if authorized_to_sign_on_behalf_of_owner is not UNSET:
            field_dict["authorizedToSignOnBehalfOfOwner"] = authorized_to_sign_on_behalf_of_owner
        if authorized_trader is not UNSET:
            field_dict["authorizedTrader"] = authorized_trader
        if us_tax_resident is not UNSET:
            field_dict["usTaxResident"] = us_tax_resident
        if translated is not UNSET:
            field_dict["translated"] = translated
        if primary_trustee is not UNSET:
            field_dict["primaryTrustee"] = primary_trustee
        if nfa_registered is not UNSET:
            field_dict["nfaRegistered"] = nfa_registered
        if nfa_registration_number is not UNSET:
            field_dict["nfaRegistrationNumber"] = nfa_registration_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.employment_details import EmploymentDetails
        from ..models.form_crs import FormCRS
        from ..models.form_w8ben import FormW8BEN
        from ..models.form_w9 import FormW9
        from ..models.identification import Identification
        from ..models.individual_name import IndividualName
        from ..models.phone_info import PhoneInfo
        from ..models.prohibited_country_questionnaire_list import ProhibitedCountryQuestionnaireList
        from ..models.residence_address import ResidenceAddress
        from ..models.tax_residency import TaxResidency

        d = src_dict.copy()
        _name = d.pop("name", UNSET)
        name: Union[Unset, IndividualName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = IndividualName.from_dict(_name)

        _native_name = d.pop("nativeName", UNSET)
        native_name: Union[Unset, IndividualName]
        if isinstance(_native_name, Unset):
            native_name = UNSET
        else:
            native_name = IndividualName.from_dict(_native_name)

        _birth_name = d.pop("birthName", UNSET)
        birth_name: Union[Unset, IndividualName]
        if isinstance(_birth_name, Unset):
            birth_name = UNSET
        else:
            birth_name = IndividualName.from_dict(_birth_name)

        _mother_maiden_name = d.pop("motherMaidenName", UNSET)
        mother_maiden_name: Union[Unset, IndividualName]
        if isinstance(_mother_maiden_name, Unset):
            mother_maiden_name = UNSET
        else:
            mother_maiden_name = IndividualName.from_dict(_mother_maiden_name)

        date_of_birth = d.pop("dateOfBirth", UNSET)

        country_of_birth = d.pop("countryOfBirth", UNSET)

        city_of_birth = d.pop("cityOfBirth", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, TrusteeIndividualGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = TrusteeIndividualGender(_gender)

        _marital_status = d.pop("maritalStatus", UNSET)
        marital_status: Union[Unset, TrusteeIndividualMaritalStatus]
        if isinstance(_marital_status, Unset):
            marital_status = UNSET
        else:
            marital_status = TrusteeIndividualMaritalStatus(_marital_status)

        num_dependents = d.pop("numDependents", UNSET)

        _residence_address = d.pop("residenceAddress", UNSET)
        residence_address: Union[Unset, ResidenceAddress]
        if isinstance(_residence_address, Unset):
            residence_address = UNSET
        else:
            residence_address = ResidenceAddress.from_dict(_residence_address)

        _mailing_address = d.pop("mailingAddress", UNSET)
        mailing_address: Union[Unset, Address]
        if isinstance(_mailing_address, Unset):
            mailing_address = UNSET
        else:
            mailing_address = Address.from_dict(_mailing_address)

        phones = []
        _phones = d.pop("phones", UNSET)
        for phones_item_data in _phones or []:
            phones_item = PhoneInfo.from_dict(phones_item_data)

            phones.append(phones_item)

        email = d.pop("email", UNSET)

        _identification = d.pop("identification", UNSET)
        identification: Union[Unset, Identification]
        if isinstance(_identification, Unset):
            identification = UNSET
        else:
            identification = Identification.from_dict(_identification)

        employment_type = d.pop("employmentType", UNSET)

        _employment_details = d.pop("employmentDetails", UNSET)
        employment_details: Union[Unset, EmploymentDetails]
        if isinstance(_employment_details, Unset):
            employment_details = UNSET
        else:
            employment_details = EmploymentDetails.from_dict(_employment_details)

        employee_title = d.pop("employeeTitle", UNSET)

        tax_residencies = []
        _tax_residencies = d.pop("taxResidencies", UNSET)
        for tax_residencies_item_data in _tax_residencies or []:
            tax_residencies_item = TaxResidency.from_dict(tax_residencies_item_data)

            tax_residencies.append(tax_residencies_item)

        _w9 = d.pop("w9", UNSET)
        w9: Union[Unset, FormW9]
        if isinstance(_w9, Unset):
            w9 = UNSET
        else:
            w9 = FormW9.from_dict(_w9)

        _w_8_ben = d.pop("w8Ben", UNSET)
        w_8_ben: Union[Unset, FormW8BEN]
        if isinstance(_w_8_ben, Unset):
            w_8_ben = UNSET
        else:
            w_8_ben = FormW8BEN.from_dict(_w_8_ben)

        _crs = d.pop("crs", UNSET)
        crs: Union[Unset, FormCRS]
        if isinstance(_crs, Unset):
            crs = UNSET
        else:
            crs = FormCRS.from_dict(_crs)

        _prohibited_country_questionnaire = d.pop("prohibitedCountryQuestionnaire", UNSET)
        prohibited_country_questionnaire: Union[Unset, ProhibitedCountryQuestionnaireList]
        if isinstance(_prohibited_country_questionnaire, Unset):
            prohibited_country_questionnaire = UNSET
        else:
            prohibited_country_questionnaire = ProhibitedCountryQuestionnaireList.from_dict(
                _prohibited_country_questionnaire
            )

        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        user_id = d.pop("userId", UNSET)

        same_mail_address = d.pop("sameMailAddress", UNSET)

        authorized_to_sign_on_behalf_of_owner = d.pop("authorizedToSignOnBehalfOfOwner", UNSET)

        authorized_trader = d.pop("authorizedTrader", UNSET)

        us_tax_resident = d.pop("usTaxResident", UNSET)

        translated = d.pop("translated", UNSET)

        primary_trustee = d.pop("primaryTrustee", UNSET)

        nfa_registered = d.pop("nfaRegistered", UNSET)

        nfa_registration_number = d.pop("nfaRegistrationNumber", UNSET)

        trustee_individual = cls(
            name=name,
            native_name=native_name,
            birth_name=birth_name,
            mother_maiden_name=mother_maiden_name,
            date_of_birth=date_of_birth,
            country_of_birth=country_of_birth,
            city_of_birth=city_of_birth,
            gender=gender,
            marital_status=marital_status,
            num_dependents=num_dependents,
            residence_address=residence_address,
            mailing_address=mailing_address,
            phones=phones,
            email=email,
            identification=identification,
            employment_type=employment_type,
            employment_details=employment_details,
            employee_title=employee_title,
            tax_residencies=tax_residencies,
            w9=w9,
            w_8_ben=w_8_ben,
            crs=crs,
            prohibited_country_questionnaire=prohibited_country_questionnaire,
            id=id,
            external_id=external_id,
            user_id=user_id,
            same_mail_address=same_mail_address,
            authorized_to_sign_on_behalf_of_owner=authorized_to_sign_on_behalf_of_owner,
            authorized_trader=authorized_trader,
            us_tax_resident=us_tax_resident,
            translated=translated,
            primary_trustee=primary_trustee,
            nfa_registered=nfa_registered,
            nfa_registration_number=nfa_registration_number,
        )

        trustee_individual.additional_properties = d
        return trustee_individual

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
