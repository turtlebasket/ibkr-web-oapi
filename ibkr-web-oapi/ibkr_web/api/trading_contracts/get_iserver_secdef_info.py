from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_iserver_secdef_info_right import GetIserverSecdefInfoRight
from ...models.sec_def_info_response import SecDefInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conid: Union[Unset, str] = UNSET,
    sectype: Union[Unset, Any] = UNSET,
    month: Union[Unset, Any] = UNSET,
    exchange: Union[Unset, Any] = UNSET,
    strike: Union[Unset, Any] = UNSET,
    right: Union[Unset, GetIserverSecdefInfoRight] = UNSET,
    issuer_id: Union[Unset, str] = UNSET,
    filters: Union[Unset, Any] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["conid"] = conid

    params["sectype"] = sectype

    params["month"] = month

    params["exchange"] = exchange

    params["strike"] = strike

    json_right: Union[Unset, str] = UNSET
    if not isinstance(right, Unset):
        json_right = right.value

    params["right"] = json_right

    params["issuerId"] = issuer_id

    params["filters"] = filters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/iserver/secdef/info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SecDefInfoResponse]]:
    if response.status_code == 200:
        response_200 = SecDefInfoResponse.from_dict(response.json())

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
) -> Response[Union[Any, SecDefInfoResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: Union[Unset, str] = UNSET,
    sectype: Union[Unset, Any] = UNSET,
    month: Union[Unset, Any] = UNSET,
    exchange: Union[Unset, Any] = UNSET,
    strike: Union[Unset, Any] = UNSET,
    right: Union[Unset, GetIserverSecdefInfoRight] = UNSET,
    issuer_id: Union[Unset, str] = UNSET,
    filters: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, SecDefInfoResponse]]:
    """SecDef info

     SecDef info

    Args:
        conid (Union[Unset, str]): Contract identifier of the underlying. May also pass the final
            derivative conid directly. Example: 265598.
        sectype (Union[Unset, Any]): Security type of the requested contract of interest.
        month (Union[Unset, Any]): Expiration month for the given derivative.
        exchange (Union[Unset, Any]): Designate the exchange you wish to receive information for
            in relation to the contract.
        strike (Union[Unset, Any]): Set the strike price for the requested contract details
        right (Union[Unset, GetIserverSecdefInfoRight]): Set the right for the given contract. *
            `C` - for Call options. * `P` - for Put options.
        issuer_id (Union[Unset, str]): Set the issuerId for the given bond issuer type. Example:
            “e1234567”.
        filters (Union[Unset, Any]): comma separted list of additional filters. Applicable when
            SecTyp is BOND

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SecDefInfoResponse]]
    """

    kwargs = _get_kwargs(
        conid=conid,
        sectype=sectype,
        month=month,
        exchange=exchange,
        strike=strike,
        right=right,
        issuer_id=issuer_id,
        filters=filters,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: Union[Unset, str] = UNSET,
    sectype: Union[Unset, Any] = UNSET,
    month: Union[Unset, Any] = UNSET,
    exchange: Union[Unset, Any] = UNSET,
    strike: Union[Unset, Any] = UNSET,
    right: Union[Unset, GetIserverSecdefInfoRight] = UNSET,
    issuer_id: Union[Unset, str] = UNSET,
    filters: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, SecDefInfoResponse]]:
    """SecDef info

     SecDef info

    Args:
        conid (Union[Unset, str]): Contract identifier of the underlying. May also pass the final
            derivative conid directly. Example: 265598.
        sectype (Union[Unset, Any]): Security type of the requested contract of interest.
        month (Union[Unset, Any]): Expiration month for the given derivative.
        exchange (Union[Unset, Any]): Designate the exchange you wish to receive information for
            in relation to the contract.
        strike (Union[Unset, Any]): Set the strike price for the requested contract details
        right (Union[Unset, GetIserverSecdefInfoRight]): Set the right for the given contract. *
            `C` - for Call options. * `P` - for Put options.
        issuer_id (Union[Unset, str]): Set the issuerId for the given bond issuer type. Example:
            “e1234567”.
        filters (Union[Unset, Any]): comma separted list of additional filters. Applicable when
            SecTyp is BOND

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SecDefInfoResponse]
    """

    return sync_detailed(
        client=client,
        conid=conid,
        sectype=sectype,
        month=month,
        exchange=exchange,
        strike=strike,
        right=right,
        issuer_id=issuer_id,
        filters=filters,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: Union[Unset, str] = UNSET,
    sectype: Union[Unset, Any] = UNSET,
    month: Union[Unset, Any] = UNSET,
    exchange: Union[Unset, Any] = UNSET,
    strike: Union[Unset, Any] = UNSET,
    right: Union[Unset, GetIserverSecdefInfoRight] = UNSET,
    issuer_id: Union[Unset, str] = UNSET,
    filters: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, SecDefInfoResponse]]:
    """SecDef info

     SecDef info

    Args:
        conid (Union[Unset, str]): Contract identifier of the underlying. May also pass the final
            derivative conid directly. Example: 265598.
        sectype (Union[Unset, Any]): Security type of the requested contract of interest.
        month (Union[Unset, Any]): Expiration month for the given derivative.
        exchange (Union[Unset, Any]): Designate the exchange you wish to receive information for
            in relation to the contract.
        strike (Union[Unset, Any]): Set the strike price for the requested contract details
        right (Union[Unset, GetIserverSecdefInfoRight]): Set the right for the given contract. *
            `C` - for Call options. * `P` - for Put options.
        issuer_id (Union[Unset, str]): Set the issuerId for the given bond issuer type. Example:
            “e1234567”.
        filters (Union[Unset, Any]): comma separted list of additional filters. Applicable when
            SecTyp is BOND

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SecDefInfoResponse]]
    """

    kwargs = _get_kwargs(
        conid=conid,
        sectype=sectype,
        month=month,
        exchange=exchange,
        strike=strike,
        right=right,
        issuer_id=issuer_id,
        filters=filters,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    conid: Union[Unset, str] = UNSET,
    sectype: Union[Unset, Any] = UNSET,
    month: Union[Unset, Any] = UNSET,
    exchange: Union[Unset, Any] = UNSET,
    strike: Union[Unset, Any] = UNSET,
    right: Union[Unset, GetIserverSecdefInfoRight] = UNSET,
    issuer_id: Union[Unset, str] = UNSET,
    filters: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, SecDefInfoResponse]]:
    """SecDef info

     SecDef info

    Args:
        conid (Union[Unset, str]): Contract identifier of the underlying. May also pass the final
            derivative conid directly. Example: 265598.
        sectype (Union[Unset, Any]): Security type of the requested contract of interest.
        month (Union[Unset, Any]): Expiration month for the given derivative.
        exchange (Union[Unset, Any]): Designate the exchange you wish to receive information for
            in relation to the contract.
        strike (Union[Unset, Any]): Set the strike price for the requested contract details
        right (Union[Unset, GetIserverSecdefInfoRight]): Set the right for the given contract. *
            `C` - for Call options. * `P` - for Put options.
        issuer_id (Union[Unset, str]): Set the issuerId for the given bond issuer type. Example:
            “e1234567”.
        filters (Union[Unset, Any]): comma separted list of additional filters. Applicable when
            SecTyp is BOND

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SecDefInfoResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            conid=conid,
            sectype=sectype,
            month=month,
            exchange=exchange,
            strike=strike,
            right=right,
            issuer_id=issuer_id,
            filters=filters,
        )
    ).parsed
