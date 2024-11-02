from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="AddCLPCapability")


@_attrs_define
class AddCLPCapability:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        documents (Union[Unset, List['Document']]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    documents: Union[Unset, List["Document"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document import Document

        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        add_clp_capability = cls(
            reference_account_id=reference_account_id,
            documents=documents,
        )

        add_clp_capability.additional_properties = d
        return add_clp_capability

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
