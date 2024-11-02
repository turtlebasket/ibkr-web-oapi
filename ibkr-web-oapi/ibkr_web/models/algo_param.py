from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.algo_param_value_class_name import AlgoParamValueClassName
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlgoParam")


@_attrs_define
class AlgoParam:
    """
    Attributes:
        gui_rank (Union[Unset, int]): Positional ranking for the algo. Used for Client Portal.
        default_value (Union[Unset, bool, float, int, str]): Default parameter value. Type defined in valueClassName
            field
        min_value (Union[Unset, int]):
        max_value (Union[Unset, int]):
        name (Union[Unset, str]): Parameter name.
        id (Union[Unset, str]): Parameter identifier for the algo.
        description (Union[Unset, str]):
        legal_strings (Union[Unset, List[str]]): Allowed values for the parameter.
        required (Union[Unset, bool]): States whether the parameter is required for the given algo order to place.
        value_class_name (Union[Unset, AlgoParamValueClassName]): Returns the variable type of the parameter.
    """

    gui_rank: Union[Unset, int] = UNSET
    default_value: Union[Unset, bool, float, int, str] = UNSET
    min_value: Union[Unset, int] = UNSET
    max_value: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    legal_strings: Union[Unset, List[str]] = UNSET
    required: Union[Unset, bool] = UNSET
    value_class_name: Union[Unset, AlgoParamValueClassName] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gui_rank = self.gui_rank

        default_value: Union[Unset, bool, float, int, str]
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        min_value = self.min_value

        max_value = self.max_value

        name = self.name

        id = self.id

        description = self.description

        legal_strings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.legal_strings, Unset):
            legal_strings = self.legal_strings

        required = self.required

        value_class_name: Union[Unset, str] = UNSET
        if not isinstance(self.value_class_name, Unset):
            value_class_name = self.value_class_name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gui_rank is not UNSET:
            field_dict["guiRank"] = gui_rank
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if legal_strings is not UNSET:
            field_dict["legalStrings"] = legal_strings
        if required is not UNSET:
            field_dict["required"] = required
        if value_class_name is not UNSET:
            field_dict["valueClassName"] = value_class_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gui_rank = d.pop("guiRank", UNSET)

        def _parse_default_value(data: object) -> Union[Unset, bool, float, int, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, bool, float, int, str], data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        min_value = d.pop("minValue", UNSET)

        max_value = d.pop("maxValue", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        legal_strings = cast(List[str], d.pop("legalStrings", UNSET))

        required = d.pop("required", UNSET)

        _value_class_name = d.pop("valueClassName", UNSET)
        value_class_name: Union[Unset, AlgoParamValueClassName]
        if isinstance(_value_class_name, Unset):
            value_class_name = UNSET
        else:
            value_class_name = AlgoParamValueClassName(_value_class_name)

        algo_param = cls(
            gui_rank=gui_rank,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            name=name,
            id=id,
            description=description,
            legal_strings=legal_strings,
            required=required,
            value_class_name=value_class_name,
        )

        algo_param.additional_properties = d
        return algo_param

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
