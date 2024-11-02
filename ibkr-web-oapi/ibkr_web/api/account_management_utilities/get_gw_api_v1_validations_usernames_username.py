from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_detail_response import ProblemDetailResponse
from ...models.user_name_available_response import UserNameAvailableResponse
from ...types import Response


def _get_kwargs(
    username: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/gw/api/v1/validations/usernames/{username}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
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
        response_200 = UserNameAvailableResponse.from_dict(response.json())

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
) -> Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Verify user availability

     Verify whether user is valid and available<br><br>**Scope**: `accounts.read` OR
    `validations.read`<br>**Security Policy**: `HTTPS`

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Verify user availability

     Verify whether user is valid and available<br><br>**Scope**: `accounts.read` OR
    `validations.read`<br>**Security Policy**: `HTTPS`

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, UserNameAvailableResponse]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Verify user availability

     Verify whether user is valid and available<br><br>**Scope**: `accounts.read` OR
    `validations.read`<br>**Security Policy**: `HTTPS`

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, UserNameAvailableResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetailResponse, UserNameAvailableResponse]]:
    """Verify user availability

     Verify whether user is valid and available<br><br>**Scope**: `accounts.read` OR
    `validations.read`<br>**Security Policy**: `HTTPS`

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, UserNameAvailableResponse]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
