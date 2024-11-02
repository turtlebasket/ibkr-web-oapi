from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_iserver_watchlists_sc import GetIserverWatchlistsSC
from ...models.watchlists_response import WatchlistsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sc: Union[Unset, GetIserverWatchlistsSC] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_sc: Union[Unset, str] = UNSET
    if not isinstance(sc, Unset):
        json_sc = sc.value

    params["SC"] = json_sc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/watchlists",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WatchlistsResponse]]:
    if response.status_code == 200:
        response_200 = WatchlistsResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, WatchlistsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sc: Union[Unset, GetIserverWatchlistsSC] = UNSET,
) -> Response[Union[Any, WatchlistsResponse]]:
    """Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

     Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

    Args:
        sc (Union[Unset, GetIserverWatchlistsSC]):  Example: USER_WATCHLIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WatchlistsResponse]]
    """

    kwargs = _get_kwargs(
        sc=sc,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sc: Union[Unset, GetIserverWatchlistsSC] = UNSET,
) -> Optional[Union[Any, WatchlistsResponse]]:
    """Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

     Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

    Args:
        sc (Union[Unset, GetIserverWatchlistsSC]):  Example: USER_WATCHLIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WatchlistsResponse]
    """

    return sync_detailed(
        client=client,
        sc=sc,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sc: Union[Unset, GetIserverWatchlistsSC] = UNSET,
) -> Response[Union[Any, WatchlistsResponse]]:
    """Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

     Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

    Args:
        sc (Union[Unset, GetIserverWatchlistsSC]):  Example: USER_WATCHLIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WatchlistsResponse]]
    """

    kwargs = _get_kwargs(
        sc=sc,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    sc: Union[Unset, GetIserverWatchlistsSC] = UNSET,
) -> Optional[Union[Any, WatchlistsResponse]]:
    """Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

     Retrieve all saved watchlists stored on IB backend for the username in use in the current Web API
    session.

    Args:
        sc (Union[Unset, GetIserverWatchlistsSC]):  Example: USER_WATCHLIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WatchlistsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            sc=sc,
        )
    ).parsed
