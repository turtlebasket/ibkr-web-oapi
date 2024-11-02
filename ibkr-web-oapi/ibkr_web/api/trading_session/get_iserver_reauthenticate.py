from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_iserver_reauthenticate_response_200 import GetIserverReauthenticateResponse200
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/reauthenticate",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetIserverReauthenticateResponse200]:
    if response.status_code == 200:
        response_200 = GetIserverReauthenticateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetIserverReauthenticateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetIserverReauthenticateResponse200]:
    """Re-authenticate the Brokerage Session

     When using the CP Gateway, this endpoint provides a way to reauthenticate to the Brokerage system as
    long as there is a valid brokerage session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIserverReauthenticateResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetIserverReauthenticateResponse200]:
    """Re-authenticate the Brokerage Session

     When using the CP Gateway, this endpoint provides a way to reauthenticate to the Brokerage system as
    long as there is a valid brokerage session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIserverReauthenticateResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetIserverReauthenticateResponse200]:
    """Re-authenticate the Brokerage Session

     When using the CP Gateway, this endpoint provides a way to reauthenticate to the Brokerage system as
    long as there is a valid brokerage session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIserverReauthenticateResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetIserverReauthenticateResponse200]:
    """Re-authenticate the Brokerage Session

     When using the CP Gateway, this endpoint provides a way to reauthenticate to the Brokerage system as
    long as there is a valid brokerage session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIserverReauthenticateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed