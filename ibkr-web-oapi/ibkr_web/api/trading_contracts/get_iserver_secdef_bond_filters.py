from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bond_filters_response import BondFiltersResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    symbol: str,
    issue_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["symbol"] = symbol

    params["issueId"] = issue_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/secdef/bond-filters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BondFiltersResponse]]:
    if response.status_code == 200:
        response_200 = BondFiltersResponse.from_dict(response.json())

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
) -> Response[Union[Any, BondFiltersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: str,
    issue_id: str,
) -> Response[Union[Any, BondFiltersResponse]]:
    """Search Bond Filter Information

     Request a list of filters relating to a given Bond issuerID. The issuerId is retrieved from
    /iserver/secdef/search and can be used in /iserver/secdef/info?issuerId={issuerId} for retrieving
    conIds.

    Args:
        symbol (str): This should always be set to “BOND” Example: BOND.
        issue_id (str): Specifies the issuerId value used to designate the bond issuer type.
            Example: e1400715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BondFiltersResponse]]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        issue_id=issue_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: str,
    issue_id: str,
) -> Optional[Union[Any, BondFiltersResponse]]:
    """Search Bond Filter Information

     Request a list of filters relating to a given Bond issuerID. The issuerId is retrieved from
    /iserver/secdef/search and can be used in /iserver/secdef/info?issuerId={issuerId} for retrieving
    conIds.

    Args:
        symbol (str): This should always be set to “BOND” Example: BOND.
        issue_id (str): Specifies the issuerId value used to designate the bond issuer type.
            Example: e1400715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BondFiltersResponse]
    """

    return sync_detailed(
        client=client,
        symbol=symbol,
        issue_id=issue_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: str,
    issue_id: str,
) -> Response[Union[Any, BondFiltersResponse]]:
    """Search Bond Filter Information

     Request a list of filters relating to a given Bond issuerID. The issuerId is retrieved from
    /iserver/secdef/search and can be used in /iserver/secdef/info?issuerId={issuerId} for retrieving
    conIds.

    Args:
        symbol (str): This should always be set to “BOND” Example: BOND.
        issue_id (str): Specifies the issuerId value used to designate the bond issuer type.
            Example: e1400715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BondFiltersResponse]]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        issue_id=issue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: str,
    issue_id: str,
) -> Optional[Union[Any, BondFiltersResponse]]:
    """Search Bond Filter Information

     Request a list of filters relating to a given Bond issuerID. The issuerId is retrieved from
    /iserver/secdef/search and can be used in /iserver/secdef/info?issuerId={issuerId} for retrieving
    conIds.

    Args:
        symbol (str): This should always be set to “BOND” Example: BOND.
        issue_id (str): Specifies the issuerId value used to designate the bond issuer type.
            Example: e1400715.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BondFiltersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            symbol=symbol,
            issue_id=issue_id,
        )
    ).parsed
