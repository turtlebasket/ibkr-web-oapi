import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.identification_card_color import IdentificationCardColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="Identification")


@_attrs_define
class Identification:
    r"""Identification information of the associated person.

    Example:
        {'citizenship': 'AUS', 'driversLicense': '989444798', 'issuingCountry': 'AUS', 'hasExpirationDate': True,
            'expirationDate': '2029-03-22', 'rta': '9999999', 'issuingState': 'AU-QLD'}

    Attributes:
        citizenship (Union[Unset, str]): Citizenship of the applicant.<br>If citizenship, citizenship2, OR citizenship3
            is classified as a ‘Prohibited Country', THEN ProhibitedCountryQuestionnaire is required.<br>List of Prohibited
            Countries an be obtained using /getEnumerations<br>Preferred id document by IssuingCountry
        citizenship2 (Union[Unset, str]): If the applicant has multiple citizenship, provide the additional citizenship
            of the applicant.<br>If citizenship, citizenship2, OR citizenship3 is classified as a ‘Prohibited Country', THEN
            ProhibitedCountryQuestionnaire is required.<br>List of Prohibited Countries an be obtained using
            /getEnumerations<br>Preferred id document by IssuingCountry
        citizenship3 (Union[Unset, str]): If the applicant has multiple citizenship, provide the additional citizenship
            of the applicant.<br>If citizenship, citizenship2, OR citizenship3 is classified as a ‘Prohibited Country', THEN
            ProhibitedCountryQuestionnaire is required.<br>List of Prohibited Countries an be obtained using
            /getEnumerations<br>Preferred id document by IssuingCountry
        ssn (Union[Unset, str]): Social security number, required for US Residents and citizens.
        sin (Union[Unset, str]): Social insurance number, required for Canada Residents and citizens.
        drivers_license (Union[Unset, str]): Drivers License<br>Pattern for AUS: ^.{0,64}$<br>Pattern for NZL:
            ^[A-Z]{2}\d{6}$
        passport (Union[Unset, str]): Passport
        alien_card (Union[Unset, str]): Alien Card
        medicare_card (Union[Unset, str]): Only applicable for Australia residents.
        card_color (Union[Unset, IdentificationCardColor]): Required if MedicareCard is provided.
        medicare_reference (Union[Unset, str]): Required if MedicareCard is provided.
        national_card (Union[Unset, str]): National Identification Card<br>Pattern by Country-<br> ARG: ^\d{8}$<br>AUS:
            ^(\d{8}|\d{9})$<br>BRA: ^\d{11}$<br>CHN: ^\d{17}(\d|X)$<br>DNK: ^\d{10}$<br>ESP: ^\d{8}[A-Z]$<br>FRA:
            ^\d{15}$<br>FRA: ^\d{4}([A-Z]|\d){3}\d{5}$<br>ITA: ^([A-Z]{2}\d{7}|\d{7}[A-Z]{2}|[A-Z]{2}\d{5}[A-Z]{2})$<br>ITA:
            ^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$<br>MEX: ^[A-Z]{4}\d{6}[A-Z]{6}\d{2}$<br>MYZ: ^\d{12}$<br>RUS:
            ^\d{10}$<br>RUS: ^\d{9}$<br>SGP: ^[A-Z]\d{7}[A-Z]$<br>SWE: ^(\d{10}|\d{12})$<br>TUR: ^\d{11}$<br>ZAF: ^\d{13}$
        issuing_country (Union[Unset, str]): Issuing country of the ID document.
        issuing_state (Union[Unset, str]): Issuing state of the ID document.
        rta (Union[Unset, str]): Only applicable IF ID_Type=DriversLicense AND IssuingCountry=AUS
        legal_residence_country (Union[Unset, str]):
        legal_residence_state (Union[Unset, str]):
        educational_qualification (Union[Unset, str]):
        fathers_name (Union[Unset, str]):
        green_card (Union[Unset, bool]):
        pan_number (Union[Unset, str]): India PanCard, required for India Residents and citizens.
        tax_id (Union[Unset, str]): Tax ID TIN within <TaxResidencies>foreign_tax_id within <W8Ben>
        proof_of_age_card (Union[Unset, str]):
        expire (Union[Unset, bool]): Indicate IF ID document has an ExpirationDate.
        expiration_date (Union[Unset, datetime.date]): Provide expiration date of the ID document. Cannot be past date.
    """

    citizenship: Union[Unset, str] = UNSET
    citizenship2: Union[Unset, str] = UNSET
    citizenship3: Union[Unset, str] = UNSET
    ssn: Union[Unset, str] = UNSET
    sin: Union[Unset, str] = UNSET
    drivers_license: Union[Unset, str] = UNSET
    passport: Union[Unset, str] = UNSET
    alien_card: Union[Unset, str] = UNSET
    medicare_card: Union[Unset, str] = UNSET
    card_color: Union[Unset, IdentificationCardColor] = UNSET
    medicare_reference: Union[Unset, str] = UNSET
    national_card: Union[Unset, str] = UNSET
    issuing_country: Union[Unset, str] = UNSET
    issuing_state: Union[Unset, str] = UNSET
    rta: Union[Unset, str] = UNSET
    legal_residence_country: Union[Unset, str] = UNSET
    legal_residence_state: Union[Unset, str] = UNSET
    educational_qualification: Union[Unset, str] = UNSET
    fathers_name: Union[Unset, str] = UNSET
    green_card: Union[Unset, bool] = UNSET
    pan_number: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    proof_of_age_card: Union[Unset, str] = UNSET
    expire: Union[Unset, bool] = UNSET
    expiration_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        citizenship = self.citizenship

        citizenship2 = self.citizenship2

        citizenship3 = self.citizenship3

        ssn = self.ssn

        sin = self.sin

        drivers_license = self.drivers_license

        passport = self.passport

        alien_card = self.alien_card

        medicare_card = self.medicare_card

        card_color: Union[Unset, str] = UNSET
        if not isinstance(self.card_color, Unset):
            card_color = self.card_color.value

        medicare_reference = self.medicare_reference

        national_card = self.national_card

        issuing_country = self.issuing_country

        issuing_state = self.issuing_state

        rta = self.rta

        legal_residence_country = self.legal_residence_country

        legal_residence_state = self.legal_residence_state

        educational_qualification = self.educational_qualification

        fathers_name = self.fathers_name

        green_card = self.green_card

        pan_number = self.pan_number

        tax_id = self.tax_id

        proof_of_age_card = self.proof_of_age_card

        expire = self.expire

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if citizenship is not UNSET:
            field_dict["citizenship"] = citizenship
        if citizenship2 is not UNSET:
            field_dict["citizenship2"] = citizenship2
        if citizenship3 is not UNSET:
            field_dict["citizenship3"] = citizenship3
        if ssn is not UNSET:
            field_dict["ssn"] = ssn
        if sin is not UNSET:
            field_dict["sin"] = sin
        if drivers_license is not UNSET:
            field_dict["driversLicense"] = drivers_license
        if passport is not UNSET:
            field_dict["passport"] = passport
        if alien_card is not UNSET:
            field_dict["alienCard"] = alien_card
        if medicare_card is not UNSET:
            field_dict["medicareCard"] = medicare_card
        if card_color is not UNSET:
            field_dict["cardColor"] = card_color
        if medicare_reference is not UNSET:
            field_dict["medicareReference"] = medicare_reference
        if national_card is not UNSET:
            field_dict["nationalCard"] = national_card
        if issuing_country is not UNSET:
            field_dict["issuingCountry"] = issuing_country
        if issuing_state is not UNSET:
            field_dict["issuingState"] = issuing_state
        if rta is not UNSET:
            field_dict["rta"] = rta
        if legal_residence_country is not UNSET:
            field_dict["legalResidenceCountry"] = legal_residence_country
        if legal_residence_state is not UNSET:
            field_dict["legalResidenceState"] = legal_residence_state
        if educational_qualification is not UNSET:
            field_dict["educationalQualification"] = educational_qualification
        if fathers_name is not UNSET:
            field_dict["fathersName"] = fathers_name
        if green_card is not UNSET:
            field_dict["greenCard"] = green_card
        if pan_number is not UNSET:
            field_dict["panNumber"] = pan_number
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if proof_of_age_card is not UNSET:
            field_dict["proofOfAgeCard"] = proof_of_age_card
        if expire is not UNSET:
            field_dict["expire"] = expire
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        citizenship = d.pop("citizenship", UNSET)

        citizenship2 = d.pop("citizenship2", UNSET)

        citizenship3 = d.pop("citizenship3", UNSET)

        ssn = d.pop("ssn", UNSET)

        sin = d.pop("sin", UNSET)

        drivers_license = d.pop("driversLicense", UNSET)

        passport = d.pop("passport", UNSET)

        alien_card = d.pop("alienCard", UNSET)

        medicare_card = d.pop("medicareCard", UNSET)

        _card_color = d.pop("cardColor", UNSET)
        card_color: Union[Unset, IdentificationCardColor]
        if isinstance(_card_color, Unset):
            card_color = UNSET
        else:
            card_color = IdentificationCardColor(_card_color)

        medicare_reference = d.pop("medicareReference", UNSET)

        national_card = d.pop("nationalCard", UNSET)

        issuing_country = d.pop("issuingCountry", UNSET)

        issuing_state = d.pop("issuingState", UNSET)

        rta = d.pop("rta", UNSET)

        legal_residence_country = d.pop("legalResidenceCountry", UNSET)

        legal_residence_state = d.pop("legalResidenceState", UNSET)

        educational_qualification = d.pop("educationalQualification", UNSET)

        fathers_name = d.pop("fathersName", UNSET)

        green_card = d.pop("greenCard", UNSET)

        pan_number = d.pop("panNumber", UNSET)

        tax_id = d.pop("taxId", UNSET)

        proof_of_age_card = d.pop("proofOfAgeCard", UNSET)

        expire = d.pop("expire", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.date]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date).date()

        identification = cls(
            citizenship=citizenship,
            citizenship2=citizenship2,
            citizenship3=citizenship3,
            ssn=ssn,
            sin=sin,
            drivers_license=drivers_license,
            passport=passport,
            alien_card=alien_card,
            medicare_card=medicare_card,
            card_color=card_color,
            medicare_reference=medicare_reference,
            national_card=national_card,
            issuing_country=issuing_country,
            issuing_state=issuing_state,
            rta=rta,
            legal_residence_country=legal_residence_country,
            legal_residence_state=legal_residence_state,
            educational_qualification=educational_qualification,
            fathers_name=fathers_name,
            green_card=green_card,
            pan_number=pan_number,
            tax_id=tax_id,
            proof_of_age_card=proof_of_age_card,
            expire=expire,
            expiration_date=expiration_date,
        )

        identification.additional_properties = d
        return identification

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
