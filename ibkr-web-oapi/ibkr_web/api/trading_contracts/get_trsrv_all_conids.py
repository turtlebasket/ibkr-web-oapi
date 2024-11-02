from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_trsrv_all_conids_response_200_item import GetTrsrvAllConidsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    exchange: str,
    asset_class: Union[Unset, Any] = "STK",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["exchange"] = exchange

    params["assetClass"] = asset_class

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/trsrv/all-conids",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["GetTrsrvAllConidsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetTrsrvAllConidsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, List["GetTrsrvAllConidsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    exchange: str,
    asset_class: Union[Unset, Any] = "STK",
) -> Response[Union[Any, List["GetTrsrvAllConidsResponse200Item"]]]:
    """All Conids by Exchange

     Send out a request to retrieve all contracts made available on a requested exchange. This returns
    all contracts that are tradable on the exchange, even those that are not using the exchange as their
    primary listing.

    Args:
        exchange (str): Exchange from which derivatives should be retrieved from. Example: AMEX.
        asset_class (Union[Unset, Any]): asset class Default: 'STK'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetTrsrvAllConidsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        exchange=exchange,
        asset_class=asset_class,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    exchange: str,
    asset_class: Union[Unset, Any] = "STK",
) -> Optional[Union[Any, List["GetTrsrvAllConidsResponse200Item"]]]:
    """All Conids by Exchange

     Send out a request to retrieve all contracts made available on a requested exchange. This returns
    all contracts that are tradable on the exchange, even those that are not using the exchange as their
    primary listing.

    Args:
        exchange (str): Exchange from which derivatives should be retrieved from. Example: AMEX.
        asset_class (Union[Unset, Any]): asset class Default: 'STK'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetTrsrvAllConidsResponse200Item']]
    """

    return sync_detailed(
        client=client,
        exchange=exchange,
        asset_class=asset_class,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    exchange: str,
    asset_class: Union[Unset, Any] = "STK",
) -> Response[Union[Any, List["GetTrsrvAllConidsResponse200Item"]]]:
    """All Conids by Exchange

     Send out a request to retrieve all contracts made available on a requested exchange. This returns
    all contracts that are tradable on the exchange, even those that are not using the exchange as their
    primary listing.

    Args:
        exchange (str): Exchange from which derivatives should be retrieved from. Example: AMEX.
        asset_class (Union[Unset, Any]): asset class Default: 'STK'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetTrsrvAllConidsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        exchange=exchange,
        asset_class=asset_class,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    exchange: str,
    asset_class: Union[Unset, Any] = "STK",
) -> Optional[Union[Any, List["GetTrsrvAllConidsResponse200Item"]]]:
    """All Conids by Exchange

     Send out a request to retrieve all contracts made available on a requested exchange. This returns
    all contracts that are tradable on the exchange, even those that are not using the exchange as their
    primary listing.

    Args:
        exchange (str): Exchange from which derivatives should be retrieved from. Example: AMEX.
        asset_class (Union[Unset, Any]): asset class Default: 'STK'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetTrsrvAllConidsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            exchange=exchange,
            asset_class=asset_class,
        )
    ).parsed
