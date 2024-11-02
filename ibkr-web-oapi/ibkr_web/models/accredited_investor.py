from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eligible_contract_participant import EligibleContractParticipant
    from ..models.qualified_purchaser import QualifiedPurchaser


T = TypeVar("T", bound="AccreditedInvestor")


@_attrs_define
class AccreditedInvestor:
    """
    Attributes:
        qualified_purchaser (Union[Unset, QualifiedPurchaser]):
        eligible_contract_participant (Union[Unset, EligibleContractParticipant]):
        signed_by (Union[Unset, List[str]]):
        reference_account_id (Union[Unset, str]):
        status (Union[Unset, bool]):
        signature (Union[Unset, str]):
    """

    qualified_purchaser: Union[Unset, "QualifiedPurchaser"] = UNSET
    eligible_contract_participant: Union[Unset, "EligibleContractParticipant"] = UNSET
    signed_by: Union[Unset, List[str]] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    status: Union[Unset, bool] = UNSET
    signature: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        qualified_purchaser: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.qualified_purchaser, Unset):
            qualified_purchaser = self.qualified_purchaser.to_dict()

        eligible_contract_participant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.eligible_contract_participant, Unset):
            eligible_contract_participant = self.eligible_contract_participant.to_dict()

        signed_by: Union[Unset, List[str]] = UNSET
        if not isinstance(self.signed_by, Unset):
            signed_by = self.signed_by

        reference_account_id = self.reference_account_id

        status = self.status

        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qualified_purchaser is not UNSET:
            field_dict["qualifiedPurchaser"] = qualified_purchaser
        if eligible_contract_participant is not UNSET:
            field_dict["eligibleContractParticipant"] = eligible_contract_participant
        if signed_by is not UNSET:
            field_dict["signedBy"] = signed_by
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if status is not UNSET:
            field_dict["status"] = status
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.eligible_contract_participant import EligibleContractParticipant
        from ..models.qualified_purchaser import QualifiedPurchaser

        d = src_dict.copy()
        _qualified_purchaser = d.pop("qualifiedPurchaser", UNSET)
        qualified_purchaser: Union[Unset, QualifiedPurchaser]
        if isinstance(_qualified_purchaser, Unset):
            qualified_purchaser = UNSET
        else:
            qualified_purchaser = QualifiedPurchaser.from_dict(_qualified_purchaser)

        _eligible_contract_participant = d.pop("eligibleContractParticipant", UNSET)
        eligible_contract_participant: Union[Unset, EligibleContractParticipant]
        if isinstance(_eligible_contract_participant, Unset):
            eligible_contract_participant = UNSET
        else:
            eligible_contract_participant = EligibleContractParticipant.from_dict(_eligible_contract_participant)

        signed_by = cast(List[str], d.pop("signedBy", UNSET))

        reference_account_id = d.pop("referenceAccountId", UNSET)

        status = d.pop("status", UNSET)

        signature = d.pop("signature", UNSET)

        accredited_investor = cls(
            qualified_purchaser=qualified_purchaser,
            eligible_contract_participant=eligible_contract_participant,
            signed_by=signed_by,
            reference_account_id=reference_account_id,
            status=status,
            signature=signature,
        )

        accredited_investor.additional_properties = d
        return accredited_investor

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
