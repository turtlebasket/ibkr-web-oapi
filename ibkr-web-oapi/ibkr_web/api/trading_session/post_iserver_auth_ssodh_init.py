from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.brokerage_session_init_request import BrokerageSessionInitRequest
from ...models.brokerage_session_status import BrokerageSessionStatus
from ...types import Response


def _get_kwargs(
    *,
    body: BrokerageSessionInitRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/iserver/auth/ssodh/init",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BrokerageSessionStatus]]:
    if response.status_code == 200:
        response_200 = BrokerageSessionStatus.from_dict(response.json())

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
) -> Response[Union[Any, BrokerageSessionStatus]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrokerageSessionInitRequest,
) -> Response[Union[Any, BrokerageSessionStatus]]:
    """Initialize Brokerage Session.

     After retrieving the access token and subsequent Live Session Token, customers can initialize their
    brokerage session with the ssodh/init endpoint.

    Args:
        body (BrokerageSessionInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BrokerageSessionStatus]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrokerageSessionInitRequest,
) -> Optional[Union[Any, BrokerageSessionStatus]]:
    """Initialize Brokerage Session.

     After retrieving the access token and subsequent Live Session Token, customers can initialize their
    brokerage session with the ssodh/init endpoint.

    Args:
        body (BrokerageSessionInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BrokerageSessionStatus]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrokerageSessionInitRequest,
) -> Response[Union[Any, BrokerageSessionStatus]]:
    """Initialize Brokerage Session.

     After retrieving the access token and subsequent Live Session Token, customers can initialize their
    brokerage session with the ssodh/init endpoint.

    Args:
        body (BrokerageSessionInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BrokerageSessionStatus]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrokerageSessionInitRequest,
) -> Optional[Union[Any, BrokerageSessionStatus]]:
    """Initialize Brokerage Session.

     After retrieving the access token and subsequent Live Session Token, customers can initialize their
    brokerage session with the ssodh/init endpoint.

    Args:
        body (BrokerageSessionInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BrokerageSessionStatus]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
