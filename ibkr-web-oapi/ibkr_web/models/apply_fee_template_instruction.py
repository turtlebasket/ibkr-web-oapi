from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApplyFeeTemplateInstruction")


@_attrs_define
class ApplyFeeTemplateInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        account_id (str):  Example: U46377.
        template_name (str):  Example: Test template.
    """

    client_instruction_id: float
    account_id: str
    template_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        account_id = self.account_id

        template_name = self.template_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "accountId": account_id,
                "templateName": template_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        account_id = d.pop("accountId")

        template_name = d.pop("templateName")

        apply_fee_template_instruction = cls(
            client_instruction_id=client_instruction_id,
            account_id=account_id,
            template_name=template_name,
        )

        apply_fee_template_instruction.additional_properties = d
        return apply_fee_template_instruction

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
