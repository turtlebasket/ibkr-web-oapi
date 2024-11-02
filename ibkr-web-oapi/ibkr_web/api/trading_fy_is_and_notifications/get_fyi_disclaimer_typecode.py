from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disclaimer_info import DisclaimerInfo
from ...models.typecodes import Typecodes
from ...types import Response


def _get_kwargs(
    typecode: Typecodes,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/fyi/disclaimer/{typecode}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DisclaimerInfo]]:
    if response.status_code == 200:
        response_200 = DisclaimerInfo.from_dict(response.json())

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
) -> Response[Union[Any, DisclaimerInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    typecode: Typecodes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DisclaimerInfo]]:
    """Get disclaimer for a certain kind of fyi

     Receive additional disclaimers based on the specified typecode.

    Args:
        typecode (Typecodes): Many FYI endpoints reference a “typecode” value. The table below
            lists the available codes and what they correspond to.
              * `BA` - Borrow Availability
              * `CA` - Comparable Algo
              * `DA` - Dividends Advisory
              * `EA` - Upcoming Earnings
              * `MF` - Mutual Fund Advisory
              * `OE` - Option Expiration
              * `PR` - Portfolio Builder Rebalance
              * `SE` - Suspend Order on Economic Event
              * `SG` - Short Term Gain turning Long Term
              * `SM` - System Messages
              * `T2` - Assignment Realizing Long-Term Gains
              * `TO` - Takeover
              * `UA` - User Alert
              * `M8` - M871 Trades
              * `PS` - Platform Use Suggestions
              * `DL` - Unexercised Option Loss Prevention Reminder
              * `PT` - Position Transfer
              * `CB` - Missing Cost Basis
              * `MS` - Milestones
              * `TD` - MiFID || 10% Deprecation Notice
              * `ST` - Save Taxes
              * `TI` - Trade Idea
              * `CT` - Cash Transfer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DisclaimerInfo]]
    """

    kwargs = _get_kwargs(
        typecode=typecode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    typecode: Typecodes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DisclaimerInfo]]:
    """Get disclaimer for a certain kind of fyi

     Receive additional disclaimers based on the specified typecode.

    Args:
        typecode (Typecodes): Many FYI endpoints reference a “typecode” value. The table below
            lists the available codes and what they correspond to.
              * `BA` - Borrow Availability
              * `CA` - Comparable Algo
              * `DA` - Dividends Advisory
              * `EA` - Upcoming Earnings
              * `MF` - Mutual Fund Advisory
              * `OE` - Option Expiration
              * `PR` - Portfolio Builder Rebalance
              * `SE` - Suspend Order on Economic Event
              * `SG` - Short Term Gain turning Long Term
              * `SM` - System Messages
              * `T2` - Assignment Realizing Long-Term Gains
              * `TO` - Takeover
              * `UA` - User Alert
              * `M8` - M871 Trades
              * `PS` - Platform Use Suggestions
              * `DL` - Unexercised Option Loss Prevention Reminder
              * `PT` - Position Transfer
              * `CB` - Missing Cost Basis
              * `MS` - Milestones
              * `TD` - MiFID || 10% Deprecation Notice
              * `ST` - Save Taxes
              * `TI` - Trade Idea
              * `CT` - Cash Transfer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DisclaimerInfo]
    """

    return sync_detailed(
        typecode=typecode,
        client=client,
    ).parsed


async def asyncio_detailed(
    typecode: Typecodes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DisclaimerInfo]]:
    """Get disclaimer for a certain kind of fyi

     Receive additional disclaimers based on the specified typecode.

    Args:
        typecode (Typecodes): Many FYI endpoints reference a “typecode” value. The table below
            lists the available codes and what they correspond to.
              * `BA` - Borrow Availability
              * `CA` - Comparable Algo
              * `DA` - Dividends Advisory
              * `EA` - Upcoming Earnings
              * `MF` - Mutual Fund Advisory
              * `OE` - Option Expiration
              * `PR` - Portfolio Builder Rebalance
              * `SE` - Suspend Order on Economic Event
              * `SG` - Short Term Gain turning Long Term
              * `SM` - System Messages
              * `T2` - Assignment Realizing Long-Term Gains
              * `TO` - Takeover
              * `UA` - User Alert
              * `M8` - M871 Trades
              * `PS` - Platform Use Suggestions
              * `DL` - Unexercised Option Loss Prevention Reminder
              * `PT` - Position Transfer
              * `CB` - Missing Cost Basis
              * `MS` - Milestones
              * `TD` - MiFID || 10% Deprecation Notice
              * `ST` - Save Taxes
              * `TI` - Trade Idea
              * `CT` - Cash Transfer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DisclaimerInfo]]
    """

    kwargs = _get_kwargs(
        typecode=typecode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    typecode: Typecodes,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DisclaimerInfo]]:
    """Get disclaimer for a certain kind of fyi

     Receive additional disclaimers based on the specified typecode.

    Args:
        typecode (Typecodes): Many FYI endpoints reference a “typecode” value. The table below
            lists the available codes and what they correspond to.
              * `BA` - Borrow Availability
              * `CA` - Comparable Algo
              * `DA` - Dividends Advisory
              * `EA` - Upcoming Earnings
              * `MF` - Mutual Fund Advisory
              * `OE` - Option Expiration
              * `PR` - Portfolio Builder Rebalance
              * `SE` - Suspend Order on Economic Event
              * `SG` - Short Term Gain turning Long Term
              * `SM` - System Messages
              * `T2` - Assignment Realizing Long-Term Gains
              * `TO` - Takeover
              * `UA` - User Alert
              * `M8` - M871 Trades
              * `PS` - Platform Use Suggestions
              * `DL` - Unexercised Option Loss Prevention Reminder
              * `PT` - Position Transfer
              * `CB` - Missing Cost Basis
              * `MS` - Milestones
              * `TD` - MiFID || 10% Deprecation Notice
              * `ST` - Save Taxes
              * `TI` - Trade Idea
              * `CT` - Cash Transfer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DisclaimerInfo]
    """

    return (
        await asyncio_detailed(
            typecode=typecode,
            client=client,
        )
    ).parsed
