from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_submission import DocumentSubmission


T = TypeVar("T", bound="ChangeMarginType")


@_attrs_define
class ChangeMarginType:
    """
    Attributes:
        document_submission (Union[Unset, DocumentSubmission]):
        reference_account_id (Union[Unset, str]):
        new_margin (Union[Unset, str]):
    """

    document_submission: Union[Unset, "DocumentSubmission"] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    new_margin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_submission: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document_submission, Unset):
            document_submission = self.document_submission.to_dict()

        reference_account_id = self.reference_account_id

        new_margin = self.new_margin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_submission is not UNSET:
            field_dict["documentSubmission"] = document_submission
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if new_margin is not UNSET:
            field_dict["newMargin"] = new_margin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_submission import DocumentSubmission

        d = src_dict.copy()
        _document_submission = d.pop("documentSubmission", UNSET)
        document_submission: Union[Unset, DocumentSubmission]
        if isinstance(_document_submission, Unset):
            document_submission = UNSET
        else:
            document_submission = DocumentSubmission.from_dict(_document_submission)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        new_margin = d.pop("newMargin", UNSET)

        change_margin_type = cls(
            document_submission=document_submission,
            reference_account_id=reference_account_id,
            new_margin=new_margin,
        )

        change_margin_type.additional_properties = d
        return change_margin_type

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
