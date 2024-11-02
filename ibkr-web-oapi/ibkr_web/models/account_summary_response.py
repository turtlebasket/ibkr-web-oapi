from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_summary_response_cash_balances_item import AccountSummaryResponseCashBalancesItem


T = TypeVar("T", bound="AccountSummaryResponse")


@_attrs_define
class AccountSummaryResponse:
    """Successful return contianing an array of at-a-glance account details.

    Attributes:
        account_type (Union[Unset, str]): Describes the unique account type. For standard individual accounts, an empty
            string is returned.
        status (Union[Unset, str]): If the account is currently non-tradeable, a status message will be dispalyed.
        balance (Union[Unset, int]): Returns the total account balance.
        sma (Union[Unset, int]): Simple Moving Average of the account.
        buying_power (Union[Unset, int]): Total buying power available for the account.
        available_funds (Union[Unset, int]): The amount of equity you have available for trading. For both the
            Securities and Commodities segments, this is calculated as: Equity with Loan Value – Initial Margin.
        excess_liquidity (Union[Unset, int]): The amount of cash in excess of the usual requirement in your account.
        net_liquidation_value (Union[Unset, int]): The basis for determining the price of the assets in your account.
        equity_with_loan_value (Union[Unset, int]): The basis for determining whether you have the necessary assets to
            either initiate or maintain security assets.
        reg_t_loan (Union[Unset, int]): The Federal Reserve Board regulation governing the amount of credit that broker
            dealers may extend to clients who borrow money to buy securities on margin.
        securities_gvp (Union[Unset, int]): Absolute value of the Long Stock Value + Short Stock Value + Long Option
            Value + Short Option Value + Fund Value.
        total_cash_value (Union[Unset, int]): Cash recognized at the time of trade + futures P&L. This value reflects
            real-time currency positions, including:
             *  Trades executed directly through the FX market.
             *  Trades executed as a result of automatic IB conversions, which occur when you trade a product in a non-base
            currency.
             *  Trades deliberately executed to close non-base currency positions using the FXCONV destination.
        accrued_interest (Union[Unset, int]): Accrued interest is the interest accruing on a security since the previous
            coupon date. If a security is sold between two payment dates, the buyer usually compensates the seller for the
            interest accrued, either within the price or as a separate payment.
        reg_t_margin (Union[Unset, int]): The initial margin requirements calculated under US Regulation T rules for
            both the securities and commodities segment of your account.
        initial_margin (Union[Unset, int]): The available initial margin for the account.
        maintenance_margin (Union[Unset, int]): The available maintenance margin for the account.
        cash_balances (Union[Unset, List['AccountSummaryResponseCashBalancesItem']]): An array containing balance
            information for all currencies held by the account.
    """

    account_type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    balance: Union[Unset, int] = UNSET
    sma: Union[Unset, int] = UNSET
    buying_power: Union[Unset, int] = UNSET
    available_funds: Union[Unset, int] = UNSET
    excess_liquidity: Union[Unset, int] = UNSET
    net_liquidation_value: Union[Unset, int] = UNSET
    equity_with_loan_value: Union[Unset, int] = UNSET
    reg_t_loan: Union[Unset, int] = UNSET
    securities_gvp: Union[Unset, int] = UNSET
    total_cash_value: Union[Unset, int] = UNSET
    accrued_interest: Union[Unset, int] = UNSET
    reg_t_margin: Union[Unset, int] = UNSET
    initial_margin: Union[Unset, int] = UNSET
    maintenance_margin: Union[Unset, int] = UNSET
    cash_balances: Union[Unset, List["AccountSummaryResponseCashBalancesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_type = self.account_type

        status = self.status

        balance = self.balance

        sma = self.sma

        buying_power = self.buying_power

        available_funds = self.available_funds

        excess_liquidity = self.excess_liquidity

        net_liquidation_value = self.net_liquidation_value

        equity_with_loan_value = self.equity_with_loan_value

        reg_t_loan = self.reg_t_loan

        securities_gvp = self.securities_gvp

        total_cash_value = self.total_cash_value

        accrued_interest = self.accrued_interest

        reg_t_margin = self.reg_t_margin

        initial_margin = self.initial_margin

        maintenance_margin = self.maintenance_margin

        cash_balances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cash_balances, Unset):
            cash_balances = []
            for cash_balances_item_data in self.cash_balances:
                cash_balances_item = cash_balances_item_data.to_dict()
                cash_balances.append(cash_balances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if status is not UNSET:
            field_dict["status"] = status
        if balance is not UNSET:
            field_dict["balance"] = balance
        if sma is not UNSET:
            field_dict["SMA"] = sma
        if buying_power is not UNSET:
            field_dict["buyingPower"] = buying_power
        if available_funds is not UNSET:
            field_dict["availableFunds"] = available_funds
        if excess_liquidity is not UNSET:
            field_dict["excessLiquidity"] = excess_liquidity
        if net_liquidation_value is not UNSET:
            field_dict["netLiquidationValue"] = net_liquidation_value
        if equity_with_loan_value is not UNSET:
            field_dict["equityWithLoanValue"] = equity_with_loan_value
        if reg_t_loan is not UNSET:
            field_dict["regTLoan"] = reg_t_loan
        if securities_gvp is not UNSET:
            field_dict["securitiesGVP"] = securities_gvp
        if total_cash_value is not UNSET:
            field_dict["totalCashValue"] = total_cash_value
        if accrued_interest is not UNSET:
            field_dict["accruedInterest"] = accrued_interest
        if reg_t_margin is not UNSET:
            field_dict["regTMargin"] = reg_t_margin
        if initial_margin is not UNSET:
            field_dict["initialMargin"] = initial_margin
        if maintenance_margin is not UNSET:
            field_dict["maintenanceMargin"] = maintenance_margin
        if cash_balances is not UNSET:
            field_dict["cashBalances"] = cash_balances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_summary_response_cash_balances_item import AccountSummaryResponseCashBalancesItem

        d = src_dict.copy()
        account_type = d.pop("accountType", UNSET)

        status = d.pop("status", UNSET)

        balance = d.pop("balance", UNSET)

        sma = d.pop("SMA", UNSET)

        buying_power = d.pop("buyingPower", UNSET)

        available_funds = d.pop("availableFunds", UNSET)

        excess_liquidity = d.pop("excessLiquidity", UNSET)

        net_liquidation_value = d.pop("netLiquidationValue", UNSET)

        equity_with_loan_value = d.pop("equityWithLoanValue", UNSET)

        reg_t_loan = d.pop("regTLoan", UNSET)

        securities_gvp = d.pop("securitiesGVP", UNSET)

        total_cash_value = d.pop("totalCashValue", UNSET)

        accrued_interest = d.pop("accruedInterest", UNSET)

        reg_t_margin = d.pop("regTMargin", UNSET)

        initial_margin = d.pop("initialMargin", UNSET)

        maintenance_margin = d.pop("maintenanceMargin", UNSET)

        cash_balances = []
        _cash_balances = d.pop("cashBalances", UNSET)
        for cash_balances_item_data in _cash_balances or []:
            cash_balances_item = AccountSummaryResponseCashBalancesItem.from_dict(cash_balances_item_data)

            cash_balances.append(cash_balances_item)

        account_summary_response = cls(
            account_type=account_type,
            status=status,
            balance=balance,
            sma=sma,
            buying_power=buying_power,
            available_funds=available_funds,
            excess_liquidity=excess_liquidity,
            net_liquidation_value=net_liquidation_value,
            equity_with_loan_value=equity_with_loan_value,
            reg_t_loan=reg_t_loan,
            securities_gvp=securities_gvp,
            total_cash_value=total_cash_value,
            accrued_interest=accrued_interest,
            reg_t_margin=reg_t_margin,
            initial_margin=initial_margin,
            maintenance_margin=maintenance_margin,
            cash_balances=cash_balances,
        )

        account_summary_response.additional_properties = d
        return account_summary_response

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
