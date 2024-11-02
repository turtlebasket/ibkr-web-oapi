from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_oauth_access_token_response_200 import PostOauthAccessTokenResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/oauth/access_token",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostOauthAccessTokenResponse200]]:
    if response.status_code == 200:
        response_200 = PostOauthAccessTokenResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PostOauthAccessTokenResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostOauthAccessTokenResponse200]]:
    """Request an access token for the IB username that has granted authorization to the consumer.

     Request an access token for the IB username that has granted authorization to the consumer.

    Args:
        authorization (Union[Unset, str]):  Example: OAuth oauth_verifier="1e1dc5666e87ca5a18e0",o
            auth_token="e0d75b4c5c1d2c0f2af7",oauth_consumer_key="TESTCONS",oauth_nonce="v235...456h",
            oauth_signature="af1%252...0nd2",oauth_signature_method="RSA-
            SHA256",oauth_timestamp="1714489450",realm="test_realm".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostOauthAccessTokenResponse200]]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostOauthAccessTokenResponse200]]:
    """Request an access token for the IB username that has granted authorization to the consumer.

     Request an access token for the IB username that has granted authorization to the consumer.

    Args:
        authorization (Union[Unset, str]):  Example: OAuth oauth_verifier="1e1dc5666e87ca5a18e0",o
            auth_token="e0d75b4c5c1d2c0f2af7",oauth_consumer_key="TESTCONS",oauth_nonce="v235...456h",
            oauth_signature="af1%252...0nd2",oauth_signature_method="RSA-
            SHA256",oauth_timestamp="1714489450",realm="test_realm".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostOauthAccessTokenResponse200]
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostOauthAccessTokenResponse200]]:
    """Request an access token for the IB username that has granted authorization to the consumer.

     Request an access token for the IB username that has granted authorization to the consumer.

    Args:
        authorization (Union[Unset, str]):  Example: OAuth oauth_verifier="1e1dc5666e87ca5a18e0",o
            auth_token="e0d75b4c5c1d2c0f2af7",oauth_consumer_key="TESTCONS",oauth_nonce="v235...456h",
            oauth_signature="af1%252...0nd2",oauth_signature_method="RSA-
            SHA256",oauth_timestamp="1714489450",realm="test_realm".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostOauthAccessTokenResponse200]]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostOauthAccessTokenResponse200]]:
    """Request an access token for the IB username that has granted authorization to the consumer.

     Request an access token for the IB username that has granted authorization to the consumer.

    Args:
        authorization (Union[Unset, str]):  Example: OAuth oauth_verifier="1e1dc5666e87ca5a18e0",o
            auth_token="e0d75b4c5c1d2c0f2af7",oauth_consumer_key="TESTCONS",oauth_nonce="v235...456h",
            oauth_signature="af1%252...0nd2",oauth_signature_method="RSA-
            SHA256",oauth_timestamp="1714489450",realm="test_realm".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostOauthAccessTokenResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
