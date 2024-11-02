from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_iserver_reply_reply_id_body import PostIserverReplyReplyIdBody
from ...types import Response


def _get_kwargs(
    reply_id: str,
    *,
    body: PostIserverReplyReplyIdBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/iserver/reply/{reply_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 401:
        return None
    if response.status_code == 500:
        return None
    if response.status_code == 503:
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
    reply_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverReplyReplyIdBody,
) -> Response[Any]:
    """Confirm an order reply message.

     Confirm an order reply message and continue with submission of order ticket.

    Args:
        reply_id (str):  Example: 99097238-9824-4830-84ef-46979aa22593.
        body (PostIserverReplyReplyIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reply_id=reply_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    reply_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverReplyReplyIdBody,
) -> Response[Any]:
    """Confirm an order reply message.

     Confirm an order reply message and continue with submission of order ticket.

    Args:
        reply_id (str):  Example: 99097238-9824-4830-84ef-46979aa22593.
        body (PostIserverReplyReplyIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reply_id=reply_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
