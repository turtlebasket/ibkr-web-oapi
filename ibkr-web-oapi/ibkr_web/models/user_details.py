from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_of_birth import DateOfBirth
    from ..models.identification import Identification
    from ..models.mailing_address import MailingAddress
    from ..models.name import Name
    from ..models.residence import Residence
    from ..models.tax_residency import TaxResidency


T = TypeVar("T", bound="UserDetails")


@_attrs_define
class UserDetails:
    """
    Attributes:
        name (Union[Unset, Name]):
        email (Union[Unset, str]):
        residence_address (Union[Unset, Residence]):
        mailing_address (Union[Unset, MailingAddress]):
        identification (Union[Unset, Identification]): Identification information of the associated person. Example:
            {'citizenship': 'AUS', 'driversLicense': '989444798', 'issuingCountry': 'AUS', 'hasExpirationDate': True,
            'expirationDate': '2029-03-22', 'rta': '9999999', 'issuingState': 'AU-QLD'}.
        tax_residencies (Union[Unset, List['TaxResidency']]):
        date_of_birth (Union[Unset, DateOfBirth]):
        same_mail_address (Union[Unset, bool]):
        external_id (Union[Unset, str]):
    """

    name: Union[Unset, "Name"] = UNSET
    email: Union[Unset, str] = UNSET
    residence_address: Union[Unset, "Residence"] = UNSET
    mailing_address: Union[Unset, "MailingAddress"] = UNSET
    identification: Union[Unset, "Identification"] = UNSET
    tax_residencies: Union[Unset, List["TaxResidency"]] = UNSET
    date_of_birth: Union[Unset, "DateOfBirth"] = UNSET
    same_mail_address: Union[Unset, bool] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        email = self.email

        residence_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.residence_address, Unset):
            residence_address = self.residence_address.to_dict()

        mailing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mailing_address, Unset):
            mailing_address = self.mailing_address.to_dict()

        identification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identification, Unset):
            identification = self.identification.to_dict()

        tax_residencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_residencies, Unset):
            tax_residencies = []
            for tax_residencies_item_data in self.tax_residencies:
                tax_residencies_item = tax_residencies_item_data.to_dict()
                tax_residencies.append(tax_residencies_item)

        date_of_birth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.to_dict()

        same_mail_address = self.same_mail_address

        external_id = self.external_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if residence_address is not UNSET:
            field_dict["residenceAddress"] = residence_address
        if mailing_address is not UNSET:
            field_dict["mailingAddress"] = mailing_address
        if identification is not UNSET:
            field_dict["identification"] = identification
        if tax_residencies is not UNSET:
            field_dict["taxResidencies"] = tax_residencies
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if same_mail_address is not UNSET:
            field_dict["sameMailAddress"] = same_mail_address
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_of_birth import DateOfBirth
        from ..models.identification import Identification
        from ..models.mailing_address import MailingAddress
        from ..models.name import Name
        from ..models.residence import Residence
        from ..models.tax_residency import TaxResidency

        d = src_dict.copy()
        _name = d.pop("name", UNSET)
        name: Union[Unset, Name]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = Name.from_dict(_name)

        email = d.pop("email", UNSET)

        _residence_address = d.pop("residenceAddress", UNSET)
        residence_address: Union[Unset, Residence]
        if isinstance(_residence_address, Unset):
            residence_address = UNSET
        else:
            residence_address = Residence.from_dict(_residence_address)

        _mailing_address = d.pop("mailingAddress", UNSET)
        mailing_address: Union[Unset, MailingAddress]
        if isinstance(_mailing_address, Unset):
            mailing_address = UNSET
        else:
            mailing_address = MailingAddress.from_dict(_mailing_address)

        _identification = d.pop("identification", UNSET)
        identification: Union[Unset, Identification]
        if isinstance(_identification, Unset):
            identification = UNSET
        else:
            identification = Identification.from_dict(_identification)

        tax_residencies = []
        _tax_residencies = d.pop("taxResidencies", UNSET)
        for tax_residencies_item_data in _tax_residencies or []:
            tax_residencies_item = TaxResidency.from_dict(tax_residencies_item_data)

            tax_residencies.append(tax_residencies_item)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, DateOfBirth]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = DateOfBirth.from_dict(_date_of_birth)

        same_mail_address = d.pop("sameMailAddress", UNSET)

        external_id = d.pop("externalId", UNSET)

        user_details = cls(
            name=name,
            email=email,
            residence_address=residence_address,
            mailing_address=mailing_address,
            identification=identification,
            tax_residencies=tax_residencies,
            date_of_birth=date_of_birth,
            same_mail_address=same_mail_address,
            external_id=external_id,
        )

        user_details.additional_properties = d
        return user_details

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
