from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dyn_account_search_response import DynAccountSearchResponse
from ...types import Response


def _get_kwargs(
    search_pattern: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/iserver/account/search/{search_pattern}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DynAccountSearchResponse]]:
    if response.status_code == 200:
        response_200 = DynAccountSearchResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DynAccountSearchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    search_pattern: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DynAccountSearchResponse]]:
    """Search Dynamic Account

     Returns a list of accounts matching a query pattern set in the request. Broker accounts configured
    with the DYNACCT property will not receive account information at login. Instead, they must
    dynamically query then set their account number. Customers without the DYNACCT property will receive
    a 503 error.

    Args:
        search_pattern (str): The pattern used to describe credentials to search for. Including
            part of part of an account ID will return the full value. Example: U123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DynAccountSearchResponse]]
    """

    kwargs = _get_kwargs(
        search_pattern=search_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    search_pattern: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DynAccountSearchResponse]]:
    """Search Dynamic Account

     Returns a list of accounts matching a query pattern set in the request. Broker accounts configured
    with the DYNACCT property will not receive account information at login. Instead, they must
    dynamically query then set their account number. Customers without the DYNACCT property will receive
    a 503 error.

    Args:
        search_pattern (str): The pattern used to describe credentials to search for. Including
            part of part of an account ID will return the full value. Example: U123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DynAccountSearchResponse]
    """

    return sync_detailed(
        search_pattern=search_pattern,
        client=client,
    ).parsed


async def asyncio_detailed(
    search_pattern: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DynAccountSearchResponse]]:
    """Search Dynamic Account

     Returns a list of accounts matching a query pattern set in the request. Broker accounts configured
    with the DYNACCT property will not receive account information at login. Instead, they must
    dynamically query then set their account number. Customers without the DYNACCT property will receive
    a 503 error.

    Args:
        search_pattern (str): The pattern used to describe credentials to search for. Including
            part of part of an account ID will return the full value. Example: U123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DynAccountSearchResponse]]
    """

    kwargs = _get_kwargs(
        search_pattern=search_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    search_pattern: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DynAccountSearchResponse]]:
    """Search Dynamic Account

     Returns a list of accounts matching a query pattern set in the request. Broker accounts configured
    with the DYNACCT property will not receive account information at login. Instead, they must
    dynamically query then set their account number. Customers without the DYNACCT property will receive
    a 503 error.

    Args:
        search_pattern (str): The pattern used to describe credentials to search for. Including
            part of part of an account ID will return the full value. Example: U123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DynAccountSearchResponse]
    """

    return (
        await asyncio_detailed(
            search_pattern=search_pattern,
            client=client,
        )
    ).parsed
