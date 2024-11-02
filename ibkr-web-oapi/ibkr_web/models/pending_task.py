import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PendingTask")


@_attrs_define
class PendingTask:
    """
    Attributes:
        task_number (Union[Unset, int]):
        form_number (Union[Unset, int]):
        form_name (Union[Unset, str]):
        action (Union[Unset, str]):
        external_id (Union[Unset, str]):
        state (Union[Unset, str]):
        url (Union[Unset, str]):
        au_10_tix_created_date (Union[Unset, datetime.datetime]):
        au_10_tix_expiry_date (Union[Unset, datetime.datetime]):
        entity_id (Union[Unset, int]):
        required_for_approval (Union[Unset, bool]):
        documentreject_reason (Union[Unset, List[str]]):
        startdate (Union[Unset, datetime.datetime]):
        online_task (Union[Unset, bool]):
        required_for_trading (Union[Unset, bool]):
    """

    task_number: Union[Unset, int] = UNSET
    form_number: Union[Unset, int] = UNSET
    form_name: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    au_10_tix_created_date: Union[Unset, datetime.datetime] = UNSET
    au_10_tix_expiry_date: Union[Unset, datetime.datetime] = UNSET
    entity_id: Union[Unset, int] = UNSET
    required_for_approval: Union[Unset, bool] = UNSET
    documentreject_reason: Union[Unset, List[str]] = UNSET
    startdate: Union[Unset, datetime.datetime] = UNSET
    online_task: Union[Unset, bool] = UNSET
    required_for_trading: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_number = self.task_number

        form_number = self.form_number

        form_name = self.form_name

        action = self.action

        external_id = self.external_id

        state = self.state

        url = self.url

        au_10_tix_created_date: Union[Unset, str] = UNSET
        if not isinstance(self.au_10_tix_created_date, Unset):
            au_10_tix_created_date = self.au_10_tix_created_date.isoformat()

        au_10_tix_expiry_date: Union[Unset, str] = UNSET
        if not isinstance(self.au_10_tix_expiry_date, Unset):
            au_10_tix_expiry_date = self.au_10_tix_expiry_date.isoformat()

        entity_id = self.entity_id

        required_for_approval = self.required_for_approval

        documentreject_reason: Union[Unset, List[str]] = UNSET
        if not isinstance(self.documentreject_reason, Unset):
            documentreject_reason = self.documentreject_reason

        startdate: Union[Unset, str] = UNSET
        if not isinstance(self.startdate, Unset):
            startdate = self.startdate.isoformat()

        online_task = self.online_task

        required_for_trading = self.required_for_trading

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_number is not UNSET:
            field_dict["taskNumber"] = task_number
        if form_number is not UNSET:
            field_dict["formNumber"] = form_number
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if action is not UNSET:
            field_dict["action"] = action
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if state is not UNSET:
            field_dict["state"] = state
        if url is not UNSET:
            field_dict["url"] = url
        if au_10_tix_created_date is not UNSET:
            field_dict["au10tixCreatedDate"] = au_10_tix_created_date
        if au_10_tix_expiry_date is not UNSET:
            field_dict["au10tixExpiryDate"] = au_10_tix_expiry_date
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if required_for_approval is not UNSET:
            field_dict["requiredForApproval"] = required_for_approval
        if documentreject_reason is not UNSET:
            field_dict["documentrejectReason"] = documentreject_reason
        if startdate is not UNSET:
            field_dict["startdate"] = startdate
        if online_task is not UNSET:
            field_dict["onlineTask"] = online_task
        if required_for_trading is not UNSET:
            field_dict["requiredForTrading"] = required_for_trading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        task_number = d.pop("taskNumber", UNSET)

        form_number = d.pop("formNumber", UNSET)

        form_name = d.pop("formName", UNSET)

        action = d.pop("action", UNSET)

        external_id = d.pop("externalId", UNSET)

        state = d.pop("state", UNSET)

        url = d.pop("url", UNSET)

        _au_10_tix_created_date = d.pop("au10tixCreatedDate", UNSET)
        au_10_tix_created_date: Union[Unset, datetime.datetime]
        if isinstance(_au_10_tix_created_date, Unset):
            au_10_tix_created_date = UNSET
        else:
            au_10_tix_created_date = isoparse(_au_10_tix_created_date)

        _au_10_tix_expiry_date = d.pop("au10tixExpiryDate", UNSET)
        au_10_tix_expiry_date: Union[Unset, datetime.datetime]
        if isinstance(_au_10_tix_expiry_date, Unset):
            au_10_tix_expiry_date = UNSET
        else:
            au_10_tix_expiry_date = isoparse(_au_10_tix_expiry_date)

        entity_id = d.pop("entityId", UNSET)

        required_for_approval = d.pop("requiredForApproval", UNSET)

        documentreject_reason = cast(List[str], d.pop("documentrejectReason", UNSET))

        _startdate = d.pop("startdate", UNSET)
        startdate: Union[Unset, datetime.datetime]
        if isinstance(_startdate, Unset):
            startdate = UNSET
        else:
            startdate = isoparse(_startdate)

        online_task = d.pop("onlineTask", UNSET)

        required_for_trading = d.pop("requiredForTrading", UNSET)

        pending_task = cls(
            task_number=task_number,
            form_number=form_number,
            form_name=form_name,
            action=action,
            external_id=external_id,
            state=state,
            url=url,
            au_10_tix_created_date=au_10_tix_created_date,
            au_10_tix_expiry_date=au_10_tix_expiry_date,
            entity_id=entity_id,
            required_for_approval=required_for_approval,
            documentreject_reason=documentreject_reason,
            startdate=startdate,
            online_task=online_task,
            required_for_trading=required_for_trading,
        )

        pending_task.additional_properties = d
        return pending_task

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
