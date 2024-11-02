from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trades_response_item import TradesResponseItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["days"] = days

    params["accountId"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/account/trades",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["TradesResponseItem"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemastrades_response_item_data in _response_200:
            componentsschemastrades_response_item = TradesResponseItem.from_dict(
                componentsschemastrades_response_item_data
            )

            response_200.append(componentsschemastrades_response_item)

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
) -> Response[Union[Any, List["TradesResponseItem"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["TradesResponseItem"]]]:
    """Retrieve a list of trades.

     Retrieve a list of trades, up to a maximum of 7 days prior.

    Args:
        days (Union[Unset, str]):  Example: 3.
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['TradesResponseItem']]]
    """

    kwargs = _get_kwargs(
        days=days,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["TradesResponseItem"]]]:
    """Retrieve a list of trades.

     Retrieve a list of trades, up to a maximum of 7 days prior.

    Args:
        days (Union[Unset, str]):  Example: 3.
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['TradesResponseItem']]
    """

    return sync_detailed(
        client=client,
        days=days,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["TradesResponseItem"]]]:
    """Retrieve a list of trades.

     Retrieve a list of trades, up to a maximum of 7 days prior.

    Args:
        days (Union[Unset, str]):  Example: 3.
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['TradesResponseItem']]]
    """

    kwargs = _get_kwargs(
        days=days,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["TradesResponseItem"]]]:
    """Retrieve a list of trades.

     Retrieve a list of trades, up to a maximum of 7 days prior.

    Args:
        days (Union[Unset, str]):  Example: 3.
        account_id (Union[Unset, str]):  Example: DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['TradesResponseItem']]
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            account_id=account_id,
        )
    ).parsed
