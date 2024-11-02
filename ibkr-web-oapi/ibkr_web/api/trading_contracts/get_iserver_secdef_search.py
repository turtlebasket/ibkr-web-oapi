from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_iserver_secdef_search_sec_type import GetIserverSecdefSearchSecType
from ...models.secdef_search_response_item import SecdefSearchResponseItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    symbol: Union[Unset, str] = UNSET,
    sec_type: Union[Unset, GetIserverSecdefSearchSecType] = GetIserverSecdefSearchSecType.STK,
    name: Union[Unset, bool] = UNSET,
    more: Union[Unset, bool] = UNSET,
    fund: Union[Unset, bool] = UNSET,
    fund_family_conid_ex: Union[Unset, str] = UNSET,
    pattern: Union[Unset, bool] = UNSET,
    referrer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["symbol"] = symbol

    json_sec_type: Union[Unset, str] = UNSET
    if not isinstance(sec_type, Unset):
        json_sec_type = sec_type.value

    params["secType"] = json_sec_type

    params["name"] = name

    params["more"] = more

    params["fund"] = fund

    params["fundFamilyConidEx"] = fund_family_conid_ex

    params["pattern"] = pattern

    params["referrer"] = referrer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/secdef/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["SecdefSearchResponseItem"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemassecdef_search_response_item_data in _response_200:
            componentsschemassecdef_search_response_item = SecdefSearchResponseItem.from_dict(
                componentsschemassecdef_search_response_item_data
            )

            response_200.append(componentsschemassecdef_search_response_item)

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
) -> Response[Union[Any, List["SecdefSearchResponseItem"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    sec_type: Union[Unset, GetIserverSecdefSearchSecType] = GetIserverSecdefSearchSecType.STK,
    name: Union[Unset, bool] = UNSET,
    more: Union[Unset, bool] = UNSET,
    fund: Union[Unset, bool] = UNSET,
    fund_family_conid_ex: Union[Unset, str] = UNSET,
    pattern: Union[Unset, bool] = UNSET,
    referrer: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        symbol (Union[Unset, str]): The ticker symbol, bond issuer type, or company name of the
            equity you are looking to trade. Example: AAPL.
        sec_type (Union[Unset, GetIserverSecdefSearchSecType]):  Default:
            GetIserverSecdefSearchSecType.STK.
        name (Union[Unset, bool]): Denotes if the symbol value is the ticker symbol or part of the
            company's name.
        more (Union[Unset, bool]):
        fund (Union[Unset, bool]): fund search
        fund_family_conid_ex (Union[Unset, str]):
        pattern (Union[Unset, bool]): pattern search
        referrer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SecdefSearchResponseItem']]]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        sec_type=sec_type,
        name=name,
        more=more,
        fund=fund,
        fund_family_conid_ex=fund_family_conid_ex,
        pattern=pattern,
        referrer=referrer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    sec_type: Union[Unset, GetIserverSecdefSearchSecType] = GetIserverSecdefSearchSecType.STK,
    name: Union[Unset, bool] = UNSET,
    more: Union[Unset, bool] = UNSET,
    fund: Union[Unset, bool] = UNSET,
    fund_family_conid_ex: Union[Unset, str] = UNSET,
    pattern: Union[Unset, bool] = UNSET,
    referrer: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        symbol (Union[Unset, str]): The ticker symbol, bond issuer type, or company name of the
            equity you are looking to trade. Example: AAPL.
        sec_type (Union[Unset, GetIserverSecdefSearchSecType]):  Default:
            GetIserverSecdefSearchSecType.STK.
        name (Union[Unset, bool]): Denotes if the symbol value is the ticker symbol or part of the
            company's name.
        more (Union[Unset, bool]):
        fund (Union[Unset, bool]): fund search
        fund_family_conid_ex (Union[Unset, str]):
        pattern (Union[Unset, bool]): pattern search
        referrer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SecdefSearchResponseItem']]
    """

    return sync_detailed(
        client=client,
        symbol=symbol,
        sec_type=sec_type,
        name=name,
        more=more,
        fund=fund,
        fund_family_conid_ex=fund_family_conid_ex,
        pattern=pattern,
        referrer=referrer,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    sec_type: Union[Unset, GetIserverSecdefSearchSecType] = GetIserverSecdefSearchSecType.STK,
    name: Union[Unset, bool] = UNSET,
    more: Union[Unset, bool] = UNSET,
    fund: Union[Unset, bool] = UNSET,
    fund_family_conid_ex: Union[Unset, str] = UNSET,
    pattern: Union[Unset, bool] = UNSET,
    referrer: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        symbol (Union[Unset, str]): The ticker symbol, bond issuer type, or company name of the
            equity you are looking to trade. Example: AAPL.
        sec_type (Union[Unset, GetIserverSecdefSearchSecType]):  Default:
            GetIserverSecdefSearchSecType.STK.
        name (Union[Unset, bool]): Denotes if the symbol value is the ticker symbol or part of the
            company's name.
        more (Union[Unset, bool]):
        fund (Union[Unset, bool]): fund search
        fund_family_conid_ex (Union[Unset, str]):
        pattern (Union[Unset, bool]): pattern search
        referrer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SecdefSearchResponseItem']]]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        sec_type=sec_type,
        name=name,
        more=more,
        fund=fund,
        fund_family_conid_ex=fund_family_conid_ex,
        pattern=pattern,
        referrer=referrer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    sec_type: Union[Unset, GetIserverSecdefSearchSecType] = GetIserverSecdefSearchSecType.STK,
    name: Union[Unset, bool] = UNSET,
    more: Union[Unset, bool] = UNSET,
    fund: Union[Unset, bool] = UNSET,
    fund_family_conid_ex: Union[Unset, str] = UNSET,
    pattern: Union[Unset, bool] = UNSET,
    referrer: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["SecdefSearchResponseItem"]]]:
    """Returns a list of contracts based on symbol.

     Returns a list of contracts based on the search symbol provided as a query param.

    Args:
        symbol (Union[Unset, str]): The ticker symbol, bond issuer type, or company name of the
            equity you are looking to trade. Example: AAPL.
        sec_type (Union[Unset, GetIserverSecdefSearchSecType]):  Default:
            GetIserverSecdefSearchSecType.STK.
        name (Union[Unset, bool]): Denotes if the symbol value is the ticker symbol or part of the
            company's name.
        more (Union[Unset, bool]):
        fund (Union[Unset, bool]): fund search
        fund_family_conid_ex (Union[Unset, str]):
        pattern (Union[Unset, bool]): pattern search
        referrer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SecdefSearchResponseItem']]
    """

    return (
        await asyncio_detailed(
            client=client,
            symbol=symbol,
            sec_type=sec_type,
            name=name,
            more=more,
            fund=fund,
            fund_family_conid_ex=fund_family_conid_ex,
            pattern=pattern,
            referrer=referrer,
        )
    ).parsed
