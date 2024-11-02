from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_cancel_success import OrderCancelSuccess
from ...models.order_submit_error import OrderSubmitError
from ...types import Response


def _get_kwargs(
    account_id: str,
    order_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/iserver/account/{account_id}/order/{order_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["OrderCancelSuccess", "OrderSubmitError"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["OrderCancelSuccess", "OrderSubmitError"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = OrderCancelSuccess.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = OrderSubmitError.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[Any, Union["OrderCancelSuccess", "OrderSubmitError"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Union["OrderCancelSuccess", "OrderSubmitError"]]]:
    """Cancel an existing, unfilled order.

     Cancel an existing, unfilled order.

    Args:
        account_id (str):  Example: DU123456.
        order_id (str):  Example: 1799796559.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['OrderCancelSuccess', 'OrderSubmitError']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Union["OrderCancelSuccess", "OrderSubmitError"]]]:
    """Cancel an existing, unfilled order.

     Cancel an existing, unfilled order.

    Args:
        account_id (str):  Example: DU123456.
        order_id (str):  Example: 1799796559.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['OrderCancelSuccess', 'OrderSubmitError']]
    """

    return sync_detailed(
        account_id=account_id,
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Union["OrderCancelSuccess", "OrderSubmitError"]]]:
    """Cancel an existing, unfilled order.

     Cancel an existing, unfilled order.

    Args:
        account_id (str):  Example: DU123456.
        order_id (str):  Example: 1799796559.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['OrderCancelSuccess', 'OrderSubmitError']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Union["OrderCancelSuccess", "OrderSubmitError"]]]:
    """Cancel an existing, unfilled order.

     Cancel an existing, unfilled order.

    Args:
        account_id (str):  Example: DU123456.
        order_id (str):  Example: 1799796559.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['OrderCancelSuccess', 'OrderSubmitError']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            order_id=order_id,
            client=client,
        )
    ).parsed
