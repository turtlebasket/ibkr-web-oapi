from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_trsrv_secdef_schedule_asset_class import GetTrsrvSecdefScheduleAssetClass
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_class: GetTrsrvSecdefScheduleAssetClass,
    symbol: str,
    exchange: Union[Unset, str] = UNSET,
    exchange_filter: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_asset_class = asset_class.value
    params["assetClass"] = json_asset_class

    params["symbol"] = symbol

    params["exchange"] = exchange

    params["exchangeFilter"] = exchange_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/trsrv/secdef/schedule",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 500:
        return None
    if response.status_code == 503:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    asset_class: GetTrsrvSecdefScheduleAssetClass,
    symbol: str,
    exchange: Union[Unset, str] = UNSET,
    exchange_filter: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Trading Schedule by Symbol

     Returns the trading schedule up to a month for the requested contract.

    Args:
        asset_class (GetTrsrvSecdefScheduleAssetClass): Specify the security type of the given
            contract. Valid asset classes are:
             * `STK` - Stock
             * `OPT` - Option
             * `FUT` - Future
             * `CFD` - Contract for Difference
             * `WAR` - Warrant
             * `SWP` - Forex
             * `FND` - Mutual Fund
             * `BND` - Bond
             * `ICS` - Inter-Commodity Spread
        symbol (str): Specify the symbol for your contract. Example: AAPL.
        exchange (Union[Unset, str]): Specify the primary exchange of your contract. Example:
            NASDAQ.
        exchange_filter (Union[Unset, str]): Specify all exchanges you want to retrieve data from.
            Example: AMEX,NASDAQ,NYSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asset_class=asset_class,
        symbol=symbol,
        exchange=exchange,
        exchange_filter=exchange_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    asset_class: GetTrsrvSecdefScheduleAssetClass,
    symbol: str,
    exchange: Union[Unset, str] = UNSET,
    exchange_filter: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Trading Schedule by Symbol

     Returns the trading schedule up to a month for the requested contract.

    Args:
        asset_class (GetTrsrvSecdefScheduleAssetClass): Specify the security type of the given
            contract. Valid asset classes are:
             * `STK` - Stock
             * `OPT` - Option
             * `FUT` - Future
             * `CFD` - Contract for Difference
             * `WAR` - Warrant
             * `SWP` - Forex
             * `FND` - Mutual Fund
             * `BND` - Bond
             * `ICS` - Inter-Commodity Spread
        symbol (str): Specify the symbol for your contract. Example: AAPL.
        exchange (Union[Unset, str]): Specify the primary exchange of your contract. Example:
            NASDAQ.
        exchange_filter (Union[Unset, str]): Specify all exchanges you want to retrieve data from.
            Example: AMEX,NASDAQ,NYSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asset_class=asset_class,
        symbol=symbol,
        exchange=exchange,
        exchange_filter=exchange_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
