from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_preview import OrderPreview
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
        "url": f"/iserver/account/{account_id}/orders/whatif",
    }

    _body = []
    for componentsschemasorders_submission_request_item_data in body:
        componentsschemasorders_submission_request_item = componentsschemasorders_submission_request_item_data.to_dict()
        _body.append(componentsschemasorders_submission_request_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, OrderPreview]]:
    if response.status_code == 200:
        response_200 = OrderPreview.from_dict(response.json())

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
) -> Response[Union[Any, OrderPreview]]:
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
) -> Response[Union[Any, OrderPreview]]:
    """Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

     Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

    Args:
        account_id (str):  Example: DU123456.
        body (List['SingleOrderSubmissionRequest']): Array of order tickets objects. Only one
            order ticket object may be submitted per request, unless constructing a bracket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrderPreview]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SingleOrderSubmissionRequest"],
) -> Optional[Union[Any, OrderPreview]]:
    """Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

     Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

    Args:
        account_id (str):  Example: DU123456.
        body (List['SingleOrderSubmissionRequest']): Array of order tickets objects. Only one
            order ticket object may be submitted per request, unless constructing a bracket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OrderPreview]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SingleOrderSubmissionRequest"],
) -> Response[Union[Any, OrderPreview]]:
    """Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

     Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

    Args:
        account_id (str):  Example: DU123456.
        body (List['SingleOrderSubmissionRequest']): Array of order tickets objects. Only one
            order ticket object may be submitted per request, unless constructing a bracket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrderPreview]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["SingleOrderSubmissionRequest"],
) -> Optional[Union[Any, OrderPreview]]:
    """Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

     Preview the projected effects of an order ticket or bracket of orders, including cost and changes to
    margin and account equity.

    Args:
        account_id (str):  Example: DU123456.
        body (List['SingleOrderSubmissionRequest']): Array of order tickets objects. Only one
            order ticket object may be submitted per request, unless constructing a bracket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OrderPreview]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
