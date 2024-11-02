from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eligible_contract_participant_details import EligibleContractParticipantDetails


T = TypeVar("T", bound="EligibleContractParticipant")


@_attrs_define
class EligibleContractParticipant:
    """
    Attributes:
        eligible_contract_participant_details (Union[Unset, List['EligibleContractParticipantDetails']]):
        status (Union[Unset, bool]):
    """

    eligible_contract_participant_details: Union[Unset, List["EligibleContractParticipantDetails"]] = UNSET
    status: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eligible_contract_participant_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.eligible_contract_participant_details, Unset):
            eligible_contract_participant_details = []
            for eligible_contract_participant_details_item_data in self.eligible_contract_participant_details:
                eligible_contract_participant_details_item = eligible_contract_participant_details_item_data.to_dict()
                eligible_contract_participant_details.append(eligible_contract_participant_details_item)

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eligible_contract_participant_details is not UNSET:
            field_dict["eligibleContractParticipantDetails"] = eligible_contract_participant_details
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.eligible_contract_participant_details import EligibleContractParticipantDetails

        d = src_dict.copy()
        eligible_contract_participant_details = []
        _eligible_contract_participant_details = d.pop("eligibleContractParticipantDetails", UNSET)
        for eligible_contract_participant_details_item_data in _eligible_contract_participant_details or []:
            eligible_contract_participant_details_item = EligibleContractParticipantDetails.from_dict(
                eligible_contract_participant_details_item_data
            )

            eligible_contract_participant_details.append(eligible_contract_participant_details_item)

        status = d.pop("status", UNSET)

        eligible_contract_participant = cls(
            eligible_contract_participant_details=eligible_contract_participant_details,
            status=status,
        )

        eligible_contract_participant.additional_properties = d
        return eligible_contract_participant

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
