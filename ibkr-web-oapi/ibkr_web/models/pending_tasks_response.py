from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response import ErrorResponse
    from ..models.pending_task import PendingTask


T = TypeVar("T", bound="PendingTasksResponse")


@_attrs_define
class PendingTasksResponse:
    """
    Attributes:
        error (Union[Unset, ErrorResponse]):
        has_error (Union[Unset, bool]):
        error_description (Union[Unset, str]):
        account_id (Union[Unset, str]):
        status (Union[Unset, str]):
        description (Union[Unset, str]):
        state (Union[Unset, str]):
        pending_tasks (Union[Unset, List['PendingTask']]):
        pending_task_present (Union[Unset, bool]):
    """

    error: Union[Unset, "ErrorResponse"] = UNSET
    has_error: Union[Unset, bool] = UNSET
    error_description: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    pending_tasks: Union[Unset, List["PendingTask"]] = UNSET
    pending_task_present: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        has_error = self.has_error

        error_description = self.error_description

        account_id = self.account_id

        status = self.status

        description = self.description

        state = self.state

        pending_tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pending_tasks, Unset):
            pending_tasks = []
            for pending_tasks_item_data in self.pending_tasks:
                pending_tasks_item = pending_tasks_item_data.to_dict()
                pending_tasks.append(pending_tasks_item)

        pending_task_present = self.pending_task_present

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if has_error is not UNSET:
            field_dict["hasError"] = has_error
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if state is not UNSET:
            field_dict["state"] = state
        if pending_tasks is not UNSET:
            field_dict["pendingTasks"] = pending_tasks
        if pending_task_present is not UNSET:
            field_dict["pendingTaskPresent"] = pending_task_present

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response import ErrorResponse
        from ..models.pending_task import PendingTask

        d = src_dict.copy()
        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorResponse]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorResponse.from_dict(_error)

        has_error = d.pop("hasError", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        account_id = d.pop("accountId", UNSET)

        status = d.pop("status", UNSET)

        description = d.pop("description", UNSET)

        state = d.pop("state", UNSET)

        pending_tasks = []
        _pending_tasks = d.pop("pendingTasks", UNSET)
        for pending_tasks_item_data in _pending_tasks or []:
            pending_tasks_item = PendingTask.from_dict(pending_tasks_item_data)

            pending_tasks.append(pending_tasks_item)

        pending_task_present = d.pop("pendingTaskPresent", UNSET)

        pending_tasks_response = cls(
            error=error,
            has_error=has_error,
            error_description=error_description,
            account_id=account_id,
            status=status,
            description=description,
            state=state,
            pending_tasks=pending_tasks,
            pending_task_present=pending_task_present,
        )

        pending_tasks_response.additional_properties = d
        return pending_tasks_response

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
