from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_entity import AddEntity
    from ..models.delete_entity import DeleteEntity
    from ..models.update_entity import UpdateEntity


T = TypeVar("T", bound="InformationChange")


@_attrs_define
class InformationChange:
    """
    Attributes:
        add_entities (Union[Unset, List['AddEntity']]):
        update_entities (Union[Unset, List['UpdateEntity']]):
        delete_entities (Union[Unset, List['DeleteEntity']]):
        ib_account_id (Union[Unset, str]):
    """

    add_entities: Union[Unset, List["AddEntity"]] = UNSET
    update_entities: Union[Unset, List["UpdateEntity"]] = UNSET
    delete_entities: Union[Unset, List["DeleteEntity"]] = UNSET
    ib_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.add_entities, Unset):
            add_entities = []
            for add_entities_item_data in self.add_entities:
                add_entities_item = add_entities_item_data.to_dict()
                add_entities.append(add_entities_item)

        update_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.update_entities, Unset):
            update_entities = []
            for update_entities_item_data in self.update_entities:
                update_entities_item = update_entities_item_data.to_dict()
                update_entities.append(update_entities_item)

        delete_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.delete_entities, Unset):
            delete_entities = []
            for delete_entities_item_data in self.delete_entities:
                delete_entities_item = delete_entities_item_data.to_dict()
                delete_entities.append(delete_entities_item)

        ib_account_id = self.ib_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_entities is not UNSET:
            field_dict["addEntities"] = add_entities
        if update_entities is not UNSET:
            field_dict["updateEntities"] = update_entities
        if delete_entities is not UNSET:
            field_dict["deleteEntities"] = delete_entities
        if ib_account_id is not UNSET:
            field_dict["ibAccountId"] = ib_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.add_entity import AddEntity
        from ..models.delete_entity import DeleteEntity
        from ..models.update_entity import UpdateEntity

        d = src_dict.copy()
        add_entities = []
        _add_entities = d.pop("addEntities", UNSET)
        for add_entities_item_data in _add_entities or []:
            add_entities_item = AddEntity.from_dict(add_entities_item_data)

            add_entities.append(add_entities_item)

        update_entities = []
        _update_entities = d.pop("updateEntities", UNSET)
        for update_entities_item_data in _update_entities or []:
            update_entities_item = UpdateEntity.from_dict(update_entities_item_data)

            update_entities.append(update_entities_item)

        delete_entities = []
        _delete_entities = d.pop("deleteEntities", UNSET)
        for delete_entities_item_data in _delete_entities or []:
            delete_entities_item = DeleteEntity.from_dict(delete_entities_item_data)

            delete_entities.append(delete_entities_item)

        ib_account_id = d.pop("ibAccountId", UNSET)

        information_change = cls(
            add_entities=add_entities,
            update_entities=update_entities,
            delete_entities=delete_entities,
            ib_account_id=ib_account_id,
        )

        information_change.additional_properties = d
        return information_change

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
