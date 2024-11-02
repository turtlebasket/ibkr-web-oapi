from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notifications_item import NotificationsItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    max_: str,
    include: Union[Unset, Any] = UNSET,
    exclude: Union[Unset, Any] = UNSET,
    id: Union[Unset, Any] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["max"] = max_

    params["include"] = include

    params["exclude"] = exclude

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/fyi/notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["NotificationsItem"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasnotifications_item_data in _response_200:
            componentsschemasnotifications_item = NotificationsItem.from_dict(componentsschemasnotifications_item_data)

            response_200.append(componentsschemasnotifications_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["NotificationsItem"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    max_: str,
    include: Union[Unset, Any] = UNSET,
    exclude: Union[Unset, Any] = UNSET,
    id: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, List["NotificationsItem"]]]:
    """Get a list of notifications

     Get a list of available notifications.

    Args:
        max_ (str): Specify the maximum number of notifications to receive. Can request a maximum
            of 10 notifications.
             Example: 10.
        include (Union[Unset, Any]): include
        exclude (Union[Unset, Any]): exclude
        id (Union[Unset, Any]): if more required, notifcationId of last notification should be
            used to define next batch border

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['NotificationsItem']]]
    """

    kwargs = _get_kwargs(
        max_=max_,
        include=include,
        exclude=exclude,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    max_: str,
    include: Union[Unset, Any] = UNSET,
    exclude: Union[Unset, Any] = UNSET,
    id: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, List["NotificationsItem"]]]:
    """Get a list of notifications

     Get a list of available notifications.

    Args:
        max_ (str): Specify the maximum number of notifications to receive. Can request a maximum
            of 10 notifications.
             Example: 10.
        include (Union[Unset, Any]): include
        exclude (Union[Unset, Any]): exclude
        id (Union[Unset, Any]): if more required, notifcationId of last notification should be
            used to define next batch border

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['NotificationsItem']]
    """

    return sync_detailed(
        client=client,
        max_=max_,
        include=include,
        exclude=exclude,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    max_: str,
    include: Union[Unset, Any] = UNSET,
    exclude: Union[Unset, Any] = UNSET,
    id: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, List["NotificationsItem"]]]:
    """Get a list of notifications

     Get a list of available notifications.

    Args:
        max_ (str): Specify the maximum number of notifications to receive. Can request a maximum
            of 10 notifications.
             Example: 10.
        include (Union[Unset, Any]): include
        exclude (Union[Unset, Any]): exclude
        id (Union[Unset, Any]): if more required, notifcationId of last notification should be
            used to define next batch border

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['NotificationsItem']]]
    """

    kwargs = _get_kwargs(
        max_=max_,
        include=include,
        exclude=exclude,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    max_: str,
    include: Union[Unset, Any] = UNSET,
    exclude: Union[Unset, Any] = UNSET,
    id: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, List["NotificationsItem"]]]:
    """Get a list of notifications

     Get a list of available notifications.

    Args:
        max_ (str): Specify the maximum number of notifications to receive. Can request a maximum
            of 10 notifications.
             Example: 10.
        include (Union[Unset, Any]): include
        exclude (Union[Unset, Any]): exclude
        id (Union[Unset, Any]): if more required, notifcationId of last notification should be
            used to define next batch border

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['NotificationsItem']]
    """

    return (
        await asyncio_detailed(
            client=client,
            max_=max_,
            include=include,
            exclude=exclude,
            id=id,
        )
    ).parsed
