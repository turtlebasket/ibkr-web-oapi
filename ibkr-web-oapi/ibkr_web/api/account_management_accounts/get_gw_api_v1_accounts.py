from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_details_response import FileDetailsResponse
from ...models.problem_detail_response import ProblemDetailResponse
from ...models.response_file_response import ResponseFileResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["account_id"] = account_id

    params["external_id"] = external_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/gw/api/v1/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetailResponse, Union["FileDetailsResponse", "ResponseFileResponse"]]]:
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

        def _parse_response_200(data: object) -> Union["FileDetailsResponse", "ResponseFileResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = FileDetailsResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ResponseFileResponse.from_dict(data)

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
) -> Response[Union[ProblemDetailResponse, Union["FileDetailsResponse", "ResponseFileResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetailResponse, Union["FileDetailsResponse", "ResponseFileResponse"]]]:
    """Retrieve Processed Application

     Retrieve the application request and IBKR response data based on IBKR accountId or externalId. Only
    available for accounts that originate via API<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        account_id (Union[Unset, str]):
        external_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, Union['FileDetailsResponse', 'ResponseFileResponse']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        external_id=external_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetailResponse, Union["FileDetailsResponse", "ResponseFileResponse"]]]:
    """Retrieve Processed Application

     Retrieve the application request and IBKR response data based on IBKR accountId or externalId. Only
    available for accounts that originate via API<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        account_id (Union[Unset, str]):
        external_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, Union['FileDetailsResponse', 'ResponseFileResponse']]
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        external_id=external_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetailResponse, Union["FileDetailsResponse", "ResponseFileResponse"]]]:
    """Retrieve Processed Application

     Retrieve the application request and IBKR response data based on IBKR accountId or externalId. Only
    available for accounts that originate via API<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        account_id (Union[Unset, str]):
        external_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, Union['FileDetailsResponse', 'ResponseFileResponse']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        external_id=external_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: Union[Unset, str] = UNSET,
    external_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetailResponse, Union["FileDetailsResponse", "ResponseFileResponse"]]]:
    """Retrieve Processed Application

     Retrieve the application request and IBKR response data based on IBKR accountId or externalId. Only
    available for accounts that originate via API<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        account_id (Union[Unset, str]):
        external_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, Union['FileDetailsResponse', 'ResponseFileResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            external_id=external_id,
        )
    ).parsed
