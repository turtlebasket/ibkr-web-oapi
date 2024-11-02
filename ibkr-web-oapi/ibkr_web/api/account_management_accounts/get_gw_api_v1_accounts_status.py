from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_status_bulk_response import AccountStatusBulkResponse
from ...models.account_status_request import AccountStatusRequest
from ...models.problem_detail_response import ProblemDetailResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_status_request: "AccountStatusRequest",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_account_status_request = account_status_request.to_dict()
    params.update(json_account_status_request)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/gw/api/v1/accounts/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountStatusBulkResponse, ProblemDetailResponse]]:
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
        response_200 = AccountStatusBulkResponse.from_dict(response.json())

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
) -> Response[Union[AccountStatusBulkResponse, ProblemDetailResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    account_status_request: "AccountStatusRequest",
) -> Response[Union[AccountStatusBulkResponse, ProblemDetailResponse]]:
    """Get Status of Accounts

     Query status of all accounts associated with ‘Client ID'<br><br>**Scope**:
    `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_status_request (AccountStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountStatusBulkResponse, ProblemDetailResponse]]
    """

    kwargs = _get_kwargs(
        account_status_request=account_status_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    account_status_request: "AccountStatusRequest",
) -> Optional[Union[AccountStatusBulkResponse, ProblemDetailResponse]]:
    """Get Status of Accounts

     Query status of all accounts associated with ‘Client ID'<br><br>**Scope**:
    `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_status_request (AccountStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountStatusBulkResponse, ProblemDetailResponse]
    """

    return sync_detailed(
        client=client,
        account_status_request=account_status_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    account_status_request: "AccountStatusRequest",
) -> Response[Union[AccountStatusBulkResponse, ProblemDetailResponse]]:
    """Get Status of Accounts

     Query status of all accounts associated with ‘Client ID'<br><br>**Scope**:
    `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_status_request (AccountStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountStatusBulkResponse, ProblemDetailResponse]]
    """

    kwargs = _get_kwargs(
        account_status_request=account_status_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    account_status_request: "AccountStatusRequest",
) -> Optional[Union[AccountStatusBulkResponse, ProblemDetailResponse]]:
    """Get Status of Accounts

     Query status of all accounts associated with ‘Client ID'<br><br>**Scope**:
    `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_status_request (AccountStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountStatusBulkResponse, ProblemDetailResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_status_request=account_status_request,
        )
    ).parsed