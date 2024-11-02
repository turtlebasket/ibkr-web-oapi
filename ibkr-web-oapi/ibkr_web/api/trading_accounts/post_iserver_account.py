from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_only_response import ErrorOnlyResponse
from ...models.post_iserver_account_body import PostIserverAccountBody
from ...models.set_account_response import SetAccountResponse
from ...types import Response


def _get_kwargs(
    *,
    body: PostIserverAccountBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/iserver/account",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorOnlyResponse, SetAccountResponse]]:
    if response.status_code == 200:
        response_200 = SetAccountResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = ErrorOnlyResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorOnlyResponse, SetAccountResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverAccountBody,
) -> Response[Union[Any, ErrorOnlyResponse, SetAccountResponse]]:
    """Switch Account

     Switch the active account for how you request data. Only available for financial advisors and multi-
    account structures.

    Args:
        body (PostIserverAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorOnlyResponse, SetAccountResponse]]
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
    body: PostIserverAccountBody,
) -> Optional[Union[Any, ErrorOnlyResponse, SetAccountResponse]]:
    """Switch Account

     Switch the active account for how you request data. Only available for financial advisors and multi-
    account structures.

    Args:
        body (PostIserverAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorOnlyResponse, SetAccountResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverAccountBody,
) -> Response[Union[Any, ErrorOnlyResponse, SetAccountResponse]]:
    """Switch Account

     Switch the active account for how you request data. Only available for financial advisors and multi-
    account structures.

    Args:
        body (PostIserverAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorOnlyResponse, SetAccountResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverAccountBody,
) -> Optional[Union[Any, ErrorOnlyResponse, SetAccountResponse]]:
    """Switch Account

     Switch the active account for how you request data. Only available for financial advisors and multi-
    account structures.

    Args:
        body (PostIserverAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorOnlyResponse, SetAccountResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
