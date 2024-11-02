import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.document_document_type import DocumentDocumentType
from ..models.document_proof_of_address_type import DocumentProofOfAddressType
from ..models.document_proof_of_identity_type import DocumentProofOfIdentityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_file_type import AttachedFileType


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """
    Attributes:
        signed_by (Union[Unset, List[str]]):
        attached_file (Union[Unset, AttachedFileType]):
        form_number (Union[Unset, int]):
        valid_address (Union[Unset, bool]):
        exec_login_timestamp (Union[Unset, int]):
        exec_timestamp (Union[Unset, int]):
        document_type (Union[Unset, DocumentDocumentType]):
        signature (Union[Unset, str]):
        external_account_id (Union[Unset, str]):
        external_individual_id (Union[Unset, str]):
        proof_of_identity_type (Union[Unset, DocumentProofOfIdentityType]):
        expiration_date (Union[Unset, datetime.date]):
        proof_of_address_type (Union[Unset, DocumentProofOfAddressType]):
    """

    signed_by: Union[Unset, List[str]] = UNSET
    attached_file: Union[Unset, "AttachedFileType"] = UNSET
    form_number: Union[Unset, int] = UNSET
    valid_address: Union[Unset, bool] = UNSET
    exec_login_timestamp: Union[Unset, int] = UNSET
    exec_timestamp: Union[Unset, int] = UNSET
    document_type: Union[Unset, DocumentDocumentType] = UNSET
    signature: Union[Unset, str] = UNSET
    external_account_id: Union[Unset, str] = UNSET
    external_individual_id: Union[Unset, str] = UNSET
    proof_of_identity_type: Union[Unset, DocumentProofOfIdentityType] = UNSET
    expiration_date: Union[Unset, datetime.date] = UNSET
    proof_of_address_type: Union[Unset, DocumentProofOfAddressType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signed_by: Union[Unset, List[str]] = UNSET
        if not isinstance(self.signed_by, Unset):
            signed_by = self.signed_by

        attached_file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attached_file, Unset):
            attached_file = self.attached_file.to_dict()

        form_number = self.form_number

        valid_address = self.valid_address

        exec_login_timestamp = self.exec_login_timestamp

        exec_timestamp = self.exec_timestamp

        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type.value

        signature = self.signature

        external_account_id = self.external_account_id

        external_individual_id = self.external_individual_id

        proof_of_identity_type: Union[Unset, str] = UNSET
        if not isinstance(self.proof_of_identity_type, Unset):
            proof_of_identity_type = self.proof_of_identity_type.value

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        proof_of_address_type: Union[Unset, str] = UNSET
        if not isinstance(self.proof_of_address_type, Unset):
            proof_of_address_type = self.proof_of_address_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signed_by is not UNSET:
            field_dict["signedBy"] = signed_by
        if attached_file is not UNSET:
            field_dict["attachedFile"] = attached_file
        if form_number is not UNSET:
            field_dict["formNumber"] = form_number
        if valid_address is not UNSET:
            field_dict["validAddress"] = valid_address
        if exec_login_timestamp is not UNSET:
            field_dict["execLoginTimestamp"] = exec_login_timestamp
        if exec_timestamp is not UNSET:
            field_dict["execTimestamp"] = exec_timestamp
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if signature is not UNSET:
            field_dict["signature"] = signature
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if external_individual_id is not UNSET:
            field_dict["externalIndividualId"] = external_individual_id
        if proof_of_identity_type is not UNSET:
            field_dict["proofOfIdentityType"] = proof_of_identity_type
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if proof_of_address_type is not UNSET:
            field_dict["proofOfAddressType"] = proof_of_address_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attached_file_type import AttachedFileType

        d = src_dict.copy()
        signed_by = cast(List[str], d.pop("signedBy", UNSET))

        _attached_file = d.pop("attachedFile", UNSET)
        attached_file: Union[Unset, AttachedFileType]
        if isinstance(_attached_file, Unset):
            attached_file = UNSET
        else:
            attached_file = AttachedFileType.from_dict(_attached_file)

        form_number = d.pop("formNumber", UNSET)

        valid_address = d.pop("validAddress", UNSET)

        exec_login_timestamp = d.pop("execLoginTimestamp", UNSET)

        exec_timestamp = d.pop("execTimestamp", UNSET)

        _document_type = d.pop("documentType", UNSET)
        document_type: Union[Unset, DocumentDocumentType]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = DocumentDocumentType(_document_type)

        signature = d.pop("signature", UNSET)

        external_account_id = d.pop("externalAccountId", UNSET)

        external_individual_id = d.pop("externalIndividualId", UNSET)

        _proof_of_identity_type = d.pop("proofOfIdentityType", UNSET)
        proof_of_identity_type: Union[Unset, DocumentProofOfIdentityType]
        if isinstance(_proof_of_identity_type, Unset):
            proof_of_identity_type = UNSET
        else:
            proof_of_identity_type = DocumentProofOfIdentityType(_proof_of_identity_type)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.date]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date).date()

        _proof_of_address_type = d.pop("proofOfAddressType", UNSET)
        proof_of_address_type: Union[Unset, DocumentProofOfAddressType]
        if isinstance(_proof_of_address_type, Unset):
            proof_of_address_type = UNSET
        else:
            proof_of_address_type = DocumentProofOfAddressType(_proof_of_address_type)

        document = cls(
            signed_by=signed_by,
            attached_file=attached_file,
            form_number=form_number,
            valid_address=valid_address,
            exec_login_timestamp=exec_login_timestamp,
            exec_timestamp=exec_timestamp,
            document_type=document_type,
            signature=signature,
            external_account_id=external_account_id,
            external_individual_id=external_individual_id,
            proof_of_identity_type=proof_of_identity_type,
            expiration_date=expiration_date,
            proof_of_address_type=proof_of_address_type,
        )

        document.additional_properties = d
        return document

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
