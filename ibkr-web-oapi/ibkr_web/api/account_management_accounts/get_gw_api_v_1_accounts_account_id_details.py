from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_details_response import AccountDetailsResponse
from ...models.problem_detail_response import ProblemDetailResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/gw/api/v1/accounts/{account_id}/details",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountDetailsResponse, ProblemDetailResponse]]:
    if response.status_code == 400:
        response_400 = ProblemDetailResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = ProblemDetailResponse.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = ProblemDetailResponse.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = AccountDetailsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ProblemDetailResponse.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AccountDetailsResponse, ProblemDetailResponse]]:
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
) -> Response[Union[AccountDetailsResponse, ProblemDetailResponse]]:
    """Get Account Information

     <br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountDetailsResponse, ProblemDetailResponse]]
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
) -> Optional[Union[AccountDetailsResponse, ProblemDetailResponse]]:
    """Get Account Information

     <br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountDetailsResponse, ProblemDetailResponse]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AccountDetailsResponse, ProblemDetailResponse]]:
    """Get Account Information

     <br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountDetailsResponse, ProblemDetailResponse]]
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
) -> Optional[Union[AccountDetailsResponse, ProblemDetailResponse]]:
    """Get Account Information

     <br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountDetailsResponse, ProblemDetailResponse]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
