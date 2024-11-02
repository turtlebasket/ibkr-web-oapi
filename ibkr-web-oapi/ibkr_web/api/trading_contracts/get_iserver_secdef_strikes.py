from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_iserver_secdef_strikes_response_200 import GetIserverSecdefStrikesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conid: str,
    sectype: str,
    month: str,
    exchange: Union[Unset, str] = "SMART",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["conid"] = conid

    params["sectype"] = sectype

    params["month"] = month

    params["exchange"] = exchange

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/secdef/strikes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetIserverSecdefStrikesResponse200]]:
    if response.status_code == 200:
        response_200 = GetIserverSecdefStrikesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetIserverSecdefStrikesResponse200]]:
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
    sectype: str,
    month: str,
    exchange: Union[Unset, str] = "SMART",
) -> Response[Union[Any, GetIserverSecdefStrikesResponse200]]:
    """Get strikes

     strikes

    Args:
        conid (str): Contract identifier of the underlying. May also pass the final derivative
            conid directly. Example: 265598.
        sectype (str): Security type of the requested contract of interest. Example: OPT.
        month (str): Expiration month for the given derivative. Example: JAN24.
        exchange (Union[Unset, str]): Exchange from which derivatives should be retrieved from.
            Default: 'SMART'. Example: NASDAQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetIserverSecdefStrikesResponse200]]
    """

    kwargs = _get_kwargs(
        conid=conid,
        sectype=sectype,
        month=month,
        exchange=exchange,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: str,
    sectype: str,
    month: str,
    exchange: Union[Unset, str] = "SMART",
) -> Optional[Union[Any, GetIserverSecdefStrikesResponse200]]:
    """Get strikes

     strikes

    Args:
        conid (str): Contract identifier of the underlying. May also pass the final derivative
            conid directly. Example: 265598.
        sectype (str): Security type of the requested contract of interest. Example: OPT.
        month (str): Expiration month for the given derivative. Example: JAN24.
        exchange (Union[Unset, str]): Exchange from which derivatives should be retrieved from.
            Default: 'SMART'. Example: NASDAQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetIserverSecdefStrikesResponse200]
    """

    return sync_detailed(
        client=client,
        conid=conid,
        sectype=sectype,
        month=month,
        exchange=exchange,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: str,
    sectype: str,
    month: str,
    exchange: Union[Unset, str] = "SMART",
) -> Response[Union[Any, GetIserverSecdefStrikesResponse200]]:
    """Get strikes

     strikes

    Args:
        conid (str): Contract identifier of the underlying. May also pass the final derivative
            conid directly. Example: 265598.
        sectype (str): Security type of the requested contract of interest. Example: OPT.
        month (str): Expiration month for the given derivative. Example: JAN24.
        exchange (Union[Unset, str]): Exchange from which derivatives should be retrieved from.
            Default: 'SMART'. Example: NASDAQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetIserverSecdefStrikesResponse200]]
    """

    kwargs = _get_kwargs(
        conid=conid,
        sectype=sectype,
        month=month,
        exchange=exchange,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: str,
    sectype: str,
    month: str,
    exchange: Union[Unset, str] = "SMART",
) -> Optional[Union[Any, GetIserverSecdefStrikesResponse200]]:
    """Get strikes

     strikes

    Args:
        conid (str): Contract identifier of the underlying. May also pass the final derivative
            conid directly. Example: 265598.
        sectype (str): Security type of the requested contract of interest. Example: OPT.
        month (str): Expiration month for the given derivative. Example: JAN24.
        exchange (Union[Unset, str]): Exchange from which derivatives should be retrieved from.
            Default: 'SMART'. Example: NASDAQ.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetIserverSecdefStrikesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            conid=conid,
            sectype=sectype,
            month=month,
            exchange=exchange,
        )
    ).parsed
