from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fyi_vt import FyiVT
from ...types import UNSET, Response


def _get_kwargs(
    *,
    enabled: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["enabled"] = enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/fyi/deliveryoptions/email",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FyiVT]]:
    if response.status_code == 200:
        response_200 = FyiVT.from_dict(response.json())

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
) -> Response[Union[Any, FyiVT]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled: Any,
) -> Response[Union[Any, FyiVT]]:
    """Enable/Disable Email Option

     Enable or disable your account’s primary email to receive notifications.

    Args:
        enabled (Any): Enable or disable your email. Value format: true: Enable; false: Disable

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FyiVT]]
    """

    kwargs = _get_kwargs(
        enabled=enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled: Any,
) -> Optional[Union[Any, FyiVT]]:
    """Enable/Disable Email Option

     Enable or disable your account’s primary email to receive notifications.

    Args:
        enabled (Any): Enable or disable your email. Value format: true: Enable; false: Disable

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FyiVT]
    """

    return sync_detailed(
        client=client,
        enabled=enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled: Any,
) -> Response[Union[Any, FyiVT]]:
    """Enable/Disable Email Option

     Enable or disable your account’s primary email to receive notifications.

    Args:
        enabled (Any): Enable or disable your email. Value format: true: Enable; false: Disable

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FyiVT]]
    """

    kwargs = _get_kwargs(
        enabled=enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled: Any,
) -> Optional[Union[Any, FyiVT]]:
    """Enable/Disable Email Option

     Enable or disable your account’s primary email to receive notifications.

    Args:
        enabled (Any): Enable or disable your email. Value format: true: Enable; false: Disable

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FyiVT]
    """

    return (
        await asyncio_detailed(
            client=client,
            enabled=enabled,
        )
    ).parsed
