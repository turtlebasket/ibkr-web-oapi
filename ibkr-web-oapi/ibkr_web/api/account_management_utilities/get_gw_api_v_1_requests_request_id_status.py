from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.am_request_status_response import AmRequestStatusResponse
from ...models.get_gw_api_v1_requests_request_id_status_type import GetGwApiV1RequestsRequestIdStatusType
from ...models.problem_detail_response import ProblemDetailResponse
from ...models.status_response import StatusResponse
from ...types import UNSET, Response


def _get_kwargs(
    request_id: str,
    *,
    type: GetGwApiV1RequestsRequestIdStatusType,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_type = type.value
    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/gw/api/v1/requests/{request_id}/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetailResponse, Union["AmRequestStatusResponse", "StatusResponse"]]]:
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

        def _parse_response_200(data: object) -> Union["AmRequestStatusResponse", "StatusResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = AmRequestStatusResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = StatusResponse.from_dict(data)

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
) -> Response[Union[ProblemDetailResponse, Union["AmRequestStatusResponse", "StatusResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetGwApiV1RequestsRequestIdStatusType,
) -> Response[Union[ProblemDetailResponse, Union["AmRequestStatusResponse", "StatusResponse"]]]:
    """Get status of a request

     Returns status for account management request<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        request_id (str):
        type (GetGwApiV1RequestsRequestIdStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, Union['AmRequestStatusResponse', 'StatusResponse']]]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetGwApiV1RequestsRequestIdStatusType,
) -> Optional[Union[ProblemDetailResponse, Union["AmRequestStatusResponse", "StatusResponse"]]]:
    """Get status of a request

     Returns status for account management request<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        request_id (str):
        type (GetGwApiV1RequestsRequestIdStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, Union['AmRequestStatusResponse', 'StatusResponse']]
    """

    return sync_detailed(
        request_id=request_id,
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetGwApiV1RequestsRequestIdStatusType,
) -> Response[Union[ProblemDetailResponse, Union["AmRequestStatusResponse", "StatusResponse"]]]:
    """Get status of a request

     Returns status for account management request<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        request_id (str):
        type (GetGwApiV1RequestsRequestIdStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetailResponse, Union['AmRequestStatusResponse', 'StatusResponse']]]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetGwApiV1RequestsRequestIdStatusType,
) -> Optional[Union[ProblemDetailResponse, Union["AmRequestStatusResponse", "StatusResponse"]]]:
    """Get status of a request

     Returns status for account management request<br><br>**Scope**: `accounts.read`<br>**Security
    Policy**: `HTTPS`

    Args:
        request_id (str):
        type (GetGwApiV1RequestsRequestIdStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetailResponse, Union['AmRequestStatusResponse', 'StatusResponse']]
    """

    return (
        await asyncio_detailed(
            request_id=request_id,
            client=client,
            type=type,
        )
    ).parsed
