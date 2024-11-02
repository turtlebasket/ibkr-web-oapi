from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_regulator_type import ORGRegulatorType
    from ..models.public_company_info_type import PublicCompanyInfoType


T = TypeVar("T", bound="ORGRegulatoryInfoType")


@_attrs_define
class ORGRegulatoryInfoType:
    """
    Attributes:
        public_company_info (Union[Unset, PublicCompanyInfoType]):
        org_regulators (Union[Unset, List['ORGRegulatorType']]):
        regulated (Union[Unset, bool]):
        public (Union[Unset, bool]):
    """

    public_company_info: Union[Unset, "PublicCompanyInfoType"] = UNSET
    org_regulators: Union[Unset, List["ORGRegulatorType"]] = UNSET
    regulated: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public_company_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_company_info, Unset):
            public_company_info = self.public_company_info.to_dict()

        org_regulators: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.org_regulators, Unset):
            org_regulators = []
            for org_regulators_item_data in self.org_regulators:
                org_regulators_item = org_regulators_item_data.to_dict()
                org_regulators.append(org_regulators_item)

        regulated = self.regulated

        public = self.public

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_company_info is not UNSET:
            field_dict["publicCompanyInfo"] = public_company_info
        if org_regulators is not UNSET:
            field_dict["orgRegulators"] = org_regulators
        if regulated is not UNSET:
            field_dict["regulated"] = regulated
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_regulator_type import ORGRegulatorType
        from ..models.public_company_info_type import PublicCompanyInfoType

        d = src_dict.copy()
        _public_company_info = d.pop("publicCompanyInfo", UNSET)
        public_company_info: Union[Unset, PublicCompanyInfoType]
        if isinstance(_public_company_info, Unset):
            public_company_info = UNSET
        else:
            public_company_info = PublicCompanyInfoType.from_dict(_public_company_info)

        org_regulators = []
        _org_regulators = d.pop("orgRegulators", UNSET)
        for org_regulators_item_data in _org_regulators or []:
            org_regulators_item = ORGRegulatorType.from_dict(org_regulators_item_data)

            org_regulators.append(org_regulators_item)

        regulated = d.pop("regulated", UNSET)

        public = d.pop("public", UNSET)

        org_regulatory_info_type = cls(
            public_company_info=public_company_info,
            org_regulators=org_regulators,
            regulated=regulated,
            public=public,
        )

        org_regulatory_info_type.additional_properties = d
        return org_regulatory_info_type

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
