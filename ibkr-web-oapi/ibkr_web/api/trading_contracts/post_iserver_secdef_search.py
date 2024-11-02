from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_iserver_secdef_search_body import PostIserverSecdefSearchBody
from ...models.secdef_search_response_item import SecdefSearchResponseItem
from ...types import Response


def _get_kwargs(
    *,
    body: PostIserverSecdefSearchBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/iserver/secdef/search",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["SecdefSearchResponseItem"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemassecdef_search_response_item_data in _response_200:
            componentsschemassecdef_search_response_item = SecdefSearchResponseItem.from_dict(
                componentsschemassecdef_search_response_item_data
            )

            response_200.append(componentsschemassecdef_search_response_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[Union[Any, List["SecdefSearchResponseItem"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverSecdefSearchBody,
) -> Response[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        body (PostIserverSecdefSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SecdefSearchResponseItem']]]
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
    body: PostIserverSecdefSearchBody,
) -> Optional[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        body (PostIserverSecdefSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SecdefSearchResponseItem']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverSecdefSearchBody,
) -> Response[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        body (PostIserverSecdefSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SecdefSearchResponseItem']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverSecdefSearchBody,
) -> Optional[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        body (PostIserverSecdefSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SecdefSearchResponseItem']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
