from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.iserver_history_response import IserverHistoryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conid: str,
    exchange: Union[Unset, str] = UNSET,
    period: str,
    bar: str,
    start_time: Union[Unset, str] = UNSET,
    outside_rth: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["conid"] = conid

    params["exchange"] = exchange

    params["period"] = period

    params["bar"] = bar

    params["startTime"] = start_time

    params["outsideRth"] = outside_rth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/marketdata/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, IserverHistoryResponse]]:
    if response.status_code == 200:
        response_200 = IserverHistoryResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, IserverHistoryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: str,
    exchange: Union[Unset, str] = UNSET,
    period: str,
    bar: str,
    start_time: Union[Unset, str] = UNSET,
    outside_rth: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, IserverHistoryResponse]]:
    """Request historical data for an instrument in the form of OHLC bars.

     Request historical data for an instrument in the form of OHLC bars.

    Args:
        conid (str):  Example: 265598.
        exchange (Union[Unset, str]):  Example: NYSE.
        period (str):  Example: 6d.
        bar (str):  Example: 5mins.
        start_time (Union[Unset, str]): UTC datetime string in format YYYYMMDD-hh:mm:ss. Example:
            20231018-16:00:00.
        outside_rth (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IserverHistoryResponse]]
    """

    kwargs = _get_kwargs(
        conid=conid,
        exchange=exchange,
        period=period,
        bar=bar,
        start_time=start_time,
        outside_rth=outside_rth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: str,
    exchange: Union[Unset, str] = UNSET,
    period: str,
    bar: str,
    start_time: Union[Unset, str] = UNSET,
    outside_rth: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, IserverHistoryResponse]]:
    """Request historical data for an instrument in the form of OHLC bars.

     Request historical data for an instrument in the form of OHLC bars.

    Args:
        conid (str):  Example: 265598.
        exchange (Union[Unset, str]):  Example: NYSE.
        period (str):  Example: 6d.
        bar (str):  Example: 5mins.
        start_time (Union[Unset, str]): UTC datetime string in format YYYYMMDD-hh:mm:ss. Example:
            20231018-16:00:00.
        outside_rth (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, IserverHistoryResponse]
    """

    return sync_detailed(
        client=client,
        conid=conid,
        exchange=exchange,
        period=period,
        bar=bar,
        start_time=start_time,
        outside_rth=outside_rth,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: str,
    exchange: Union[Unset, str] = UNSET,
    period: str,
    bar: str,
    start_time: Union[Unset, str] = UNSET,
    outside_rth: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, IserverHistoryResponse]]:
    """Request historical data for an instrument in the form of OHLC bars.

     Request historical data for an instrument in the form of OHLC bars.

    Args:
        conid (str):  Example: 265598.
        exchange (Union[Unset, str]):  Example: NYSE.
        period (str):  Example: 6d.
        bar (str):  Example: 5mins.
        start_time (Union[Unset, str]): UTC datetime string in format YYYYMMDD-hh:mm:ss. Example:
            20231018-16:00:00.
        outside_rth (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IserverHistoryResponse]]
    """

    kwargs = _get_kwargs(
        conid=conid,
        exchange=exchange,
        period=period,
        bar=bar,
        start_time=start_time,
        outside_rth=outside_rth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: str,
    exchange: Union[Unset, str] = UNSET,
    period: str,
    bar: str,
    start_time: Union[Unset, str] = UNSET,
    outside_rth: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, IserverHistoryResponse]]:
    """Request historical data for an instrument in the form of OHLC bars.

     Request historical data for an instrument in the form of OHLC bars.

    Args:
        conid (str):  Example: 265598.
        exchange (Union[Unset, str]):  Example: NYSE.
        period (str):  Example: 6d.
        bar (str):  Example: 5mins.
        start_time (Union[Unset, str]): UTC datetime string in format YYYYMMDD-hh:mm:ss. Example:
            20231018-16:00:00.
        outside_rth (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, IserverHistoryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            conid=conid,
            exchange=exchange,
            period=period,
            bar=bar,
            start_time=start_time,
            outside_rth=outside_rth,
        )
    ).parsed
