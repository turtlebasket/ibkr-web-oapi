from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_submission import DocumentSubmission
    from ..models.trading_permission import TradingPermission


T = TypeVar("T", bound="AddTradingPermissions")


@_attrs_define
class AddTradingPermissions:
    """
    Attributes:
        trading_permissions (Union[Unset, List['TradingPermission']]):
        document_submission (Union[Unset, DocumentSubmission]):
        reference_account_id (Union[Unset, str]):
    """

    trading_permissions: Union[Unset, List["TradingPermission"]] = UNSET
    document_submission: Union[Unset, "DocumentSubmission"] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trading_permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trading_permissions, Unset):
            trading_permissions = []
            for trading_permissions_item_data in self.trading_permissions:
                trading_permissions_item = trading_permissions_item_data.to_dict()
                trading_permissions.append(trading_permissions_item)

        document_submission: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document_submission, Unset):
            document_submission = self.document_submission.to_dict()

        reference_account_id = self.reference_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trading_permissions is not UNSET:
            field_dict["tradingPermissions"] = trading_permissions
        if document_submission is not UNSET:
            field_dict["documentSubmission"] = document_submission
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_submission import DocumentSubmission
        from ..models.trading_permission import TradingPermission

        d = src_dict.copy()
        trading_permissions = []
        _trading_permissions = d.pop("tradingPermissions", UNSET)
        for trading_permissions_item_data in _trading_permissions or []:
            trading_permissions_item = TradingPermission.from_dict(trading_permissions_item_data)

            trading_permissions.append(trading_permissions_item)

        _document_submission = d.pop("documentSubmission", UNSET)
        document_submission: Union[Unset, DocumentSubmission]
        if isinstance(_document_submission, Unset):
            document_submission = UNSET
        else:
            document_submission = DocumentSubmission.from_dict(_document_submission)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        add_trading_permissions = cls(
            trading_permissions=trading_permissions,
            document_submission=document_submission,
            reference_account_id=reference_account_id,
        )

        add_trading_permissions.additional_properties = d
        return add_trading_permissions

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
