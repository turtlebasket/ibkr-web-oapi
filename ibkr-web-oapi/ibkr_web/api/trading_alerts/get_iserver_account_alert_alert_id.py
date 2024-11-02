from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_details import AlertDetails
from ...models.get_iserver_account_alert_alert_id_type import GetIserverAccountAlertAlertIdType
from ...types import UNSET, Response


def _get_kwargs(
    alert_id: str,
    *,
    type: GetIserverAccountAlertAlertIdType,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_type = type.value
    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/iserver/account/alert/{alert_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertDetails, Any]]:
    if response.status_code == 200:
        response_200 = AlertDetails.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AlertDetails, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetIserverAccountAlertAlertIdType,
) -> Response[Union[AlertDetails, Any]]:
    """Get details of a specific alert

     Request details of a specific alert by providing the assigned alertId Id.

    Args:
        alert_id (str): alert identifier, internally referenced as order id
        type (GetIserverAccountAlertAlertIdType): queryType

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertDetails, Any]]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetIserverAccountAlertAlertIdType,
) -> Optional[Union[AlertDetails, Any]]:
    """Get details of a specific alert

     Request details of a specific alert by providing the assigned alertId Id.

    Args:
        alert_id (str): alert identifier, internally referenced as order id
        type (GetIserverAccountAlertAlertIdType): queryType

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertDetails, Any]
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetIserverAccountAlertAlertIdType,
) -> Response[Union[AlertDetails, Any]]:
    """Get details of a specific alert

     Request details of a specific alert by providing the assigned alertId Id.

    Args:
        alert_id (str): alert identifier, internally referenced as order id
        type (GetIserverAccountAlertAlertIdType): queryType

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertDetails, Any]]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: GetIserverAccountAlertAlertIdType,
) -> Optional[Union[AlertDetails, Any]]:
    """Get details of a specific alert

     Request details of a specific alert by providing the assigned alertId Id.

    Args:
        alert_id (str): alert identifier, internally referenced as order id
        type (GetIserverAccountAlertAlertIdType): queryType

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertDetails, Any]
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
            type=type,
        )
    ).parsed
