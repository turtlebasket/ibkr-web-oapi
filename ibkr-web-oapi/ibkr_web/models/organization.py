from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_identification import OrganizationIdentification
    from ..models.regulatory_information import RegulatoryInformation


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        identification (Union[Unset, OrganizationIdentification]):
        regulatory_information (Union[Unset, RegulatoryInformation]):
    """

    identification: Union[Unset, "OrganizationIdentification"] = UNSET
    regulatory_information: Union[Unset, "RegulatoryInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identification, Unset):
            identification = self.identification.to_dict()

        regulatory_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regulatory_information, Unset):
            regulatory_information = self.regulatory_information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identification is not UNSET:
            field_dict["identification"] = identification
        if regulatory_information is not UNSET:
            field_dict["regulatoryInformation"] = regulatory_information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_identification import OrganizationIdentification
        from ..models.regulatory_information import RegulatoryInformation

        d = src_dict.copy()
        _identification = d.pop("identification", UNSET)
        identification: Union[Unset, OrganizationIdentification]
        if isinstance(_identification, Unset):
            identification = UNSET
        else:
            identification = OrganizationIdentification.from_dict(_identification)

        _regulatory_information = d.pop("regulatoryInformation", UNSET)
        regulatory_information: Union[Unset, RegulatoryInformation]
        if isinstance(_regulatory_information, Unset):
            regulatory_information = UNSET
        else:
            regulatory_information = RegulatoryInformation.from_dict(_regulatory_information)

        organization = cls(
            identification=identification,
            regulatory_information=regulatory_information,
        )

        organization.additional_properties = d
        return organization

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
