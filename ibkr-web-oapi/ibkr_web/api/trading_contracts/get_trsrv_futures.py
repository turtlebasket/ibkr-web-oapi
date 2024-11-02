from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    symbols: str,
    exchange: Union[Unset, Any] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["symbols"] = symbols

    params["exchange"] = exchange

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/trsrv/futures",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    symbols: str,
    exchange: Union[Unset, Any] = UNSET,
) -> Response[Any]:
    """Future  Security Definition By Symbol

     Returns a list of non-expired future contracts for given symbol(s)

    Args:
        symbols (str): Indicate the symbol(s) of the underlier you are trying to retrieve futures
            on. Accepts comma delimited string of symbols. Example: ES,MES.
        exchange (Union[Unset, Any]): exchange

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        symbols=symbols,
        exchange=exchange,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    symbols: str,
    exchange: Union[Unset, Any] = UNSET,
) -> Response[Any]:
    """Future  Security Definition By Symbol

     Returns a list of non-expired future contracts for given symbol(s)

    Args:
        symbols (str): Indicate the symbol(s) of the underlier you are trying to retrieve futures
            on. Accepts comma delimited string of symbols. Example: ES,MES.
        exchange (Union[Unset, Any]): exchange

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        symbols=symbols,
        exchange=exchange,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
