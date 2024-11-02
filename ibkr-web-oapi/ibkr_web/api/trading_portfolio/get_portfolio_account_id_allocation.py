from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.portfolio_allocations import PortfolioAllocations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    model: Union[Unset, Any] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model"] = model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/portfolio/{account_id}/allocation",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PortfolioAllocations]]:
    if response.status_code == 200:
        response_200 = PortfolioAllocations.from_dict(response.json())

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
) -> Response[Union[Any, PortfolioAllocations]]:
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
    model: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, PortfolioAllocations]]:
    """Get an account's allocations by asset class, sector group, and sector.

     Get an account's allocations by asset class, sector group, and sector.

    Args:
        account_id (str): Account ID whose allocations are requested.
        model (Union[Unset, Any]): model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PortfolioAllocations]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        model=model,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    model: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, PortfolioAllocations]]:
    """Get an account's allocations by asset class, sector group, and sector.

     Get an account's allocations by asset class, sector group, and sector.

    Args:
        account_id (str): Account ID whose allocations are requested.
        model (Union[Unset, Any]): model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PortfolioAllocations]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        model=model,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    model: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, PortfolioAllocations]]:
    """Get an account's allocations by asset class, sector group, and sector.

     Get an account's allocations by asset class, sector group, and sector.

    Args:
        account_id (str): Account ID whose allocations are requested.
        model (Union[Unset, Any]): model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PortfolioAllocations]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        model=model,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    model: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, PortfolioAllocations]]:
    """Get an account's allocations by asset class, sector group, and sector.

     Get an account's allocations by asset class, sector group, and sector.

    Args:
        account_id (str): Account ID whose allocations are requested.
        model (Union[Unset, Any]): model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PortfolioAllocations]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            model=model,
        )
    ).parsed
