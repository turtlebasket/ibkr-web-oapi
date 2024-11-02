import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistrationTask")


@_attrs_define
class RegistrationTask:
    """
    Attributes:
        external_id (Union[Unset, str]):
        form_name (Union[Unset, str]):
        action (Union[Unset, str]):
        is_required_for_approval (Union[Unset, bool]):
        is_completed (Union[Unset, bool]):
        date_completed (Union[Unset, datetime.datetime]):
        state (Union[Unset, str]):
    """

    external_id: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    is_required_for_approval: Union[Unset, bool] = UNSET
    is_completed: Union[Unset, bool] = UNSET
    date_completed: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id

        form_name = self.form_name

        action = self.action

        is_required_for_approval = self.is_required_for_approval

        is_completed = self.is_completed

        date_completed: Union[Unset, str] = UNSET
        if not isinstance(self.date_completed, Unset):
            date_completed = self.date_completed.isoformat()

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if action is not UNSET:
            field_dict["action"] = action
        if is_required_for_approval is not UNSET:
            field_dict["isRequiredForApproval"] = is_required_for_approval
        if is_completed is not UNSET:
            field_dict["isCompleted"] = is_completed
        if date_completed is not UNSET:
            field_dict["dateCompleted"] = date_completed
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_id = d.pop("externalId", UNSET)

        form_name = d.pop("formName", UNSET)

        action = d.pop("action", UNSET)

        is_required_for_approval = d.pop("isRequiredForApproval", UNSET)

        is_completed = d.pop("isCompleted", UNSET)

        _date_completed = d.pop("dateCompleted", UNSET)
        date_completed: Union[Unset, datetime.datetime]
        if isinstance(_date_completed, Unset):
            date_completed = UNSET
        else:
            date_completed = isoparse(_date_completed)

        state = d.pop("state", UNSET)

        registration_task = cls(
            external_id=external_id,
            form_name=form_name,
            action=action,
            is_required_for_approval=is_required_for_approval,
            is_completed=is_completed,
            date_completed=date_completed,
            state=state,
        )

        registration_task.additional_properties = d
        return registration_task

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
