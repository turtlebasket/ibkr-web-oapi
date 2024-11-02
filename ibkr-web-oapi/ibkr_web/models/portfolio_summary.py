from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_summary_accountcode import PortfolioSummaryAccountcode
    from ..models.portfolio_summary_accountready import PortfolioSummaryAccountready
    from ..models.portfolio_summary_accounttype import PortfolioSummaryAccounttype
    from ..models.portfolio_summary_accruedcash import PortfolioSummaryAccruedcash
    from ..models.portfolio_summary_accruedcash_c import PortfolioSummaryAccruedcashC
    from ..models.portfolio_summary_accruedcash_s import PortfolioSummaryAccruedcashS
    from ..models.portfolio_summary_accrueddividend import PortfolioSummaryAccrueddividend
    from ..models.portfolio_summary_accrueddividend_c import PortfolioSummaryAccrueddividendC
    from ..models.portfolio_summary_accrueddividend_s import PortfolioSummaryAccrueddividendS
    from ..models.portfolio_summary_availablefunds import PortfolioSummaryAvailablefunds
    from ..models.portfolio_summary_availablefunds_c import PortfolioSummaryAvailablefundsC
    from ..models.portfolio_summary_availablefunds_s import PortfolioSummaryAvailablefundsS
    from ..models.portfolio_summary_availabletotrade import PortfolioSummaryAvailabletotrade
    from ..models.portfolio_summary_availabletotrade_c import PortfolioSummaryAvailabletotradeC
    from ..models.portfolio_summary_availabletotrade_s import PortfolioSummaryAvailabletotradeS
    from ..models.portfolio_summary_availabletowithdraw import PortfolioSummaryAvailabletowithdraw
    from ..models.portfolio_summary_availabletowithdraw_c import PortfolioSummaryAvailabletowithdrawC
    from ..models.portfolio_summary_availabletowithdraw_s import PortfolioSummaryAvailabletowithdrawS
    from ..models.portfolio_summary_billable import PortfolioSummaryBillable
    from ..models.portfolio_summary_billable_c import PortfolioSummaryBillableC
    from ..models.portfolio_summary_billable_s import PortfolioSummaryBillableS
    from ..models.portfolio_summary_buyingpower import PortfolioSummaryBuyingpower
    from ..models.portfolio_summary_columnprio_c import PortfolioSummaryColumnprioC
    from ..models.portfolio_summary_columnprio_s import PortfolioSummaryColumnprioS
    from ..models.portfolio_summary_cushion import PortfolioSummaryCushion
    from ..models.portfolio_summary_daytradesremaining import PortfolioSummaryDaytradesremaining
    from ..models.portfolio_summary_daytradesremainingt_1 import PortfolioSummaryDaytradesremainingt1
    from ..models.portfolio_summary_daytradesremainingt_2 import PortfolioSummaryDaytradesremainingt2
    from ..models.portfolio_summary_daytradesremainingt_3 import PortfolioSummaryDaytradesremainingt3
    from ..models.portfolio_summary_daytradesremainingt_4 import PortfolioSummaryDaytradesremainingt4
    from ..models.portfolio_summary_daytradingstatus_s import PortfolioSummaryDaytradingstatusS
    from ..models.portfolio_summary_depositoncredithold import PortfolioSummaryDepositoncredithold
    from ..models.portfolio_summary_equitywithloanvalue import PortfolioSummaryEquitywithloanvalue
    from ..models.portfolio_summary_equitywithloanvalue_c import PortfolioSummaryEquitywithloanvalueC
    from ..models.portfolio_summary_equitywithloanvalue_s import PortfolioSummaryEquitywithloanvalueS
    from ..models.portfolio_summary_excessliquidity import PortfolioSummaryExcessliquidity
    from ..models.portfolio_summary_excessliquidity_c import PortfolioSummaryExcessliquidityC
    from ..models.portfolio_summary_excessliquidity_s import PortfolioSummaryExcessliquidityS
    from ..models.portfolio_summary_fullavailablefunds import PortfolioSummaryFullavailablefunds
    from ..models.portfolio_summary_fullavailablefunds_c import PortfolioSummaryFullavailablefundsC
    from ..models.portfolio_summary_fullavailablefunds_s import PortfolioSummaryFullavailablefundsS
    from ..models.portfolio_summary_fullexcessliquidity import PortfolioSummaryFullexcessliquidity
    from ..models.portfolio_summary_fullexcessliquidity_c import PortfolioSummaryFullexcessliquidityC
    from ..models.portfolio_summary_fullexcessliquidity_s import PortfolioSummaryFullexcessliquidityS
    from ..models.portfolio_summary_fullinitmarginreq import PortfolioSummaryFullinitmarginreq
    from ..models.portfolio_summary_fullinitmarginreq_c import PortfolioSummaryFullinitmarginreqC
    from ..models.portfolio_summary_fullinitmarginreq_s import PortfolioSummaryFullinitmarginreqS
    from ..models.portfolio_summary_fullmaintmarginreq import PortfolioSummaryFullmaintmarginreq
    from ..models.portfolio_summary_fullmaintmarginreq_c import PortfolioSummaryFullmaintmarginreqC
    from ..models.portfolio_summary_fullmaintmarginreq_s import PortfolioSummaryFullmaintmarginreqS
    from ..models.portfolio_summary_grosspositionvalue import PortfolioSummaryGrosspositionvalue
    from ..models.portfolio_summary_grosspositionvalue_s import PortfolioSummaryGrosspositionvalueS
    from ..models.portfolio_summary_guarantee import PortfolioSummaryGuarantee
    from ..models.portfolio_summary_guarantee_c import PortfolioSummaryGuaranteeC
    from ..models.portfolio_summary_guarantee_s import PortfolioSummaryGuaranteeS
    from ..models.portfolio_summary_highestseverity import PortfolioSummaryHighestseverity
    from ..models.portfolio_summary_indianstockhaircut import PortfolioSummaryIndianstockhaircut
    from ..models.portfolio_summary_indianstockhaircut_c import PortfolioSummaryIndianstockhaircutC
    from ..models.portfolio_summary_indianstockhaircut_s import PortfolioSummaryIndianstockhaircutS
    from ..models.portfolio_summary_initmarginreq import PortfolioSummaryInitmarginreq
    from ..models.portfolio_summary_initmarginreq_c import PortfolioSummaryInitmarginreqC
    from ..models.portfolio_summary_initmarginreq_s import PortfolioSummaryInitmarginreqS
    from ..models.portfolio_summary_leverage_s import PortfolioSummaryLeverageS
    from ..models.portfolio_summary_lookaheadavailablefunds import PortfolioSummaryLookaheadavailablefunds
    from ..models.portfolio_summary_lookaheadavailablefunds_c import PortfolioSummaryLookaheadavailablefundsC
    from ..models.portfolio_summary_lookaheadavailablefunds_s import PortfolioSummaryLookaheadavailablefundsS
    from ..models.portfolio_summary_lookaheadexcessliquidity import PortfolioSummaryLookaheadexcessliquidity
    from ..models.portfolio_summary_lookaheadexcessliquidity_c import PortfolioSummaryLookaheadexcessliquidityC
    from ..models.portfolio_summary_lookaheadexcessliquidity_s import PortfolioSummaryLookaheadexcessliquidityS
    from ..models.portfolio_summary_lookaheadinitmarginreq import PortfolioSummaryLookaheadinitmarginreq
    from ..models.portfolio_summary_lookaheadinitmarginreq_c import PortfolioSummaryLookaheadinitmarginreqC
    from ..models.portfolio_summary_lookaheadinitmarginreq_s import PortfolioSummaryLookaheadinitmarginreqS
    from ..models.portfolio_summary_lookaheadmaintmarginreq import PortfolioSummaryLookaheadmaintmarginreq
    from ..models.portfolio_summary_lookaheadmaintmarginreq_c import PortfolioSummaryLookaheadmaintmarginreqC
    from ..models.portfolio_summary_lookaheadmaintmarginreq_s import PortfolioSummaryLookaheadmaintmarginreqS
    from ..models.portfolio_summary_lookaheadnextchange import PortfolioSummaryLookaheadnextchange
    from ..models.portfolio_summary_maintmarginreq import PortfolioSummaryMaintmarginreq
    from ..models.portfolio_summary_maintmarginreq_c import PortfolioSummaryMaintmarginreqC
    from ..models.portfolio_summary_maintmarginreq_s import PortfolioSummaryMaintmarginreqS
    from ..models.portfolio_summary_netliquidation import PortfolioSummaryNetliquidation
    from ..models.portfolio_summary_netliquidation_c import PortfolioSummaryNetliquidationC
    from ..models.portfolio_summary_netliquidation_s import PortfolioSummaryNetliquidationS
    from ..models.portfolio_summary_netliquidationuncertainty import PortfolioSummaryNetliquidationuncertainty
    from ..models.portfolio_summary_nlvandmargininreview import PortfolioSummaryNlvandmargininreview
    from ..models.portfolio_summary_pasharesvalue import PortfolioSummaryPasharesvalue
    from ..models.portfolio_summary_pasharesvalue_c import PortfolioSummaryPasharesvalueC
    from ..models.portfolio_summary_pasharesvalue_s import PortfolioSummaryPasharesvalueS
    from ..models.portfolio_summary_physicalcertificatevalue import PortfolioSummaryPhysicalcertificatevalue
    from ..models.portfolio_summary_physicalcertificatevalue_c import PortfolioSummaryPhysicalcertificatevalueC
    from ..models.portfolio_summary_physicalcertificatevalue_s import PortfolioSummaryPhysicalcertificatevalueS
    from ..models.portfolio_summary_postexpirationexcess import PortfolioSummaryPostexpirationexcess
    from ..models.portfolio_summary_postexpirationexcess_c import PortfolioSummaryPostexpirationexcessC
    from ..models.portfolio_summary_postexpirationexcess_s import PortfolioSummaryPostexpirationexcessS
    from ..models.portfolio_summary_postexpirationmargin import PortfolioSummaryPostexpirationmargin
    from ..models.portfolio_summary_postexpirationmargin_c import PortfolioSummaryPostexpirationmarginC
    from ..models.portfolio_summary_postexpirationmargin_s import PortfolioSummaryPostexpirationmarginS
    from ..models.portfolio_summary_previousdayequitywithloanvalue import PortfolioSummaryPreviousdayequitywithloanvalue
    from ..models.portfolio_summary_previousdayequitywithloanvalue_s import (
        PortfolioSummaryPreviousdayequitywithloanvalueS,
    )
    from ..models.portfolio_summary_regtequity import PortfolioSummaryRegtequity
    from ..models.portfolio_summary_regtequity_s import PortfolioSummaryRegtequityS
    from ..models.portfolio_summary_regtmargin import PortfolioSummaryRegtmargin
    from ..models.portfolio_summary_regtmargin_s import PortfolioSummaryRegtmarginS
    from ..models.portfolio_summary_segmenttitle_c import PortfolioSummarySegmenttitleC
    from ..models.portfolio_summary_segmenttitle_s import PortfolioSummarySegmenttitleS
    from ..models.portfolio_summary_sma import PortfolioSummarySma
    from ..models.portfolio_summary_sma_s import PortfolioSummarySmaS
    from ..models.portfolio_summary_totalcashvalue import PortfolioSummaryTotalcashvalue
    from ..models.portfolio_summary_totalcashvalue_c import PortfolioSummaryTotalcashvalueC
    from ..models.portfolio_summary_totalcashvalue_s import PortfolioSummaryTotalcashvalueS
    from ..models.portfolio_summary_totaldebitcardpendingcharges import PortfolioSummaryTotaldebitcardpendingcharges
    from ..models.portfolio_summary_totaldebitcardpendingcharges_c import PortfolioSummaryTotaldebitcardpendingchargesC
    from ..models.portfolio_summary_totaldebitcardpendingcharges_s import PortfolioSummaryTotaldebitcardpendingchargesS
    from ..models.portfolio_summary_tradingtype_s import PortfolioSummaryTradingtypeS
    from ..models.portfolio_summary_whatifpmenabled import PortfolioSummaryWhatifpmenabled


T = TypeVar("T", bound="PortfolioSummary")


@_attrs_define
class PortfolioSummary:
    """
    Attributes:
        accountcode (Union[Unset, PortfolioSummaryAccountcode]):
        accountready (Union[Unset, PortfolioSummaryAccountready]):
        accounttype (Union[Unset, PortfolioSummaryAccounttype]):
        accruedcash (Union[Unset, PortfolioSummaryAccruedcash]):
        accruedcash_c (Union[Unset, PortfolioSummaryAccruedcashC]):
        accruedcash_s (Union[Unset, PortfolioSummaryAccruedcashS]):
        accrueddividend (Union[Unset, PortfolioSummaryAccrueddividend]):
        accrueddividend_c (Union[Unset, PortfolioSummaryAccrueddividendC]):
        accrueddividend_s (Union[Unset, PortfolioSummaryAccrueddividendS]):
        availablefunds (Union[Unset, PortfolioSummaryAvailablefunds]):
        availablefunds_c (Union[Unset, PortfolioSummaryAvailablefundsC]):
        availablefunds_s (Union[Unset, PortfolioSummaryAvailablefundsS]):
        availabletotrade (Union[Unset, PortfolioSummaryAvailabletotrade]):
        availabletotrade_c (Union[Unset, PortfolioSummaryAvailabletotradeC]):
        availabletotrade_s (Union[Unset, PortfolioSummaryAvailabletotradeS]):
        availabletowithdraw (Union[Unset, PortfolioSummaryAvailabletowithdraw]):
        availabletowithdraw_c (Union[Unset, PortfolioSummaryAvailabletowithdrawC]):
        availabletowithdraw_s (Union[Unset, PortfolioSummaryAvailabletowithdrawS]):
        billable (Union[Unset, PortfolioSummaryBillable]):
        billable_c (Union[Unset, PortfolioSummaryBillableC]):
        billable_s (Union[Unset, PortfolioSummaryBillableS]):
        buyingpower (Union[Unset, PortfolioSummaryBuyingpower]):
        columnprio_c (Union[Unset, PortfolioSummaryColumnprioC]):
        columnprio_s (Union[Unset, PortfolioSummaryColumnprioS]):
        cushion (Union[Unset, PortfolioSummaryCushion]):
        daytradesremaining (Union[Unset, PortfolioSummaryDaytradesremaining]):
        daytradesremainingt1 (Union[Unset, PortfolioSummaryDaytradesremainingt1]):
        daytradesremainingt2 (Union[Unset, PortfolioSummaryDaytradesremainingt2]):
        daytradesremainingt3 (Union[Unset, PortfolioSummaryDaytradesremainingt3]):
        daytradesremainingt4 (Union[Unset, PortfolioSummaryDaytradesremainingt4]):
        daytradingstatus_s (Union[Unset, PortfolioSummaryDaytradingstatusS]):
        depositoncredithold (Union[Unset, PortfolioSummaryDepositoncredithold]):
        equitywithloanvalue (Union[Unset, PortfolioSummaryEquitywithloanvalue]):
        equitywithloanvalue_c (Union[Unset, PortfolioSummaryEquitywithloanvalueC]):
        equitywithloanvalue_s (Union[Unset, PortfolioSummaryEquitywithloanvalueS]):
        excessliquidity (Union[Unset, PortfolioSummaryExcessliquidity]):
        excessliquidity_c (Union[Unset, PortfolioSummaryExcessliquidityC]):
        excessliquidity_s (Union[Unset, PortfolioSummaryExcessliquidityS]):
        fullavailablefunds (Union[Unset, PortfolioSummaryFullavailablefunds]):
        fullavailablefunds_c (Union[Unset, PortfolioSummaryFullavailablefundsC]):
        fullavailablefunds_s (Union[Unset, PortfolioSummaryFullavailablefundsS]):
        fullexcessliquidity (Union[Unset, PortfolioSummaryFullexcessliquidity]):
        fullexcessliquidity_c (Union[Unset, PortfolioSummaryFullexcessliquidityC]):
        fullexcessliquidity_s (Union[Unset, PortfolioSummaryFullexcessliquidityS]):
        fullinitmarginreq (Union[Unset, PortfolioSummaryFullinitmarginreq]):
        fullinitmarginreq_c (Union[Unset, PortfolioSummaryFullinitmarginreqC]):
        fullinitmarginreq_s (Union[Unset, PortfolioSummaryFullinitmarginreqS]):
        fullmaintmarginreq (Union[Unset, PortfolioSummaryFullmaintmarginreq]):
        fullmaintmarginreq_c (Union[Unset, PortfolioSummaryFullmaintmarginreqC]):
        fullmaintmarginreq_s (Union[Unset, PortfolioSummaryFullmaintmarginreqS]):
        grosspositionvalue (Union[Unset, PortfolioSummaryGrosspositionvalue]):
        grosspositionvalue_s (Union[Unset, PortfolioSummaryGrosspositionvalueS]):
        guarantee (Union[Unset, PortfolioSummaryGuarantee]):
        guarantee_c (Union[Unset, PortfolioSummaryGuaranteeC]):
        guarantee_s (Union[Unset, PortfolioSummaryGuaranteeS]):
        highestseverity (Union[Unset, PortfolioSummaryHighestseverity]):
        indianstockhaircut (Union[Unset, PortfolioSummaryIndianstockhaircut]):
        indianstockhaircut_c (Union[Unset, PortfolioSummaryIndianstockhaircutC]):
        indianstockhaircut_s (Union[Unset, PortfolioSummaryIndianstockhaircutS]):
        initmarginreq (Union[Unset, PortfolioSummaryInitmarginreq]):
        initmarginreq_c (Union[Unset, PortfolioSummaryInitmarginreqC]):
        initmarginreq_s (Union[Unset, PortfolioSummaryInitmarginreqS]):
        leverage_s (Union[Unset, PortfolioSummaryLeverageS]):
        lookaheadavailablefunds (Union[Unset, PortfolioSummaryLookaheadavailablefunds]):
        lookaheadavailablefunds_c (Union[Unset, PortfolioSummaryLookaheadavailablefundsC]):
        lookaheadavailablefunds_s (Union[Unset, PortfolioSummaryLookaheadavailablefundsS]):
        lookaheadexcessliquidity (Union[Unset, PortfolioSummaryLookaheadexcessliquidity]):
        lookaheadexcessliquidity_c (Union[Unset, PortfolioSummaryLookaheadexcessliquidityC]):
        lookaheadexcessliquidity_s (Union[Unset, PortfolioSummaryLookaheadexcessliquidityS]):
        lookaheadinitmarginreq (Union[Unset, PortfolioSummaryLookaheadinitmarginreq]):
        lookaheadinitmarginreq_c (Union[Unset, PortfolioSummaryLookaheadinitmarginreqC]):
        lookaheadinitmarginreq_s (Union[Unset, PortfolioSummaryLookaheadinitmarginreqS]):
        lookaheadmaintmarginreq (Union[Unset, PortfolioSummaryLookaheadmaintmarginreq]):
        lookaheadmaintmarginreq_c (Union[Unset, PortfolioSummaryLookaheadmaintmarginreqC]):
        lookaheadmaintmarginreq_s (Union[Unset, PortfolioSummaryLookaheadmaintmarginreqS]):
        lookaheadnextchange (Union[Unset, PortfolioSummaryLookaheadnextchange]):
        maintmarginreq (Union[Unset, PortfolioSummaryMaintmarginreq]):
        maintmarginreq_c (Union[Unset, PortfolioSummaryMaintmarginreqC]):
        maintmarginreq_s (Union[Unset, PortfolioSummaryMaintmarginreqS]):
        netliquidation (Union[Unset, PortfolioSummaryNetliquidation]):
        netliquidation_c (Union[Unset, PortfolioSummaryNetliquidationC]):
        netliquidation_s (Union[Unset, PortfolioSummaryNetliquidationS]):
        netliquidationuncertainty (Union[Unset, PortfolioSummaryNetliquidationuncertainty]):
        nlvandmargininreview (Union[Unset, PortfolioSummaryNlvandmargininreview]):
        pasharesvalue (Union[Unset, PortfolioSummaryPasharesvalue]):
        pasharesvalue_c (Union[Unset, PortfolioSummaryPasharesvalueC]):
        pasharesvalue_s (Union[Unset, PortfolioSummaryPasharesvalueS]):
        physicalcertificatevalue (Union[Unset, PortfolioSummaryPhysicalcertificatevalue]):
        physicalcertificatevalue_c (Union[Unset, PortfolioSummaryPhysicalcertificatevalueC]):
        physicalcertificatevalue_s (Union[Unset, PortfolioSummaryPhysicalcertificatevalueS]):
        postexpirationexcess (Union[Unset, PortfolioSummaryPostexpirationexcess]):
        postexpirationexcess_c (Union[Unset, PortfolioSummaryPostexpirationexcessC]):
        postexpirationexcess_s (Union[Unset, PortfolioSummaryPostexpirationexcessS]):
        postexpirationmargin (Union[Unset, PortfolioSummaryPostexpirationmargin]):
        postexpirationmargin_c (Union[Unset, PortfolioSummaryPostexpirationmarginC]):
        postexpirationmargin_s (Union[Unset, PortfolioSummaryPostexpirationmarginS]):
        previousdayequitywithloanvalue (Union[Unset, PortfolioSummaryPreviousdayequitywithloanvalue]):
        previousdayequitywithloanvalue_s (Union[Unset, PortfolioSummaryPreviousdayequitywithloanvalueS]):
        regtequity (Union[Unset, PortfolioSummaryRegtequity]):
        regtequity_s (Union[Unset, PortfolioSummaryRegtequityS]):
        regtmargin (Union[Unset, PortfolioSummaryRegtmargin]):
        regtmargin_s (Union[Unset, PortfolioSummaryRegtmarginS]):
        segmenttitle_c (Union[Unset, PortfolioSummarySegmenttitleC]):
        segmenttitle_s (Union[Unset, PortfolioSummarySegmenttitleS]):
        sma (Union[Unset, PortfolioSummarySma]):
        sma_s (Union[Unset, PortfolioSummarySmaS]):
        totalcashvalue (Union[Unset, PortfolioSummaryTotalcashvalue]):
        totalcashvalue_c (Union[Unset, PortfolioSummaryTotalcashvalueC]):
        totalcashvalue_s (Union[Unset, PortfolioSummaryTotalcashvalueS]):
        totaldebitcardpendingcharges (Union[Unset, PortfolioSummaryTotaldebitcardpendingcharges]):
        totaldebitcardpendingcharges_c (Union[Unset, PortfolioSummaryTotaldebitcardpendingchargesC]):
        totaldebitcardpendingcharges_s (Union[Unset, PortfolioSummaryTotaldebitcardpendingchargesS]):
        tradingtype_s (Union[Unset, PortfolioSummaryTradingtypeS]):
        whatifpmenabled (Union[Unset, PortfolioSummaryWhatifpmenabled]):
    """

    accountcode: Union[Unset, "PortfolioSummaryAccountcode"] = UNSET
    accountready: Union[Unset, "PortfolioSummaryAccountready"] = UNSET
    accounttype: Union[Unset, "PortfolioSummaryAccounttype"] = UNSET
    accruedcash: Union[Unset, "PortfolioSummaryAccruedcash"] = UNSET
    accruedcash_c: Union[Unset, "PortfolioSummaryAccruedcashC"] = UNSET
    accruedcash_s: Union[Unset, "PortfolioSummaryAccruedcashS"] = UNSET
    accrueddividend: Union[Unset, "PortfolioSummaryAccrueddividend"] = UNSET
    accrueddividend_c: Union[Unset, "PortfolioSummaryAccrueddividendC"] = UNSET
    accrueddividend_s: Union[Unset, "PortfolioSummaryAccrueddividendS"] = UNSET
    availablefunds: Union[Unset, "PortfolioSummaryAvailablefunds"] = UNSET
    availablefunds_c: Union[Unset, "PortfolioSummaryAvailablefundsC"] = UNSET
    availablefunds_s: Union[Unset, "PortfolioSummaryAvailablefundsS"] = UNSET
    availabletotrade: Union[Unset, "PortfolioSummaryAvailabletotrade"] = UNSET
    availabletotrade_c: Union[Unset, "PortfolioSummaryAvailabletotradeC"] = UNSET
    availabletotrade_s: Union[Unset, "PortfolioSummaryAvailabletotradeS"] = UNSET
    availabletowithdraw: Union[Unset, "PortfolioSummaryAvailabletowithdraw"] = UNSET
    availabletowithdraw_c: Union[Unset, "PortfolioSummaryAvailabletowithdrawC"] = UNSET
    availabletowithdraw_s: Union[Unset, "PortfolioSummaryAvailabletowithdrawS"] = UNSET
    billable: Union[Unset, "PortfolioSummaryBillable"] = UNSET
    billable_c: Union[Unset, "PortfolioSummaryBillableC"] = UNSET
    billable_s: Union[Unset, "PortfolioSummaryBillableS"] = UNSET
    buyingpower: Union[Unset, "PortfolioSummaryBuyingpower"] = UNSET
    columnprio_c: Union[Unset, "PortfolioSummaryColumnprioC"] = UNSET
    columnprio_s: Union[Unset, "PortfolioSummaryColumnprioS"] = UNSET
    cushion: Union[Unset, "PortfolioSummaryCushion"] = UNSET
    daytradesremaining: Union[Unset, "PortfolioSummaryDaytradesremaining"] = UNSET
    daytradesremainingt1: Union[Unset, "PortfolioSummaryDaytradesremainingt1"] = UNSET
    daytradesremainingt2: Union[Unset, "PortfolioSummaryDaytradesremainingt2"] = UNSET
    daytradesremainingt3: Union[Unset, "PortfolioSummaryDaytradesremainingt3"] = UNSET
    daytradesremainingt4: Union[Unset, "PortfolioSummaryDaytradesremainingt4"] = UNSET
    daytradingstatus_s: Union[Unset, "PortfolioSummaryDaytradingstatusS"] = UNSET
    depositoncredithold: Union[Unset, "PortfolioSummaryDepositoncredithold"] = UNSET
    equitywithloanvalue: Union[Unset, "PortfolioSummaryEquitywithloanvalue"] = UNSET
    equitywithloanvalue_c: Union[Unset, "PortfolioSummaryEquitywithloanvalueC"] = UNSET
    equitywithloanvalue_s: Union[Unset, "PortfolioSummaryEquitywithloanvalueS"] = UNSET
    excessliquidity: Union[Unset, "PortfolioSummaryExcessliquidity"] = UNSET
    excessliquidity_c: Union[Unset, "PortfolioSummaryExcessliquidityC"] = UNSET
    excessliquidity_s: Union[Unset, "PortfolioSummaryExcessliquidityS"] = UNSET
    fullavailablefunds: Union[Unset, "PortfolioSummaryFullavailablefunds"] = UNSET
    fullavailablefunds_c: Union[Unset, "PortfolioSummaryFullavailablefundsC"] = UNSET
    fullavailablefunds_s: Union[Unset, "PortfolioSummaryFullavailablefundsS"] = UNSET
    fullexcessliquidity: Union[Unset, "PortfolioSummaryFullexcessliquidity"] = UNSET
    fullexcessliquidity_c: Union[Unset, "PortfolioSummaryFullexcessliquidityC"] = UNSET
    fullexcessliquidity_s: Union[Unset, "PortfolioSummaryFullexcessliquidityS"] = UNSET
    fullinitmarginreq: Union[Unset, "PortfolioSummaryFullinitmarginreq"] = UNSET
    fullinitmarginreq_c: Union[Unset, "PortfolioSummaryFullinitmarginreqC"] = UNSET
    fullinitmarginreq_s: Union[Unset, "PortfolioSummaryFullinitmarginreqS"] = UNSET
    fullmaintmarginreq: Union[Unset, "PortfolioSummaryFullmaintmarginreq"] = UNSET
    fullmaintmarginreq_c: Union[Unset, "PortfolioSummaryFullmaintmarginreqC"] = UNSET
    fullmaintmarginreq_s: Union[Unset, "PortfolioSummaryFullmaintmarginreqS"] = UNSET
    grosspositionvalue: Union[Unset, "PortfolioSummaryGrosspositionvalue"] = UNSET
    grosspositionvalue_s: Union[Unset, "PortfolioSummaryGrosspositionvalueS"] = UNSET
    guarantee: Union[Unset, "PortfolioSummaryGuarantee"] = UNSET
    guarantee_c: Union[Unset, "PortfolioSummaryGuaranteeC"] = UNSET
    guarantee_s: Union[Unset, "PortfolioSummaryGuaranteeS"] = UNSET
    highestseverity: Union[Unset, "PortfolioSummaryHighestseverity"] = UNSET
    indianstockhaircut: Union[Unset, "PortfolioSummaryIndianstockhaircut"] = UNSET
    indianstockhaircut_c: Union[Unset, "PortfolioSummaryIndianstockhaircutC"] = UNSET
    indianstockhaircut_s: Union[Unset, "PortfolioSummaryIndianstockhaircutS"] = UNSET
    initmarginreq: Union[Unset, "PortfolioSummaryInitmarginreq"] = UNSET
    initmarginreq_c: Union[Unset, "PortfolioSummaryInitmarginreqC"] = UNSET
    initmarginreq_s: Union[Unset, "PortfolioSummaryInitmarginreqS"] = UNSET
    leverage_s: Union[Unset, "PortfolioSummaryLeverageS"] = UNSET
    lookaheadavailablefunds: Union[Unset, "PortfolioSummaryLookaheadavailablefunds"] = UNSET
    lookaheadavailablefunds_c: Union[Unset, "PortfolioSummaryLookaheadavailablefundsC"] = UNSET
    lookaheadavailablefunds_s: Union[Unset, "PortfolioSummaryLookaheadavailablefundsS"] = UNSET
    lookaheadexcessliquidity: Union[Unset, "PortfolioSummaryLookaheadexcessliquidity"] = UNSET
    lookaheadexcessliquidity_c: Union[Unset, "PortfolioSummaryLookaheadexcessliquidityC"] = UNSET
    lookaheadexcessliquidity_s: Union[Unset, "PortfolioSummaryLookaheadexcessliquidityS"] = UNSET
    lookaheadinitmarginreq: Union[Unset, "PortfolioSummaryLookaheadinitmarginreq"] = UNSET
    lookaheadinitmarginreq_c: Union[Unset, "PortfolioSummaryLookaheadinitmarginreqC"] = UNSET
    lookaheadinitmarginreq_s: Union[Unset, "PortfolioSummaryLookaheadinitmarginreqS"] = UNSET
    lookaheadmaintmarginreq: Union[Unset, "PortfolioSummaryLookaheadmaintmarginreq"] = UNSET
    lookaheadmaintmarginreq_c: Union[Unset, "PortfolioSummaryLookaheadmaintmarginreqC"] = UNSET
    lookaheadmaintmarginreq_s: Union[Unset, "PortfolioSummaryLookaheadmaintmarginreqS"] = UNSET
    lookaheadnextchange: Union[Unset, "PortfolioSummaryLookaheadnextchange"] = UNSET
    maintmarginreq: Union[Unset, "PortfolioSummaryMaintmarginreq"] = UNSET
    maintmarginreq_c: Union[Unset, "PortfolioSummaryMaintmarginreqC"] = UNSET
    maintmarginreq_s: Union[Unset, "PortfolioSummaryMaintmarginreqS"] = UNSET
    netliquidation: Union[Unset, "PortfolioSummaryNetliquidation"] = UNSET
    netliquidation_c: Union[Unset, "PortfolioSummaryNetliquidationC"] = UNSET
    netliquidation_s: Union[Unset, "PortfolioSummaryNetliquidationS"] = UNSET
    netliquidationuncertainty: Union[Unset, "PortfolioSummaryNetliquidationuncertainty"] = UNSET
    nlvandmargininreview: Union[Unset, "PortfolioSummaryNlvandmargininreview"] = UNSET
    pasharesvalue: Union[Unset, "PortfolioSummaryPasharesvalue"] = UNSET
    pasharesvalue_c: Union[Unset, "PortfolioSummaryPasharesvalueC"] = UNSET
    pasharesvalue_s: Union[Unset, "PortfolioSummaryPasharesvalueS"] = UNSET
    physicalcertificatevalue: Union[Unset, "PortfolioSummaryPhysicalcertificatevalue"] = UNSET
    physicalcertificatevalue_c: Union[Unset, "PortfolioSummaryPhysicalcertificatevalueC"] = UNSET
    physicalcertificatevalue_s: Union[Unset, "PortfolioSummaryPhysicalcertificatevalueS"] = UNSET
    postexpirationexcess: Union[Unset, "PortfolioSummaryPostexpirationexcess"] = UNSET
    postexpirationexcess_c: Union[Unset, "PortfolioSummaryPostexpirationexcessC"] = UNSET
    postexpirationexcess_s: Union[Unset, "PortfolioSummaryPostexpirationexcessS"] = UNSET
    postexpirationmargin: Union[Unset, "PortfolioSummaryPostexpirationmargin"] = UNSET
    postexpirationmargin_c: Union[Unset, "PortfolioSummaryPostexpirationmarginC"] = UNSET
    postexpirationmargin_s: Union[Unset, "PortfolioSummaryPostexpirationmarginS"] = UNSET
    previousdayequitywithloanvalue: Union[Unset, "PortfolioSummaryPreviousdayequitywithloanvalue"] = UNSET
    previousdayequitywithloanvalue_s: Union[Unset, "PortfolioSummaryPreviousdayequitywithloanvalueS"] = UNSET
    regtequity: Union[Unset, "PortfolioSummaryRegtequity"] = UNSET
    regtequity_s: Union[Unset, "PortfolioSummaryRegtequityS"] = UNSET
    regtmargin: Union[Unset, "PortfolioSummaryRegtmargin"] = UNSET
    regtmargin_s: Union[Unset, "PortfolioSummaryRegtmarginS"] = UNSET
    segmenttitle_c: Union[Unset, "PortfolioSummarySegmenttitleC"] = UNSET
    segmenttitle_s: Union[Unset, "PortfolioSummarySegmenttitleS"] = UNSET
    sma: Union[Unset, "PortfolioSummarySma"] = UNSET
    sma_s: Union[Unset, "PortfolioSummarySmaS"] = UNSET
    totalcashvalue: Union[Unset, "PortfolioSummaryTotalcashvalue"] = UNSET
    totalcashvalue_c: Union[Unset, "PortfolioSummaryTotalcashvalueC"] = UNSET
    totalcashvalue_s: Union[Unset, "PortfolioSummaryTotalcashvalueS"] = UNSET
    totaldebitcardpendingcharges: Union[Unset, "PortfolioSummaryTotaldebitcardpendingcharges"] = UNSET
    totaldebitcardpendingcharges_c: Union[Unset, "PortfolioSummaryTotaldebitcardpendingchargesC"] = UNSET
    totaldebitcardpendingcharges_s: Union[Unset, "PortfolioSummaryTotaldebitcardpendingchargesS"] = UNSET
    tradingtype_s: Union[Unset, "PortfolioSummaryTradingtypeS"] = UNSET
    whatifpmenabled: Union[Unset, "PortfolioSummaryWhatifpmenabled"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.portfolio_summary_accruedcash_s import PortfolioSummaryAccruedcashS
        from ..models.portfolio_summary_whatifpmenabled import PortfolioSummaryWhatifpmenabled
        from ..models.portfolio_summary_physicalcertificatevalue import PortfolioSummaryPhysicalcertificatevalue
        from ..models.portfolio_summary_fullmaintmarginreq_s import PortfolioSummaryFullmaintmarginreqS
        from ..models.portfolio_summary_segmenttitle_c import PortfolioSummarySegmenttitleC
        from ..models.portfolio_summary_accrueddividend_s import PortfolioSummaryAccrueddividendS
        from ..models.portfolio_summary_lookaheadmaintmarginreq_c import PortfolioSummaryLookaheadmaintmarginreqC
        from ..models.portfolio_summary_totalcashvalue_s import PortfolioSummaryTotalcashvalueS
        from ..models.portfolio_summary_accrueddividend import PortfolioSummaryAccrueddividend
        from ..models.portfolio_summary_lookaheadinitmarginreq_s import PortfolioSummaryLookaheadinitmarginreqS
        from ..models.portfolio_summary_netliquidationuncertainty import PortfolioSummaryNetliquidationuncertainty
        from ..models.portfolio_summary_billable_c import PortfolioSummaryBillableC
        from ..models.portfolio_summary_leverage_s import PortfolioSummaryLeverageS
        from ..models.portfolio_summary_physicalcertificatevalue_c import PortfolioSummaryPhysicalcertificatevalueC

        accountcode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accountcode, Unset):
            accountcode = self.accountcode.to_dict()

        accountready: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accountready, Unset):
            accountready = self.accountready.to_dict()

        accounttype: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accounttype, Unset):
            accounttype = self.accounttype.to_dict()

        accruedcash: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accruedcash, Unset):
            accruedcash = self.accruedcash.to_dict()

        accruedcash_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accruedcash_c, Unset):
            accruedcash_c = self.accruedcash_c.to_dict()

        accruedcash_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accruedcash_s, Unset):
            accruedcash_s = self.accruedcash_s.to_dict()

        accrueddividend: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accrueddividend, Unset):
            accrueddividend = self.accrueddividend.to_dict()

        accrueddividend_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accrueddividend_c, Unset):
            accrueddividend_c = self.accrueddividend_c.to_dict()

        accrueddividend_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accrueddividend_s, Unset):
            accrueddividend_s = self.accrueddividend_s.to_dict()

        availablefunds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availablefunds, Unset):
            availablefunds = self.availablefunds.to_dict()

        availablefunds_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availablefunds_c, Unset):
            availablefunds_c = self.availablefunds_c.to_dict()

        availablefunds_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availablefunds_s, Unset):
            availablefunds_s = self.availablefunds_s.to_dict()

        availabletotrade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availabletotrade, Unset):
            availabletotrade = self.availabletotrade.to_dict()

        availabletotrade_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availabletotrade_c, Unset):
            availabletotrade_c = self.availabletotrade_c.to_dict()

        availabletotrade_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availabletotrade_s, Unset):
            availabletotrade_s = self.availabletotrade_s.to_dict()

        availabletowithdraw: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availabletowithdraw, Unset):
            availabletowithdraw = self.availabletowithdraw.to_dict()

        availabletowithdraw_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availabletowithdraw_c, Unset):
            availabletowithdraw_c = self.availabletowithdraw_c.to_dict()

        availabletowithdraw_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.availabletowithdraw_s, Unset):
            availabletowithdraw_s = self.availabletowithdraw_s.to_dict()

        billable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billable, Unset):
            billable = self.billable.to_dict()

        billable_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billable_c, Unset):
            billable_c = self.billable_c.to_dict()

        billable_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billable_s, Unset):
            billable_s = self.billable_s.to_dict()

        buyingpower: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyingpower, Unset):
            buyingpower = self.buyingpower.to_dict()

        columnprio_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.columnprio_c, Unset):
            columnprio_c = self.columnprio_c.to_dict()

        columnprio_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.columnprio_s, Unset):
            columnprio_s = self.columnprio_s.to_dict()

        cushion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cushion, Unset):
            cushion = self.cushion.to_dict()

        daytradesremaining: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daytradesremaining, Unset):
            daytradesremaining = self.daytradesremaining.to_dict()

        daytradesremainingt1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daytradesremainingt1, Unset):
            daytradesremainingt1 = self.daytradesremainingt1.to_dict()

        daytradesremainingt2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daytradesremainingt2, Unset):
            daytradesremainingt2 = self.daytradesremainingt2.to_dict()

        daytradesremainingt3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daytradesremainingt3, Unset):
            daytradesremainingt3 = self.daytradesremainingt3.to_dict()

        daytradesremainingt4: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daytradesremainingt4, Unset):
            daytradesremainingt4 = self.daytradesremainingt4.to_dict()

        daytradingstatus_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daytradingstatus_s, Unset):
            daytradingstatus_s = self.daytradingstatus_s.to_dict()

        depositoncredithold: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.depositoncredithold, Unset):
            depositoncredithold = self.depositoncredithold.to_dict()

        equitywithloanvalue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equitywithloanvalue, Unset):
            equitywithloanvalue = self.equitywithloanvalue.to_dict()

        equitywithloanvalue_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equitywithloanvalue_c, Unset):
            equitywithloanvalue_c = self.equitywithloanvalue_c.to_dict()

        equitywithloanvalue_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equitywithloanvalue_s, Unset):
            equitywithloanvalue_s = self.equitywithloanvalue_s.to_dict()

        excessliquidity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.excessliquidity, Unset):
            excessliquidity = self.excessliquidity.to_dict()

        excessliquidity_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.excessliquidity_c, Unset):
            excessliquidity_c = self.excessliquidity_c.to_dict()

        excessliquidity_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.excessliquidity_s, Unset):
            excessliquidity_s = self.excessliquidity_s.to_dict()

        fullavailablefunds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullavailablefunds, Unset):
            fullavailablefunds = self.fullavailablefunds.to_dict()

        fullavailablefunds_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullavailablefunds_c, Unset):
            fullavailablefunds_c = self.fullavailablefunds_c.to_dict()

        fullavailablefunds_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullavailablefunds_s, Unset):
            fullavailablefunds_s = self.fullavailablefunds_s.to_dict()

        fullexcessliquidity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullexcessliquidity, Unset):
            fullexcessliquidity = self.fullexcessliquidity.to_dict()

        fullexcessliquidity_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullexcessliquidity_c, Unset):
            fullexcessliquidity_c = self.fullexcessliquidity_c.to_dict()

        fullexcessliquidity_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullexcessliquidity_s, Unset):
            fullexcessliquidity_s = self.fullexcessliquidity_s.to_dict()

        fullinitmarginreq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullinitmarginreq, Unset):
            fullinitmarginreq = self.fullinitmarginreq.to_dict()

        fullinitmarginreq_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullinitmarginreq_c, Unset):
            fullinitmarginreq_c = self.fullinitmarginreq_c.to_dict()

        fullinitmarginreq_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullinitmarginreq_s, Unset):
            fullinitmarginreq_s = self.fullinitmarginreq_s.to_dict()

        fullmaintmarginreq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullmaintmarginreq, Unset):
            fullmaintmarginreq = self.fullmaintmarginreq.to_dict()

        fullmaintmarginreq_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullmaintmarginreq_c, Unset):
            fullmaintmarginreq_c = self.fullmaintmarginreq_c.to_dict()

        fullmaintmarginreq_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fullmaintmarginreq_s, Unset):
            fullmaintmarginreq_s = self.fullmaintmarginreq_s.to_dict()

        grosspositionvalue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grosspositionvalue, Unset):
            grosspositionvalue = self.grosspositionvalue.to_dict()

        grosspositionvalue_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grosspositionvalue_s, Unset):
            grosspositionvalue_s = self.grosspositionvalue_s.to_dict()

        guarantee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guarantee, Unset):
            guarantee = self.guarantee.to_dict()

        guarantee_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guarantee_c, Unset):
            guarantee_c = self.guarantee_c.to_dict()

        guarantee_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guarantee_s, Unset):
            guarantee_s = self.guarantee_s.to_dict()

        highestseverity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.highestseverity, Unset):
            highestseverity = self.highestseverity.to_dict()

        indianstockhaircut: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indianstockhaircut, Unset):
            indianstockhaircut = self.indianstockhaircut.to_dict()

        indianstockhaircut_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indianstockhaircut_c, Unset):
            indianstockhaircut_c = self.indianstockhaircut_c.to_dict()

        indianstockhaircut_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indianstockhaircut_s, Unset):
            indianstockhaircut_s = self.indianstockhaircut_s.to_dict()

        initmarginreq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initmarginreq, Unset):
            initmarginreq = self.initmarginreq.to_dict()

        initmarginreq_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initmarginreq_c, Unset):
            initmarginreq_c = self.initmarginreq_c.to_dict()

        initmarginreq_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initmarginreq_s, Unset):
            initmarginreq_s = self.initmarginreq_s.to_dict()

        leverage_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leverage_s, Unset):
            leverage_s = self.leverage_s.to_dict()

        lookaheadavailablefunds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadavailablefunds, Unset):
            lookaheadavailablefunds = self.lookaheadavailablefunds.to_dict()

        lookaheadavailablefunds_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadavailablefunds_c, Unset):
            lookaheadavailablefunds_c = self.lookaheadavailablefunds_c.to_dict()

        lookaheadavailablefunds_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadavailablefunds_s, Unset):
            lookaheadavailablefunds_s = self.lookaheadavailablefunds_s.to_dict()

        lookaheadexcessliquidity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadexcessliquidity, Unset):
            lookaheadexcessliquidity = self.lookaheadexcessliquidity.to_dict()

        lookaheadexcessliquidity_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadexcessliquidity_c, Unset):
            lookaheadexcessliquidity_c = self.lookaheadexcessliquidity_c.to_dict()

        lookaheadexcessliquidity_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadexcessliquidity_s, Unset):
            lookaheadexcessliquidity_s = self.lookaheadexcessliquidity_s.to_dict()

        lookaheadinitmarginreq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadinitmarginreq, Unset):
            lookaheadinitmarginreq = self.lookaheadinitmarginreq.to_dict()

        lookaheadinitmarginreq_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadinitmarginreq_c, Unset):
            lookaheadinitmarginreq_c = self.lookaheadinitmarginreq_c.to_dict()

        lookaheadinitmarginreq_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadinitmarginreq_s, Unset):
            lookaheadinitmarginreq_s = self.lookaheadinitmarginreq_s.to_dict()

        lookaheadmaintmarginreq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadmaintmarginreq, Unset):
            lookaheadmaintmarginreq = self.lookaheadmaintmarginreq.to_dict()

        lookaheadmaintmarginreq_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadmaintmarginreq_c, Unset):
            lookaheadmaintmarginreq_c = self.lookaheadmaintmarginreq_c.to_dict()

        lookaheadmaintmarginreq_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadmaintmarginreq_s, Unset):
            lookaheadmaintmarginreq_s = self.lookaheadmaintmarginreq_s.to_dict()

        lookaheadnextchange: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lookaheadnextchange, Unset):
            lookaheadnextchange = self.lookaheadnextchange.to_dict()

        maintmarginreq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maintmarginreq, Unset):
            maintmarginreq = self.maintmarginreq.to_dict()

        maintmarginreq_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maintmarginreq_c, Unset):
            maintmarginreq_c = self.maintmarginreq_c.to_dict()

        maintmarginreq_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maintmarginreq_s, Unset):
            maintmarginreq_s = self.maintmarginreq_s.to_dict()

        netliquidation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.netliquidation, Unset):
            netliquidation = self.netliquidation.to_dict()

        netliquidation_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.netliquidation_c, Unset):
            netliquidation_c = self.netliquidation_c.to_dict()

        netliquidation_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.netliquidation_s, Unset):
            netliquidation_s = self.netliquidation_s.to_dict()

        netliquidationuncertainty: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.netliquidationuncertainty, Unset):
            netliquidationuncertainty = self.netliquidationuncertainty.to_dict()

        nlvandmargininreview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nlvandmargininreview, Unset):
            nlvandmargininreview = self.nlvandmargininreview.to_dict()

        pasharesvalue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pasharesvalue, Unset):
            pasharesvalue = self.pasharesvalue.to_dict()

        pasharesvalue_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pasharesvalue_c, Unset):
            pasharesvalue_c = self.pasharesvalue_c.to_dict()

        pasharesvalue_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pasharesvalue_s, Unset):
            pasharesvalue_s = self.pasharesvalue_s.to_dict()

        physicalcertificatevalue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.physicalcertificatevalue, Unset):
            physicalcertificatevalue = self.physicalcertificatevalue.to_dict()

        physicalcertificatevalue_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.physicalcertificatevalue_c, Unset):
            physicalcertificatevalue_c = self.physicalcertificatevalue_c.to_dict()

        physicalcertificatevalue_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.physicalcertificatevalue_s, Unset):
            physicalcertificatevalue_s = self.physicalcertificatevalue_s.to_dict()

        postexpirationexcess: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postexpirationexcess, Unset):
            postexpirationexcess = self.postexpirationexcess.to_dict()

        postexpirationexcess_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postexpirationexcess_c, Unset):
            postexpirationexcess_c = self.postexpirationexcess_c.to_dict()

        postexpirationexcess_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postexpirationexcess_s, Unset):
            postexpirationexcess_s = self.postexpirationexcess_s.to_dict()

        postexpirationmargin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postexpirationmargin, Unset):
            postexpirationmargin = self.postexpirationmargin.to_dict()

        postexpirationmargin_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postexpirationmargin_c, Unset):
            postexpirationmargin_c = self.postexpirationmargin_c.to_dict()

        postexpirationmargin_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postexpirationmargin_s, Unset):
            postexpirationmargin_s = self.postexpirationmargin_s.to_dict()

        previousdayequitywithloanvalue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previousdayequitywithloanvalue, Unset):
            previousdayequitywithloanvalue = self.previousdayequitywithloanvalue.to_dict()

        previousdayequitywithloanvalue_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previousdayequitywithloanvalue_s, Unset):
            previousdayequitywithloanvalue_s = self.previousdayequitywithloanvalue_s.to_dict()

        regtequity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regtequity, Unset):
            regtequity = self.regtequity.to_dict()

        regtequity_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regtequity_s, Unset):
            regtequity_s = self.regtequity_s.to_dict()

        regtmargin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regtmargin, Unset):
            regtmargin = self.regtmargin.to_dict()

        regtmargin_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regtmargin_s, Unset):
            regtmargin_s = self.regtmargin_s.to_dict()

        segmenttitle_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.segmenttitle_c, Unset):
            segmenttitle_c = self.segmenttitle_c.to_dict()

        segmenttitle_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.segmenttitle_s, Unset):
            segmenttitle_s = self.segmenttitle_s.to_dict()

        sma: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sma, Unset):
            sma = self.sma.to_dict()

        sma_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sma_s, Unset):
            sma_s = self.sma_s.to_dict()

        totalcashvalue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totalcashvalue, Unset):
            totalcashvalue = self.totalcashvalue.to_dict()

        totalcashvalue_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totalcashvalue_c, Unset):
            totalcashvalue_c = self.totalcashvalue_c.to_dict()

        totalcashvalue_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totalcashvalue_s, Unset):
            totalcashvalue_s = self.totalcashvalue_s.to_dict()

        totaldebitcardpendingcharges: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totaldebitcardpendingcharges, Unset):
            totaldebitcardpendingcharges = self.totaldebitcardpendingcharges.to_dict()

        totaldebitcardpendingcharges_c: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totaldebitcardpendingcharges_c, Unset):
            totaldebitcardpendingcharges_c = self.totaldebitcardpendingcharges_c.to_dict()

        totaldebitcardpendingcharges_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totaldebitcardpendingcharges_s, Unset):
            totaldebitcardpendingcharges_s = self.totaldebitcardpendingcharges_s.to_dict()

        tradingtype_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tradingtype_s, Unset):
            tradingtype_s = self.tradingtype_s.to_dict()

        whatifpmenabled: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.whatifpmenabled, Unset):
            whatifpmenabled = self.whatifpmenabled.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accountcode is not UNSET:
            field_dict["accountcode"] = accountcode
        if accountready is not UNSET:
            field_dict["accountready"] = accountready
        if accounttype is not UNSET:
            field_dict["accounttype"] = accounttype
        if accruedcash is not UNSET:
            field_dict["accruedcash"] = accruedcash
        if accruedcash_c is not UNSET:
            field_dict["accruedcash-c"] = accruedcash_c
        if accruedcash_s is not UNSET:
            field_dict["accruedcash-s"] = accruedcash_s
        if accrueddividend is not UNSET:
            field_dict["accrueddividend"] = accrueddividend
        if accrueddividend_c is not UNSET:
            field_dict["accrueddividend-c"] = accrueddividend_c
        if accrueddividend_s is not UNSET:
            field_dict["accrueddividend-s"] = accrueddividend_s
        if availablefunds is not UNSET:
            field_dict["availablefunds"] = availablefunds
        if availablefunds_c is not UNSET:
            field_dict["availablefunds-c"] = availablefunds_c
        if availablefunds_s is not UNSET:
            field_dict["availablefunds-s"] = availablefunds_s
        if availabletotrade is not UNSET:
            field_dict["availabletotrade"] = availabletotrade
        if availabletotrade_c is not UNSET:
            field_dict["availabletotrade-c"] = availabletotrade_c
        if availabletotrade_s is not UNSET:
            field_dict["availabletotrade-s"] = availabletotrade_s
        if availabletowithdraw is not UNSET:
            field_dict["availabletowithdraw"] = availabletowithdraw
        if availabletowithdraw_c is not UNSET:
            field_dict["availabletowithdraw-c"] = availabletowithdraw_c
        if availabletowithdraw_s is not UNSET:
            field_dict["availabletowithdraw-s"] = availabletowithdraw_s
        if billable is not UNSET:
            field_dict["billable"] = billable
        if billable_c is not UNSET:
            field_dict["billable-c"] = billable_c
        if billable_s is not UNSET:
            field_dict["billable-s"] = billable_s
        if buyingpower is not UNSET:
            field_dict["buyingpower"] = buyingpower
        if columnprio_c is not UNSET:
            field_dict["columnprio-c"] = columnprio_c
        if columnprio_s is not UNSET:
            field_dict["columnprio-s"] = columnprio_s
        if cushion is not UNSET:
            field_dict["cushion"] = cushion
        if daytradesremaining is not UNSET:
            field_dict["daytradesremaining"] = daytradesremaining
        if daytradesremainingt1 is not UNSET:
            field_dict["daytradesremainingt+1"] = daytradesremainingt1
        if daytradesremainingt2 is not UNSET:
            field_dict["daytradesremainingt+2"] = daytradesremainingt2
        if daytradesremainingt3 is not UNSET:
            field_dict["daytradesremainingt+3"] = daytradesremainingt3
        if daytradesremainingt4 is not UNSET:
            field_dict["daytradesremainingt+4"] = daytradesremainingt4
        if daytradingstatus_s is not UNSET:
            field_dict["daytradingstatus-s"] = daytradingstatus_s
        if depositoncredithold is not UNSET:
            field_dict["depositoncredithold"] = depositoncredithold
        if equitywithloanvalue is not UNSET:
            field_dict["equitywithloanvalue"] = equitywithloanvalue
        if equitywithloanvalue_c is not UNSET:
            field_dict["equitywithloanvalue-c"] = equitywithloanvalue_c
        if equitywithloanvalue_s is not UNSET:
            field_dict["equitywithloanvalue-s"] = equitywithloanvalue_s
        if excessliquidity is not UNSET:
            field_dict["excessliquidity"] = excessliquidity
        if excessliquidity_c is not UNSET:
            field_dict["excessliquidity-c"] = excessliquidity_c
        if excessliquidity_s is not UNSET:
            field_dict["excessliquidity-s"] = excessliquidity_s
        if fullavailablefunds is not UNSET:
            field_dict["fullavailablefunds"] = fullavailablefunds
        if fullavailablefunds_c is not UNSET:
            field_dict["fullavailablefunds-c"] = fullavailablefunds_c
        if fullavailablefunds_s is not UNSET:
            field_dict["fullavailablefunds-s"] = fullavailablefunds_s
        if fullexcessliquidity is not UNSET:
            field_dict["fullexcessliquidity"] = fullexcessliquidity
        if fullexcessliquidity_c is not UNSET:
            field_dict["fullexcessliquidity-c"] = fullexcessliquidity_c
        if fullexcessliquidity_s is not UNSET:
            field_dict["fullexcessliquidity-s"] = fullexcessliquidity_s
        if fullinitmarginreq is not UNSET:
            field_dict["fullinitmarginreq"] = fullinitmarginreq
        if fullinitmarginreq_c is not UNSET:
            field_dict["fullinitmarginreq-c"] = fullinitmarginreq_c
        if fullinitmarginreq_s is not UNSET:
            field_dict["fullinitmarginreq-s"] = fullinitmarginreq_s
        if fullmaintmarginreq is not UNSET:
            field_dict["fullmaintmarginreq"] = fullmaintmarginreq
        if fullmaintmarginreq_c is not UNSET:
            field_dict["fullmaintmarginreq-c"] = fullmaintmarginreq_c
        if fullmaintmarginreq_s is not UNSET:
            field_dict["fullmaintmarginreq-s"] = fullmaintmarginreq_s
        if grosspositionvalue is not UNSET:
            field_dict["grosspositionvalue"] = grosspositionvalue
        if grosspositionvalue_s is not UNSET:
            field_dict["grosspositionvalue-s"] = grosspositionvalue_s
        if guarantee is not UNSET:
            field_dict["guarantee"] = guarantee
        if guarantee_c is not UNSET:
            field_dict["guarantee-c"] = guarantee_c
        if guarantee_s is not UNSET:
            field_dict["guarantee-s"] = guarantee_s
        if highestseverity is not UNSET:
            field_dict["highestseverity"] = highestseverity
        if indianstockhaircut is not UNSET:
            field_dict["indianstockhaircut"] = indianstockhaircut
        if indianstockhaircut_c is not UNSET:
            field_dict["indianstockhaircut-c"] = indianstockhaircut_c
        if indianstockhaircut_s is not UNSET:
            field_dict["indianstockhaircut-s"] = indianstockhaircut_s
        if initmarginreq is not UNSET:
            field_dict["initmarginreq"] = initmarginreq
        if initmarginreq_c is not UNSET:
            field_dict["initmarginreq-c"] = initmarginreq_c
        if initmarginreq_s is not UNSET:
            field_dict["initmarginreq-s"] = initmarginreq_s
        if leverage_s is not UNSET:
            field_dict["leverage-s"] = leverage_s
        if lookaheadavailablefunds is not UNSET:
            field_dict["lookaheadavailablefunds"] = lookaheadavailablefunds
        if lookaheadavailablefunds_c is not UNSET:
            field_dict["lookaheadavailablefunds-c"] = lookaheadavailablefunds_c
        if lookaheadavailablefunds_s is not UNSET:
            field_dict["lookaheadavailablefunds-s"] = lookaheadavailablefunds_s
        if lookaheadexcessliquidity is not UNSET:
            field_dict["lookaheadexcessliquidity"] = lookaheadexcessliquidity
        if lookaheadexcessliquidity_c is not UNSET:
            field_dict["lookaheadexcessliquidity-c"] = lookaheadexcessliquidity_c
        if lookaheadexcessliquidity_s is not UNSET:
            field_dict["lookaheadexcessliquidity-s"] = lookaheadexcessliquidity_s
        if lookaheadinitmarginreq is not UNSET:
            field_dict["lookaheadinitmarginreq"] = lookaheadinitmarginreq
        if lookaheadinitmarginreq_c is not UNSET:
            field_dict["lookaheadinitmarginreq-c"] = lookaheadinitmarginreq_c
        if lookaheadinitmarginreq_s is not UNSET:
            field_dict["lookaheadinitmarginreq-s"] = lookaheadinitmarginreq_s
        if lookaheadmaintmarginreq is not UNSET:
            field_dict["lookaheadmaintmarginreq"] = lookaheadmaintmarginreq
        if lookaheadmaintmarginreq_c is not UNSET:
            field_dict["lookaheadmaintmarginreq-c"] = lookaheadmaintmarginreq_c
        if lookaheadmaintmarginreq_s is not UNSET:
            field_dict["lookaheadmaintmarginreq-s"] = lookaheadmaintmarginreq_s
        if lookaheadnextchange is not UNSET:
            field_dict["lookaheadnextchange"] = lookaheadnextchange
        if maintmarginreq is not UNSET:
            field_dict["maintmarginreq"] = maintmarginreq
        if maintmarginreq_c is not UNSET:
            field_dict["maintmarginreq-c"] = maintmarginreq_c
        if maintmarginreq_s is not UNSET:
            field_dict["maintmarginreq-s"] = maintmarginreq_s
        if netliquidation is not UNSET:
            field_dict["netliquidation"] = netliquidation
        if netliquidation_c is not UNSET:
            field_dict["netliquidation-c"] = netliquidation_c
        if netliquidation_s is not UNSET:
            field_dict["netliquidation-s"] = netliquidation_s
        if netliquidationuncertainty is not UNSET:
            field_dict["netliquidationuncertainty"] = netliquidationuncertainty
        if nlvandmargininreview is not UNSET:
            field_dict["nlvandmargininreview"] = nlvandmargininreview
        if pasharesvalue is not UNSET:
            field_dict["pasharesvalue"] = pasharesvalue
        if pasharesvalue_c is not UNSET:
            field_dict["pasharesvalue-c"] = pasharesvalue_c
        if pasharesvalue_s is not UNSET:
            field_dict["pasharesvalue-s"] = pasharesvalue_s
        if physicalcertificatevalue is not UNSET:
            field_dict["physicalcertificatevalue"] = physicalcertificatevalue
        if physicalcertificatevalue_c is not UNSET:
            field_dict["physicalcertificatevalue-c"] = physicalcertificatevalue_c
        if physicalcertificatevalue_s is not UNSET:
            field_dict["physicalcertificatevalue-s"] = physicalcertificatevalue_s
        if postexpirationexcess is not UNSET:
            field_dict["postexpirationexcess"] = postexpirationexcess
        if postexpirationexcess_c is not UNSET:
            field_dict["postexpirationexcess-c"] = postexpirationexcess_c
        if postexpirationexcess_s is not UNSET:
            field_dict["postexpirationexcess-s"] = postexpirationexcess_s
        if postexpirationmargin is not UNSET:
            field_dict["postexpirationmargin"] = postexpirationmargin
        if postexpirationmargin_c is not UNSET:
            field_dict["postexpirationmargin-c"] = postexpirationmargin_c
        if postexpirationmargin_s is not UNSET:
            field_dict["postexpirationmargin-s"] = postexpirationmargin_s
        if previousdayequitywithloanvalue is not UNSET:
            field_dict["previousdayequitywithloanvalue"] = previousdayequitywithloanvalue
        if previousdayequitywithloanvalue_s is not UNSET:
            field_dict["previousdayequitywithloanvalue-s"] = previousdayequitywithloanvalue_s
        if regtequity is not UNSET:
            field_dict["regtequity"] = regtequity
        if regtequity_s is not UNSET:
            field_dict["regtequity-s"] = regtequity_s
        if regtmargin is not UNSET:
            field_dict["regtmargin"] = regtmargin
        if regtmargin_s is not UNSET:
            field_dict["regtmargin-s"] = regtmargin_s
        if segmenttitle_c is not UNSET:
            field_dict["segmenttitle-c"] = segmenttitle_c
        if segmenttitle_s is not UNSET:
            field_dict["segmenttitle-s"] = segmenttitle_s
        if sma is not UNSET:
            field_dict["sma"] = sma
        if sma_s is not UNSET:
            field_dict["sma-s"] = sma_s
        if totalcashvalue is not UNSET:
            field_dict["totalcashvalue"] = totalcashvalue
        if totalcashvalue_c is not UNSET:
            field_dict["totalcashvalue-c"] = totalcashvalue_c
        if totalcashvalue_s is not UNSET:
            field_dict["totalcashvalue-s"] = totalcashvalue_s
        if totaldebitcardpendingcharges is not UNSET:
            field_dict["totaldebitcardpendingcharges"] = totaldebitcardpendingcharges
        if totaldebitcardpendingcharges_c is not UNSET:
            field_dict["totaldebitcardpendingcharges-c"] = totaldebitcardpendingcharges_c
        if totaldebitcardpendingcharges_s is not UNSET:
            field_dict["totaldebitcardpendingcharges-s"] = totaldebitcardpendingcharges_s
        if tradingtype_s is not UNSET:
            field_dict["tradingtype-s"] = tradingtype_s
        if whatifpmenabled is not UNSET:
            field_dict["whatifpmenabled"] = whatifpmenabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.portfolio_summary_accountcode import PortfolioSummaryAccountcode
        from ..models.portfolio_summary_accountready import PortfolioSummaryAccountready
        from ..models.portfolio_summary_accounttype import PortfolioSummaryAccounttype
        from ..models.portfolio_summary_accruedcash import PortfolioSummaryAccruedcash
        from ..models.portfolio_summary_accruedcash_c import PortfolioSummaryAccruedcashC
        from ..models.portfolio_summary_accruedcash_s import PortfolioSummaryAccruedcashS
        from ..models.portfolio_summary_accrueddividend import PortfolioSummaryAccrueddividend
        from ..models.portfolio_summary_accrueddividend_c import PortfolioSummaryAccrueddividendC
        from ..models.portfolio_summary_accrueddividend_s import PortfolioSummaryAccrueddividendS
        from ..models.portfolio_summary_availablefunds import PortfolioSummaryAvailablefunds
        from ..models.portfolio_summary_availablefunds_c import PortfolioSummaryAvailablefundsC
        from ..models.portfolio_summary_availablefunds_s import PortfolioSummaryAvailablefundsS
        from ..models.portfolio_summary_availabletotrade import PortfolioSummaryAvailabletotrade
        from ..models.portfolio_summary_availabletotrade_c import PortfolioSummaryAvailabletotradeC
        from ..models.portfolio_summary_availabletotrade_s import PortfolioSummaryAvailabletotradeS
        from ..models.portfolio_summary_availabletowithdraw import PortfolioSummaryAvailabletowithdraw
        from ..models.portfolio_summary_availabletowithdraw_c import PortfolioSummaryAvailabletowithdrawC
        from ..models.portfolio_summary_availabletowithdraw_s import PortfolioSummaryAvailabletowithdrawS
        from ..models.portfolio_summary_billable import PortfolioSummaryBillable
        from ..models.portfolio_summary_billable_c import PortfolioSummaryBillableC
        from ..models.portfolio_summary_billable_s import PortfolioSummaryBillableS
        from ..models.portfolio_summary_buyingpower import PortfolioSummaryBuyingpower
        from ..models.portfolio_summary_columnprio_c import PortfolioSummaryColumnprioC
        from ..models.portfolio_summary_columnprio_s import PortfolioSummaryColumnprioS
        from ..models.portfolio_summary_cushion import PortfolioSummaryCushion
        from ..models.portfolio_summary_daytradesremaining import PortfolioSummaryDaytradesremaining
        from ..models.portfolio_summary_daytradesremainingt_1 import PortfolioSummaryDaytradesremainingt1
        from ..models.portfolio_summary_daytradesremainingt_2 import PortfolioSummaryDaytradesremainingt2
        from ..models.portfolio_summary_daytradesremainingt_3 import PortfolioSummaryDaytradesremainingt3
        from ..models.portfolio_summary_daytradesremainingt_4 import PortfolioSummaryDaytradesremainingt4
        from ..models.portfolio_summary_daytradingstatus_s import PortfolioSummaryDaytradingstatusS
        from ..models.portfolio_summary_depositoncredithold import PortfolioSummaryDepositoncredithold
        from ..models.portfolio_summary_equitywithloanvalue import PortfolioSummaryEquitywithloanvalue
        from ..models.portfolio_summary_equitywithloanvalue_c import PortfolioSummaryEquitywithloanvalueC
        from ..models.portfolio_summary_equitywithloanvalue_s import PortfolioSummaryEquitywithloanvalueS
        from ..models.portfolio_summary_excessliquidity import PortfolioSummaryExcessliquidity
        from ..models.portfolio_summary_excessliquidity_c import PortfolioSummaryExcessliquidityC
        from ..models.portfolio_summary_excessliquidity_s import PortfolioSummaryExcessliquidityS
        from ..models.portfolio_summary_fullavailablefunds import PortfolioSummaryFullavailablefunds
        from ..models.portfolio_summary_fullavailablefunds_c import PortfolioSummaryFullavailablefundsC
        from ..models.portfolio_summary_fullavailablefunds_s import PortfolioSummaryFullavailablefundsS
        from ..models.portfolio_summary_fullexcessliquidity import PortfolioSummaryFullexcessliquidity
        from ..models.portfolio_summary_fullexcessliquidity_c import PortfolioSummaryFullexcessliquidityC
        from ..models.portfolio_summary_fullexcessliquidity_s import PortfolioSummaryFullexcessliquidityS
        from ..models.portfolio_summary_fullinitmarginreq import PortfolioSummaryFullinitmarginreq
        from ..models.portfolio_summary_fullinitmarginreq_c import PortfolioSummaryFullinitmarginreqC
        from ..models.portfolio_summary_fullinitmarginreq_s import PortfolioSummaryFullinitmarginreqS
        from ..models.portfolio_summary_fullmaintmarginreq import PortfolioSummaryFullmaintmarginreq
        from ..models.portfolio_summary_fullmaintmarginreq_c import PortfolioSummaryFullmaintmarginreqC
        from ..models.portfolio_summary_fullmaintmarginreq_s import PortfolioSummaryFullmaintmarginreqS
        from ..models.portfolio_summary_grosspositionvalue import PortfolioSummaryGrosspositionvalue
        from ..models.portfolio_summary_grosspositionvalue_s import PortfolioSummaryGrosspositionvalueS
        from ..models.portfolio_summary_guarantee import PortfolioSummaryGuarantee
        from ..models.portfolio_summary_guarantee_c import PortfolioSummaryGuaranteeC
        from ..models.portfolio_summary_guarantee_s import PortfolioSummaryGuaranteeS
        from ..models.portfolio_summary_highestseverity import PortfolioSummaryHighestseverity
        from ..models.portfolio_summary_indianstockhaircut import PortfolioSummaryIndianstockhaircut
        from ..models.portfolio_summary_indianstockhaircut_c import PortfolioSummaryIndianstockhaircutC
        from ..models.portfolio_summary_indianstockhaircut_s import PortfolioSummaryIndianstockhaircutS
        from ..models.portfolio_summary_initmarginreq import PortfolioSummaryInitmarginreq
        from ..models.portfolio_summary_initmarginreq_c import PortfolioSummaryInitmarginreqC
        from ..models.portfolio_summary_initmarginreq_s import PortfolioSummaryInitmarginreqS
        from ..models.portfolio_summary_leverage_s import PortfolioSummaryLeverageS
        from ..models.portfolio_summary_lookaheadavailablefunds import PortfolioSummaryLookaheadavailablefunds
        from ..models.portfolio_summary_lookaheadavailablefunds_c import PortfolioSummaryLookaheadavailablefundsC
        from ..models.portfolio_summary_lookaheadavailablefunds_s import PortfolioSummaryLookaheadavailablefundsS
        from ..models.portfolio_summary_lookaheadexcessliquidity import PortfolioSummaryLookaheadexcessliquidity
        from ..models.portfolio_summary_lookaheadexcessliquidity_c import PortfolioSummaryLookaheadexcessliquidityC
        from ..models.portfolio_summary_lookaheadexcessliquidity_s import PortfolioSummaryLookaheadexcessliquidityS
        from ..models.portfolio_summary_lookaheadinitmarginreq import PortfolioSummaryLookaheadinitmarginreq
        from ..models.portfolio_summary_lookaheadinitmarginreq_c import PortfolioSummaryLookaheadinitmarginreqC
        from ..models.portfolio_summary_lookaheadinitmarginreq_s import PortfolioSummaryLookaheadinitmarginreqS
        from ..models.portfolio_summary_lookaheadmaintmarginreq import PortfolioSummaryLookaheadmaintmarginreq
        from ..models.portfolio_summary_lookaheadmaintmarginreq_c import PortfolioSummaryLookaheadmaintmarginreqC
        from ..models.portfolio_summary_lookaheadmaintmarginreq_s import PortfolioSummaryLookaheadmaintmarginreqS
        from ..models.portfolio_summary_lookaheadnextchange import PortfolioSummaryLookaheadnextchange
        from ..models.portfolio_summary_maintmarginreq import PortfolioSummaryMaintmarginreq
        from ..models.portfolio_summary_maintmarginreq_c import PortfolioSummaryMaintmarginreqC
        from ..models.portfolio_summary_maintmarginreq_s import PortfolioSummaryMaintmarginreqS
        from ..models.portfolio_summary_netliquidation import PortfolioSummaryNetliquidation
        from ..models.portfolio_summary_netliquidation_c import PortfolioSummaryNetliquidationC
        from ..models.portfolio_summary_netliquidation_s import PortfolioSummaryNetliquidationS
        from ..models.portfolio_summary_netliquidationuncertainty import PortfolioSummaryNetliquidationuncertainty
        from ..models.portfolio_summary_nlvandmargininreview import PortfolioSummaryNlvandmargininreview
        from ..models.portfolio_summary_pasharesvalue import PortfolioSummaryPasharesvalue
        from ..models.portfolio_summary_pasharesvalue_c import PortfolioSummaryPasharesvalueC
        from ..models.portfolio_summary_pasharesvalue_s import PortfolioSummaryPasharesvalueS
        from ..models.portfolio_summary_physicalcertificatevalue import PortfolioSummaryPhysicalcertificatevalue
        from ..models.portfolio_summary_physicalcertificatevalue_c import PortfolioSummaryPhysicalcertificatevalueC
        from ..models.portfolio_summary_physicalcertificatevalue_s import PortfolioSummaryPhysicalcertificatevalueS
        from ..models.portfolio_summary_postexpirationexcess import PortfolioSummaryPostexpirationexcess
        from ..models.portfolio_summary_postexpirationexcess_c import PortfolioSummaryPostexpirationexcessC
        from ..models.portfolio_summary_postexpirationexcess_s import PortfolioSummaryPostexpirationexcessS
        from ..models.portfolio_summary_postexpirationmargin import PortfolioSummaryPostexpirationmargin
        from ..models.portfolio_summary_postexpirationmargin_c import PortfolioSummaryPostexpirationmarginC
        from ..models.portfolio_summary_postexpirationmargin_s import PortfolioSummaryPostexpirationmarginS
        from ..models.portfolio_summary_previousdayequitywithloanvalue import (
            PortfolioSummaryPreviousdayequitywithloanvalue,
        )
        from ..models.portfolio_summary_previousdayequitywithloanvalue_s import (
            PortfolioSummaryPreviousdayequitywithloanvalueS,
        )
        from ..models.portfolio_summary_regtequity import PortfolioSummaryRegtequity
        from ..models.portfolio_summary_regtequity_s import PortfolioSummaryRegtequityS
        from ..models.portfolio_summary_regtmargin import PortfolioSummaryRegtmargin
        from ..models.portfolio_summary_regtmargin_s import PortfolioSummaryRegtmarginS
        from ..models.portfolio_summary_segmenttitle_c import PortfolioSummarySegmenttitleC
        from ..models.portfolio_summary_segmenttitle_s import PortfolioSummarySegmenttitleS
        from ..models.portfolio_summary_sma import PortfolioSummarySma
        from ..models.portfolio_summary_sma_s import PortfolioSummarySmaS
        from ..models.portfolio_summary_totalcashvalue import PortfolioSummaryTotalcashvalue
        from ..models.portfolio_summary_totalcashvalue_c import PortfolioSummaryTotalcashvalueC
        from ..models.portfolio_summary_totalcashvalue_s import PortfolioSummaryTotalcashvalueS
        from ..models.portfolio_summary_totaldebitcardpendingcharges import PortfolioSummaryTotaldebitcardpendingcharges
        from ..models.portfolio_summary_totaldebitcardpendingcharges_c import (
            PortfolioSummaryTotaldebitcardpendingchargesC,
        )
        from ..models.portfolio_summary_totaldebitcardpendingcharges_s import (
            PortfolioSummaryTotaldebitcardpendingchargesS,
        )
        from ..models.portfolio_summary_tradingtype_s import PortfolioSummaryTradingtypeS
        from ..models.portfolio_summary_whatifpmenabled import PortfolioSummaryWhatifpmenabled

        d = src_dict.copy()
        _accountcode = d.pop("accountcode", UNSET)
        accountcode: Union[Unset, PortfolioSummaryAccountcode]
        if isinstance(_accountcode, Unset):
            accountcode = UNSET
        else:
            accountcode = PortfolioSummaryAccountcode.from_dict(_accountcode)

        _accountready = d.pop("accountready", UNSET)
        accountready: Union[Unset, PortfolioSummaryAccountready]
        if isinstance(_accountready, Unset):
            accountready = UNSET
        else:
            accountready = PortfolioSummaryAccountready.from_dict(_accountready)

        _accounttype = d.pop("accounttype", UNSET)
        accounttype: Union[Unset, PortfolioSummaryAccounttype]
        if isinstance(_accounttype, Unset):
            accounttype = UNSET
        else:
            accounttype = PortfolioSummaryAccounttype.from_dict(_accounttype)

        _accruedcash = d.pop("accruedcash", UNSET)
        accruedcash: Union[Unset, PortfolioSummaryAccruedcash]
        if isinstance(_accruedcash, Unset):
            accruedcash = UNSET
        else:
            accruedcash = PortfolioSummaryAccruedcash.from_dict(_accruedcash)

        _accruedcash_c = d.pop("accruedcash-c", UNSET)
        accruedcash_c: Union[Unset, PortfolioSummaryAccruedcashC]
        if isinstance(_accruedcash_c, Unset):
            accruedcash_c = UNSET
        else:
            accruedcash_c = PortfolioSummaryAccruedcashC.from_dict(_accruedcash_c)

        _accruedcash_s = d.pop("accruedcash-s", UNSET)
        accruedcash_s: Union[Unset, PortfolioSummaryAccruedcashS]
        if isinstance(_accruedcash_s, Unset):
            accruedcash_s = UNSET
        else:
            accruedcash_s = PortfolioSummaryAccruedcashS.from_dict(_accruedcash_s)

        _accrueddividend = d.pop("accrueddividend", UNSET)
        accrueddividend: Union[Unset, PortfolioSummaryAccrueddividend]
        if isinstance(_accrueddividend, Unset):
            accrueddividend = UNSET
        else:
            accrueddividend = PortfolioSummaryAccrueddividend.from_dict(_accrueddividend)

        _accrueddividend_c = d.pop("accrueddividend-c", UNSET)
        accrueddividend_c: Union[Unset, PortfolioSummaryAccrueddividendC]
        if isinstance(_accrueddividend_c, Unset):
            accrueddividend_c = UNSET
        else:
            accrueddividend_c = PortfolioSummaryAccrueddividendC.from_dict(_accrueddividend_c)

        _accrueddividend_s = d.pop("accrueddividend-s", UNSET)
        accrueddividend_s: Union[Unset, PortfolioSummaryAccrueddividendS]
        if isinstance(_accrueddividend_s, Unset):
            accrueddividend_s = UNSET
        else:
            accrueddividend_s = PortfolioSummaryAccrueddividendS.from_dict(_accrueddividend_s)

        _availablefunds = d.pop("availablefunds", UNSET)
        availablefunds: Union[Unset, PortfolioSummaryAvailablefunds]
        if isinstance(_availablefunds, Unset):
            availablefunds = UNSET
        else:
            availablefunds = PortfolioSummaryAvailablefunds.from_dict(_availablefunds)

        _availablefunds_c = d.pop("availablefunds-c", UNSET)
        availablefunds_c: Union[Unset, PortfolioSummaryAvailablefundsC]
        if isinstance(_availablefunds_c, Unset):
            availablefunds_c = UNSET
        else:
            availablefunds_c = PortfolioSummaryAvailablefundsC.from_dict(_availablefunds_c)

        _availablefunds_s = d.pop("availablefunds-s", UNSET)
        availablefunds_s: Union[Unset, PortfolioSummaryAvailablefundsS]
        if isinstance(_availablefunds_s, Unset):
            availablefunds_s = UNSET
        else:
            availablefunds_s = PortfolioSummaryAvailablefundsS.from_dict(_availablefunds_s)

        _availabletotrade = d.pop("availabletotrade", UNSET)
        availabletotrade: Union[Unset, PortfolioSummaryAvailabletotrade]
        if isinstance(_availabletotrade, Unset):
            availabletotrade = UNSET
        else:
            availabletotrade = PortfolioSummaryAvailabletotrade.from_dict(_availabletotrade)

        _availabletotrade_c = d.pop("availabletotrade-c", UNSET)
        availabletotrade_c: Union[Unset, PortfolioSummaryAvailabletotradeC]
        if isinstance(_availabletotrade_c, Unset):
            availabletotrade_c = UNSET
        else:
            availabletotrade_c = PortfolioSummaryAvailabletotradeC.from_dict(_availabletotrade_c)

        _availabletotrade_s = d.pop("availabletotrade-s", UNSET)
        availabletotrade_s: Union[Unset, PortfolioSummaryAvailabletotradeS]
        if isinstance(_availabletotrade_s, Unset):
            availabletotrade_s = UNSET
        else:
            availabletotrade_s = PortfolioSummaryAvailabletotradeS.from_dict(_availabletotrade_s)

        _availabletowithdraw = d.pop("availabletowithdraw", UNSET)
        availabletowithdraw: Union[Unset, PortfolioSummaryAvailabletowithdraw]
        if isinstance(_availabletowithdraw, Unset):
            availabletowithdraw = UNSET
        else:
            availabletowithdraw = PortfolioSummaryAvailabletowithdraw.from_dict(_availabletowithdraw)

        _availabletowithdraw_c = d.pop("availabletowithdraw-c", UNSET)
        availabletowithdraw_c: Union[Unset, PortfolioSummaryAvailabletowithdrawC]
        if isinstance(_availabletowithdraw_c, Unset):
            availabletowithdraw_c = UNSET
        else:
            availabletowithdraw_c = PortfolioSummaryAvailabletowithdrawC.from_dict(_availabletowithdraw_c)

        _availabletowithdraw_s = d.pop("availabletowithdraw-s", UNSET)
        availabletowithdraw_s: Union[Unset, PortfolioSummaryAvailabletowithdrawS]
        if isinstance(_availabletowithdraw_s, Unset):
            availabletowithdraw_s = UNSET
        else:
            availabletowithdraw_s = PortfolioSummaryAvailabletowithdrawS.from_dict(_availabletowithdraw_s)

        _billable = d.pop("billable", UNSET)
        billable: Union[Unset, PortfolioSummaryBillable]
        if isinstance(_billable, Unset):
            billable = UNSET
        else:
            billable = PortfolioSummaryBillable.from_dict(_billable)

        _billable_c = d.pop("billable-c", UNSET)
        billable_c: Union[Unset, PortfolioSummaryBillableC]
        if isinstance(_billable_c, Unset):
            billable_c = UNSET
        else:
            billable_c = PortfolioSummaryBillableC.from_dict(_billable_c)

        _billable_s = d.pop("billable-s", UNSET)
        billable_s: Union[Unset, PortfolioSummaryBillableS]
        if isinstance(_billable_s, Unset):
            billable_s = UNSET
        else:
            billable_s = PortfolioSummaryBillableS.from_dict(_billable_s)

        _buyingpower = d.pop("buyingpower", UNSET)
        buyingpower: Union[Unset, PortfolioSummaryBuyingpower]
        if isinstance(_buyingpower, Unset):
            buyingpower = UNSET
        else:
            buyingpower = PortfolioSummaryBuyingpower.from_dict(_buyingpower)

        _columnprio_c = d.pop("columnprio-c", UNSET)
        columnprio_c: Union[Unset, PortfolioSummaryColumnprioC]
        if isinstance(_columnprio_c, Unset):
            columnprio_c = UNSET
        else:
            columnprio_c = PortfolioSummaryColumnprioC.from_dict(_columnprio_c)

        _columnprio_s = d.pop("columnprio-s", UNSET)
        columnprio_s: Union[Unset, PortfolioSummaryColumnprioS]
        if isinstance(_columnprio_s, Unset):
            columnprio_s = UNSET
        else:
            columnprio_s = PortfolioSummaryColumnprioS.from_dict(_columnprio_s)

        _cushion = d.pop("cushion", UNSET)
        cushion: Union[Unset, PortfolioSummaryCushion]
        if isinstance(_cushion, Unset):
            cushion = UNSET
        else:
            cushion = PortfolioSummaryCushion.from_dict(_cushion)

        _daytradesremaining = d.pop("daytradesremaining", UNSET)
        daytradesremaining: Union[Unset, PortfolioSummaryDaytradesremaining]
        if isinstance(_daytradesremaining, Unset):
            daytradesremaining = UNSET
        else:
            daytradesremaining = PortfolioSummaryDaytradesremaining.from_dict(_daytradesremaining)

        _daytradesremainingt1 = d.pop("daytradesremainingt+1", UNSET)
        daytradesremainingt1: Union[Unset, PortfolioSummaryDaytradesremainingt1]
        if isinstance(_daytradesremainingt1, Unset):
            daytradesremainingt1 = UNSET
        else:
            daytradesremainingt1 = PortfolioSummaryDaytradesremainingt1.from_dict(_daytradesremainingt1)

        _daytradesremainingt2 = d.pop("daytradesremainingt+2", UNSET)
        daytradesremainingt2: Union[Unset, PortfolioSummaryDaytradesremainingt2]
        if isinstance(_daytradesremainingt2, Unset):
            daytradesremainingt2 = UNSET
        else:
            daytradesremainingt2 = PortfolioSummaryDaytradesremainingt2.from_dict(_daytradesremainingt2)

        _daytradesremainingt3 = d.pop("daytradesremainingt+3", UNSET)
        daytradesremainingt3: Union[Unset, PortfolioSummaryDaytradesremainingt3]
        if isinstance(_daytradesremainingt3, Unset):
            daytradesremainingt3 = UNSET
        else:
            daytradesremainingt3 = PortfolioSummaryDaytradesremainingt3.from_dict(_daytradesremainingt3)

        _daytradesremainingt4 = d.pop("daytradesremainingt+4", UNSET)
        daytradesremainingt4: Union[Unset, PortfolioSummaryDaytradesremainingt4]
        if isinstance(_daytradesremainingt4, Unset):
            daytradesremainingt4 = UNSET
        else:
            daytradesremainingt4 = PortfolioSummaryDaytradesremainingt4.from_dict(_daytradesremainingt4)

        _daytradingstatus_s = d.pop("daytradingstatus-s", UNSET)
        daytradingstatus_s: Union[Unset, PortfolioSummaryDaytradingstatusS]
        if isinstance(_daytradingstatus_s, Unset):
            daytradingstatus_s = UNSET
        else:
            daytradingstatus_s = PortfolioSummaryDaytradingstatusS.from_dict(_daytradingstatus_s)

        _depositoncredithold = d.pop("depositoncredithold", UNSET)
        depositoncredithold: Union[Unset, PortfolioSummaryDepositoncredithold]
        if isinstance(_depositoncredithold, Unset):
            depositoncredithold = UNSET
        else:
            depositoncredithold = PortfolioSummaryDepositoncredithold.from_dict(_depositoncredithold)

        _equitywithloanvalue = d.pop("equitywithloanvalue", UNSET)
        equitywithloanvalue: Union[Unset, PortfolioSummaryEquitywithloanvalue]
        if isinstance(_equitywithloanvalue, Unset):
            equitywithloanvalue = UNSET
        else:
            equitywithloanvalue = PortfolioSummaryEquitywithloanvalue.from_dict(_equitywithloanvalue)

        _equitywithloanvalue_c = d.pop("equitywithloanvalue-c", UNSET)
        equitywithloanvalue_c: Union[Unset, PortfolioSummaryEquitywithloanvalueC]
        if isinstance(_equitywithloanvalue_c, Unset):
            equitywithloanvalue_c = UNSET
        else:
            equitywithloanvalue_c = PortfolioSummaryEquitywithloanvalueC.from_dict(_equitywithloanvalue_c)

        _equitywithloanvalue_s = d.pop("equitywithloanvalue-s", UNSET)
        equitywithloanvalue_s: Union[Unset, PortfolioSummaryEquitywithloanvalueS]
        if isinstance(_equitywithloanvalue_s, Unset):
            equitywithloanvalue_s = UNSET
        else:
            equitywithloanvalue_s = PortfolioSummaryEquitywithloanvalueS.from_dict(_equitywithloanvalue_s)

        _excessliquidity = d.pop("excessliquidity", UNSET)
        excessliquidity: Union[Unset, PortfolioSummaryExcessliquidity]
        if isinstance(_excessliquidity, Unset):
            excessliquidity = UNSET
        else:
            excessliquidity = PortfolioSummaryExcessliquidity.from_dict(_excessliquidity)

        _excessliquidity_c = d.pop("excessliquidity-c", UNSET)
        excessliquidity_c: Union[Unset, PortfolioSummaryExcessliquidityC]
        if isinstance(_excessliquidity_c, Unset):
            excessliquidity_c = UNSET
        else:
            excessliquidity_c = PortfolioSummaryExcessliquidityC.from_dict(_excessliquidity_c)

        _excessliquidity_s = d.pop("excessliquidity-s", UNSET)
        excessliquidity_s: Union[Unset, PortfolioSummaryExcessliquidityS]
        if isinstance(_excessliquidity_s, Unset):
            excessliquidity_s = UNSET
        else:
            excessliquidity_s = PortfolioSummaryExcessliquidityS.from_dict(_excessliquidity_s)

        _fullavailablefunds = d.pop("fullavailablefunds", UNSET)
        fullavailablefunds: Union[Unset, PortfolioSummaryFullavailablefunds]
        if isinstance(_fullavailablefunds, Unset):
            fullavailablefunds = UNSET
        else:
            fullavailablefunds = PortfolioSummaryFullavailablefunds.from_dict(_fullavailablefunds)

        _fullavailablefunds_c = d.pop("fullavailablefunds-c", UNSET)
        fullavailablefunds_c: Union[Unset, PortfolioSummaryFullavailablefundsC]
        if isinstance(_fullavailablefunds_c, Unset):
            fullavailablefunds_c = UNSET
        else:
            fullavailablefunds_c = PortfolioSummaryFullavailablefundsC.from_dict(_fullavailablefunds_c)

        _fullavailablefunds_s = d.pop("fullavailablefunds-s", UNSET)
        fullavailablefunds_s: Union[Unset, PortfolioSummaryFullavailablefundsS]
        if isinstance(_fullavailablefunds_s, Unset):
            fullavailablefunds_s = UNSET
        else:
            fullavailablefunds_s = PortfolioSummaryFullavailablefundsS.from_dict(_fullavailablefunds_s)

        _fullexcessliquidity = d.pop("fullexcessliquidity", UNSET)
        fullexcessliquidity: Union[Unset, PortfolioSummaryFullexcessliquidity]
        if isinstance(_fullexcessliquidity, Unset):
            fullexcessliquidity = UNSET
        else:
            fullexcessliquidity = PortfolioSummaryFullexcessliquidity.from_dict(_fullexcessliquidity)

        _fullexcessliquidity_c = d.pop("fullexcessliquidity-c", UNSET)
        fullexcessliquidity_c: Union[Unset, PortfolioSummaryFullexcessliquidityC]
        if isinstance(_fullexcessliquidity_c, Unset):
            fullexcessliquidity_c = UNSET
        else:
            fullexcessliquidity_c = PortfolioSummaryFullexcessliquidityC.from_dict(_fullexcessliquidity_c)

        _fullexcessliquidity_s = d.pop("fullexcessliquidity-s", UNSET)
        fullexcessliquidity_s: Union[Unset, PortfolioSummaryFullexcessliquidityS]
        if isinstance(_fullexcessliquidity_s, Unset):
            fullexcessliquidity_s = UNSET
        else:
            fullexcessliquidity_s = PortfolioSummaryFullexcessliquidityS.from_dict(_fullexcessliquidity_s)

        _fullinitmarginreq = d.pop("fullinitmarginreq", UNSET)
        fullinitmarginreq: Union[Unset, PortfolioSummaryFullinitmarginreq]
        if isinstance(_fullinitmarginreq, Unset):
            fullinitmarginreq = UNSET
        else:
            fullinitmarginreq = PortfolioSummaryFullinitmarginreq.from_dict(_fullinitmarginreq)

        _fullinitmarginreq_c = d.pop("fullinitmarginreq-c", UNSET)
        fullinitmarginreq_c: Union[Unset, PortfolioSummaryFullinitmarginreqC]
        if isinstance(_fullinitmarginreq_c, Unset):
            fullinitmarginreq_c = UNSET
        else:
            fullinitmarginreq_c = PortfolioSummaryFullinitmarginreqC.from_dict(_fullinitmarginreq_c)

        _fullinitmarginreq_s = d.pop("fullinitmarginreq-s", UNSET)
        fullinitmarginreq_s: Union[Unset, PortfolioSummaryFullinitmarginreqS]
        if isinstance(_fullinitmarginreq_s, Unset):
            fullinitmarginreq_s = UNSET
        else:
            fullinitmarginreq_s = PortfolioSummaryFullinitmarginreqS.from_dict(_fullinitmarginreq_s)

        _fullmaintmarginreq = d.pop("fullmaintmarginreq", UNSET)
        fullmaintmarginreq: Union[Unset, PortfolioSummaryFullmaintmarginreq]
        if isinstance(_fullmaintmarginreq, Unset):
            fullmaintmarginreq = UNSET
        else:
            fullmaintmarginreq = PortfolioSummaryFullmaintmarginreq.from_dict(_fullmaintmarginreq)

        _fullmaintmarginreq_c = d.pop("fullmaintmarginreq-c", UNSET)
        fullmaintmarginreq_c: Union[Unset, PortfolioSummaryFullmaintmarginreqC]
        if isinstance(_fullmaintmarginreq_c, Unset):
            fullmaintmarginreq_c = UNSET
        else:
            fullmaintmarginreq_c = PortfolioSummaryFullmaintmarginreqC.from_dict(_fullmaintmarginreq_c)

        _fullmaintmarginreq_s = d.pop("fullmaintmarginreq-s", UNSET)
        fullmaintmarginreq_s: Union[Unset, PortfolioSummaryFullmaintmarginreqS]
        if isinstance(_fullmaintmarginreq_s, Unset):
            fullmaintmarginreq_s = UNSET
        else:
            fullmaintmarginreq_s = PortfolioSummaryFullmaintmarginreqS.from_dict(_fullmaintmarginreq_s)

        _grosspositionvalue = d.pop("grosspositionvalue", UNSET)
        grosspositionvalue: Union[Unset, PortfolioSummaryGrosspositionvalue]
        if isinstance(_grosspositionvalue, Unset):
            grosspositionvalue = UNSET
        else:
            grosspositionvalue = PortfolioSummaryGrosspositionvalue.from_dict(_grosspositionvalue)

        _grosspositionvalue_s = d.pop("grosspositionvalue-s", UNSET)
        grosspositionvalue_s: Union[Unset, PortfolioSummaryGrosspositionvalueS]
        if isinstance(_grosspositionvalue_s, Unset):
            grosspositionvalue_s = UNSET
        else:
            grosspositionvalue_s = PortfolioSummaryGrosspositionvalueS.from_dict(_grosspositionvalue_s)

        _guarantee = d.pop("guarantee", UNSET)
        guarantee: Union[Unset, PortfolioSummaryGuarantee]
        if isinstance(_guarantee, Unset):
            guarantee = UNSET
        else:
            guarantee = PortfolioSummaryGuarantee.from_dict(_guarantee)

        _guarantee_c = d.pop("guarantee-c", UNSET)
        guarantee_c: Union[Unset, PortfolioSummaryGuaranteeC]
        if isinstance(_guarantee_c, Unset):
            guarantee_c = UNSET
        else:
            guarantee_c = PortfolioSummaryGuaranteeC.from_dict(_guarantee_c)

        _guarantee_s = d.pop("guarantee-s", UNSET)
        guarantee_s: Union[Unset, PortfolioSummaryGuaranteeS]
        if isinstance(_guarantee_s, Unset):
            guarantee_s = UNSET
        else:
            guarantee_s = PortfolioSummaryGuaranteeS.from_dict(_guarantee_s)

        _highestseverity = d.pop("highestseverity", UNSET)
        highestseverity: Union[Unset, PortfolioSummaryHighestseverity]
        if isinstance(_highestseverity, Unset):
            highestseverity = UNSET
        else:
            highestseverity = PortfolioSummaryHighestseverity.from_dict(_highestseverity)

        _indianstockhaircut = d.pop("indianstockhaircut", UNSET)
        indianstockhaircut: Union[Unset, PortfolioSummaryIndianstockhaircut]
        if isinstance(_indianstockhaircut, Unset):
            indianstockhaircut = UNSET
        else:
            indianstockhaircut = PortfolioSummaryIndianstockhaircut.from_dict(_indianstockhaircut)

        _indianstockhaircut_c = d.pop("indianstockhaircut-c", UNSET)
        indianstockhaircut_c: Union[Unset, PortfolioSummaryIndianstockhaircutC]
        if isinstance(_indianstockhaircut_c, Unset):
            indianstockhaircut_c = UNSET
        else:
            indianstockhaircut_c = PortfolioSummaryIndianstockhaircutC.from_dict(_indianstockhaircut_c)

        _indianstockhaircut_s = d.pop("indianstockhaircut-s", UNSET)
        indianstockhaircut_s: Union[Unset, PortfolioSummaryIndianstockhaircutS]
        if isinstance(_indianstockhaircut_s, Unset):
            indianstockhaircut_s = UNSET
        else:
            indianstockhaircut_s = PortfolioSummaryIndianstockhaircutS.from_dict(_indianstockhaircut_s)

        _initmarginreq = d.pop("initmarginreq", UNSET)
        initmarginreq: Union[Unset, PortfolioSummaryInitmarginreq]
        if isinstance(_initmarginreq, Unset):
            initmarginreq = UNSET
        else:
            initmarginreq = PortfolioSummaryInitmarginreq.from_dict(_initmarginreq)

        _initmarginreq_c = d.pop("initmarginreq-c", UNSET)
        initmarginreq_c: Union[Unset, PortfolioSummaryInitmarginreqC]
        if isinstance(_initmarginreq_c, Unset):
            initmarginreq_c = UNSET
        else:
            initmarginreq_c = PortfolioSummaryInitmarginreqC.from_dict(_initmarginreq_c)

        _initmarginreq_s = d.pop("initmarginreq-s", UNSET)
        initmarginreq_s: Union[Unset, PortfolioSummaryInitmarginreqS]
        if isinstance(_initmarginreq_s, Unset):
            initmarginreq_s = UNSET
        else:
            initmarginreq_s = PortfolioSummaryInitmarginreqS.from_dict(_initmarginreq_s)

        _leverage_s = d.pop("leverage-s", UNSET)
        leverage_s: Union[Unset, PortfolioSummaryLeverageS]
        if isinstance(_leverage_s, Unset):
            leverage_s = UNSET
        else:
            leverage_s = PortfolioSummaryLeverageS.from_dict(_leverage_s)

        _lookaheadavailablefunds = d.pop("lookaheadavailablefunds", UNSET)
        lookaheadavailablefunds: Union[Unset, PortfolioSummaryLookaheadavailablefunds]
        if isinstance(_lookaheadavailablefunds, Unset):
            lookaheadavailablefunds = UNSET
        else:
            lookaheadavailablefunds = PortfolioSummaryLookaheadavailablefunds.from_dict(_lookaheadavailablefunds)

        _lookaheadavailablefunds_c = d.pop("lookaheadavailablefunds-c", UNSET)
        lookaheadavailablefunds_c: Union[Unset, PortfolioSummaryLookaheadavailablefundsC]
        if isinstance(_lookaheadavailablefunds_c, Unset):
            lookaheadavailablefunds_c = UNSET
        else:
            lookaheadavailablefunds_c = PortfolioSummaryLookaheadavailablefundsC.from_dict(_lookaheadavailablefunds_c)

        _lookaheadavailablefunds_s = d.pop("lookaheadavailablefunds-s", UNSET)
        lookaheadavailablefunds_s: Union[Unset, PortfolioSummaryLookaheadavailablefundsS]
        if isinstance(_lookaheadavailablefunds_s, Unset):
            lookaheadavailablefunds_s = UNSET
        else:
            lookaheadavailablefunds_s = PortfolioSummaryLookaheadavailablefundsS.from_dict(_lookaheadavailablefunds_s)

        _lookaheadexcessliquidity = d.pop("lookaheadexcessliquidity", UNSET)
        lookaheadexcessliquidity: Union[Unset, PortfolioSummaryLookaheadexcessliquidity]
        if isinstance(_lookaheadexcessliquidity, Unset):
            lookaheadexcessliquidity = UNSET
        else:
            lookaheadexcessliquidity = PortfolioSummaryLookaheadexcessliquidity.from_dict(_lookaheadexcessliquidity)

        _lookaheadexcessliquidity_c = d.pop("lookaheadexcessliquidity-c", UNSET)
        lookaheadexcessliquidity_c: Union[Unset, PortfolioSummaryLookaheadexcessliquidityC]
        if isinstance(_lookaheadexcessliquidity_c, Unset):
            lookaheadexcessliquidity_c = UNSET
        else:
            lookaheadexcessliquidity_c = PortfolioSummaryLookaheadexcessliquidityC.from_dict(
                _lookaheadexcessliquidity_c
            )

        _lookaheadexcessliquidity_s = d.pop("lookaheadexcessliquidity-s", UNSET)
        lookaheadexcessliquidity_s: Union[Unset, PortfolioSummaryLookaheadexcessliquidityS]
        if isinstance(_lookaheadexcessliquidity_s, Unset):
            lookaheadexcessliquidity_s = UNSET
        else:
            lookaheadexcessliquidity_s = PortfolioSummaryLookaheadexcessliquidityS.from_dict(
                _lookaheadexcessliquidity_s
            )

        _lookaheadinitmarginreq = d.pop("lookaheadinitmarginreq", UNSET)
        lookaheadinitmarginreq: Union[Unset, PortfolioSummaryLookaheadinitmarginreq]
        if isinstance(_lookaheadinitmarginreq, Unset):
            lookaheadinitmarginreq = UNSET
        else:
            lookaheadinitmarginreq = PortfolioSummaryLookaheadinitmarginreq.from_dict(_lookaheadinitmarginreq)

        _lookaheadinitmarginreq_c = d.pop("lookaheadinitmarginreq-c", UNSET)
        lookaheadinitmarginreq_c: Union[Unset, PortfolioSummaryLookaheadinitmarginreqC]
        if isinstance(_lookaheadinitmarginreq_c, Unset):
            lookaheadinitmarginreq_c = UNSET
        else:
            lookaheadinitmarginreq_c = PortfolioSummaryLookaheadinitmarginreqC.from_dict(_lookaheadinitmarginreq_c)

        _lookaheadinitmarginreq_s = d.pop("lookaheadinitmarginreq-s", UNSET)
        lookaheadinitmarginreq_s: Union[Unset, PortfolioSummaryLookaheadinitmarginreqS]
        if isinstance(_lookaheadinitmarginreq_s, Unset):
            lookaheadinitmarginreq_s = UNSET
        else:
            lookaheadinitmarginreq_s = PortfolioSummaryLookaheadinitmarginreqS.from_dict(_lookaheadinitmarginreq_s)

        _lookaheadmaintmarginreq = d.pop("lookaheadmaintmarginreq", UNSET)
        lookaheadmaintmarginreq: Union[Unset, PortfolioSummaryLookaheadmaintmarginreq]
        if isinstance(_lookaheadmaintmarginreq, Unset):
            lookaheadmaintmarginreq = UNSET
        else:
            lookaheadmaintmarginreq = PortfolioSummaryLookaheadmaintmarginreq.from_dict(_lookaheadmaintmarginreq)

        _lookaheadmaintmarginreq_c = d.pop("lookaheadmaintmarginreq-c", UNSET)
        lookaheadmaintmarginreq_c: Union[Unset, PortfolioSummaryLookaheadmaintmarginreqC]
        if isinstance(_lookaheadmaintmarginreq_c, Unset):
            lookaheadmaintmarginreq_c = UNSET
        else:
            lookaheadmaintmarginreq_c = PortfolioSummaryLookaheadmaintmarginreqC.from_dict(_lookaheadmaintmarginreq_c)

        _lookaheadmaintmarginreq_s = d.pop("lookaheadmaintmarginreq-s", UNSET)
        lookaheadmaintmarginreq_s: Union[Unset, PortfolioSummaryLookaheadmaintmarginreqS]
        if isinstance(_lookaheadmaintmarginreq_s, Unset):
            lookaheadmaintmarginreq_s = UNSET
        else:
            lookaheadmaintmarginreq_s = PortfolioSummaryLookaheadmaintmarginreqS.from_dict(_lookaheadmaintmarginreq_s)

        _lookaheadnextchange = d.pop("lookaheadnextchange", UNSET)
        lookaheadnextchange: Union[Unset, PortfolioSummaryLookaheadnextchange]
        if isinstance(_lookaheadnextchange, Unset):
            lookaheadnextchange = UNSET
        else:
            lookaheadnextchange = PortfolioSummaryLookaheadnextchange.from_dict(_lookaheadnextchange)

        _maintmarginreq = d.pop("maintmarginreq", UNSET)
        maintmarginreq: Union[Unset, PortfolioSummaryMaintmarginreq]
        if isinstance(_maintmarginreq, Unset):
            maintmarginreq = UNSET
        else:
            maintmarginreq = PortfolioSummaryMaintmarginreq.from_dict(_maintmarginreq)

        _maintmarginreq_c = d.pop("maintmarginreq-c", UNSET)
        maintmarginreq_c: Union[Unset, PortfolioSummaryMaintmarginreqC]
        if isinstance(_maintmarginreq_c, Unset):
            maintmarginreq_c = UNSET
        else:
            maintmarginreq_c = PortfolioSummaryMaintmarginreqC.from_dict(_maintmarginreq_c)

        _maintmarginreq_s = d.pop("maintmarginreq-s", UNSET)
        maintmarginreq_s: Union[Unset, PortfolioSummaryMaintmarginreqS]
        if isinstance(_maintmarginreq_s, Unset):
            maintmarginreq_s = UNSET
        else:
            maintmarginreq_s = PortfolioSummaryMaintmarginreqS.from_dict(_maintmarginreq_s)

        _netliquidation = d.pop("netliquidation", UNSET)
        netliquidation: Union[Unset, PortfolioSummaryNetliquidation]
        if isinstance(_netliquidation, Unset):
            netliquidation = UNSET
        else:
            netliquidation = PortfolioSummaryNetliquidation.from_dict(_netliquidation)

        _netliquidation_c = d.pop("netliquidation-c", UNSET)
        netliquidation_c: Union[Unset, PortfolioSummaryNetliquidationC]
        if isinstance(_netliquidation_c, Unset):
            netliquidation_c = UNSET
        else:
            netliquidation_c = PortfolioSummaryNetliquidationC.from_dict(_netliquidation_c)

        _netliquidation_s = d.pop("netliquidation-s", UNSET)
        netliquidation_s: Union[Unset, PortfolioSummaryNetliquidationS]
        if isinstance(_netliquidation_s, Unset):
            netliquidation_s = UNSET
        else:
            netliquidation_s = PortfolioSummaryNetliquidationS.from_dict(_netliquidation_s)

        _netliquidationuncertainty = d.pop("netliquidationuncertainty", UNSET)
        netliquidationuncertainty: Union[Unset, PortfolioSummaryNetliquidationuncertainty]
        if isinstance(_netliquidationuncertainty, Unset):
            netliquidationuncertainty = UNSET
        else:
            netliquidationuncertainty = PortfolioSummaryNetliquidationuncertainty.from_dict(_netliquidationuncertainty)

        _nlvandmargininreview = d.pop("nlvandmargininreview", UNSET)
        nlvandmargininreview: Union[Unset, PortfolioSummaryNlvandmargininreview]
        if isinstance(_nlvandmargininreview, Unset):
            nlvandmargininreview = UNSET
        else:
            nlvandmargininreview = PortfolioSummaryNlvandmargininreview.from_dict(_nlvandmargininreview)

        _pasharesvalue = d.pop("pasharesvalue", UNSET)
        pasharesvalue: Union[Unset, PortfolioSummaryPasharesvalue]
        if isinstance(_pasharesvalue, Unset):
            pasharesvalue = UNSET
        else:
            pasharesvalue = PortfolioSummaryPasharesvalue.from_dict(_pasharesvalue)

        _pasharesvalue_c = d.pop("pasharesvalue-c", UNSET)
        pasharesvalue_c: Union[Unset, PortfolioSummaryPasharesvalueC]
        if isinstance(_pasharesvalue_c, Unset):
            pasharesvalue_c = UNSET
        else:
            pasharesvalue_c = PortfolioSummaryPasharesvalueC.from_dict(_pasharesvalue_c)

        _pasharesvalue_s = d.pop("pasharesvalue-s", UNSET)
        pasharesvalue_s: Union[Unset, PortfolioSummaryPasharesvalueS]
        if isinstance(_pasharesvalue_s, Unset):
            pasharesvalue_s = UNSET
        else:
            pasharesvalue_s = PortfolioSummaryPasharesvalueS.from_dict(_pasharesvalue_s)

        _physicalcertificatevalue = d.pop("physicalcertificatevalue", UNSET)
        physicalcertificatevalue: Union[Unset, PortfolioSummaryPhysicalcertificatevalue]
        if isinstance(_physicalcertificatevalue, Unset):
            physicalcertificatevalue = UNSET
        else:
            physicalcertificatevalue = PortfolioSummaryPhysicalcertificatevalue.from_dict(_physicalcertificatevalue)

        _physicalcertificatevalue_c = d.pop("physicalcertificatevalue-c", UNSET)
        physicalcertificatevalue_c: Union[Unset, PortfolioSummaryPhysicalcertificatevalueC]
        if isinstance(_physicalcertificatevalue_c, Unset):
            physicalcertificatevalue_c = UNSET
        else:
            physicalcertificatevalue_c = PortfolioSummaryPhysicalcertificatevalueC.from_dict(
                _physicalcertificatevalue_c
            )

        _physicalcertificatevalue_s = d.pop("physicalcertificatevalue-s", UNSET)
        physicalcertificatevalue_s: Union[Unset, PortfolioSummaryPhysicalcertificatevalueS]
        if isinstance(_physicalcertificatevalue_s, Unset):
            physicalcertificatevalue_s = UNSET
        else:
            physicalcertificatevalue_s = PortfolioSummaryPhysicalcertificatevalueS.from_dict(
                _physicalcertificatevalue_s
            )

        _postexpirationexcess = d.pop("postexpirationexcess", UNSET)
        postexpirationexcess: Union[Unset, PortfolioSummaryPostexpirationexcess]
        if isinstance(_postexpirationexcess, Unset):
            postexpirationexcess = UNSET
        else:
            postexpirationexcess = PortfolioSummaryPostexpirationexcess.from_dict(_postexpirationexcess)

        _postexpirationexcess_c = d.pop("postexpirationexcess-c", UNSET)
        postexpirationexcess_c: Union[Unset, PortfolioSummaryPostexpirationexcessC]
        if isinstance(_postexpirationexcess_c, Unset):
            postexpirationexcess_c = UNSET
        else:
            postexpirationexcess_c = PortfolioSummaryPostexpirationexcessC.from_dict(_postexpirationexcess_c)

        _postexpirationexcess_s = d.pop("postexpirationexcess-s", UNSET)
        postexpirationexcess_s: Union[Unset, PortfolioSummaryPostexpirationexcessS]
        if isinstance(_postexpirationexcess_s, Unset):
            postexpirationexcess_s = UNSET
        else:
            postexpirationexcess_s = PortfolioSummaryPostexpirationexcessS.from_dict(_postexpirationexcess_s)

        _postexpirationmargin = d.pop("postexpirationmargin", UNSET)
        postexpirationmargin: Union[Unset, PortfolioSummaryPostexpirationmargin]
        if isinstance(_postexpirationmargin, Unset):
            postexpirationmargin = UNSET
        else:
            postexpirationmargin = PortfolioSummaryPostexpirationmargin.from_dict(_postexpirationmargin)

        _postexpirationmargin_c = d.pop("postexpirationmargin-c", UNSET)
        postexpirationmargin_c: Union[Unset, PortfolioSummaryPostexpirationmarginC]
        if isinstance(_postexpirationmargin_c, Unset):
            postexpirationmargin_c = UNSET
        else:
            postexpirationmargin_c = PortfolioSummaryPostexpirationmarginC.from_dict(_postexpirationmargin_c)

        _postexpirationmargin_s = d.pop("postexpirationmargin-s", UNSET)
        postexpirationmargin_s: Union[Unset, PortfolioSummaryPostexpirationmarginS]
        if isinstance(_postexpirationmargin_s, Unset):
            postexpirationmargin_s = UNSET
        else:
            postexpirationmargin_s = PortfolioSummaryPostexpirationmarginS.from_dict(_postexpirationmargin_s)

        _previousdayequitywithloanvalue = d.pop("previousdayequitywithloanvalue", UNSET)
        previousdayequitywithloanvalue: Union[Unset, PortfolioSummaryPreviousdayequitywithloanvalue]
        if isinstance(_previousdayequitywithloanvalue, Unset):
            previousdayequitywithloanvalue = UNSET
        else:
            previousdayequitywithloanvalue = PortfolioSummaryPreviousdayequitywithloanvalue.from_dict(
                _previousdayequitywithloanvalue
            )

        _previousdayequitywithloanvalue_s = d.pop("previousdayequitywithloanvalue-s", UNSET)
        previousdayequitywithloanvalue_s: Union[Unset, PortfolioSummaryPreviousdayequitywithloanvalueS]
        if isinstance(_previousdayequitywithloanvalue_s, Unset):
            previousdayequitywithloanvalue_s = UNSET
        else:
            previousdayequitywithloanvalue_s = PortfolioSummaryPreviousdayequitywithloanvalueS.from_dict(
                _previousdayequitywithloanvalue_s
            )

        _regtequity = d.pop("regtequity", UNSET)
        regtequity: Union[Unset, PortfolioSummaryRegtequity]
        if isinstance(_regtequity, Unset):
            regtequity = UNSET
        else:
            regtequity = PortfolioSummaryRegtequity.from_dict(_regtequity)

        _regtequity_s = d.pop("regtequity-s", UNSET)
        regtequity_s: Union[Unset, PortfolioSummaryRegtequityS]
        if isinstance(_regtequity_s, Unset):
            regtequity_s = UNSET
        else:
            regtequity_s = PortfolioSummaryRegtequityS.from_dict(_regtequity_s)

        _regtmargin = d.pop("regtmargin", UNSET)
        regtmargin: Union[Unset, PortfolioSummaryRegtmargin]
        if isinstance(_regtmargin, Unset):
            regtmargin = UNSET
        else:
            regtmargin = PortfolioSummaryRegtmargin.from_dict(_regtmargin)

        _regtmargin_s = d.pop("regtmargin-s", UNSET)
        regtmargin_s: Union[Unset, PortfolioSummaryRegtmarginS]
        if isinstance(_regtmargin_s, Unset):
            regtmargin_s = UNSET
        else:
            regtmargin_s = PortfolioSummaryRegtmarginS.from_dict(_regtmargin_s)

        _segmenttitle_c = d.pop("segmenttitle-c", UNSET)
        segmenttitle_c: Union[Unset, PortfolioSummarySegmenttitleC]
        if isinstance(_segmenttitle_c, Unset):
            segmenttitle_c = UNSET
        else:
            segmenttitle_c = PortfolioSummarySegmenttitleC.from_dict(_segmenttitle_c)

        _segmenttitle_s = d.pop("segmenttitle-s", UNSET)
        segmenttitle_s: Union[Unset, PortfolioSummarySegmenttitleS]
        if isinstance(_segmenttitle_s, Unset):
            segmenttitle_s = UNSET
        else:
            segmenttitle_s = PortfolioSummarySegmenttitleS.from_dict(_segmenttitle_s)

        _sma = d.pop("sma", UNSET)
        sma: Union[Unset, PortfolioSummarySma]
        if isinstance(_sma, Unset):
            sma = UNSET
        else:
            sma = PortfolioSummarySma.from_dict(_sma)

        _sma_s = d.pop("sma-s", UNSET)
        sma_s: Union[Unset, PortfolioSummarySmaS]
        if isinstance(_sma_s, Unset):
            sma_s = UNSET
        else:
            sma_s = PortfolioSummarySmaS.from_dict(_sma_s)

        _totalcashvalue = d.pop("totalcashvalue", UNSET)
        totalcashvalue: Union[Unset, PortfolioSummaryTotalcashvalue]
        if isinstance(_totalcashvalue, Unset):
            totalcashvalue = UNSET
        else:
            totalcashvalue = PortfolioSummaryTotalcashvalue.from_dict(_totalcashvalue)

        _totalcashvalue_c = d.pop("totalcashvalue-c", UNSET)
        totalcashvalue_c: Union[Unset, PortfolioSummaryTotalcashvalueC]
        if isinstance(_totalcashvalue_c, Unset):
            totalcashvalue_c = UNSET
        else:
            totalcashvalue_c = PortfolioSummaryTotalcashvalueC.from_dict(_totalcashvalue_c)

        _totalcashvalue_s = d.pop("totalcashvalue-s", UNSET)
        totalcashvalue_s: Union[Unset, PortfolioSummaryTotalcashvalueS]
        if isinstance(_totalcashvalue_s, Unset):
            totalcashvalue_s = UNSET
        else:
            totalcashvalue_s = PortfolioSummaryTotalcashvalueS.from_dict(_totalcashvalue_s)

        _totaldebitcardpendingcharges = d.pop("totaldebitcardpendingcharges", UNSET)
        totaldebitcardpendingcharges: Union[Unset, PortfolioSummaryTotaldebitcardpendingcharges]
        if isinstance(_totaldebitcardpendingcharges, Unset):
            totaldebitcardpendingcharges = UNSET
        else:
            totaldebitcardpendingcharges = PortfolioSummaryTotaldebitcardpendingcharges.from_dict(
                _totaldebitcardpendingcharges
            )

        _totaldebitcardpendingcharges_c = d.pop("totaldebitcardpendingcharges-c", UNSET)
        totaldebitcardpendingcharges_c: Union[Unset, PortfolioSummaryTotaldebitcardpendingchargesC]
        if isinstance(_totaldebitcardpendingcharges_c, Unset):
            totaldebitcardpendingcharges_c = UNSET
        else:
            totaldebitcardpendingcharges_c = PortfolioSummaryTotaldebitcardpendingchargesC.from_dict(
                _totaldebitcardpendingcharges_c
            )

        _totaldebitcardpendingcharges_s = d.pop("totaldebitcardpendingcharges-s", UNSET)
        totaldebitcardpendingcharges_s: Union[Unset, PortfolioSummaryTotaldebitcardpendingchargesS]
        if isinstance(_totaldebitcardpendingcharges_s, Unset):
            totaldebitcardpendingcharges_s = UNSET
        else:
            totaldebitcardpendingcharges_s = PortfolioSummaryTotaldebitcardpendingchargesS.from_dict(
                _totaldebitcardpendingcharges_s
            )

        _tradingtype_s = d.pop("tradingtype-s", UNSET)
        tradingtype_s: Union[Unset, PortfolioSummaryTradingtypeS]
        if isinstance(_tradingtype_s, Unset):
            tradingtype_s = UNSET
        else:
            tradingtype_s = PortfolioSummaryTradingtypeS.from_dict(_tradingtype_s)

        _whatifpmenabled = d.pop("whatifpmenabled", UNSET)
        whatifpmenabled: Union[Unset, PortfolioSummaryWhatifpmenabled]
        if isinstance(_whatifpmenabled, Unset):
            whatifpmenabled = UNSET
        else:
            whatifpmenabled = PortfolioSummaryWhatifpmenabled.from_dict(_whatifpmenabled)

        portfolio_summary = cls(
            accountcode=accountcode,
            accountready=accountready,
            accounttype=accounttype,
            accruedcash=accruedcash,
            accruedcash_c=accruedcash_c,
            accruedcash_s=accruedcash_s,
            accrueddividend=accrueddividend,
            accrueddividend_c=accrueddividend_c,
            accrueddividend_s=accrueddividend_s,
            availablefunds=availablefunds,
            availablefunds_c=availablefunds_c,
            availablefunds_s=availablefunds_s,
            availabletotrade=availabletotrade,
            availabletotrade_c=availabletotrade_c,
            availabletotrade_s=availabletotrade_s,
            availabletowithdraw=availabletowithdraw,
            availabletowithdraw_c=availabletowithdraw_c,
            availabletowithdraw_s=availabletowithdraw_s,
            billable=billable,
            billable_c=billable_c,
            billable_s=billable_s,
            buyingpower=buyingpower,
            columnprio_c=columnprio_c,
            columnprio_s=columnprio_s,
            cushion=cushion,
            daytradesremaining=daytradesremaining,
            daytradesremainingt1=daytradesremainingt1,
            daytradesremainingt2=daytradesremainingt2,
            daytradesremainingt3=daytradesremainingt3,
            daytradesremainingt4=daytradesremainingt4,
            daytradingstatus_s=daytradingstatus_s,
            depositoncredithold=depositoncredithold,
            equitywithloanvalue=equitywithloanvalue,
            equitywithloanvalue_c=equitywithloanvalue_c,
            equitywithloanvalue_s=equitywithloanvalue_s,
            excessliquidity=excessliquidity,
            excessliquidity_c=excessliquidity_c,
            excessliquidity_s=excessliquidity_s,
            fullavailablefunds=fullavailablefunds,
            fullavailablefunds_c=fullavailablefunds_c,
            fullavailablefunds_s=fullavailablefunds_s,
            fullexcessliquidity=fullexcessliquidity,
            fullexcessliquidity_c=fullexcessliquidity_c,
            fullexcessliquidity_s=fullexcessliquidity_s,
            fullinitmarginreq=fullinitmarginreq,
            fullinitmarginreq_c=fullinitmarginreq_c,
            fullinitmarginreq_s=fullinitmarginreq_s,
            fullmaintmarginreq=fullmaintmarginreq,
            fullmaintmarginreq_c=fullmaintmarginreq_c,
            fullmaintmarginreq_s=fullmaintmarginreq_s,
            grosspositionvalue=grosspositionvalue,
            grosspositionvalue_s=grosspositionvalue_s,
            guarantee=guarantee,
            guarantee_c=guarantee_c,
            guarantee_s=guarantee_s,
            highestseverity=highestseverity,
            indianstockhaircut=indianstockhaircut,
            indianstockhaircut_c=indianstockhaircut_c,
            indianstockhaircut_s=indianstockhaircut_s,
            initmarginreq=initmarginreq,
            initmarginreq_c=initmarginreq_c,
            initmarginreq_s=initmarginreq_s,
            leverage_s=leverage_s,
            lookaheadavailablefunds=lookaheadavailablefunds,
            lookaheadavailablefunds_c=lookaheadavailablefunds_c,
            lookaheadavailablefunds_s=lookaheadavailablefunds_s,
            lookaheadexcessliquidity=lookaheadexcessliquidity,
            lookaheadexcessliquidity_c=lookaheadexcessliquidity_c,
            lookaheadexcessliquidity_s=lookaheadexcessliquidity_s,
            lookaheadinitmarginreq=lookaheadinitmarginreq,
            lookaheadinitmarginreq_c=lookaheadinitmarginreq_c,
            lookaheadinitmarginreq_s=lookaheadinitmarginreq_s,
            lookaheadmaintmarginreq=lookaheadmaintmarginreq,
            lookaheadmaintmarginreq_c=lookaheadmaintmarginreq_c,
            lookaheadmaintmarginreq_s=lookaheadmaintmarginreq_s,
            lookaheadnextchange=lookaheadnextchange,
            maintmarginreq=maintmarginreq,
            maintmarginreq_c=maintmarginreq_c,
            maintmarginreq_s=maintmarginreq_s,
            netliquidation=netliquidation,
            netliquidation_c=netliquidation_c,
            netliquidation_s=netliquidation_s,
            netliquidationuncertainty=netliquidationuncertainty,
            nlvandmargininreview=nlvandmargininreview,
            pasharesvalue=pasharesvalue,
            pasharesvalue_c=pasharesvalue_c,
            pasharesvalue_s=pasharesvalue_s,
            physicalcertificatevalue=physicalcertificatevalue,
            physicalcertificatevalue_c=physicalcertificatevalue_c,
            physicalcertificatevalue_s=physicalcertificatevalue_s,
            postexpirationexcess=postexpirationexcess,
            postexpirationexcess_c=postexpirationexcess_c,
            postexpirationexcess_s=postexpirationexcess_s,
            postexpirationmargin=postexpirationmargin,
            postexpirationmargin_c=postexpirationmargin_c,
            postexpirationmargin_s=postexpirationmargin_s,
            previousdayequitywithloanvalue=previousdayequitywithloanvalue,
            previousdayequitywithloanvalue_s=previousdayequitywithloanvalue_s,
            regtequity=regtequity,
            regtequity_s=regtequity_s,
            regtmargin=regtmargin,
            regtmargin_s=regtmargin_s,
            segmenttitle_c=segmenttitle_c,
            segmenttitle_s=segmenttitle_s,
            sma=sma,
            sma_s=sma_s,
            totalcashvalue=totalcashvalue,
            totalcashvalue_c=totalcashvalue_c,
            totalcashvalue_s=totalcashvalue_s,
            totaldebitcardpendingcharges=totaldebitcardpendingcharges,
            totaldebitcardpendingcharges_c=totaldebitcardpendingcharges_c,
            totaldebitcardpendingcharges_s=totaldebitcardpendingcharges_s,
            tradingtype_s=tradingtype_s,
            whatifpmenabled=whatifpmenabled,
        )

        portfolio_summary.additional_properties = d
        return portfolio_summary

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
