from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failed_tickle_response import FailedTickleResponse
from ...models.successful_tickle_response import SuccessfulTickleResponse
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/tickle",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["FailedTickleResponse", "SuccessfulTickleResponse"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["FailedTickleResponse", "SuccessfulTickleResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemastickle_response_type_0 = SuccessfulTickleResponse.from_dict(data)

                return componentsschemastickle_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemastickle_response_type_1 = FailedTickleResponse.from_dict(data)

            return componentsschemastickle_response_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Union["FailedTickleResponse", "SuccessfulTickleResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Union["FailedTickleResponse", "SuccessfulTickleResponse"]]]:
    """Server ping.

     If the gateway has not received any requests for several minutes an open session will automatically
    timeout. The tickle endpoint pings the server to prevent the session from ending. It is expected to
    call this endpoint approximately every 60 seconds to maintain the connection to the brokerage
    session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['FailedTickleResponse', 'SuccessfulTickleResponse']]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Union["FailedTickleResponse", "SuccessfulTickleResponse"]]]:
    """Server ping.

     If the gateway has not received any requests for several minutes an open session will automatically
    timeout. The tickle endpoint pings the server to prevent the session from ending. It is expected to
    call this endpoint approximately every 60 seconds to maintain the connection to the brokerage
    session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['FailedTickleResponse', 'SuccessfulTickleResponse']]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Union["FailedTickleResponse", "SuccessfulTickleResponse"]]]:
    """Server ping.

     If the gateway has not received any requests for several minutes an open session will automatically
    timeout. The tickle endpoint pings the server to prevent the session from ending. It is expected to
    call this endpoint approximately every 60 seconds to maintain the connection to the brokerage
    session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['FailedTickleResponse', 'SuccessfulTickleResponse']]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Union["FailedTickleResponse", "SuccessfulTickleResponse"]]]:
    """Server ping.

     If the gateway has not received any requests for several minutes an open session will automatically
    timeout. The tickle endpoint pings the server to prevent the session from ending. It is expected to
    call this endpoint approximately every 60 seconds to maintain the connection to the brokerage
    session.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['FailedTickleResponse', 'SuccessfulTickleResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
