from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccountsResponseChartPeriods")


@_attrs_define
class UserAccountsResponseChartPeriods:
    """
    Attributes:
        stk (Union[Unset, List[str]]):
        cfd (Union[Unset, List[str]]):
        opt (Union[Unset, List[str]]):
        fop (Union[Unset, List[str]]):
        war (Union[Unset, List[str]]):
        iopt (Union[Unset, List[str]]):
        fut (Union[Unset, List[str]]):
        cash (Union[Unset, List[str]]):
        ind (Union[Unset, List[str]]):
        bond (Union[Unset, List[str]]):
        fund (Union[Unset, List[str]]):
        cmdty (Union[Unset, List[str]]):
        physs (Union[Unset, List[str]]):
        crypto (Union[Unset, List[str]]):
    """

    stk: Union[Unset, List[str]] = UNSET
    cfd: Union[Unset, List[str]] = UNSET
    opt: Union[Unset, List[str]] = UNSET
    fop: Union[Unset, List[str]] = UNSET
    war: Union[Unset, List[str]] = UNSET
    iopt: Union[Unset, List[str]] = UNSET
    fut: Union[Unset, List[str]] = UNSET
    cash: Union[Unset, List[str]] = UNSET
    ind: Union[Unset, List[str]] = UNSET
    bond: Union[Unset, List[str]] = UNSET
    fund: Union[Unset, List[str]] = UNSET
    cmdty: Union[Unset, List[str]] = UNSET
    physs: Union[Unset, List[str]] = UNSET
    crypto: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stk: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stk, Unset):
            stk = self.stk

        cfd: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cfd, Unset):
            cfd = self.cfd

        opt: Union[Unset, List[str]] = UNSET
        if not isinstance(self.opt, Unset):
            opt = self.opt

        fop: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fop, Unset):
            fop = self.fop

        war: Union[Unset, List[str]] = UNSET
        if not isinstance(self.war, Unset):
            war = self.war

        iopt: Union[Unset, List[str]] = UNSET
        if not isinstance(self.iopt, Unset):
            iopt = self.iopt

        fut: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fut, Unset):
            fut = self.fut

        cash: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cash, Unset):
            cash = self.cash

        ind: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ind, Unset):
            ind = self.ind

        bond: Union[Unset, List[str]] = UNSET
        if not isinstance(self.bond, Unset):
            bond = self.bond

        fund: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fund, Unset):
            fund = self.fund

        cmdty: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cmdty, Unset):
            cmdty = self.cmdty

        physs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.physs, Unset):
            physs = self.physs

        crypto: Union[Unset, List[str]] = UNSET
        if not isinstance(self.crypto, Unset):
            crypto = self.crypto

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stk is not UNSET:
            field_dict["STK"] = stk
        if cfd is not UNSET:
            field_dict["CFD"] = cfd
        if opt is not UNSET:
            field_dict["OPT"] = opt
        if fop is not UNSET:
            field_dict["FOP"] = fop
        if war is not UNSET:
            field_dict["WAR"] = war
        if iopt is not UNSET:
            field_dict["IOPT"] = iopt
        if fut is not UNSET:
            field_dict["FUT"] = fut
        if cash is not UNSET:
            field_dict["CASH"] = cash
        if ind is not UNSET:
            field_dict["IND"] = ind
        if bond is not UNSET:
            field_dict["BOND"] = bond
        if fund is not UNSET:
            field_dict["FUND"] = fund
        if cmdty is not UNSET:
            field_dict["CMDTY"] = cmdty
        if physs is not UNSET:
            field_dict["PHYSS"] = physs
        if crypto is not UNSET:
            field_dict["CRYPTO"] = crypto

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stk = cast(List[str], d.pop("STK", UNSET))

        cfd = cast(List[str], d.pop("CFD", UNSET))

        opt = cast(List[str], d.pop("OPT", UNSET))

        fop = cast(List[str], d.pop("FOP", UNSET))

        war = cast(List[str], d.pop("WAR", UNSET))

        iopt = cast(List[str], d.pop("IOPT", UNSET))

        fut = cast(List[str], d.pop("FUT", UNSET))

        cash = cast(List[str], d.pop("CASH", UNSET))

        ind = cast(List[str], d.pop("IND", UNSET))

        bond = cast(List[str], d.pop("BOND", UNSET))

        fund = cast(List[str], d.pop("FUND", UNSET))

        cmdty = cast(List[str], d.pop("CMDTY", UNSET))

        physs = cast(List[str], d.pop("PHYSS", UNSET))

        crypto = cast(List[str], d.pop("CRYPTO", UNSET))

        user_accounts_response_chart_periods = cls(
            stk=stk,
            cfd=cfd,
            opt=opt,
            fop=fop,
            war=war,
            iopt=iopt,
            fut=fut,
            cash=cash,
            ind=ind,
            bond=bond,
            fund=fund,
            cmdty=cmdty,
            physs=physs,
            crypto=crypto,
        )

        user_accounts_response_chart_periods.additional_properties = d
        return user_accounts_response_chart_periods

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
