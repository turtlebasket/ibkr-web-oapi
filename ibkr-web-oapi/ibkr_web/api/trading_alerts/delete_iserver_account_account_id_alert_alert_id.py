from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_deletion_response import AlertDeletionResponse
from ...models.delete_iserver_account_account_id_alert_alert_id_body import (
    DeleteIserverAccountAccountIdAlertAlertIdBody,
)
from ...models.error_only_response import ErrorOnlyResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    alert_id: str,
    *,
    body: DeleteIserverAccountAccountIdAlertAlertIdBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/iserver/account/{account_id}/alert/{alert_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]:
    if response.status_code == 200:
        response_200 = AlertDeletionResponse.from_dict(response.json())

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
) -> Response[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteIserverAccountAccountIdAlertAlertIdBody,
) -> Response[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]:
    """Delete an alert

     Permanently delete an existing alert. Deleting an MTA alert will reset it to the default state.

    Args:
        account_id (str):  Example: U1234567.
        alert_id (str): order_id returned from the original alert creation, or from the list of
            available alerts. Example: 9876543210.
        body (DeleteIserverAccountAccountIdAlertAlertIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteIserverAccountAccountIdAlertAlertIdBody,
) -> Optional[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]:
    """Delete an alert

     Permanently delete an existing alert. Deleting an MTA alert will reset it to the default state.

    Args:
        account_id (str):  Example: U1234567.
        alert_id (str): order_id returned from the original alert creation, or from the list of
            available alerts. Example: 9876543210.
        body (DeleteIserverAccountAccountIdAlertAlertIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertDeletionResponse, Any, ErrorOnlyResponse]
    """

    return sync_detailed(
        account_id=account_id,
        alert_id=alert_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteIserverAccountAccountIdAlertAlertIdBody,
) -> Response[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]:
    """Delete an alert

     Permanently delete an existing alert. Deleting an MTA alert will reset it to the default state.

    Args:
        account_id (str):  Example: U1234567.
        alert_id (str): order_id returned from the original alert creation, or from the list of
            available alerts. Example: 9876543210.
        body (DeleteIserverAccountAccountIdAlertAlertIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        alert_id=alert_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteIserverAccountAccountIdAlertAlertIdBody,
) -> Optional[Union[AlertDeletionResponse, Any, ErrorOnlyResponse]]:
    """Delete an alert

     Permanently delete an existing alert. Deleting an MTA alert will reset it to the default state.

    Args:
        account_id (str):  Example: U1234567.
        alert_id (str): order_id returned from the original alert creation, or from the list of
            available alerts. Example: 9876543210.
        body (DeleteIserverAccountAccountIdAlertAlertIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertDeletionResponse, Any, ErrorOnlyResponse]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            alert_id=alert_id,
            client=client,
            body=body,
        )
    ).parsed
