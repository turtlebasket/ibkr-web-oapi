from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_gw_api_v1_external_cash_transfers_query_body_instruction_type import (
    PostGwApiV1ExternalCashTransfersQueryBodyInstructionType,
)

if TYPE_CHECKING:
    from ..models.query_ira_contributions import QueryIRAContributions
    from ..models.query_withdrawable_funds import QueryWithdrawableFunds
    from ..models.query_withdrawable_without_origin_hold_funds import QueryWithdrawableWithoutOriginHoldFunds


T = TypeVar("T", bound="PostGwApiV1ExternalCashTransfersQueryBody")


@_attrs_define
class PostGwApiV1ExternalCashTransfersQueryBody:
    """
    Attributes:
        instruction_type (PostGwApiV1ExternalCashTransfersQueryBodyInstructionType):
        instruction (Union['QueryIRAContributions', 'QueryWithdrawableFunds',
            'QueryWithdrawableWithoutOriginHoldFunds']):
    """

    instruction_type: PostGwApiV1ExternalCashTransfersQueryBodyInstructionType
    instruction: Union["QueryIRAContributions", "QueryWithdrawableFunds", "QueryWithdrawableWithoutOriginHoldFunds"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.query_withdrawable_funds import QueryWithdrawableFunds
        from ..models.query_withdrawable_without_origin_hold_funds import QueryWithdrawableWithoutOriginHoldFunds

        instruction_type = self.instruction_type.value

        instruction: Dict[str, Any]
        if isinstance(self.instruction, QueryWithdrawableFunds):
            instruction = self.instruction.to_dict()
        elif isinstance(self.instruction, QueryWithdrawableWithoutOriginHoldFunds):
            instruction = self.instruction.to_dict()
        else:
            instruction = self.instruction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instructionType": instruction_type,
                "instruction": instruction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_ira_contributions import QueryIRAContributions
        from ..models.query_withdrawable_funds import QueryWithdrawableFunds
        from ..models.query_withdrawable_without_origin_hold_funds import QueryWithdrawableWithoutOriginHoldFunds

        d = src_dict.copy()
        instruction_type = PostGwApiV1ExternalCashTransfersQueryBodyInstructionType(d.pop("instructionType"))

        def _parse_instruction(
            data: object,
        ) -> Union["QueryIRAContributions", "QueryWithdrawableFunds", "QueryWithdrawableWithoutOriginHoldFunds"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instruction_type_0 = QueryWithdrawableFunds.from_dict(data)

                return instruction_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instruction_type_1 = QueryWithdrawableWithoutOriginHoldFunds.from_dict(data)

                return instruction_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            instruction_type_2 = QueryIRAContributions.from_dict(data)

            return instruction_type_2

        instruction = _parse_instruction(d.pop("instruction"))

        post_gw_api_v1_external_cash_transfers_query_body = cls(
            instruction_type=instruction_type,
            instruction=instruction,
        )

        post_gw_api_v1_external_cash_transfers_query_body.additional_properties = d
        return post_gw_api_v1_external_cash_transfers_query_body

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
