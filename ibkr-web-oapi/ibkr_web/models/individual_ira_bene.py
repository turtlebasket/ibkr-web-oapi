from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_ira_bene_identification import IndividualIRABeneIdentification
    from ..models.individual_ira_bene_location import IndividualIRABeneLocation


T = TypeVar("T", bound="IndividualIRABene")


@_attrs_define
class IndividualIRABene:
    """
    Attributes:
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        date_of_birth (Union[Unset, str]):
        type (Union[Unset, str]):
        identification (Union[Unset, IndividualIRABeneIdentification]):
        location (Union[Unset, IndividualIRABeneLocation]):
        relationship (Union[Unset, str]):
        ownership (Union[Unset, int]):
        per_stripes (Union[Unset, str]):
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    identification: Union[Unset, "IndividualIRABeneIdentification"] = UNSET
    location: Union[Unset, "IndividualIRABeneLocation"] = UNSET
    relationship: Union[Unset, str] = UNSET
    ownership: Union[Unset, int] = UNSET
    per_stripes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        date_of_birth = self.date_of_birth

        type = self.type

        identification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identification, Unset):
            identification = self.identification.to_dict()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        relationship = self.relationship

        ownership = self.ownership

        per_stripes = self.per_stripes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if type is not UNSET:
            field_dict["type"] = type
        if identification is not UNSET:
            field_dict["identification"] = identification
        if location is not UNSET:
            field_dict["location"] = location
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if per_stripes is not UNSET:
            field_dict["perStripes"] = per_stripes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.individual_ira_bene_identification import IndividualIRABeneIdentification
        from ..models.individual_ira_bene_location import IndividualIRABeneLocation

        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        date_of_birth = d.pop("dateOfBirth", UNSET)

        type = d.pop("type", UNSET)

        _identification = d.pop("identification", UNSET)
        identification: Union[Unset, IndividualIRABeneIdentification]
        if isinstance(_identification, Unset):
            identification = UNSET
        else:
            identification = IndividualIRABeneIdentification.from_dict(_identification)

        _location = d.pop("location", UNSET)
        location: Union[Unset, IndividualIRABeneLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = IndividualIRABeneLocation.from_dict(_location)

        relationship = d.pop("relationship", UNSET)

        ownership = d.pop("ownership", UNSET)

        per_stripes = d.pop("perStripes", UNSET)

        individual_ira_bene = cls(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            type=type,
            identification=identification,
            location=location,
            relationship=relationship,
            ownership=ownership,
            per_stripes=per_stripes,
        )

        individual_ira_bene.additional_properties = d
        return individual_ira_bene

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
