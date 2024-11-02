from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contract_info import ContractInfo
from ...types import Response


def _get_kwargs(
    conid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/iserver/contract/{conid}/info",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ContractInfo]]:
    if response.status_code == 200:
        response_200 = ContractInfo.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, ContractInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ContractInfo]]:
    """Contract information by Contract ID

     Requests full contract details for the given conid.

    Args:
        conid (str): Contract identifier for the requested contract of interest. Example: 265598.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ContractInfo]]
    """

    kwargs = _get_kwargs(
        conid=conid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ContractInfo]]:
    """Contract information by Contract ID

     Requests full contract details for the given conid.

    Args:
        conid (str): Contract identifier for the requested contract of interest. Example: 265598.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ContractInfo]
    """

    return sync_detailed(
        conid=conid,
        client=client,
    ).parsed


async def asyncio_detailed(
    conid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ContractInfo]]:
    """Contract information by Contract ID

     Requests full contract details for the given conid.

    Args:
        conid (str): Contract identifier for the requested contract of interest. Example: 265598.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ContractInfo]]
    """

    kwargs = _get_kwargs(
        conid=conid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ContractInfo]]:
    """Contract information by Contract ID

     Requests full contract details for the given conid.

    Args:
        conid (str): Contract identifier for the requested contract of interest. Example: 265598.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ContractInfo]
    """

    return (
        await asyncio_detailed(
            conid=conid,
            client=client,
        )
    ).parsed
