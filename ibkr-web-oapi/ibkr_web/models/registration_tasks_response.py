from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response import ErrorResponse
    from ..models.registration_task import RegistrationTask


T = TypeVar("T", bound="RegistrationTasksResponse")


@_attrs_define
class RegistrationTasksResponse:
    """
    Attributes:
        error (Union[Unset, ErrorResponse]):
        has_error (Union[Unset, bool]):
        error_description (Union[Unset, str]):
        account_id (Union[Unset, str]):
        status (Union[Unset, str]):
        description (Union[Unset, str]):
        state (Union[Unset, str]):
        registration_task_present (Union[Unset, bool]):
        registration_tasks (Union[Unset, List['RegistrationTask']]):
    """

    error: Union[Unset, "ErrorResponse"] = UNSET
    has_error: Union[Unset, bool] = UNSET
    error_description: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    registration_task_present: Union[Unset, bool] = UNSET
    registration_tasks: Union[Unset, List["RegistrationTask"]] = UNSET
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

        registration_task_present = self.registration_task_present

        registration_tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.registration_tasks, Unset):
            registration_tasks = []
            for registration_tasks_item_data in self.registration_tasks:
                registration_tasks_item = registration_tasks_item_data.to_dict()
                registration_tasks.append(registration_tasks_item)

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
        if registration_task_present is not UNSET:
            field_dict["registrationTaskPresent"] = registration_task_present
        if registration_tasks is not UNSET:
            field_dict["registrationTasks"] = registration_tasks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response import ErrorResponse
        from ..models.registration_task import RegistrationTask

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

        registration_task_present = d.pop("registrationTaskPresent", UNSET)

        registration_tasks = []
        _registration_tasks = d.pop("registrationTasks", UNSET)
        for registration_tasks_item_data in _registration_tasks or []:
            registration_tasks_item = RegistrationTask.from_dict(registration_tasks_item_data)

            registration_tasks.append(registration_tasks_item)

        registration_tasks_response = cls(
            error=error,
            has_error=has_error,
            error_description=error_description,
            account_id=account_id,
            status=status,
            description=description,
            state=state,
            registration_task_present=registration_task_present,
            registration_tasks=registration_tasks,
        )

        registration_tasks_response.additional_properties = d
        return registration_tasks_response

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
