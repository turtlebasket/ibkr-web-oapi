from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.individual_name_salutation import IndividualNameSalutation
from ..models.individual_name_suffix import IndividualNameSuffix
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualName")


@_attrs_define
class IndividualName:
    """
    Attributes:
        salutation (Union[Unset, IndividualNameSalutation]):
        first (Union[Unset, str]):
        last (Union[Unset, str]):
        middle (Union[Unset, str]):
        suffix (Union[Unset, IndividualNameSuffix]):
        title (Union[Unset, str]):
    """

    salutation: Union[Unset, IndividualNameSalutation] = UNSET
    first: Union[Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    middle: Union[Unset, str] = UNSET
    suffix: Union[Unset, IndividualNameSuffix] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        salutation: Union[Unset, str] = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.value

        first = self.first

        last = self.last

        middle = self.middle

        suffix: Union[Unset, str] = UNSET
        if not isinstance(self.suffix, Unset):
            suffix = self.suffix.value

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if middle is not UNSET:
            field_dict["middle"] = middle
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _salutation = d.pop("salutation", UNSET)
        salutation: Union[Unset, IndividualNameSalutation]
        if isinstance(_salutation, Unset):
            salutation = UNSET
        else:
            salutation = IndividualNameSalutation(_salutation)

        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        middle = d.pop("middle", UNSET)

        _suffix = d.pop("suffix", UNSET)
        suffix: Union[Unset, IndividualNameSuffix]
        if isinstance(_suffix, Unset):
            suffix = UNSET
        else:
            suffix = IndividualNameSuffix(_suffix)

        title = d.pop("title", UNSET)

        individual_name = cls(
            salutation=salutation,
            first=first,
            last=last,
            middle=middle,
            suffix=suffix,
            title=title,
        )

        individual_name.additional_properties = d
        return individual_name

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
