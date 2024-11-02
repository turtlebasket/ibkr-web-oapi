from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.single_order_submission_request import SingleOrderSubmissionRequest
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: List["SingleOrderSubmissionRequest"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/iserver/account/{account_id}/orders",
    }

    _body = []
    for componentsschemasorders_submission_request_item_data in body:
        componentsschemasorders_submission_request_item = componentsschemasorders_submission_request_item_data.to_dict()
        _body.append(componentsschemasorders_submission_request_item)

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
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SingleOrderSubmissionRequest"],
) -> Response[Any]:
    """Submit a new order(s) ticket, bracket, or OCA group.

     Submit a new order(s) ticket, bracket, or OCA group.

    Args:
        account_id (str):  Example: DU123456.
        body (List['SingleOrderSubmissionRequest']): Array of order tickets objects. Only one
            order ticket object may be submitted per request, unless constructing a bracket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SingleOrderSubmissionRequest"],
) -> Response[Any]:
    """Submit a new order(s) ticket, bracket, or OCA group.

     Submit a new order(s) ticket, bracket, or OCA group.

    Args:
        account_id (str):  Example: DU123456.
        body (List['SingleOrderSubmissionRequest']): Array of order tickets objects. Only one
            order ticket object may be submitted per request, unless constructing a bracket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
