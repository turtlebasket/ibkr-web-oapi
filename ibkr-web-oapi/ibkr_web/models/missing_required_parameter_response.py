from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invalid_argument import InvalidArgument


T = TypeVar("T", bound="MissingRequiredParameterResponse")


@_attrs_define
class MissingRequiredParameterResponse:
    """
    Attributes:
        type (str):  Example: /invalid-argument.
        title (str):  Example: Bad Request.
        status (int):  Example: 400.
        invalid_arguments (Union[Unset, List['InvalidArgument']]):
    """

    type: str
    title: str
    status: int
    invalid_arguments: Union[Unset, List["InvalidArgument"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        title = self.title

        status = self.status

        invalid_arguments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_arguments, Unset):
            invalid_arguments = []
            for invalid_arguments_item_data in self.invalid_arguments:
                invalid_arguments_item = invalid_arguments_item_data.to_dict()
                invalid_arguments.append(invalid_arguments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "title": title,
                "status": status,
            }
        )
        if invalid_arguments is not UNSET:
            field_dict["invalidArguments"] = invalid_arguments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invalid_argument import InvalidArgument

        d = src_dict.copy()
        type = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        invalid_arguments = []
        _invalid_arguments = d.pop("invalidArguments", UNSET)
        for invalid_arguments_item_data in _invalid_arguments or []:
            invalid_arguments_item = InvalidArgument.from_dict(invalid_arguments_item_data)

            invalid_arguments.append(invalid_arguments_item)

        missing_required_parameter_response = cls(
            type=type,
            title=title,
            status=status,
            invalid_arguments=invalid_arguments,
        )

        missing_required_parameter_response.additional_properties = d
        return missing_required_parameter_response

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
