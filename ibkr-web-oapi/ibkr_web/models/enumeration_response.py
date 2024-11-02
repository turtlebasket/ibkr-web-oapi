from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.array_node import ArrayNode


T = TypeVar("T", bound="EnumerationResponse")


@_attrs_define
class EnumerationResponse:
    """
    Attributes:
        enumerations_type (Union[Unset, str]):
        form_number (Union[Unset, str]):
        json_data (Union[Unset, ArrayNode]):
    """

    enumerations_type: Union[Unset, str] = UNSET
    form_number: Union[Unset, str] = UNSET
    json_data: Union[Unset, "ArrayNode"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enumerations_type = self.enumerations_type

        form_number = self.form_number

        json_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json_data, Unset):
            json_data = self.json_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enumerations_type is not UNSET:
            field_dict["enumerationsType"] = enumerations_type
        if form_number is not UNSET:
            field_dict["formNumber"] = form_number
        if json_data is not UNSET:
            field_dict["jsonData"] = json_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.array_node import ArrayNode

        d = src_dict.copy()
        enumerations_type = d.pop("enumerationsType", UNSET)

        form_number = d.pop("formNumber", UNSET)

        _json_data = d.pop("jsonData", UNSET)
        json_data: Union[Unset, ArrayNode]
        if isinstance(_json_data, Unset):
            json_data = UNSET
        else:
            json_data = ArrayNode.from_dict(_json_data)

        enumeration_response = cls(
            enumerations_type=enumerations_type,
            form_number=form_number,
            json_data=json_data,
        )

        enumeration_response.additional_properties = d
        return enumeration_response

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
