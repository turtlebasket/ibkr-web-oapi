from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_activation_request import AlertActivationRequest
from ...models.alert_activation_response import AlertActivationResponse
from ...models.error_only_response import ErrorOnlyResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: AlertActivationRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/iserver/account/{account_id}/alert/activate",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]:
    if response.status_code == 200:
        response_200 = AlertActivationResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = ErrorOnlyResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]:
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
    body: AlertActivationRequest,
) -> Response[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]:
    """Activate or deactivate an alert

     Activate or Deactivate existing alerts created for this account. This does not delete alerts, but
    disables notifications until reactivated.

    Args:
        account_id (str):  Example: U1234567.
        body (AlertActivationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertActivationRequest,
) -> Optional[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]:
    """Activate or deactivate an alert

     Activate or Deactivate existing alerts created for this account. This does not delete alerts, but
    disables notifications until reactivated.

    Args:
        account_id (str):  Example: U1234567.
        body (AlertActivationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertActivationResponse, Any, ErrorOnlyResponse]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertActivationRequest,
) -> Response[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]:
    """Activate or deactivate an alert

     Activate or Deactivate existing alerts created for this account. This does not delete alerts, but
    disables notifications until reactivated.

    Args:
        account_id (str):  Example: U1234567.
        body (AlertActivationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertActivationRequest,
) -> Optional[Union[AlertActivationResponse, Any, ErrorOnlyResponse]]:
    """Activate or deactivate an alert

     Activate or Deactivate existing alerts created for this account. This does not delete alerts, but
    disables notifications until reactivated.

    Args:
        account_id (str):  Example: U1234567.
        body (AlertActivationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertActivationResponse, Any, ErrorOnlyResponse]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
