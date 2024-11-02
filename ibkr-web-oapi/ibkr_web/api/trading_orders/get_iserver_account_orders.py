from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_iserver_account_orders_filters import GetIserverAccountOrdersFilters
from ...models.live_orders_response import LiveOrdersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filters: Union[Unset, GetIserverAccountOrdersFilters] = UNSET,
    force: Union[Unset, bool] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_filters: Union[Unset, str] = UNSET
    if not isinstance(filters, Unset):
        json_filters = filters.value

    params["filters"] = json_filters

    params["force"] = force

    params["accountId"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/account/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LiveOrdersResponse]]:
    if response.status_code == 200:
        response_200 = LiveOrdersResponse.from_dict(response.json())

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
) -> Response[Union[Any, LiveOrdersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, GetIserverAccountOrdersFilters] = UNSET,
    force: Union[Unset, bool] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, LiveOrdersResponse]]:
    """Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

     Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

    Args:
        filters (Union[Unset, GetIserverAccountOrdersFilters]):  Example: Filled,SortByTime.
        force (Union[Unset, bool]):
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LiveOrdersResponse]]
    """

    kwargs = _get_kwargs(
        filters=filters,
        force=force,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, GetIserverAccountOrdersFilters] = UNSET,
    force: Union[Unset, bool] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, LiveOrdersResponse]]:
    """Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

     Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

    Args:
        filters (Union[Unset, GetIserverAccountOrdersFilters]):  Example: Filled,SortByTime.
        force (Union[Unset, bool]):
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LiveOrdersResponse]
    """

    return sync_detailed(
        client=client,
        filters=filters,
        force=force,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, GetIserverAccountOrdersFilters] = UNSET,
    force: Union[Unset, bool] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, LiveOrdersResponse]]:
    """Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

     Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

    Args:
        filters (Union[Unset, GetIserverAccountOrdersFilters]):  Example: Filled,SortByTime.
        force (Union[Unset, bool]):
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LiveOrdersResponse]]
    """

    kwargs = _get_kwargs(
        filters=filters,
        force=force,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, GetIserverAccountOrdersFilters] = UNSET,
    force: Union[Unset, bool] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, LiveOrdersResponse]]:
    """Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

     Retrieves open orders and filled or cancelled orders submitted during the current brokerage session.

    Args:
        filters (Union[Unset, GetIserverAccountOrdersFilters]):  Example: Filled,SortByTime.
        force (Union[Unset, bool]):
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LiveOrdersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
            force=force,
            account_id=account_id,
        )
    ).parsed
