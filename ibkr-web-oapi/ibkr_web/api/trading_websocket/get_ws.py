from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ws_connection import GetWsConnection
from ...models.get_ws_upgrade import GetWsUpgrade
from ...types import UNSET, Response


def _get_kwargs(
    *,
    oauth_token: str,
    connection: GetWsConnection,
    upgrade: GetWsUpgrade,
    api: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["Connection"] = str(connection)

    headers["Upgrade"] = str(upgrade)

    cookies = {}
    cookies["api"] = api

    params: Dict[str, Any] = {}

    params["oauth_token"] = oauth_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ws",
        "params": params,
        "cookies": cookies,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 101:
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
    oauth_token: str,
    connection: GetWsConnection,
    upgrade: GetWsUpgrade,
    api: str,
) -> Response[Any]:
    """Open websocket.

     Open websocket.

    Args:
        oauth_token (str):  Example: a1b2c3d4.
        connection (GetWsConnection):
        upgrade (GetWsUpgrade):
        api (str):  Example: c8fh17fnjr01hfnrh39rhfh8shd1hd93.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        oauth_token=oauth_token,
        connection=connection,
        upgrade=upgrade,
        api=api,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    oauth_token: str,
    connection: GetWsConnection,
    upgrade: GetWsUpgrade,
    api: str,
) -> Response[Any]:
    """Open websocket.

     Open websocket.

    Args:
        oauth_token (str):  Example: a1b2c3d4.
        connection (GetWsConnection):
        upgrade (GetWsUpgrade):
        api (str):  Example: c8fh17fnjr01hfnrh39rhfh8shd1hd93.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        oauth_token=oauth_token,
        connection=connection,
        upgrade=upgrade,
        api=api,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
