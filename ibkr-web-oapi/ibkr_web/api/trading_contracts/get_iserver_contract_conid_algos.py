from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_iserver_contract_conid_algos_algos import GetIserverContractConidAlgosAlgos
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conid: str,
    *,
    algos: Union[Unset, GetIserverContractConidAlgosAlgos] = UNSET,
    add_description: Union[Unset, str] = "0",
    add_params: Union[Unset, str] = "0",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_algos: Union[Unset, str] = UNSET
    if not isinstance(algos, Unset):
        json_algos = algos.value

    params["algos"] = json_algos

    params["addDescription"] = add_description

    params["addParams"] = add_params

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/iserver/contract/{conid}/algos",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 401:
        return None
    if response.status_code == 500:
        return None
    if response.status_code == 503:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    algos: Union[Unset, GetIserverContractConidAlgosAlgos] = UNSET,
    add_description: Union[Unset, str] = "0",
    add_params: Union[Unset, str] = "0",
) -> Response[Any]:
    """Search Algo Params by Contract ID

     Returns supported IB Algos for contract. A pre-flight request must be submitted before retrieving
    information

    Args:
        conid (str): Contract identifier for the requested contract of interest.
        algos (Union[Unset, GetIserverContractConidAlgosAlgos]): List of algo ids delimited by “;”
            to filter by. Max of 8 algos ids can be specified. Case sensitive to algo id.
        add_description (Union[Unset, str]): Whether or not to add algo descriptions to response.
            Set to 1 for yes, 0 for no. Default: '0'.
        add_params (Union[Unset, str]): Whether or not to show algo parameters. Set to 1 for yes,
            0 for no. Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        conid=conid,
        algos=algos,
        add_description=add_description,
        add_params=add_params,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    conid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    algos: Union[Unset, GetIserverContractConidAlgosAlgos] = UNSET,
    add_description: Union[Unset, str] = "0",
    add_params: Union[Unset, str] = "0",
) -> Response[Any]:
    """Search Algo Params by Contract ID

     Returns supported IB Algos for contract. A pre-flight request must be submitted before retrieving
    information

    Args:
        conid (str): Contract identifier for the requested contract of interest.
        algos (Union[Unset, GetIserverContractConidAlgosAlgos]): List of algo ids delimited by “;”
            to filter by. Max of 8 algos ids can be specified. Case sensitive to algo id.
        add_description (Union[Unset, str]): Whether or not to add algo descriptions to response.
            Set to 1 for yes, 0 for no. Default: '0'.
        add_params (Union[Unset, str]): Whether or not to show algo parameters. Set to 1 for yes,
            0 for no. Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        conid=conid,
        algos=algos,
        add_description=add_description,
        add_params=add_params,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
