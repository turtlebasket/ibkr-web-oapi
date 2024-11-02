from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_statements_response import GetStatementsResponse
from ...models.insufficient_scope_response import InsufficientScopeResponse
from ...models.internal_server_error_response import InternalServerErrorResponse
from ...models.invalid_access_token_response import InvalidAccessTokenResponse
from ...models.missing_required_parameter_response import MissingRequiredParameterResponse
from ...models.stmt_request import StmtRequest
from ...models.unauthorized_access_response import UnauthorizedAccessResponse
from ...types import Response


def _get_kwargs(
    *,
    body: StmtRequest,
    authorization: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["authorization"] = authorization

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/gw/api/v1/statements",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetStatementsResponse,
        InsufficientScopeResponse,
        InternalServerErrorResponse,
        InvalidAccessTokenResponse,
        MissingRequiredParameterResponse,
        UnauthorizedAccessResponse,
    ]
]:
    if response.status_code == 200:
        response_200 = GetStatementsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = MissingRequiredParameterResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = InvalidAccessTokenResponse.from_dict(response.json())

        return response_401
    if response.status_code == 402:
        response_402 = UnauthorizedAccessResponse.from_dict(response.json())

        return response_402
    if response.status_code == 403:
        response_403 = InsufficientScopeResponse.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = InternalServerErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetStatementsResponse,
        InsufficientScopeResponse,
        InternalServerErrorResponse,
        InvalidAccessTokenResponse,
        MissingRequiredParameterResponse,
        UnauthorizedAccessResponse,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StmtRequest,
    authorization: str,
) -> Response[
    Union[
        GetStatementsResponse,
        InsufficientScopeResponse,
        InternalServerErrorResponse,
        InvalidAccessTokenResponse,
        MissingRequiredParameterResponse,
        UnauthorizedAccessResponse,
    ]
]:
    """Generates statements in supported formats based on request parameters.

     <br>**Scope**: `statements.read` OR `statements.write`<br>**Security Policy**: `Signed JWT`

    Args:
        authorization (str):  Example: Bearer eyJ0eXAiOiJKV1....
        body (StmtRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStatementsResponse, InsufficientScopeResponse, InternalServerErrorResponse, InvalidAccessTokenResponse, MissingRequiredParameterResponse, UnauthorizedAccessResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StmtRequest,
    authorization: str,
) -> Optional[
    Union[
        GetStatementsResponse,
        InsufficientScopeResponse,
        InternalServerErrorResponse,
        InvalidAccessTokenResponse,
        MissingRequiredParameterResponse,
        UnauthorizedAccessResponse,
    ]
]:
    """Generates statements in supported formats based on request parameters.

     <br>**Scope**: `statements.read` OR `statements.write`<br>**Security Policy**: `Signed JWT`

    Args:
        authorization (str):  Example: Bearer eyJ0eXAiOiJKV1....
        body (StmtRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStatementsResponse, InsufficientScopeResponse, InternalServerErrorResponse, InvalidAccessTokenResponse, MissingRequiredParameterResponse, UnauthorizedAccessResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StmtRequest,
    authorization: str,
) -> Response[
    Union[
        GetStatementsResponse,
        InsufficientScopeResponse,
        InternalServerErrorResponse,
        InvalidAccessTokenResponse,
        MissingRequiredParameterResponse,
        UnauthorizedAccessResponse,
    ]
]:
    """Generates statements in supported formats based on request parameters.

     <br>**Scope**: `statements.read` OR `statements.write`<br>**Security Policy**: `Signed JWT`

    Args:
        authorization (str):  Example: Bearer eyJ0eXAiOiJKV1....
        body (StmtRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStatementsResponse, InsufficientScopeResponse, InternalServerErrorResponse, InvalidAccessTokenResponse, MissingRequiredParameterResponse, UnauthorizedAccessResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StmtRequest,
    authorization: str,
) -> Optional[
    Union[
        GetStatementsResponse,
        InsufficientScopeResponse,
        InternalServerErrorResponse,
        InvalidAccessTokenResponse,
        MissingRequiredParameterResponse,
        UnauthorizedAccessResponse,
    ]
]:
    """Generates statements in supported formats based on request parameters.

     <br>**Scope**: `statements.read` OR `statements.write`<br>**Security Policy**: `Signed JWT`

    Args:
        authorization (str):  Example: Bearer eyJ0eXAiOiJKV1....
        body (StmtRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStatementsResponse, InsufficientScopeResponse, InternalServerErrorResponse, InvalidAccessTokenResponse, MissingRequiredParameterResponse, UnauthorizedAccessResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
