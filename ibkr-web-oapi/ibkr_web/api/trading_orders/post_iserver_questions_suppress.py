from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_iserver_questions_suppress_body import PostIserverQuestionsSuppressBody
from ...models.post_iserver_questions_suppress_response_200 import PostIserverQuestionsSuppressResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostIserverQuestionsSuppressBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/iserver/questions/suppress",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostIserverQuestionsSuppressResponse200]]:
    if response.status_code == 200:
        response_200 = PostIserverQuestionsSuppressResponse200.from_dict(response.json())

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
) -> Response[Union[Any, PostIserverQuestionsSuppressResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverQuestionsSuppressBody,
) -> Response[Union[Any, PostIserverQuestionsSuppressResponse200]]:
    """Suppress the specified order reply messages.

     Suppress the specified order reply messages for the duration of the brokerage session.

    Args:
        body (PostIserverQuestionsSuppressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostIserverQuestionsSuppressResponse200]]
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
    body: PostIserverQuestionsSuppressBody,
) -> Optional[Union[Any, PostIserverQuestionsSuppressResponse200]]:
    """Suppress the specified order reply messages.

     Suppress the specified order reply messages for the duration of the brokerage session.

    Args:
        body (PostIserverQuestionsSuppressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostIserverQuestionsSuppressResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverQuestionsSuppressBody,
) -> Response[Union[Any, PostIserverQuestionsSuppressResponse200]]:
    """Suppress the specified order reply messages.

     Suppress the specified order reply messages for the duration of the brokerage session.

    Args:
        body (PostIserverQuestionsSuppressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostIserverQuestionsSuppressResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverQuestionsSuppressBody,
) -> Optional[Union[Any, PostIserverQuestionsSuppressResponse200]]:
    """Suppress the specified order reply messages.

     Suppress the specified order reply messages for the duration of the brokerage session.

    Args:
        body (PostIserverQuestionsSuppressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostIserverQuestionsSuppressResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
