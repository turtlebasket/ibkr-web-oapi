from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_portfolio_account_id_positions_invalidate_response_200 import (
    PostPortfolioAccountIdPositionsInvalidateResponse200,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/portfolio/{account_id}/positions/invalidate",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]:
    if response.status_code == 200:
        response_200 = PostPortfolioAccountIdPositionsInvalidateResponse200.from_dict(response.json())

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
) -> Response[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]:
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
) -> Response[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]:
    """Instructs IB to discard cached portfolio positions for a given account.

     Instructs IB to discard cached portfolio positions for a given account, so that the next request for
    positions delivers freshly obtained data.

    Args:
        account_id (str): Account ID whose cached portfolio positions will be discarded. Example:
            DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]:
    """Instructs IB to discard cached portfolio positions for a given account.

     Instructs IB to discard cached portfolio positions for a given account, so that the next request for
    positions delivers freshly obtained data.

    Args:
        account_id (str): Account ID whose cached portfolio positions will be discarded. Example:
            DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]:
    """Instructs IB to discard cached portfolio positions for a given account.

     Instructs IB to discard cached portfolio positions for a given account, so that the next request for
    positions delivers freshly obtained data.

    Args:
        account_id (str): Account ID whose cached portfolio positions will be discarded. Example:
            DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]]:
    """Instructs IB to discard cached portfolio positions for a given account.

     Instructs IB to discard cached portfolio positions for a given account, so that the next request for
    positions delivers freshly obtained data.

    Args:
        account_id (str): Account ID whose cached portfolio positions will be discarded. Example:
            DU123456.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostPortfolioAccountIdPositionsInvalidateResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
