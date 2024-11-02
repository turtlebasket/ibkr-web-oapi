from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_iserver_account_allocation_group_single_body import PostIserverAccountAllocationGroupSingleBody
from ...types import Response


def _get_kwargs(
    *,
    body: PostIserverAccountAllocationGroupSingleBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/iserver/account/allocation/group/single",
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverAccountAllocationGroupSingleBody,
) -> Response[Any]:
    """Retrieve Single Allocation Group

     Retrieves the configuration of a single account group. This describes the name of the allocation
    group, the specific accounts contained in the group, and the allocation method in use along with any
    relevant quantities.

    Args:
        body (PostIserverAccountAllocationGroupSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostIserverAccountAllocationGroupSingleBody,
) -> Response[Any]:
    """Retrieve Single Allocation Group

     Retrieves the configuration of a single account group. This describes the name of the allocation
    group, the specific accounts contained in the group, and the allocation method in use along with any
    relevant quantities.

    Args:
        body (PostIserverAccountAllocationGroupSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
