from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_information import FinancialInformation


T = TypeVar("T", bound="ChangeFinancialInformation")


@_attrs_define
class ChangeFinancialInformation:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        reference_user_name (Union[Unset, str]):
        new_financial_information (Union[Unset, FinancialInformation]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    reference_user_name: Union[Unset, str] = UNSET
    new_financial_information: Union[Unset, "FinancialInformation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        reference_user_name = self.reference_user_name

        new_financial_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_financial_information, Unset):
            new_financial_information = self.new_financial_information.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if reference_user_name is not UNSET:
            field_dict["referenceUserName"] = reference_user_name
        if new_financial_information is not UNSET:
            field_dict["newFinancialInformation"] = new_financial_information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_information import FinancialInformation

        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        reference_user_name = d.pop("referenceUserName", UNSET)

        _new_financial_information = d.pop("newFinancialInformation", UNSET)
        new_financial_information: Union[Unset, FinancialInformation]
        if isinstance(_new_financial_information, Unset):
            new_financial_information = UNSET
        else:
            new_financial_information = FinancialInformation.from_dict(_new_financial_information)

        change_financial_information = cls(
            reference_account_id=reference_account_id,
            reference_user_name=reference_user_name,
            new_financial_information=new_financial_information,
        )

        change_financial_information.additional_properties = d
        return change_financial_information

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
