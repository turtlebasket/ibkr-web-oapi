from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fyi_unreadnumber_response_200 import GetFyiUnreadnumberResponse200
from ...models.get_fyi_unreadnumber_response_423 import GetFyiUnreadnumberResponse423
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/fyi/unreadnumber",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]:
    if response.status_code == 200:
        response_200 = GetFyiUnreadnumberResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 423:
        response_423 = GetFyiUnreadnumberResponse423.from_dict(response.json())

        return response_423
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
) -> Response[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]:
    """Unread Bulletins

     Returns the total number of unread notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]:
    """Unread Bulletins

     Returns the total number of unread notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]:
    """Unread Bulletins

     Returns the total number of unread notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]]:
    """Unread Bulletins

     Returns the total number of unread notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetFyiUnreadnumberResponse200, GetFyiUnreadnumberResponse423]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
