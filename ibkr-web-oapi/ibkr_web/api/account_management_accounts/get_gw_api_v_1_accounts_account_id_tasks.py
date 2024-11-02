from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gw_api_v1_accounts_account_id_tasks_type import GetGwApiV1AccountsAccountIdTasksType
from ...models.pending_tasks_response import PendingTasksResponse
from ...models.problem_detail_response import ProblemDetailResponse
from ...models.registration_tasks_response import RegistrationTasksResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    type: Union[Unset, GetGwApiV1AccountsAccountIdTasksType] = GetGwApiV1AccountsAccountIdTasksType.REGISTRATION,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/gw/api/v1/accounts/{account_id}/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetailResponse, Union["PendingTasksResponse", "RegistrationTasksResponse"]]]:
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

        def _parse_response_200(data: object) -> Union["PendingTasksResponse", "RegistrationTasksResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RegistrationTasksResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = PendingTasksResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[ProblemDetailResponse, Union["PendingTasksResponse", "RegistrationTasksResponse"]]]:
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
    type: Union[Unset, GetGwApiV1AccountsAccountIdTasksType] = GetGwApiV1AccountsAccountIdTasksType.REGISTRATION,
) -> Response[Union[ProblemDetailResponse, Union["PendingTasksResponse", "RegistrationTasksResponse"]]]:
    """Get Registration Tasks

     Query registration tasks assigned to account and pending tasks that are required for account
    approval<br><br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):
        type (Union[Unset, GetGwApiV1AccountsAccountIdTasksType]):  Default:
            GetGwApiV1AccountsAccountIdTasksType.REGISTRATION.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, Union['PendingTasksResponse', 'RegistrationTasksResponse']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetGwApiV1AccountsAccountIdTasksType] = GetGwApiV1AccountsAccountIdTasksType.REGISTRATION,
) -> Optional[Union[ProblemDetailResponse, Union["PendingTasksResponse", "RegistrationTasksResponse"]]]:
    """Get Registration Tasks

     Query registration tasks assigned to account and pending tasks that are required for account
    approval<br><br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):
        type (Union[Unset, GetGwApiV1AccountsAccountIdTasksType]):  Default:
            GetGwApiV1AccountsAccountIdTasksType.REGISTRATION.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, Union['PendingTasksResponse', 'RegistrationTasksResponse']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetGwApiV1AccountsAccountIdTasksType] = GetGwApiV1AccountsAccountIdTasksType.REGISTRATION,
) -> Response[Union[ProblemDetailResponse, Union["PendingTasksResponse", "RegistrationTasksResponse"]]]:
    """Get Registration Tasks

     Query registration tasks assigned to account and pending tasks that are required for account
    approval<br><br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):
        type (Union[Unset, GetGwApiV1AccountsAccountIdTasksType]):  Default:
            GetGwApiV1AccountsAccountIdTasksType.REGISTRATION.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, Union['PendingTasksResponse', 'RegistrationTasksResponse']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetGwApiV1AccountsAccountIdTasksType] = GetGwApiV1AccountsAccountIdTasksType.REGISTRATION,
) -> Optional[Union[ProblemDetailResponse, Union["PendingTasksResponse", "RegistrationTasksResponse"]]]:
    """Get Registration Tasks

     Query registration tasks assigned to account and pending tasks that are required for account
    approval<br><br>**Scope**: `accounts.read`<br>**Security Policy**: `HTTPS`

    Args:
        account_id (str):
        type (Union[Unset, GetGwApiV1AccountsAccountIdTasksType]):  Default:
            GetGwApiV1AccountsAccountIdTasksType.REGISTRATION.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, Union['PendingTasksResponse', 'RegistrationTasksResponse']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            type=type,
        )
    ).parsed
